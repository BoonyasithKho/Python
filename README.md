# Python API Tutorial: Getting Started with APIs
Credit : https://www.dataquest.io/blog/python-api-tutorial/

API (Application Programming Interface)  is a server that you can use to retrieve and send data to using code. APIs are most commonly used to retrieve data, and that will be the focus of this beginner tutorial.

## Making API Requests in Python
In Python, the most common library for making requests and working with APIs is the requests library. The requests library isn’t part of the standard Python library, so you’ll need to install it to get started.
If you use pip to manage your Python packages, you can install requests using the following command:
```
pip install requests
```
If you use conda, the command you’ll need is:
```
conda install requests
```
Once you’ve installed the library, you’ll need to import it. Let’s start with that important step: 
```python
import requests
```
## Making Our First API Request
To make a ‘GET’ request, we’ll use the requests.get() function, which requires one argument — the URL we want to make the request to. We’ll start by making a request to an API endpoint that doesn’t exist, so we can see what that response code looks like.
```python
response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")
```
The get() function returns a response object. We can use the response.status_code attribute to receive the status code for our request:
```python
print(response.status_code)
```
## API Status Codes
  Status codes are returned with every request that is made to a web server. Status codes indicate information about what happened with a request. Here are some codes that are relevant to GET requests:
  200: Everything went okay, and the result has been returned (if any).
  301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
  400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
  401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
  403: The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.
  404: The resource you tried to access wasn’t found on the server.
  503: The server is not ready to handle the request.

## API Documentation
The documentation tells us that the API response we’ll get is in JSON format. In the next section we’ll learn about JSON, but first let’s use the response.json() method to see the data we received back from the API:
```python
print(response.json())
```
## Working with JSON Data in Python
  JSON (JavaScript Object Notation) is the language of APIs. JSON is a way to encode data structures that ensures that they are easily readable by machines. JSON is the primary format in which data is passed back and forth to APIs, and most API servers will send their responses in JSON format.

  Python has great JSON support with the json package. The json package is part of the standard library, so we don’t have to install anything to use it. We can both convert lists and dictionaries to JSON, and convert strings to lists and dictionaries. In the case of our ISS Pass data, it is a dictionary encoded to a string in JSON format. The json library has two main functions:
  
  **json.dumps()** — Takes in a Python object, and converts (dumps) it to a string. The dumps() function is particularly useful as we can use it to print a formatted string which makes it easier to understand the JSON output
  
  **json.loads()** — Takes a JSON string, and converts (loads) it to a Python object. 

## Using an API with Query Parameters
  We can do this by adding an optional keyword argument, params, to our request. We can make a dictionary with these parameters, and then pass them into the requests.get function. Here’s what our dictionary would look like, using coordinates for New York City: 
```json
parameters = {
  "lat": 40.71,
  "lon": -74
  }
```
  Let’s make a request using these coordinates and see what response we get. 
```python
response = requests.get("https://api.open-notify.org/iss-pass.json", params=parameters)
```
## Understanding the Pass Times
  The JSON response matches what the documentation specified:
    * A dictionary with three keys
    * The third key, response, contains a list of pass times
    * Each pass time is a dictionary with risetime (pass start time) and duration keys.
  Let’s extract the pass times from our JSON object: 
```python
pass_times = response.json()['response']
```
Next we’ll use a loop to extract just the five risetime values: 
```python
risetimes = []
for d in pass_times:
  time = d['risetime']
  risetimes.append(time)
print(risetimes)
```
  These times are difficult to understand – they are in a format known as timestamp or epoch. Essentially the time is measured in the number of seconds since January 1st 1970. We can use the Python datetime.fromtimestamp() method to convert these into easier to understand times:
```python
from datetime import datetime
times = []
  
for rt in risetimes:
  time = datetime.fromtimestamp(rt)
  times.append(time)
  print(time)
```
