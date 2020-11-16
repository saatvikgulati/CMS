from django.test import TestCase,Client
from .models import Content,Comment
from django.urls import reverse
from .forms import ContentCreateForm,CommentForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from .validators import validate_file_extension
# Create your tests here.
class BasicsTest(TestCase):
    def test_fieldscontent(self):
        item=Content()
        user=User(username="Testing User",password='testing101')
        user.save()
        item.author=user
        item.date_posted=timezone.now()
        item.title='Testing Title'
        item.body='Testing Body'
        item.summary='Testing Summary'
        item.categories='Testing Category'
        item.save()
        record=Content.objects.filter(title='Testing Title').first()
        self.assertEqual(record,item)
    def test_fieldscomment(self):
        item=Content()
        user=User(username="Testing User",password='testing101')
        user.save()
        item.author=user
        item.date_posted=timezone.now()
        item.title='Testing Title'
        item.body='Testing Body'
        item.summary='Testing Summary'
        item.categories='Testing Category'
        item.save()
        item2=Comment()
        user_id=user.id
        item2.post=item
        item2.author=user
        item2.body="Test Body"
        item2.create_on=timezone.now()
        item2.save()
        record=Comment.objects.filter(body='Test Body').first()
        self.assertEqual(record,item2)
class views(TestCase):
    def setUp(self):
        self.register_url=reverse('author-register')
        self.client=Client()
        self.user={
            'username':'Testing User',
            'password':'testing101',
            'password1':'testing101',
        }
    def test_contentlistview(self):
        response=self.client.get(reverse('content-home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateNotUsed(response='content/home.html')
    def test_register_page_loads(self):
        response=self.client.get(reverse('author-register'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateNotUsed(response='content/register.html')
    def test_registration_successful(self):
        response=self.client.post(self.register_url,self.user,format='text/html')
        if response:
            self.assertEqual(response.status_code,200)
    def test_content_create(self):
        response=self.client.get(reverse('content-create'))
        self.assertTemplateNotUsed(response='content/content_form.html')
    def test_content_update(self):
        response=self.client.get(reverse('content-create'))
        self.assertTemplateNotUsed('content/content-detail.html')
    def test_add_comment_to_post(self):
        item=Content()
        user=User(username="Testing User",password='testing101')
        user.save()
        item.author=user
        item.date_posted=timezone.now()
        item.title='Testing Title'
        item.body='Testing Body'
        item.summary='Testing Summary'
        item.categories='Testing Category'
        item.save()
        item_id=Content.objects.filter(id=item.id).first()
        comment=Comment()
        comment.post=item
        comment.author=user
        comment.body='Comment Body'
        comment.create_on=timezone.now()
        comment.save()
        response=self.client.get(reverse('content-detail',item_id))
        self.assertTemplateNotUsed('content/content-detail2.html')

class test_form(TestCase):
    def test_contentcreateform(self):
        upload_file = open("D:\Data Warehousing and mining\Datawarehousingandmining.pdf", 'rb')
        form=ContentCreateForm(data={
            'title':'Testing title',
            'body':'Testing body',
            'summary':'Testing summary',
            'categories':'Testing',
            'pdf': SimpleUploadedFile(upload_file.name, upload_file.read()),
        })
        print(upload_file)
        print(form.errors)
        self.assertTrue(form.is_valid())
    def test_commentform(self):
        form=CommentForm(data={'body':'Testing body'})
        self.assertTrue(form.is_valid())