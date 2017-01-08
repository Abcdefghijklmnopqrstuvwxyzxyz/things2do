from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

# Create your models here.

class ContactItem(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="contact_book");
	contact_list = models.ForeignKey(User, on_delete = models.CASCADE, related_name="friends");

	#Statistics
	login_count = models.PositiveIntegerField('Login Count', default = 1);
	
	def __str__(self):
		return "%s's contact book" % self.user.username;

class Plan(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE);
	name = models.CharField(max_length = 100, verbose_name = "Plan Name");
	create_time = models.DateTimeField('Create time', default = timezone.now());
	start_time = models.DateTimeField('Start time',  default = timezone.now());
	end_time = models.DateTimeField('Plan Deadline');
	last_modified = models.DateTimeField('Last Modified Time', default = timezone.now());
	description = models.TextField('Plan Description', blank = True);
	importance = models.SmallIntegerField('Importance', default=0);

	#Plan porpeties
	is_active = models.BooleanField('Is Active');
	is_complete = models.BooleanField('Is Completed', default = False);
	is_overtime = models.BooleanField('Is Overtime', default = False);

	#NOTE: The location field is for future use.
	#location = models.TextField('Location');
	#For extract information, like location.
	#extract_info = models.FileField();

	def __str__(self):
		return "%s's plan: %s" % (self.user.username, self.name);

	def is_deadline_comming(self):
		return self.end_time - timezone.now() <= timedelta(days=3);


class t2DoApp:
	#FUTURE: A Model class for webpage app on dashboard.
	pass;
