from auth import views as authviews
from django.conf.urls import url
from django.urls import path

app_name = 'auth'

urlpatterns = [
    url('^$', authviews.Login.as_view()),
    path('login', authviews.get_name, name='login'),
    path('home', authviews.homepage, name='home')
    ]
