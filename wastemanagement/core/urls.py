from django.urls import path
from core.views import home, scan, contact, complain
from django.conf import settings
from django.conf.urls.static import static
from core.views import WasteImageListView, WasteImageDetailView, WasteImageUploadView


urlpatterns = [
    path('', home, name='home'),
    path('scan/', scan, name='scan'),
    path('contact/', contact, name='contact'),
    path('complain/', complain, name='complain'),
    path('waste', WasteImageListView.as_view(), name='waste-list'),
    path('waste/upload/', WasteImageUploadView.as_view(), name='waste-upload'),
    path('detail/<int:pk>/', WasteImageDetailView.as_view(), name='waste-detail'),
]