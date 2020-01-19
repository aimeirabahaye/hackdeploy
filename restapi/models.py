from django.db import models

# Create your models here.

class Poster(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='')
    description = models.CharField(max_length=250)
    class Meta:
        ordering = ('last_name',)


class Worker(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='')
    description = models.CharField(max_length=250)
    rating = models.fields.IntegerField(default=5)

    class Meta:
        ordering = ('last_name',)

class Message(models.Model):
    worker_id = models.fields.IntegerField(default=0)
    task_id = models.fields.IntegerField(default=0) 
    message_content = models.CharField(max_length=250)

class Task(models.Model):
    taskName = models.fields.CharField(max_length=45)
    poster_id = models.fields.IntegerField(default=0)
    HOUSE_KEEPING = 'HK'
    REPAIRS = "REP"
    DELIVERY = "DEL"

    CATEGORIES = (
        (HOUSE_KEEPING, 'House Keeping'),
        (REPAIRS, 'Repairs'),
        (DELIVERY, "Del"),
    )

    category = models.CharField(
        max_length=3,
        choices=CATEGORIES,
        default=HOUSE_KEEPING,
    )

    description = models.CharField(max_length=500)

    dueDate = models.DateField()
    latitude = models.DecimalField(decimal_places=6,max_digits=10)
    longtitude =  models.DecimalField(decimal_places=6,max_digits=10)
    status = models.BooleanField(default=False)
