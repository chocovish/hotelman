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
    company_name = models.CharField(max_length=30,null=True,blank=True)
    address = models.CharField(max_length=60,null=True,blank=True)
    phone = models.CharField(max_length=13,null=True,blank=True)
    person_count = models.CharField(max_length=30)
    gstin = models.CharField(max_length=30,blank=True,null=True)
    date = models.DateField()

    room_no = models.CharField(max_length=7)
    check_in = models.DateField()
    check_out = models.DateField()
    days_count = models.IntegerField()
    rate = models.IntegerField()

    room_no_2 = models.CharField(max_length=7,blank=True, null=True)
    check_in_2 = models.DateField(blank=True, null=True)
    check_out_2 = models.DateField(blank=True, null=True)
    days_count_2 = models.IntegerField(default=0)
    rate_2 = models.IntegerField(default=0)


    room_no_3 = models.CharField(max_length=7,blank=True, null=True)
    check_in_3 = models.DateField(blank=True, null=True)
    check_out_3 = models.DateField(blank=True, null=True)
    days_count_3 = models.IntegerField(default=0)
    rate_3 = models.IntegerField(default=0)

    discount = models.IntegerField(default=0)
    is_gst = models.BooleanField(default=False)

    def gst(self):
        gst = 0
        if self.rate>=1000: gst = (self.days_count*self.rate)*6/100
        if self.rate_2 >= 1000: gst = gst + ((self.days_count_2*self.rate_2)*6/100)
        if self.rate_3>=1000: gst = gst + ((self.days_count_3*self.rate_3)*6/100)
        return gst

    def total(self): return (self.rate*self.days_count)
    def total_2(self): return (self.rate_2*self.days_count_2)
    def total_3(self): return (self.rate_3*self.days_count_3)
    
    def total_with_gst(self): return (self.total() + self.total_2() + self.total_3() + self.gst()*2) - self.discount
    
    def __str__(self): return self.name+ " " + self.room_no


class Count(models.Model):
    value = models.IntegerField()