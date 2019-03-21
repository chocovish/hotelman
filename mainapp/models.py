from django.db import models

# Create your models here.
class Room(models.Model):
    room_no = models.CharField(max_length=5,unique=True)
    description = models.CharField(max_length=100,default="No description given")

    def __str__(self):
        return self.room_no + " " + self.description

class Invoice(models.Model):
    invoice_no = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30,blank=True)
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=13)
    person_count = models.CharField(max_length=30)
    gstin = models.CharField(max_length=30,blank=True,null=True)
    date = models.DateField()
    room_no = models.CharField(max_length=7)
    check_in = models.DateField()
    check_out = models.DateField()
    days_count = models.IntegerField()
    rate = models.IntegerField()
    discount = models.IntegerField()
    is_gst = models.BooleanField(default=False)
    def gst(self):
        if self.rate>=1000:
            gst = (self.days_count*self.rate)*6/100
        else: gst = 0
        return gst

    def total(self): return (self.rate*self.days_count)-self.discount
    
    def total_with_gst(self): return self.total() + self.gst()
    
    
    def __str__(self): return self.name+ " " + self.room_no