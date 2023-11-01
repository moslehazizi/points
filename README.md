Points

This is a simple course management web application. included some features.

Teachers can: Create articles for their courses, Do course attendance flow, Insert result for exams, Send message to students, Upload files for their courses.

Students can: See articles of courses, See results of exams, Download files that teachers uploaded, Sent message to teachers.

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
Once pip has finished downloading the dependencies:

	(env)$ python manage.py runserver
	
And navigate to http://127.0.0.1:8000/.
