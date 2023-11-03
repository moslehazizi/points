Points

This is a simple course management web application. It comes with basic build-in features that every course management system should have, such as that instructors can create articles for their courses, do course attendance flow, insert result for exams, send message to students, upload files of their courses such as book, article, animation and ect, also learners can See articles of courses, see results of exams, download files that teachers uploaded and send message to teachers.

setup

The first thing to do is to clone the repository:

	$ git clone https://github.com/moslehazizi/points.git
	$ cd points

Create a virtual environment to install dependencies in and activate it:

	$ virtualenv env
	$ source env/bin/activate

Then install the dependencies:

	(env)$ pip install -r requirements.txt
	
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.
Once pip has finished downloading the dependencies migrate models to your database:

 	(env)$ python manage.py migrate

To check admin panel create a super user:

	(env)$ python manage.py createsuperuser

Add your username, email and password to log in to django admin panel after running the project.
Insert data from csv files by running scripts, So:

	(env)$ python manage.py runscript user_load
 	(env)$ python manage.py runscript course_load
  	(env)$ python manage.py runscript day_load
   	(env)$ python manage.py runscript dp_load
    (env)$ python manage.py runscript result_load
    (env)$ python manage.py runscript exam_load
	

Now:

	(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000/.

You can log in as instructor:

 	username: 1111111111
  	password: testpass123
   
Log in as learner:

	username: 3333333333
 	password: testpass123




