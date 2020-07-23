# Create Codespace
1. Create codespace and point to https://github.com/shaofengzhu/learncodespace.git
2. Inside codespace, please
```console
pip3 install flask
pip3 install officepylib/officepy-0.0.3.tar.gz
```
3. Run app.py
4. Setup port forward

# Excel
1. Access `http://localhost:<port>/functions.html`, click "Generate Manifest", then save the manifst file.

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
