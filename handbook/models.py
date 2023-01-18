from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


COMPANY_TYPES_CHOICES=(
    ("Internet Shop","3 жас"),
    ("SuperMarket","4 жас"),
    ("Shopping center","5 жас"),
    ("Furniture Shop","6 жас"),
    ("IT Company","Қосымша ақпарат"),
    ("Educational Center","Жаңалықтар")
)
COMPANY_RATE_CHOICES=(
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5")
)


# Create your models here.
class Company(models.Model):
    company_name=models.CharField(verbose_name='Курс тақырыбы',max_length=40,blank=True)
    company_about=models.TextField(verbose_name='Курс сипаттамасы',blank=True)
    company_phone=models.CharField(verbose_name='Байланыс',max_length=30,blank=True)
    comapny_category=models.CharField(verbose_name='Қай жасқа арналған',max_length=40,choices=COMPANY_TYPES_CHOICES,blank=True)
    company_email=models.EmailField(verbose_name='Email',blank=True)
    company_logo=models.ImageField(verbose_name='Сурет орналастыру',blank=True,upload_to='logos/',null=True,default='settings.MEDIA_ROOT/logos/1.png')
    company_video=models.FileField(verbose_name='Видео орналастыру',blank=True,upload_to='logos/',null=True,default='settings.MEDIA_ROOT/logos/earth.mp4')
    published_date=models.DateTimeField(blank=True, null=True)

    def get_media_url(self):
        return self.company_logo.url.replace('media/','')
    #def get_video_url(self):
    #    return self.company_video.url.replace('media/','')
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.company_name

class Rate(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    rate=models.CharField(max_length=150,choices=COMPANY_RATE_CHOICES)
    

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.company)+":"+self.rate

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
        
    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class videos(models.Model):
    video_id = models.CharField(blank=False, max_length=32)
    file_name = models.CharField(blank=False, max_length=500)
    def __str__(self):
        return self.id