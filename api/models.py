from django.db import models
import random

# Create your models here.

class Workout(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)  # create an after save function which makes this from the date as words + a random 4 digit number
    notes = models.TextField(blank=True, null=True)
    exercieses = models.ForeignKey(
        Exercise,
        null=True,
        on_delete=models.SET_NULL
    )
    duration = models.DurationField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name
    

    # ---------- functions for creating the name (unique like a url slug) on Workout creation

    # def unique_name_generator(self):
    #     """
    #     Method for generating a random name for each Workout instance upon saving
    #     it.
    #     This method:
    #     -takes the date and converts into a string / formats it to be valid in a url
    #     -generates a random 4 digit number to append to the end of the date string
    #     -returns this string as the name
    #     e.g. 2021-09-01 => 
    #     """
    #     # something like:
    #     date = '18/04/23'
    #     day, month, year = (int(x) for x in date.split('/'))
    #     simple_date = datetime.date(year, month, day)
    #     day_of_week = simple_date.strftime("%A")
    #     random_name = f'{day_of_week}-{month}-{year}-{random.randint(1000, 9999)}'

    #     return random_name

    # def save(self, *agrs, **kwargs):
    #     """
    #     Overrides save method
    #     Sets slug if it doesnt already have one OR if the song name has
    #     been changed.
    #     (The change in the song name is checked by splitting the existing slug
    #     and indexing it so that the number on the end is removed and comparing
    #     it with the song's name split by spaces, if these don't match, then the
    #     name has been updated and so the slug is recreated).
    #     If no audio_file is present, it forces the public
    #     status to be False so that the song can't be displayed to users.
    #     (For custom songs, the song doesn't need to be public for the user
    #     of that song or the admin to view/edit its details)
    #     Calls the save method again.
    #     -FINISH
    #     """

    #     if not self.slug or not self.slug.split('-')[:-1] == self.name.lower().split(' '):
    #         print('setting the slug')
    #         self.slug = self.unique_slug_generator()
    #         print('slug = ', self.slug)

    #     if not self.audio_file:
    #         self.public = False

    #     if not self.image:
    #         self.image = 'placeholder.jpg'
    #     super().save(*agrs, **kwargs)



class Exercise(models.Model):
    """
    Inherits Django's models.Model and represents the Exercise table in the database
    Contains the fields:
    name - required, unique
    type - required, choices
    sets - optional for applicable exercises
    reps - optional for applicable exercises
    weight - optional for applicable exercises, default in kgs
    duration - optional for applicable exercises
    """
    name = models.CharField(max_length=100, null=False, unique=True)
    type = models.CharField(max_length=100, null=False, choices=('Pull', 'Push', 'Legs', 'Core', 'Cardio', 'Other'))
    sets = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)  # will this need to be vairable? (need a range?)
    weight = models.IntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return self.name
