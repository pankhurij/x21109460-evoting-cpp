cd evoting
# Install dependencies
pip install pipenv

pipenv shell
# Install django
pipenv install django

cd evoting
# Serve on localhost:8000
python manage.py runserver
A pipeline starts by default when a change has taken 
place in the code's source . AWS Code Pipeline would 
pull the source code for the pipeline directly from 
GitHub.
At the same time the stages like build, test, and 
deployment actions would run one by one in parallel 
in order to increase the workflow speeds and we can 
say any update we make to script it goes through a 
series of continuous processes before being deployed.
The last step is again the deployment, as we have 
already chosen the deployment method i.e AWS 
Elastic beanstalk. So, it would deploy the changes with 
the help of AWS EBS.
