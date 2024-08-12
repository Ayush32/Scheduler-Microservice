## Step by step guide to run this project

* Download and extract the zip file by
* git clone https://github.com/Ayush32/Scheduler-Microservice.git
* open Command Prompt - Install Virtualenv using -> pip install virtualenv
* Open the Scheduler-Microservice directory inside VScode
* Open terminal in vscode and setup virtual enviroment by following steps

              virtualenv venv
              Go to scripts directory then activate the virtual environment - venv\Scripts\activate
              go back to main directory by using cd.. for windows
              
* Install django, djangorestframework, psycopg2 by following command, copy and paste

              pip install Django==5.1 djangorestframework==3.15.2 APScheduler==3.10.4
* Now run the following command to save your model into the database.

              Go to the scheduler_service directory
              cd scheduler_service
              Run the below command
              python manage.py makemigrations
              python manage.py migrate
              
* Now run the following command to runserver
  
              python manage.py runserver
              Open in Chrome/IE - http://127.0.0.1:8000/jobs/
              all job - http://127.0.0.1:8000/jobs/
              specific job id :  http://127.0.0.1:8000/jobs/job_id = http://127.0.0.1:8000/jobs/1
              create job : http://127.0.0.1:8000/jobs/new
