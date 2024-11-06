from django.db import models

#creating company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)             
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT','IT'), ('Non IT', 'Non IT')))  # these are tuples
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # def __str__(self):   # this return human readable representation
    #     return self.name


#creating employee model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    position = models.CharField(max_length=50, choices=(('Manager', 'Manager'), ('Backend Developer', 'Backend Developer'), ('Frontend Developer', 'Frontend Developer')))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)  #CASCADE: Deletes all related objects when the referenced object is deleted.

    def __str__(self):
        return self.name
