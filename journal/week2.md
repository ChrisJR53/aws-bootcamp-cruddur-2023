# Week 2 — Distributed Tracing

## Required Homework

### Weekly Videos
All videos in todo list watched.

### Instrument Honeycomb with OTEL
Firstly, I added the OTEL details into my ```docker-compose.yml``` file:

![OTEL Details](/journal/resources/images/week2/01_api_set_opentel.PNG)

I then added the dependencies for OTEL into the ```requirements.txt``` file in the backend flask app and installed them with ```$ pip install -r requirements.txt```:

![OTEL Dependencies](/journal/resources/images/week2/02_req_install_opentel.PNG)

Honeycomb tracing details were added to the ```app.py``` file on the flask app, as was a simple span processor to output local log details:

![Simple Processor](/journal/resources/images/week2/03_simple_processor.PNG)

Once that was all impemented, I used ```$ docker compose up``` to get the application running and generate some traces, which came through to my Honeycomb dashboard:

![Hooneycomb Traces](/journal/resources/images/week2/04_honeycomb_traces.PNG)

I added the implementation of spans to the application code and managed to view them on Honeycomb as well:

![Honeycomb Spans](/journal/resources/images/week2/05_honeycomb_spans.PNG)

I then tested out the Query function in Honeycomb to visualize ```COUNT``` and group by ```trace.trace_id```:

![Honeycomb Query](/journal/resources/images/week2/06_honeycomb_query.PNG)

Within a span I used the Fields search to confirm the ```app.now``` and ```app.result_length``` were successfully reporting from the app:

![Honeycomb Fields](/journal/resources/images/week2/07_honeycomb_app_field.PNG)

I then searched using the visualize ```HEATMAP(duration_ms)``` to provide a heatmap illustaration of the differences in time of each trace and ```P90(duration_ms)``` to view the length of traces in the 90th percentile:

![Honeycomb Heatmap](/journal/resources/images/week2/08_honeycomb_heatmap_p90.PNG)
(Apologies for lightmode here, the heatmap dots wouldn't show otherwise!)

### Instrument AWS X-Ray
Firstly I added the AWS X-Ray requirements to the ```requirements.txt``` file in the flask app, and then installed it with ```$ pip install -r requirements.txt```:

![Xray Install](/journal/resources/images/week2/09_xray_install.PNG)

I then created the file ```aws/json/xray.json``` and added the "Cruddur" sampling rule. I then used the code below to create the "Cruddur" group in AWS X-Ray
```
$ aws xray create-group \
    --group-name "Cruddur" \
    --filter-expression "service(\"$FLASK_ADDRESS\") {fault OR error}"
```
The terminal output confirms the successful creation of this group:

![Xray Group](/journal/resources/images/week2/10_xray_create_group.PNG)

My AWS console also confirms the "Cruddur" group creation:

![Console Proof](/journal/resources/images/week2/11_xray_group_proof.PNG)

I then created a filter for X-Ray using ```$ aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json```:

![Xray Filter](/journal/resources/images/week2/12_xray_create_filter.PNG)

Next I used ```$ docker compose up``` and viewed the output for the flask app to confirm X-Ray data was being sent to AWS:

![Xray Data](/journal/resources/images/week2/13_xray_send_data.PNG)

Finally I could confirm the traces had made their way into my AWS console for viewing:

![Xray Success](/journal/resources/images/week2/14_xray_success.PNG)

### Configure custom logger to send to CloudWatch Logs
Firstly I added the AWS CloudWatch requirements to the ```requirements.txt``` file in the flask app, and then installed it with ```$ pip install -r requirements.txt```:

![Install Watchtower](/journal/resources/images/week2/15_cloudwatch_watchtower.PNG)

I then added the setup configuration to the backend ```app.py``` file:

![CloudWatch Setup](/journal/resources/images/week2/16_cloudwatch_app_install.PNG)

Finally I used ```$ docker compose up``` and confirmed that logs were being sent to my AWS account:

![CloudWatch Proof](/journal/resources/images/week2/17_cloudwatch_proof.PNG)

