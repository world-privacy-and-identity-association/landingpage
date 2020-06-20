# Landing Page for CA website

## Installation

Requires python 3

To install:

```
virtualenv -p python3
. bin/activate
pip install -r requirements.txt
```

Then edit config.py.example into config.py with your settings.

To debug-run linux:

```
LANG=C.UTF-8 FLASK_DEBUG=1 FLASK_APP=landingpage.py flask run
```

To debug-run windows:

```
set LANG=C.UTF-8
set FLASK_DEBUG=1
set FLASK_APP=landingpage.py
flask run
```
