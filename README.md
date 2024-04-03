Package requirements :
django
django rest framework

commands for above package installations are as follows:
pip3 install django and djangorestframework

how to run the project:
1. open terminal or command prompt.
2. cd into the directory where you have the project
3. make sure required packages are installed (it is assumed you have python installed)
4. run command in order:
   a. python3 manage.py makemigrations
   b. python3 manage.py migrate
   c. python3 manage.py createsuperuser
   d. enter your desired username, email and password
   e. python3 manage.py runserver