# about todolist project
- use `npm run serve` to start dev server


# about backend project
- command to init db
```
set FLASK_APP=appserver.py
flask db init

# init migration
flask db migrate -m "Initial migration."

# apply the migration
flask db upgrade
```
- use `python appserver.py` to start the flask restful service