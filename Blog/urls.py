from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.ListPost.as_view(), name='list-post'),
    path('create/', views.CreatePost.as_view(), name='create-post'),
    path('delete/<slug:slug>', views.DeletePost.as_view(), name='delete-post'),
    path('<slug:slug>/', views.DetailPost.as_view(), name='detail-post'),
]
