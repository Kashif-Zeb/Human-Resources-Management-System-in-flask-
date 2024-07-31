#! /usr/bin/bash
# :: This batch file try to provide similar functionality to the windows users to run the hr
# :: in Dev mode as provided to LINUX/UNIX users in the relevant (runDebug.sh) file.
# :: Dev server config vars are set here.
 
# export FLASK_APP=app
# export FLASK_ENV=development
 
export FLASK_APP=bds.runApp
export PYTHONPATH=$(pwd)
# export PYTHONPATH=/media/kashif/test/fb/bds


 
# :: Development DB config vars are set here
export DB_NAME=hr2
export DB_URL=localhost
export DB_USER=root
export DB_PWD=kashif
export DB_PORT=3306
 
# echo "$DB_NAME $DB_URL $DB_PORT $DB_USER $DB_PWD"
# export CLIENT_ID=898268028028-daft8k12cf9u0dtdptr7rk9bus08so8g.apps.googleusercontent.com
# :: Test DB config vars are set here
 
 
# :: Production DB config vars are set here
 
python3 runApp.py