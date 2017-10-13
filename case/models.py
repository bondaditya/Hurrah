from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class Demand(models.Model):
	employee_name1 = models.CharField(max_length=120, blank=False, default = 'Aditya')
	monthly_forcast1 = models.PositiveIntegerField(default=60, blank = False)
	monthly_forcast_update1 = models.PositiveIntegerField(default=60, blank = False)
	employee_name2 = models.CharField(max_length=120, blank=False, default = 'Aditya')
	monthly_forcast2 = models.PositiveIntegerField(default=60, blank = False)
	monthly_forcast_update2 = models.PositiveIntegerField(default=60, blank = False)
	employee_name3 = models.CharField(max_length=120, blank=False, default = 'Aditya')
	monthly_forcast3 = models.PositiveIntegerField(default=60, blank = False)
	monthly_forcast_update3 = models.PositiveIntegerField(default=60, blank = False)
	employee_name4 = models.CharField(max_length=120, blank=False, default = 'Aditya')
	monthly_forcast4 = models.PositiveIntegerField(default=60, blank = False)
	monthly_forcast_update4 = models.PositiveIntegerField(default=60, blank = False)





	def __str__(self): 
		return self.employee_name1

class Product(models.Model):
	#user = models.ForeignKey(User)
	design = models.BooleanField(default=False)
	battery = models.BooleanField(default=False)
	gestures = models.BooleanField(default=False)
	durability = models.BooleanField(default=False)
	inventory_cost = models.PositiveIntegerField(default=4, blank=False)
	monthly_order1 = models.PositiveIntegerField(verbose_name="Marks and Maxwell",validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
	monthly_order2 = models.PositiveIntegerField(verbose_name="Chopra and Company",validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
	monthly_order3 = models.PositiveIntegerField(verbose_name="Daggit Enterprises",validators=[MaxValueValidator(30)], default=0, help_text="Max Value is 30")
	bull_whip_factor = models.BooleanField(verbose_name="Disclose the demand with Vendors",default=False)


	def __str__(self):
		return self.user.username 

class Forcast(models.Model):
	
	forcast = models.PositiveIntegerField(blank=False,default=60)


	def __str__(self):
		return self.user.usernam 

# class Vendor(models.Model):
# 	user = models.ForeignKey(User)
# 	monthly_order1 = models.PositiveIntegerField(verbose_name="Marks and Maxwell",validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
# 	monthly_order2 = models.PositiveIntegerField(verbose_name="Chopra and Company",validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
# 	monthly_order3 = models.PositiveIntegerField(verbose_name="Daggit Enterprises",validators=[MaxValueValidator(30)], default=0, help_text="Max Value is 30")

# 	def __str__(self):
# 		return self.user.username 












