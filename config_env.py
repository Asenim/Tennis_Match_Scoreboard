from dotenv import load_dotenv
import os

load_dotenv()

SQL_DRIVER = os.environ.get('SQL_DRIVER')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

# # Linux Path
# LinuxJinjaPATH = os.environ.get('LJinjaPATH')
# # UWSGI Conf
# LinuxUWSGIPATH = os.environ.get('LUWSGIPATH')
# UWSGI_HOST = os.environ.get('UWSGI_HOST')
# UWSGI_PORT = os.environ.get('UWSGI_PORT')
