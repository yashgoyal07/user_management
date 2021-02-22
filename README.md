# user_management
It is user management system by which another system can pull or store the information.

# pre-requisite
* Python Version - 3.8.5
* mysql Version - 8.0.23
* pip 20.0.2

# project installation

1. Clone the Repository.
1. cd into Repository.
1. Make virtual environment.
   > python -m venv venv
1. Activate the virtual environment.
   > source venv/bin/activate
1. Install requirements.txt file
   > pip install -r requirements.txt
1. export path of src directory into PYTHONPATH. For Example: 
   > export PYTHONPATH=:/home/yashgoyal07/Music/user_management/src
1. export your mysql root and password.
   > export MYSQL_USER = '#####'
   > 
   > export MYSQL_PASSWORD = '######'

# database setup
1. Create database in mysql with name 'usr_mgmt'.
   > CREATE DATABASE usr_mgmt;
1. copy the CREATE_USER_TABLE query from helpers/mysql_queries.py in the repo and make table in 'usr_mgmt' database with name 'user'.
   > CREATE TABLE user ('copied query');
   
# run
1. run the below command.
   > python3 src/views/views.py
1. go to following link.
   > http://127.0.0.1:5000

# postman Collection
1. import collection in Postman from following link.
   > https://www.getpostman.com/collections/8501374bd7e9189fd60f
