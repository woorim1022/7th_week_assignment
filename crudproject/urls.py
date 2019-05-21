"""crudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import crudapp.views
import accounts.views
import photo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudapp.views.home, name="home"),
    path('blog/<int:blog_id>/', crudapp.views.detail, name = "detail"),
    path('accounts/', include('accounts.urls')),
    path('photo/photo/', photo.views.photo, name='photo'),
    path('crudapp/new/', crudapp.views.new, name='new'),
    path('crudapp/postcreate/', crudapp.views.postcreate, name='postcreate'),
    path('crudapp/edit', crudapp.views.edit, name='edit'),
    path('crudapp/postupdate/<int:blog_id>/', crudapp.views.postupdate, name='postupdate'),
    path('crudapp/postdelete/<int:blog_id>', crudapp.views.postdelete, name='postdelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

