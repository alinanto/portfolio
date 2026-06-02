from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_fn, name='home'),
    path('demo/clt/', views.demo_clt, name='demo_clt'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('favicon.ico', views.favicon, name='favicon'),
    path('martor/uploader/', views.image_uploader, name='martor_image_uploader'),
]

