from django.test import TestCase
from django.urls import reverse


class FooTest(TestCase):
    def setUp(self):
        self.a = 1

    def tearDown(self):
        del self.a

    def this_wont_run(self):
        print('Fail')

    def test_this_will(self):
        print ('Win')
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    def test_basic(self):
        assert self.a == 1
