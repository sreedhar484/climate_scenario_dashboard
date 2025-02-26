from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='pics',default='default.png')
    bio = models.TextField(default=None,blank=True)
    role = (('participent', 'Participent'), ('admin', 'Admin'))
    acc_type = models.CharField(max_length=100, choices=role, default='participent')

    def __str__(self):
        return self.user.username

class ConsentDocument(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = RichTextField(blank=True,null=True)
    version = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ConsentStatus(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('signed', 'Signed'),
        ('declined', 'Declined'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(ConsentDocument, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    signed_at = models.DateTimeField(null=True, blank=True)
    declined_at = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(blank=True)

class AuditLog(models.Model):
    ACTION_CHOICES = (
        ('document_upload', 'Document Upload'),
        ('consent_signed', 'Consent Signed'),
        # Add more choices as needed
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()


class corban_pricing(models.Model):
    model_name = models.CharField(max_length=100)
    scenario = models.CharField(max_length=100)
    region_category = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    variable = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    year_2020 = models.FloatField()
    year_2025 = models.FloatField()
    year_2030 = models.FloatField()
    year_2035 = models.FloatField()
    year_2040 = models.FloatField()
    year_2045 = models.FloatField()
    year_2050 = models.FloatField()
    year_2055 = models.FloatField()
    year_2060 = models.FloatField()
    year_2065 = models.FloatField()
    year_2070 = models.FloatField()
    year_2075 = models.FloatField()
    year_2080 = models.FloatField()
    year_2085 = models.FloatField()
    year_2090 = models.FloatField()
    year_2095 = models.FloatField()
    year_2100 = models.FloatField()
    def __str__(self):
        return self.region
    
class economic_forecast(models.Model):
    model_name = models.CharField(max_length=100)
    scenario = models.CharField(max_length=100)
    region_category = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    variable = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    year_2020 = models.FloatField(default=0)
    year_2025 = models.FloatField(default=0)
    year_2030 = models.FloatField(default=0)
    year_2035 = models.FloatField(default=0)
    year_2040 = models.FloatField(default=0)
    year_2045 = models.FloatField(default=0)
    year_2050 = models.FloatField(default=0)
    year_2055 = models.FloatField(default=0)
    year_2060 = models.FloatField(default=0)
    year_2070 = models.FloatField(default=0)
    year_2080 = models.FloatField(default=0)
    year_2090 = models.FloatField(default=0)
    year_2100 = models.FloatField(default=0)
    def __str__(self):
        return self.region
    

class co2_emission(models.Model):
    model_name = models.CharField(max_length=100)
    scenario = models.CharField(max_length=100)
    region_category = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    variable = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    year_2020 = models.FloatField()
    year_2025 = models.FloatField()
    year_2030 = models.FloatField()
    year_2035 = models.FloatField()
    year_2040 = models.FloatField()
    year_2045 = models.FloatField()
    year_2050 = models.FloatField()
    year_2055 = models.FloatField()
    year_2060 = models.FloatField()
    year_2065 = models.FloatField()
    year_2070 = models.FloatField()
    year_2075 = models.FloatField()
    year_2080 = models.FloatField()
    year_2085 = models.FloatField()
    year_2090 = models.FloatField()
    year_2095 = models.FloatField()
    year_2100 = models.FloatField()
    def __str__(self):
        return self.region
    
class energy_cost(models.Model):
    model_name = models.CharField(max_length=100)
    scenario = models.CharField(max_length=100)
    region_category = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    variable = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    year_2020 = models.FloatField()
    year_2025 = models.FloatField()
    year_2030 = models.FloatField()
    year_2035 = models.FloatField()
    year_2040 = models.FloatField()
    year_2045 = models.FloatField()
    year_2050 = models.FloatField()
    year_2055 = models.FloatField()
    year_2060 = models.FloatField()
    year_2065 = models.FloatField()
    year_2070 = models.FloatField()
    year_2075 = models.FloatField()
    year_2080 = models.FloatField()
    year_2085 = models.FloatField()
    year_2090 = models.FloatField()
    year_2095 = models.FloatField()
    year_2100 = models.FloatField()
    def __str__(self):
        return self.region