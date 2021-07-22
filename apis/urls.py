from django.urls import path

from apis import views

urlpatterns = [
    path('create/', views.create_student),
    path('get_data/<int:pk>', views.get_data_by_id),
    path('get_data/', views.get_all_data),
]