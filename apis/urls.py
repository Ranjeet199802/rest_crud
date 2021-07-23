from django.urls import path

from apis import views

urlpatterns = [
    path('create/', views.CreateStudent.as_view()),
    path('get_student/', views.GetStudent.as_view()),
    path('update_student/<int:pk>', views.UpdateStudent.as_view()),
    path('delete_student/<int:pk>', views.DeleteStudent.as_view()),
    # path('get_data/<int:pk>', views.get_data_by_id),
    # path('get_data/', views.get_all_data),
]