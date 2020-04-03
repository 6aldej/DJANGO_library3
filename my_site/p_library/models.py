from django.db import models

class Author(models.Model):  
    full_name = models.CharField(max_length=120)  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Friend(models.Model):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=12)
    vk = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='covers', blank=True)
    full_count = models.BooleanField(default=True)
    publisher = models.ForeignKey('Publisher',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='books'
        )
    friends = models.ManyToManyField(Friend, blank=True)

    def __str__(self):
        return self.title

class Publisher(models.Model):
    title=models.CharField(max_length=120)
    def __str__(self):
        return self.title
