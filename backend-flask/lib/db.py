from psycopg_pool import ConnectionPool
import os
import re
import sys
from flask import current_app as app

class Db:
  def __init__(self):
    self.init_pool()

  def template(self, name):
    template_path = os.path.join(app.root_path, 'db', 'sql', name + '.sql')

    with open(template_path, 'r') as f:
      template_content = f.read()

    return template_content

  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)

  def print_sql(self, title, sql):
    cyan='\033[1;36m'
    no_color='\033[0m'
    print(f'\n{cyan}SQL STATEMENT --[{title}]-----{no_color}')
    print(sql)
    print('')

  def query_commit(self, sql, params):
    self.print_sql("commit with returning", sql)

    pattern = r"\bRETURNING\b"
    is_returning_id = re.search(pattern, sql)

    try:
      with self.pool.connection() as conn:
        cur = conn.cursor()
        cur.execute(sql, params)
        
        if is_returning_id:
          returning_id = cur.fetchone()[0]
          
        conn.commit()

        if is_returning_id:
          return returning_id

    except Exception as err:
      self.print_sql_err(err)
  
  # return an array of json objects
  def query_array_json(self, sql):
    print('SQL STATEMENT --[array]-----')
    print(sql)
    print('')
    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        json = cur.fetchone()
        return json[0]

  # retrun a json object
  def query_object_json(self, sql):
    print('SQL STATEMENT --[object]-----')
    print(sql)
    print('')
    wrapped_sql = self.query_wrap_object(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        json = cur.fetchone()
        return json[0]

  def query_wrap_object(self, template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {template}
    ) object_row);
    """
    return sql

  def query_wrap_array(self, template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql

  def print_sql_err(self, err):
    try:
      # get details about the exception
      err_type, err_obj, traceback = sys.exc_info()

      # get the line number when exception occured
      line_num = traceback.tb_lineno

      # print the connect() error
      print ("\npsycopg ERROR:", err, "on line number:", line_num)
      print ("psycopg traceback:", traceback, "-- type:", err_type)

      # print the pgcode and pgerror exceptions
      print ("pgerror:", err.pgerror)
      print ("pgcode:", err.pgcode, "\n")

    except:
      return print('Error debugger failure')

db = Db()
