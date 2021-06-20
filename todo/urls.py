from django.urls import path
from todo import views
from rest_framework.urlpatterns import format_suffix_patterns
 
urlpatterns = [
    path('todo/', views.todo_list),
    path('todo/<int:pk>', views.todo_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
