# Technical Task for a position of MS SQL Engineer @ Spark Networks

Dear candidate

As part of the recruitment process, we would like to ask you to accomplish the following assessment task which should take not more than a couple of evenings of your time. Please do your best and aim for an end-to-end MVP solution.

As <em>result</em> of the exercise, it is expected to receive a link to the <em>github/gitlab/bitbucket repo</em> with working executable code base and instruction on how to run it, and with the detailed report (as <em>markdown README.md</em> file) containing justification of your tech choices.

## Description

We would like to propose you to familiarise yourself with the housing market in Berlin, hence to suggest you to make data integration for the flats available for rent in Berlin. In order to complete that exercise, we would like to formulate the following task for you:

1. Build a stateless service to load data batches into hot storage (database). <em>The service should consume data batches appearing at the pipeline input on hourly basis</em>. An example of expected incoming data batch is present in the repo as <strong>raw_data_example.json.zip</strong>. <p>Please preserve all raw data imported into pipeline, but make <u>only required dimensions</u> accessible to an end user.

    Required data dimensions:

    - flat size
    - number of rooms: sleeping rooms, living rooms, bathrooms, toilets
    - price: cold and warm, additional expenses, parking lot price
    - location: city, district, street, house number, longitude, latitude
    - agency fact data: agency name, agent name, email, phone number provided as unchanged raw data for DWH engineer user/role and as GDPR compliant/anonymised data accessible to BI
    - flat advertisement meta data: is active, when created, when updated, has flat's pictures


2. Build a star, or snowflake (the one which you think is more appropriate) data model in the DB of your choice.

    For example, model can include the following tables:

    - fact_flat
    - dim_address
    - dim_agency
    - dim_city
    - dim_district

<br>
Please use the MS SQL tech stack.

Good luck and hopefully see you soon in our headquarters for onsite interview.
<br>
<br>Best regards


See why Spark Networks employees love where they work: check out our <a href="https://www.glassdoor.com/Reviews/Spark-Networks-Reviews-E31363.htm" target="_balnk">Glassdoor reviews</a>!

<a href="mailto:www.spark.net" target="_blank">www.spark.net</a>

Geschäftsführer: Michael Schrezenmaier, Herbert Sablotny
Eingetragen beim Amtsgericht Berlin-Charlottenburg, HRB 115958 B, Registergericht: AG Charlottenburg (Berlin)    
