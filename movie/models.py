from django.db import models

# Create your models here.
CATEGRY_CHOICES = (
    ('A', 'ACTION'),
    ('B', 'DRAMA'),
    ('C', 'COMEDY'),
    ('D', 'ROMANCE')
)
LANGUAGE_CHOICES = (
    ('EN', 'ENGLISH'),
    ('YR', 'YORUBA')
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MA', 'MOST ADDED'),
    ('TR', 'TOP RATED')
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    descripton = models.TextField(max_length=200)
    image = models.ImageField(default="movie.jpg", upload_to="movies")
    category = models.CharField(choices=CATEGRY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=False)


    def __str__(self):
        return self.title

