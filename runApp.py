from hr.api import create_app
# from hr.celery_settings import make_celery
from dotenv import load_dotenv
import os
load_dotenv()
application = create_app()
celery_app = application.extensions["celery"]
# celery = make_celery(app=application)
# port  =  os.getenv("port",5000)
if __name__ == "__main__":
    application.run(host="127.0.0.1", port=5009,debug=True)
