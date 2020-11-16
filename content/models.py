from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .validators import validate_file_extension
from django.urls import reverse
# Create your models here.
class Content(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)
    title=models.CharField(max_length=30)
    body=models.TextField(max_length=300)
    summary=models.CharField(max_length=60)
    pdf=models.FileField(upload_to='content_pdf',validators=[validate_file_extension])
    categories=models.CharField(max_length=300)
    def __str__(self):
        return self.title
    def get_absolute_url(self): #the reverse method will return the data as string
        return reverse('content-detail',kwargs={'pk':self.pk})
    def delete(self,*args,**kwargs):
        self.pdf.delete()
        super().delete(*args,**kwargs)
    def save(self, *args, **kwargs):
        try:
            this = Content.objects.get(id=self.id)
            if this.MyFileFieldName != self.MyFileFieldName:
                this.MyFileFieldName.delete()
        except: pass
        super(Content, self).save(*args, **kwargs)

class Comment(models.Model):
    post=models.ForeignKey(Content,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.CharField(max_length=200,default=None)
    create_on=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.body