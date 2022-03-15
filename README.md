# file structures
- file/folder description
```
backend: backend project root
    |---- tasks.db: the sqlite db file
    |---- upload: the folder of uploaded images
    |---- migrations: the folder to store SQLAlchemy db schema migrtion files
    |---- todoapi: the folder of backend api source codes
todolist: frontend project root
    |---- src: the folder of frontend source codes
```

# Backend project

## env preparation
- package installation
```
# in backend\ folder
pip install -r requirements.txt
```

## restful service startup
- use `python appserver.py` in backend\ folder to start the flask restful service
- the service will be hosted on http://127.0.0.1:5000/

## simple api self-testing
- open the url(`http://127.0.0.1:5000/api/hello/ted/`) in any browser, you will see the json returned as below
```
{
  "msg": "Hello ted"
}
```

## commands to init/migration/upgrade db
You can also create your own database file using commands below.
```
# setup environment before executing flask-migrate db commands
set FLASK_APP=appserver.py
flask db init

# init migration
flask db migrate -m "Initial migration."

# apply the migration
flask db upgrade
```

# Todolist project

## environment preparation
- run `npm install` in todolist\ folder
- run `npm run serve` to start dev server

## app entrypoint
- open url `http://localhost:8080/` in any browser

## app screenshot
![screenshot](/screenshot.png)
1. create task
2. list task