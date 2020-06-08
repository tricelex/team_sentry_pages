from django.db import models




class AddPage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title