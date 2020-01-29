from django.urls import path, include
from . import views

app_name='main_oper_face'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:chat_id>/', views.installations, name='installations'),
#     path('<int:chat_id>/<int:id>/', views.installation, name='install'),
#
# ]

# extra_urls = [
#     path('', views.installations, name='installations'),
#     path('installation/<int:id>/', views.installation, name='install'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:chat_id>/', views.installations, name='installations'),
    path('<int:chat_id>/<int:id>/', views.installation, name='install'),
]
