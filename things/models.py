from django.db import models
from polymorphic import PolymorphicModel


class Person(PolymorphicModel):

    p_id = models.CharField(max_length=10)
    

class Thing(models.Model):

    t_id = models.CharField(max_length=10)  


class LivePeople(Person):
    
    age = models.IntegerField(max_length=2)

class DeadPeople(Person):
    
    age_at_death = models.IntegerField(max_length=2)



class LiveThings(models.Model):

    thing = models.ForeignKey(Thing)
    person = models.ForeignKey(LivePeople, unique=True)


class DeadThings(models.Model):

    thing = models.ForeignKey(Thing)
    person = models.ForeignKey(DeadPeople, unique=True)