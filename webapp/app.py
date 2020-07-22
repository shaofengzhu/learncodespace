from flask import Flask, request, escape, Response
from officepy import customfunctions

import functions

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	name = request.args.get("name", "World")
	return f"Hello, {escape(name)}"

@app.route("/functions", methods = ["GET", "POST"])
def agave_functions():
	
	if request.method == "POST":
		requestPayloadObj = request.get_json(force=True)
		responseText = customfunctions.invokeWithPayload(requestPayloadObj)
	else:
		responseText = customfunctions.registration.getMetadataJson()

	response = Response(responseText)
	response.headers["Content-Type"] = "application/json"
	return response

@app.route("/functions.html", methods = ["GET"])
def agave_page():
	responseText = customfunctions.getPageHtml()
	response = Response(responseText)
	response.headers["Content-Type"] = "text/html"
	return response
