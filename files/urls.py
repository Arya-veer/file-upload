from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from. import views

urlpatterns=[
    path('upload/',views.uploadView,name="upload_url"),
    path('home/',views.Files.as_view(), name="home_page")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)