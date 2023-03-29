from django.db import models

# Create your models here.
class Make(models.Model):
	auto = models.CharField(max_length=10)