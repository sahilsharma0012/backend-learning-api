from celery import shared_task
import time
from datetime import datetime

from django.core.mail import send_mail

from pypdf import PdfReader

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


# @shared_task
# def send_welcome_email():
    
#     print("Sending Email...")
    
#     send_mail(subject = "Welcome", message = 'Welcome to our Django + Celery app', from_email = 'admin@example.com',recipient_list = ['sahil@example.com'],fail_silently = False,)
    
#     return 'Email Sent'


# @shared_task
# def send_welcome_email(email):
    
#     print("Sending Email...")
    
#     send_mail(subject = "Welcome", message = "Welcome to Django and Celery app", from_email = "admin@example.com", recipient_list = [email], fail_silently = False)
    
#     return f"Email Sent to {email}"


"""
In [1]: from todo.tasks import send_welcome_email

In [2]: result = send_welcome_email.apply_async(args = ["test@example.com"], countdown = 10)

In [3]: result.status
Out[3]: 'SUCCESS'

In [4]: result = send_welcome_email.apply_async(args = ["test@example.com"], countdown = 10)

In [5]: result.status
Out[5]: 'PENDING'

In [6]: result.status
Out[6]: 'PENDING'

In [7]: result.status
Out[7]: 'PENDING'

In [8]: result.status
Out[8]: 'PENDING'

In [9]: result.status
Out[9]: 'PENDING'

In [10]: result.status
Out[10]: 'PENDING'

In [11]: result.status
Out[11]: 'PENDING'

In [12]: result.status
Out[12]: 'SUCCESS'

In [13]: result = send_welcome_email.apply_async(args = ["test@example.com"], countdown = 10) # send_welcome_email.delay("test@example.com")

In [14]: result.get()
Out[14]: 'Email Sent to test@example.com'

In [15]: result.status
Out[15]: 'SUCCESS'

In [16]: result = send_welcome_email.apply_async(args = ["test@example.com"], countdown = 10)  

In [17]: result.ready()
Out[17]: False

In [18]: result.ready()
Out[18]: True

In [19]: result.status
Out[19]: 'SUCCESS'

In [20]:     
    
"""


@shared_task(bind = True, max_tries = 3)
def send_welcome_email(self, email):
    
    try:
        print(f"Sendig Email To {email}")
        
        # # force an error intentionally
        # x = 10 / 0

        
        send_mail(subject = "Wlecome", message = "Welcome to our Django + Celery", from_email = "admin@example.com", recipient_list = [email], fail_silently = False)
        
        return f"Email Send to {email}"
    
    except Exception as exc:
        raise self.retry(exc = exc, countdown = 5)
    

#####
########
###########
    
@shared_task
def print_current_time():
    
    print(f"current Time : {datetime.now()}")
    
    return "Time Printed"

"""
Start the celery beat : celery -A todo_project beat --loglevel=info

"""


####
######
#########

@shared_task
def add(x, y):
    
    print(f"Adding {x} + {y}")
    return x + y


@shared_task
def multiply(result):
    
    print(f"Multiplying {result} * 10")
    return result * 10

"""
In [1]: from celery import chain

In [2]: from todo.tasks import add, multiply

In [3]: result = chain(add.s(5,5), multiply.s())()

In [4]: result.get()
Out[4]: 100


"""



####
######
########

@shared_task
def square(x):
    time.sleep(3)
    return x**2


@shared_task
def cube(x):
    time.sleep(3)
    return x*x*x 


@shared_task
def double(x):
    time.sleep(3)
    return x*2

"""
    In [1]: from celery import group

In [2]: from todo.tasks import square, cube, double

In [3]: result = group(square.s(5), cube.s(5), double.s(5))()

In [4]: result
Out[4]: <GroupResult: 5613e2f6-12f3-4247-abf4-677ae4ce5135 [af4a8e70-ed6c-4a6c-8b38-4ee4892fcf76, 071f1f98-7a86-41db-ba77-c19e453c12e2, e782d915-e96d-4e3d-bcf3-7e83a086a642]>

In [5]: result.ready()
Out[5]: True
    
"""


####
######
########

@shared_task
def add_result(results):
    return sum(results)

"""
In [1]: from celery import chord

In [2]: from todo.tasks import square, cube, double, add_result

In [3]: result = chord([square.s(5), cube.s(5), double.s(5)])(add_result.s())

In [4]: result.get()
Out[4]: 160
    
"""


####
######
#########

@shared_task
def process_todo_creation(title):
    
    print(f"Started Processing : {title}")
    
    time.sleep(10)
    
    print(f"Finished Processing : {title}")
    
    return "Task Completed"



####
#######
###########

@shared_task
def process_pdf(file_path):
    
    print("Started PDF Processing...")
    
    reader = PdfReader(file_path)
    
    text = ""
    
    for page in reader.pages:
        text += page.extract_text()
        
    print(text[:300])
    
    return "PDF Processed"


