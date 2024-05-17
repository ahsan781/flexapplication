from django.urls import path, include
from . import views
from .views import*

urlpatterns = [
    path('', views.index, name='index'),
     path('about/', views.about, name='about'),
      path('contact/', views.contact, name='contact'),
       path('pricing/', views.pricing, name='pricing'),
        path('service/', views.Service, name='Service'),
         path('support/', views.support, name='support'),
          path('login/', views.login , name='login'),
           path('signup/', views.signup, name='signup'),
            path('Userlogout/', views.Userlogout, name='Userlogout'),

]