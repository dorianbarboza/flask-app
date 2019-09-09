################################################################
# Otro requisito para la migración de la base de datos         #
# es el archivo manage.py . Cree un archivo llamado manage.py  #
################################################################

################################
# Install                      #
# pip install flask_script     #
# pip install flask_migrate    #
# pip install psycopg2-binary  #
################################

"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
"""
