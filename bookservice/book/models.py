from django.db import models


class Book(models.Model):
    CATEGORY_OPTIONS = [
        ('Novel', 'Novel'),
        ('Fashion', 'Fashion'),
        ('Cuisine', 'Cuisine'),
        ('Religion', 'Religion'),
        ('Other', 'Other')
    ]

    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    percent_completed = models.DecimalField(decimal_places=2, max_digits=4)
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=25)
    date = models.DateField(default='django.utils.timezone.now')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.title) + ' by ' + str(self.author)
