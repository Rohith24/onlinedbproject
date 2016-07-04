from __future__ import unicode_literals

from idlelib.idle_test.test_io import S

from django.db import models

# Create your models here.
class College(models.Model):
    name=models.CharField(max_length=100)
    Acronym=models.CharField(max_length=10)
    location=models.CharField(max_length=25)
    contact=models.EmailField()

    def __unicode__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=100)
    college=models.ForeignKey(College)
    emailid=models.EmailField(max_length=256)
    dbnames=models.CharField(max_length=100)
    droppedout=models.BooleanField(default=0,max_length=1)

    def __unicode__(self):
        return self.name

class Mark(models.Model):
    student=models.OneToOneField(Student)
    transform=models.IntegerField()
    from_custom_base26=models.IntegerField()
    get_pig_latin=models.IntegerField()
    top_chars=models.IntegerField()
    total=models.IntegerField()

    def __unicode__(self):
        return str(self.student)

class Teachers(models.Model):
    name=models.CharField(max_length=30)
    college=models.ForeignKey(College)
    def __unicode__(self):
        return self.name
