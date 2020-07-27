# Create Codespace
1. Create codespace and point to https://github.com/shaofengzhu/learncodespace.git
2. Run app.py
3. Setup port forward using VS code as there is bug when using browser port forward.
4. Configure local HTTPS reverse proxy for the port-forwrad as Excel requires HTTPS web site.
```console
REM Only need to run office-addin-dev-certs once
npx office-addin-dev-certs install --days 365
REM The <port> is the port created by VS code port forward
npx office-addin-https-reverse-proxy --port 5500 --url http://localhost:<port>
```

# Excel
1. Access `https://localhost:5500/functions.html`, click "Generate Manifest", then save the manifst file.

2. Access `https://microsoft-my.sharepoint-df.com/`, create a Excel file

3. Click "Insert" -> "Add-ins", in the dialog, click the "Manage My Add-ins" -> "Upload My Add-in", use the file you saved in step 1.

4. Now, a new Ribbon tab "Python" will show up. Please click "Python" -> "Show Taskpane", then in the taskpane, click "Register Functions with Excel".

5. Now, you could type in "=PYTHON.ADD(1,2)" in the Excel.

# Add a new function
To add a new function, please go to codespace, stop run app.py, then modify the functions.py, add some code like
```python
@customfunctions.customfunction(name = "MYMUL")
def mymull(x, y):
	return x * y
```

Run the app.py

Now, go to Excel, click the "Python" -> "Show Taskpane", click "Register Functions with Excel".

# Troubleshooting
## If you created a new codespace
Please cleanup the browser cache, and generate a new manifest.

## If officepy package does not work
Inside codespace, please
```console
pip3 install -r requirements.txt
```
