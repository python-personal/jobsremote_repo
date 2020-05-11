import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','completeproject.settings')
import django
django.setup()
from completeapp.models import *
from faker import Faker
from random import *
fake=Faker()
# def phonenumbergen():
#      d1=randint(7,9)
#      num=''+str(d1)
#      for i in range(9):
#           num=num+str(randint(0,9))
#           return int(num)

def populate(n):
    for i in range(n):
        fname=fake.name()
        fmarks=fake.random_int(min=1,max=100)
        frollno=fake.random_int(min=1,max=999)
        faddress=fake.address()
        student_record=Student.objects.get_or_create('name':fname,'marks':fmarks,'rollno':frollno,'address':faddress)
        # fdate=fake.date()
        # fcompany=fake.company()
        # ftitle=fake.random_element(elements=('project Manager','Team Leader','software Engineer'))
        # feligibility=fake.random_element(elements=('BTech','MTech','MCA','MBA'))
        # femail=fake.email()
        # fphonenumber=phonenumbergen()
        # hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
        # chennaijobs_record=chennaijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
populate(10)
