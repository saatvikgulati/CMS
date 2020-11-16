from django.test import TestCase,Client
from .models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth.models import User
from author.forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.core.validators import RegexValidator
import DNS
DNS.defaults['server']=['8.8.8.8', '8.8.4.4']
# Create your tests here.
class BasicsTest(TestCase):
    def test_fields(self):
        item=Profile()
        user=User(username='Testing User',password='testing101')
        user.save()
        item.user=user
        item.phone='1234567890'
        item.address='Testing address'
        item.city='Testing City'
        item.state='Maharasthra'
        item.country='India'
        item.pincode='400071'
        item.save()
        record=Profile.objects.filter(address='Testing address').first()
        self.assertEqual(record,item)
class TestForms(TestCase):
    def test_UserRegisterationForm(self):
        form=UserRegisterForm(data={
            'username':'Testing_User',
            'first_name':'Test',
            'last_name':'User',
            'email':'rajtester@gmail.com',
            'phone':'1234567890',
            'pincode':'400071',
            'password1':'testing101',
            'password2':'testing101',
        })
        self.assertTrue(form.is_valid())
    def test_UserUpdateForm(self):
        form=UserUpdateForm(data={
            'email':'rajtester@gmail.com',
            'first_name':'Test',
            'last_name':'User1',
        })
        self.assertTrue(form.is_valid())
    def test_ProfileUpdateForm(self):
        upload_file = open("D:\Pics\culturalday.JPG", 'rb')
        form=ProfileUpdateForm(data={
            'country':'IN',
            'city':'Mumbai',
            'state':'Maharasthra',
            'phone':'1234567890',
            'address':'Testing address',
            'pincode':'400071',
            'image':SimpleUploadedFile(upload_file.name, upload_file.read()),
        })
        self.assertTrue(form.is_valid())
class view(TestCase):
    def setUp(self):
        self.register_url=reverse('author-register')
        self.client=Client()
        self.user={
            'username':'Testing User',
            'password':'testing101',
            'password1':'testing101',
        }