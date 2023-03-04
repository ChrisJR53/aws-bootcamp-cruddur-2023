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

