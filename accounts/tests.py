from django.test import TestCase, Client
from .models import User
import datetime



# Create your tests here.
class TestUserObject(TestCase):
    def setUp(self):
        self.testUserName = 'test1'
        self.testUserEmail = 'test@test.com'
        self.testUserPass = '123test123'
        User.objects.create(username=self.testUserName, email=self.testUserEmail, password=self.testUserPass)

    def test_exists_user(self):
        self.assertEqual(User.objects.count(), 1)
        self.User = User.objects.first()
        self.assertEqual(self.User.username, self.testUserName)
        self.assertEqual(self.User.email, self.testUserEmail)
        self.assertEqual(self.User.password, self.testUserPass)

    def test_change_user(self):
        self.testCityName = 'Stuttgart'
        self.testZipCode = 70188
        self.testBirthDate = datetime.date(1969, 6, 9)
        self.User = User.objects.first()
        self.User.city_name = self.testCityName
        self.User.zip_code = self.testZipCode
        self.User.birth_date = self.testBirthDate
        self.User.save()
        self.UserUpdated = User.objects.first()
        self.assertEqual(self.UserUpdated.city_name, self.testCityName)
        self.assertEqual(self.UserUpdated.zip_code, self.testZipCode)
        self.assertEqual(self.UserUpdated.birth_date, self.testBirthDate)

    def test_delete_user(self):
        User.objects.all().delete()
        self.assertEqual(User.objects.count(), 0)

class TestUserAuthentication(TestCase):
    def setUp(self):
        self.testUserName = 'test1'
        self.testUserEmail = 'test@test.com'
        self.testUserPass = '123test123'
        User.objects.create(username=self.testUserName, email=self.testUserEmail, password=self.testUserPass)

    def test_user_can_authenticate(self):
        client = Client()
        self.assertNotContains('sessionid', client.cookies)
        self.response = client.post('/accounts/login/', dict(username=self.testUserName, password=self.testUserPass), content_type='application/json')
        self.assertEqual(self.response.status_code, 302) # redirect to LOGIN_REDIRECT_URL
        self.assertContains('sessionid', client.cookies)
        self.assertEqual(self.response.redirect_uri, LOGIN_REDIRECT_URL)
