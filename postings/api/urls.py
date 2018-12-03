from .views import BlogUserRudView, BlogUserAPIView,BlogUserListAPIView
from django.urls import path


app_name='postings'
urlpatterns = [
    path('', BlogUserAPIView.as_view(), name='user-create'),
    path('all/', BlogUserListAPIView.as_view(), name='user-listcreate'),
    path('<int:pk>', BlogUserRudView.as_view(), name='user-rud'),
]
