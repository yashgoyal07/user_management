# user_management
It is user management api by which we can pull or store the users information.

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
1. export your mysql user and password.
   > export MYSQL_USER='#####'
   > 
   > export MYSQL_PASSWORD='######'

# database setup
1. Create database in mysql with name 'usr_mgmt'.
   > CREATE DATABASE usr_mgmt;
1. Make the 'user' table using query from :-
   > src/helpers/mysql_queries.py#L7-L24
   
# run
1. run the below command.
   > python3 src/views/views.py
1. go to following link.
   > http://127.0.0.1:5000

# postman Collection
1. import collection in Postman from following link.
   > https://www.getpostman.com/collections/8501374bd7e9189fd60f
