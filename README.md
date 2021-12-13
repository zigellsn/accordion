# HTML Accordion implementation with Django, htmx and _hyperscript

## Installation

Install [Python 3.10](https://www.python.org/) if necessary.
Install and configure [Node.js](https://nodejs.org/) if you want to change the style sheet.

In the main directory run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate --run-syncdb
python manage.py runserver
```

Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---
**Do not run in production!**

---

## Accordion

The relevant code is located in ./templates/accordion.html and in ./Accordion/static/behavior/accordion_click._hs
