from django.urls import reverse, resolve


class TestUrls:

    def test_home(self):
        path = reverse('home')
        return resolve(path).view_name == 'home'
