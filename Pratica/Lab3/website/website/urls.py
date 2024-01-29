"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booklist/', views.listbooks, name="listbooks"),
    path('bookdetails/<str:title>', views.bookdetails, name="bookdetails"),
    path('authorslist/', views.listauthors, name="authorslist"),
    path('authordetails/<str:name>', views.authordetails, name="authordetails"),
    path('publisherslist/', views.listpublisher, name="publisherslist"),
    path('publisherdetails/<str:name>', views.publisherdetails, name="publisherdetails"),
    path('authorbooks/<str:author>', views.getAuthorBooks, name="authorbooks"),
    path('publisherauthors/<str:publisher_name>', views.publisherAuthors, name='publisherauthors')

]
