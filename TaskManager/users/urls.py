
# from django.urls import path, include
# from users import views


# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     # path('users/', views.users_list),

#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]

from django.urls import path
from .views import MyObtainTokenPairView, RegisterView, UserList
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('users/', UserList.as_view()),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
