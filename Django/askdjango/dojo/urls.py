from django.urls import path, re_path
from . import views

urlpatterns = [
    # re_path(r'^sum/(?P<x>\d+)/$', views.mysum),
    # re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    # re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    # re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello)
    path('hello/<str:name>/<int:age>/', views.hello) # django2.0의 path 설정
    # path('sum/<int:x>/', views.mysum),  # django2.0의 path 설정
    # path('sum/<int:x>/<int:y>/', views.mysum),  # django2.0의 path 설정
    # path('sum/<int:x>/<int:y>/<int:z>/', views.mysum),  # django2.0의 path 설정
]