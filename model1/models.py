from django.db import models

class Team(models.Model):
	name = models.CharField(max_length = 60)
	location = models.CharField(max_length = 60)
	payroll = models.IntegerField()

class Player(models.Model):
	name = models.CharField(max_length=20)
	number = models.CharField(max_length=20)
	height = models.CharField(max_length=20)
	weight = models.CharField(max_length=20)
	hand = models.CharField(max_length=20)
	team = models.ForeignKey(Team, default = '', on_delete=models.CASCADE)

