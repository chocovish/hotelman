from django.db import models

# Create your models here.
class Room(models.Model):
    room_no = models.CharField(max_length=5,unique=True)
    description = models.CharField(max_length=100,default="No description given")

    def __str__(self):
        return self.room_no + " " + self.description

class Invoice(models.Model):
    invoice_no = models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30,null=True,blank=True)
    address = models.CharField(max_length=60,null=True,blank=True)
    phone = models.CharField(max_length=13,null=True,blank=True)
    person_count = models.CharField(max_length=30)
    gstin = models.CharField(max_length=30,blank=True,null=True)
    date = models.DateField()

    room_no = models.CharField(max_length=7)
    check_in = models.DateField(verbose_name="Room In")
    check_out = models.DateField(verbose_name="Room Out")
    days_count = models.IntegerField()
    rate = models.IntegerField()

    room_no_2 = models.CharField(max_length=7,blank=True, null=True)
    check_in_2 = models.DateField(blank=True, null=True, verbose_name="Room In 2")
    check_out_2 = models.DateField(blank=True, null=True, verbose_name="Room out 2")
    days_count_2 = models.IntegerField(default=0)
    rate_2 = models.IntegerField(default=0)


    room_no_3 = models.CharField(max_length=7,blank=True, null=True)
    check_in_3 = models.DateField(blank=True, null=True, verbose_name="Room In 3")
    check_out_3 = models.DateField(blank=True, null=True, verbose_name="Room out 3")
    days_count_3 = models.IntegerField(default=0)
    rate_3 = models.IntegerField(default=0)

    discount = models.IntegerField(default=0)
    remark = models.CharField(max_length=50,null=True,blank=True)
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
    def total_without_gst(self): return self.total() + self.total_2() + self.total_3() - self.discount
    def total_days(self): return self.days_count + self.days_count_2 + self.days_count_3

    def final_checkout(self):
        if self.check_out_3: return self.check_out_3
        elif self.check_out_2: return self.check_out_2
        else: return self.check_out

    def room_change(self):
        if self.check_in_3: return [self.check_in_3,self.check_in_2]
        elif self.check_in_2: return [self.check_in_2]
        else: return [None]
        
    
    def __str__(self): return self.name+ " " + self.room_no


class Count(models.Model):
    value = models.IntegerField()