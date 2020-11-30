from django.urls import path
from.import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('subscriber/list/', views.subscriber_list, name='subscriber-list'),
    path('subscriber/create/', views.create_subscriber, name='create-subscriber'),
    path('subscriber/<email>/delete/', views.delete_subscriber, name='subscriber-list'),
]
