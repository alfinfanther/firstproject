# firstproject
sample coding

#install redis server
for run this app, you must install redis server

#celery worker
celery -A firstproject worker -l info 

#celery beat
celery -A firstproject beat -l info
