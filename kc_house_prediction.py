from app import app, db
from app.models import User, Estimate, DataModel


@app.shell_context_processor
def db_shell_context():
    return {'db': db, 'User': User, 'Estimate': Estimate, 'DataModel': DataModel}
