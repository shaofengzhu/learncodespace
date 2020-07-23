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
	print(f"{request.method} /functions")
	if request.method == "POST":
		data = request.get_data(as_text = True)
		print("Body=" + data)
		requestPayloadObj = request.get_json(force=True)
		print("Invoke function")
		responseText = customfunctions.invokeWithPayload(requestPayloadObj)
	else:
		responseText = customfunctions.registration.getMetadataJson()

	response = Response(responseText)
	response.headers["Content-Type"] = "application/json"
	response.headers["Access-Control-Allow-Origin"] = "*"
	return response

@app.route("/functions.html", methods = ["GET"])
def agave_page():
	responseText = customfunctions.getPageHtml(devMode = True)
	response = Response(responseText)
	response.headers["Content-Type"] = "text/html"
	return response

if __name__ == "__main__":
	app.run()
