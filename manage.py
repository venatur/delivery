#!/usr/bin/env python
import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


migrate = Migrate(app, db)
migrate.init_app(app, db)
manager = Manager(app)
db.init_app(app)

def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
