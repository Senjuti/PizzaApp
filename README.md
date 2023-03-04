## How to Run

Change your directory to the ```venv/Scripts``` directory.

Make venv on Unix by running:

```
source activate
```

Make venv on Windows Powershell by running:

```
.\Activate.ps1
```

Change your directory to the root directory and install requirements:
```
(venv) $ pip install -r requirements.txt
```

Run the Flask application on Unix by:
```
(venv) $ export FLASK_APP=app
(venv) $ export FLASK_ENV=development
(venv) $ flask run
```

On Windows by:
```
(venv)> set FLASK_APP=app
(venv)> set FLASK_ENV=development
(venv)> flask run
```

Open a browser and type in the URL ```http://localhost:5000/```.