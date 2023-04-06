from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField(max_length=254)
    choices = models.JSONField()

    def __str(self):
       mail = self.email
       topics = self.choices
       return {mail:mail, topics:topics}
    
    class Meta:
        app_label = 'homepage'
    

class NewsArticle(models.Model):
    title = models.CharField(max_length= 400)
    description = models.TextField(max_length= 800)
    news_category = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
