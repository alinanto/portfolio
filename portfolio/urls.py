from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_fn, name='render_fn'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('favicon.ico', views.favicon, name='favicon'),
]

