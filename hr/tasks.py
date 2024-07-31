# from .celery_setting import 
import json
from celery import shared_task
from celery.utils.log import get_task_logger
import logging
from flask import current_app
import os
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '.', 'uploads')
UPLOAD_FOLDER= UPLOAD_FOLDER.split("hr/./")
UPLOAD_FOLDER = UPLOAD_FOLDER[0]+UPLOAD_FOLDER[1]
@shared_task(bind=True,max_retries=3)
def file(self,employee):
    # print("helpppppppppppppppppppppppppppp")
    os.path.join("upload")
    data = {"kk":[1,2,3,4,5]}
    logger.info("start writing data in file")
    file_path = os.path.join(UPLOAD_FOLDER, "file.txt")
    with open(file_path,"w") as f:
        
        f.write(json.dumps(employee)) 
        f.close()