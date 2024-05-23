from django.db import models



# Create your models here.
class Baby(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=150)
    parents_name = models.CharField(max_length=150)
    drop_off = models.CharField(max_length=150)
    pickedby = models.CharField(max_length=150)
    periodofstay = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    time_in =models.DateTimeField( auto_now_add=True)
    time_out = models.CharField(max_length=150)


    def __str__(self):

       return self.first_name +  "    "  + self.last_name


class  Sitter(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=150)
    next_of_kin = models.CharField(max_length=100)
    NIN = models.CharField(max_length=150)
    recommender_name = models.CharField(max_length=150)
    level_of_education = models.CharField(max_length=150)
    sitter_number = models.CharField(max_length=150)
    contacts = models.CharField(max_length=150)


    def __str__(self):
       return self.name +  "    "  + self.next_of_kin


class Doll(models.Model):
    doll_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField(max_length=100)
    

    def __str__(self):
        return self.doll_name 


class Procurement(models.Model):
    name_of_item = models.CharField(max_length=100)
    quantity = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name_of_item


class  AssignProcurement(models.Model):
    name_of_item = models.ForeignKey(Procurement, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    babyname = models.ForeignKey(Baby, on_delete=models.CASCADE)

class DollSales(models.Model):
    doll_name = models.ForeignKey(Doll, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    babyname = models.ForeignKey(Baby, on_delete=models.CASCADE)
    price_of_doll = models.IntegerField()   












      