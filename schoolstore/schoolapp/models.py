
# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ManyToManyField('Department',blank=True)
    course = models.ManyToManyField('Course',blank=True)
    purpose = models.CharField(max_length=50, choices=[('enquiry', 'Enquiry'), ('place_order', 'Place Order'), ('return', 'Return')])
    materials_provide = models.ManyToManyField(
        'Material',
        blank=True,
    )

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
