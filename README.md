# Entry Task

> Entry Task

## Requirement
1. Python 3.7 
2. Node.js (npm)
3. MySQL (set the root account's password to be `root`)

## Build Setup

### Python virtual environment
1. `pip install virtualenv`
2. `virtualenv venv`
3. Activate base on your OS. (See Google)
4. See `(venv)` at start of your command line

### Python dependencies
1. `pip install -r requirements.txt`
2. `python manage.py makemigrations`
3. `python manage.py migration`
4. `python manage.py createsuperuser` (superuser account)
5. `python manage.py runserver`

### JS dependencies
1. `cd frontend`
2. `npm install`
3. `npm run build`

### Finally
Open `127.0.0.1:8000/` for login check.
