# accounts/urls.py
from django.urls import path
from .views import SignUpView, TopicListView
from .import views

urlpatterns = [
    path('', TopicListView.as_view(), name ='news'),
    path('news/<int:pk>/', views.post_detail, name ='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
]