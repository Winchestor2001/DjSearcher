from django.db import models


class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Subject(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    downloads = models.BigIntegerField(default=0)
    file_size = models.FloatField(default=0)
    file = models.FileField(upload_to='all_files/')

    def __str__(self):
        return str(self.name)



