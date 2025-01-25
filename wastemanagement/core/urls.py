from django.urls import path
from core.views import home, scan, contact, complain
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('scan/', scan, name='scan'),
    path('contact/', contact, name='contact'),
    path('complain/', complain, name='complain'),
]