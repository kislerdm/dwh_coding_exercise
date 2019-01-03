# immobilienscout24 APIs for tech task

To get a list of the available API end-points, go to <a href="https://api.immobilienscout24.de/our-apis.html" target="_blank">https://api.immobilienscout24.de/our-apis.html</a>.

The required data can be fetched using two end points:
1. <a href="https://api.immobilienscout24.de/our-apis/search.html" target="_blank">search API</a>, to get the list of flats
2. <a href="https://api.immobilienscout24.de/our-apis/expose.html" target="_blank">exposé API</a>, to fetch the data of one flat

## How to get an access token

1. Go to <a href="https://api.immobilienscout24.de/useful/tutorials-sdks-plugins/tutorial-customer-website.html" target="_blank">the tutorial</a> and click <a href="https://rest.immobilienscout24.de/restapi/security/registration" target="_blank">register</a>.

2. Fill the required fields:

	- "Projekt- / Produktname": you_project_name (e.g. test-spark-dwh)
	- "URL": any_working_url (e.g. https://www.google.de/?q=dwhtest)
	- "Programmiersprache": python
	- "Anwendungsfall / Berechtigungen": leave default option selected
	- "Kategorie / Beschreibung": "Testsystem" free_text in the field (e.g. dwh-test)

3. Click "Registrieren" (you will need to create a profile on immobilienscout24.de)

4. Copy "API key" and "API Secret"

5. Go to the <a href="https://api.immobilienscout24.de/get-started/playground.html" target="_blank">playground info page</a>. Here, you can try API end points and see what is required to get the token and resolve the task.

6. In the "Authentication Frame", click "Use a own costumer key and secret" and insert the key and secret you copied on the <i>step 4</i> -> select "Live" instead of "Sandbox" -> click "Change" button.

7. Click "Request Token" in the "oAuth-Frame" frame

8. Click "Authorize"

9. Enter your immobilienscout24.de credentials, or register -> Click "Bestätigen" once you logged in

10. Click "Access Token"

11. Copy returned "Access Token" and "Token Secret"

## Credentials

In the end, your oAuth token is a json similar to the file <strong><em>script/token.json</em></strong> (please <a href="mailto:dmitry.kisler@affinitas.de" target="_blank">contact me</a> if you need a token credentials file).

## Example

As an example of how to fetch a daily sample of data required for the task, you can use the python script in <strong><em>script/tech_task_dwh_spark_demo.py</em></strong>.
