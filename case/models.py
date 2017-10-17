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
	inventory_cost = models.PositiveIntegerField(default=4, null=False, blank=False)
	monthly_order1 = models.PositiveIntegerField(verbose_name="Marks and Maxwell",validators=[MaxValueValidator(60)], default=0, help_text="Max Value is 60")
	monthly_order2 = models.PositiveIntegerField(verbose_name="Chopra and Company",validators=[MaxValueValidator(75)], default=0, help_text="Max Value is 75")
	monthly_order3 = models.PositiveIntegerField(verbose_name="Daggit Enterprises",validators=[MaxValueValidator(100)], default=0, help_text="Max Value is 100")
	bull_whip_factor = models.BooleanField(verbose_name="Disclose the demand with Vendors",default=False)
	mod_count = models.PositiveIntegerField(default=0)


	def __str__(self):
		return ("%s")%self.design


	def save(self):
		self.mod_count +=1
		return super(Product, self).save()

	@property
	def month1_vendor1(self):
		return self.monthly_order1
	@property
	def month2_vendor1(self):
		return self.monthly_order1

	@property
	def month3_vendor1(self):
		return self.monthly_order1 

	@property
	def month1_vendor2(self):
		return 0
	@property
	def month2_vendor2(self):
		return self.monthly_order2

	@property
	def month3_vendor2(self):
		return self.monthly_order2

	@property
	def month1_vendor3(self):
		return 0
	@property
	def month2_vendor3(self):
		return 0

	@property
	def month3_vendor3(self):
		return 0

	@property
	def month1(self):
		return self.month1_vendor1+self.month1_vendor2+self.month1_vendor3 

	@property
	def month2(self):
		return self.month2_vendor1+self.month2_vendor2+self.month2_vendor3 

	@property
	def month3(self):
		return self.month3_vendor1+self.month3_vendor2+self.month3_vendor3 


class Product2(models.Model):
	#user = models.ForeignKey(User)
	design = models.BooleanField(default=False)
	battery = models.BooleanField(default=False)
	gestures = models.BooleanField(default=False)
	durability = models.BooleanField(default=False)
	inventory_cost = models.PositiveIntegerField(default=4, null=False, blank=False)
	monthly_order1 = models.PositiveIntegerField(verbose_name="Marks and Maxwell",validators=[MaxValueValidator(60)], default=0, help_text="Max Value is 60")
	monthly_order2 = models.PositiveIntegerField(verbose_name="Chopra and Company",validators=[MaxValueValidator(75)], default=0, help_text="Max Value is 75")
	monthly_order3 = models.PositiveIntegerField(verbose_name="Daggit Enterprises",validators=[MaxValueValidator(100)], default=0, help_text="Max Value is 100")
	bull_whip_factor = models.BooleanField(verbose_name="Disclose the demand with Vendors",default=False)
	mod_count = models.PositiveIntegerField(default=0)


	def __str__(self):
		return ("%s")%self.design
	def save(self):
		self.mod_count +=1
		return super(Product2,self).save()

	@property
	def month4_vendor1(self):
		return self.monthly_order1
	@property
	def month5_vendor1(self):
		return self.monthly_order1

	@property
	def month6_vendor1(self):
		return self.monthly_order1 

	@property
	def month4_vendor2(self):
		return 0
	@property
	def month5_vendor2(self):
		return self.monthly_order2

	@property
	def month6_vendor2(self):
		return self.monthly_order2

	@property
	def month4_vendor3(self):
		return 0
	@property
	def month5_vendor3(self):
		return 0

	@property
	def month6_vendor3(self):
		return 0

	@property
	def month4(self):
		return self.month4_vendor1+self.month4_vendor2+self.month4_vendor3 

	@property
	def month5(self):
		return self.month5_vendor1+self.month5_vendor2+self.month5_vendor3 

	@property
	def month6(self):
		return self.month6_vendor1+self.month6_vendor2+self.month6_vendor3 

class Product3(models.Model):
	#user = models.ForeignKey(User)
	design = models.BooleanField(default=False)
	battery = models.BooleanField(default=False)
	gestures = models.BooleanField(default=False)
	durability = models.BooleanField(default=False)
	inventory_cost = models.PositiveIntegerField(default=4, null=False, blank=False)
	monthly_order1 = models.PositiveIntegerField(verbose_name="Marks and Maxwell",validators=[MaxValueValidator(60)], default=0, help_text="Max Value is 60")
	monthly_order2 = models.PositiveIntegerField(verbose_name="Chopra and Company",validators=[MaxValueValidator(75)], default=0, help_text="Max Value is 75")
	monthly_order3 = models.PositiveIntegerField(verbose_name="Daggit Enterprises",validators=[MaxValueValidator(100)], default=0, help_text="Max Value is 100")
	bull_whip_factor = models.BooleanField(verbose_name="Disclose the demand with Vendors",default=False)
	mod_count = models.PositiveIntegerField(default=0)


	def __str__(self):
		return ("%s")%self.design

	def save(self):
		self.mod_count +=1
		return super(Product3,self).save()

	@property
	def month7_vendor1(self):
		return self.monthly_order1
	@property
	def month8_vendor1(self):
		return self.monthly_order1

	@property
	def month9_vendor1(self):
		return self.monthly_order1 

	@property
	def month7_vendor2(self):
		return 0
	@property
	def month8_vendor2(self):
		return self.monthly_order2

	@property
	def month9_vendor2(self):
		return self.monthly_order2

	@property
	def month7_vendor3(self):
		return 0
	@property
	def month8_vendor3(self):
		return 0

	@property
	def month9_vendor3(self):
		return 0

	@property
	def month7(self):
		return self.month7_vendor1+self.month7_vendor2+self.month7_vendor3 

	@property
	def month8(self):
		return self.month8_vendor1+self.month8_vendor2+self.month8_vendor3 

	@property
	def month9(self):
		return self.month9_vendor1+self.month9_vendor2+self.month9_vendor3 

class Product4(models.Model):
	#user = models.ForeignKey(User)
	design = models.BooleanField(default=False)
	battery = models.BooleanField(default=False)
	gestures = models.BooleanField(default=False)
	durability = models.BooleanField(default=False)
	inventory_cost = models.PositiveIntegerField(default=4, null=False, blank=False)
	monthly_order1 = models.PositiveIntegerField(verbose_name="Marks and Maxwell",validators=[MaxValueValidator(60)], default=0, help_text="Max Value is 60")
	monthly_order2 = models.PositiveIntegerField(verbose_name="Chopra and Company",validators=[MaxValueValidator(75)], default=0, help_text="Max Value is 75")
	monthly_order3 = models.PositiveIntegerField(verbose_name="Daggit Enterprises",validators=[MaxValueValidator(100)], default=0, help_text="Max Value is 100")
	bull_whip_factor = models.BooleanField(verbose_name="Disclose the demand with Vendors",default=False)
	mod_count = models.PositiveIntegerField(default=0)


	def __str__(self):
		return ("%s")%self.design

	def save(self):
		self.mod_count +=1
		return super(Product4,self).save() 

	@property
	def month10_vendor1(self):
		return self.monthly_order1
	@property
	def month11_vendor1(self):
		return self.monthly_order1

	@property
	def month12_vendor1(self):
		return self.monthly_order1 

	@property
	def month10_vendor2(self):
		return 0
	@property
	def month11_vendor2(self):
		return self.monthly_order2

	@property
	def month12_vendor2(self):
		return self.monthly_order2

	@property
	def month10_vendor3(self):
		return 0
	@property
	def month11_vendor3(self):
		return 0

	@property
	def month12_vendor3(self):
		return 0

	@property
	def month10(self):
		return self.month10_vendor1+self.month10_vendor2+self.month10_vendor3 

	@property
	def month11(self):
		return self.month11_vendor1+self.month11_vendor2+self.month11_vendor3 

	@property
	def month12(self):
		return self.month12_vendor1+self.month12_vendor2+self.month12_vendor3 

class Forcast(models.Model):
	
	forcast = models.PositiveIntegerField(blank=False,default=60)


	def __str__(self):
		return self.forcast
# class Vendor(models.Model):
# 	user = models.ForeignKey(User)
# 	monthly_order1 = models.PositiveIntegerField(verbose_name="Marks and Maxwell",validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
# 	monthly_order2 = models.PositiveIntegerField(verbose_name="Chopra and Company",validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
# 	monthly_order3 = models.PositiveIntegerField(verbose_name="Daggit Enterprises",validators=[MaxValueValidator(30)], default=0, help_text="Max Value is 30")

# 	def __str__(self):
# 		return self.user.username 












