from app import create_app,db
from flask_script import Manager,Server
from app.models import Category,User,Peptalk,Comments
from  flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager



# Creating app instances
# app = create_app('development')
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

#Migration
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, Category = Category, User = User, Peptalk = Peptalk, Comments = Comments)


if __name__ == '__main__':
    manager.run()
