# Todolist project
- use `npm run serve` to start dev server


# Backend project
- commands to init/migration/upgrade db
```
# setup environment before executing flask-migrate db commands
set FLASK_APP=appserver.py
flask db init

# init migration
flask db migrate -m "Initial migration."

# apply the migration
flask db upgrade
```
- use `python appserver.py` to start the flask restful service