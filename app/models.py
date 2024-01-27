from django.db import models

# Create your models here.


#homepage
    
class Banner(models.Model):
    sub_text = models.CharField(max_length=100,blank=True)
    primary_text = models.CharField(max_length=100,blank=True)
    primary_sub = models.CharField(max_length=100,blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.primary_text
    
class AboutPic(models.Model):
    image = models.ImageField(upload_to='about-pic-upload/')
    image_title = models.CharField(max_length=50,blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.image_title
    
class HighlightsEvent(models.Model):
    url = models.URLField(max_length=255, blank=True)
    image = models.ImageField(upload_to='highlights-event/')
    title = models.CharField(max_length=50, blank=True)
    time = models.TimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True, verbose_name="Start ng date")
    date_from = models.DateField(blank=True, null=True, verbose_name="End ng date")
    location = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True, null=True)
    link_desc = models.CharField(max_length=255, blank=True)
    details = models.CharField(max_length=100, blank=True, verbose_name="Hosted By")
    
    def __str__(self):
        return self.title
    
class SoftwareTools(models.Model):
    url = models.URLField(max_length=255, blank=True)
    image = models.ImageField(upload_to='software-tools/')
    
class SoftwareToolsResource(models.Model):
    url = models.URLField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='software-resources/')
    desc = models.CharField(max_length=255, blank=True)