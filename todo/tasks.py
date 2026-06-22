from celery import shared_task
import time

from django.core.mail import send_mail

# Celery Task
@shared_task
def print_message():
    
    print("Task Started")
    
    time.sleep(5)
    
    print("Task Completed")
    
    return "Done"



## Start celery worker : 
"""
    celery -A todo_project worker --loglevel=info

                (OR)
                
    celery -A todo_project worker --pool=solo --loglevel=info
    
    
    
python manage.py shell   

In [1]: from todo.tasks import print_message
   ...: 
   ...: result = print_message.delay()
   ...: 
   ...: result.status
Out[1]: 'PENDING'

In [2]: result.status
Out[2]: 'SUCCESS'

In [3]: result.status
Out[3]: 'SUCCESS'

In [4]: result.get()
Out[4]: 'Done'

In [5]: result.ready()
Out[5]: True

In [6]: 
""" 


@shared_task
def send_welcome_email():
    
    print("Sending Email...")
    
    send_mail(subject = "Welcome", message = 'Welcome to our Django + Celery app', from_email = 'admin@example.com',recipient_list = ['sahil@example.com'],fail_silently = False,)
    
    return 'Email Sent'