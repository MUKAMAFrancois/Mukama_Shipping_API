from django.urls import path
from . import views


# tokens using simplejwt. 
#It gives access token and Refresh token when access time is over
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns=[
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),

    # tokens using simplejwt
    path("jwt/create_token/",TokenObtainPairView.as_view(), name="obtain_token"),
    path("jwt/refresh_token/",TokenRefreshView.as_view(), name="refresh_token"),
    path("jwt/verify_token/",TokenVerifyView.as_view(), name="verify_token"),



    

]