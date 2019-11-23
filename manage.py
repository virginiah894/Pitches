import os
from app import create_pitch,db
from app.models import User,Role
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

app = create_pitch('development')

manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role = Role)
if __name__ == '__main__':
    manager.run()

