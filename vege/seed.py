from faker import Faker
fake = Faker()
import random
from .models import *

def seed_db(n=10)->None:
  try:  
        department_obj = Department.objects.all() 
        for i in range(0,n):
             
            random_idx= random.randint(0, len(department_obj)-1)
            dept_obj= department_obj[random_idx]

            student_id_str= f"STU-0{random.randint(100,999)}"
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()
        

            student_id_obj = StudentID.objects.create(student_id=student_id_str)
        
            student_obj=Student.objects.create(
            department = dept_obj,
            student_id = student_id_obj,
            student_name = student_name,
            student_email = student_email,
            student_age = student_age,
            student_address = student_address,
            )

  except Exception as e:
      print(e)