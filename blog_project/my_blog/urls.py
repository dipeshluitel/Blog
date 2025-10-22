from django.urls import path
from my_blog import views

urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about')
]
