from django.db import models
from django.urls import reverse
from datetime import date

# MEALS = (
#     ('B', 'Breakfast'),
#     ('L', 'Lunch'),
#     ('D', 'Dinner')
# )

# class Toy(models.Model):
#   name = models.CharField(max_length=50)
#   color = models.CharField(max_length=20)

#   def __str__(self):
#     return self.name

#   def get_absolute_url(self):
#     return reverse('toys_detail', kwargs={'pk': self.id})

class Bird(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
#   tree = models.ManyToManyField(Tree)

  # ownership feild (relationship to the user)
#   user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

#   def get_absolute_url(self):
#     return reverse('detail', kwargs={'cat_id': self.id})

#   def fed_for_today(self):
#     return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

# class Feeding(models.Model):
#   date = models.DateField('feeding date')
#   meal = models.CharField(
#     max_length=1,
#     choices=MEALS,
#     default=MEALS[0][0]
#   )
#   cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

#   def __str__(self):
#     # Nice method for obtaining the friendly value of a Field.choice
#     return f"{self.get_meal_display()} on {self.date}"

#   # change the default sort
#   class Meta:
#     ordering = ['-date']

# class Photo(models.Model):
#     # store the URL of the image on AWS
#     url = models.CharField(max_length=200)
#     # Relationship to the cat
#     cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

#     def __str__(self):
#       return f"Photo for cat id #{self.cat_id} @ {self.url}"