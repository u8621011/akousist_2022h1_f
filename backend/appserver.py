

from todoapi.application import create_app
from todoapi.models import db
from flask_migrate import Migrate

app = create_app()

migrate = Migrate(app, db)

app.run(host='0.0.0.0')