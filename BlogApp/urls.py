from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.Home,name='Home'),
    path("about/", views.About,name='About'),
    path("contact/", views.Contact,name='Contact'),
    path("detail/<str:id>", views.Detail,name='Detail'),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
