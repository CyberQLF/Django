from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name = 'main'),
    path('blog/', views.blog, name='blog'),
    path('<int:num>/', views.blog_detail, name = 'blog_detail'),
path('blog/<int:num>/', views.blog_type, name = 'blog_type')
]

