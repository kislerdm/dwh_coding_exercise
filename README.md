# Technical Task for a position of DWH Engineer @ Spark Networks

Dear candidate

As part of the recruitment process, we would like to ask you to accomplish the following assessment task which should take not more than a couple of evenings of your time. Remember to do your best and aim for an end-to-end MVP solution, but keep in mind that the purpose of the task is to check the way of how you think and approach the problem.

As <em>result</em> of the exercise, it is expected to receive a link to the <em>github/gitlab/bitbucket repo</em> with working executable scripts, queries (or a docker container) and instruction on how to run the code, and with the detailed report (as <em>markdown README.md</em> file) containing justification of your tech choices.

## Description

1. Build a scalable pipeline to fetch on hourly basis dim and fact data of the <strong>flats in Berlin</strong> available for <em>rent</em> at <a href="https://www.immobilienscout24.de/Suche/S-T/Wohnung-Miete/Berlin/Berlin" target="_blank">immobilienscout24.de</a> assuming (micro-) batch processing based on a data sample <strong><em>raw_data_example.json.zip</em></strong>.

    Required data dimensions:

    - flat size
    - number of rooms: sleeping rooms, living rooms, bathrooms, toilets
    - price: cold and warm, additional expenses, parking lot price
    - location: city, district, street, house number, longitude, latitude
    - agency fact data: agency name, agent name, email, phone number provided as unchanged raw data for DWH engineer user/role and as GDPR compliant/anonymised data accessible to BI
    - flat advertisement meta data: is active, when created, when updated, has flat's pictures
    <p><i>plus</i> any dimensions you would find useful for analysis

<em>Note</em>: preserve all raw data imported into pipeline, but make only required dimensions accessible to an end user.

2. Build a star, or snowflake (the one which you think is more appropriate) data model in the DB of your choice.

    For example, model can include the following tables:

    - fact_flat
    - dim_address
    - dim_agency
    - dim_city
    - dim_district

<br>
You are free to choose tech stack for the pipeline architecture and for ETL/ELT/aggregation. Note that we prefer to keep the business logic as a service, i.e. in python code, and not as database stored procedures.

<em>Note</em>: we would strongly recommend you to consider employing tools/services and languages we use at DWH:
- AWS: <strong>S3, Lambda, ECR, Fargate, CloudWatch</strong>
- DBs: <strong>AWS RDS PostgreSQL, or AWS Redshift</strong> or <strong>Snowflake</strong>
- DSL/Programming language: <strong>Python (ver. >= 3.6.5)</strong> and <strong>SQL</strong>
- EDA/Reporting: <strong>Tableau</strong>, or <strong>Qlikview</strong>   

Good luck and hopefully see you soon in our headquarters for an on-side interview.
<br>
<br>Best regards
<br>Dmitry Kisler
<br><strong>DWH Team Lead</strong>

Spark Networks
<br>Mobil: +49 (0)173 522 8056
<br><a href="mailto:dmitry.kisler@affinitas.de" target="_blank">dmitry.kisler@affinitas.de</a>

Kohlfurter Straße 41/43
<br>10999 Berlin
<br>Germany

See why Spark Networks employees love where they work: check out our <a href="https://www.glassdoor.com/Reviews/Spark-Networks-Reviews-E31363.htm" target="_balnk">Glassdoor reviews</a>!

<a href="mailto:www.spark.net" target="_blank">www.spark.net</a>

Geschäftsführer: Michael Schrezenmaier, Herbert Sablotny
Eingetragen beim Amtsgericht Berlin-Charlottenburg, HRB 115958 B, Registergericht: AG Charlottenburg (Berlin)    
