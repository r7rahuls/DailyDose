from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('save_email', views.save_email, name='save_email'),
    path('fetch_news/', views.news, name='fetch_news'),
    path('serve_css/', views.serve_css, name='serve_css'),
]
