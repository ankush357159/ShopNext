from django.urls import path
from api.views import user_views
from api.views.user_views import ChangePasswordView, LogoutView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="logout"),
    path("logout/", LogoutView.as_view(), name="token_obtain_pair"),
    path("register/", user_views.RegisterUserCreatView.as_view(), name="register_user"),
    path(
        "user-detail/<str:pk>/",
        user_views.RegisterUserDetailView.as_view(),
        name="user_details",
    ),
    path(
        "update-user/<str:pk>/",
        user_views.RegisterUserUpdateView.as_view(),
        name="update_user",
    ),
    path(
        "delete-user/<str:pk>/",
        user_views.RegisterUserDeleteView.as_view(),
        name="delete_user",
    ),
    path(
        "users/",
        user_views.RegisterUserListView.as_view(),
        name="delete_user",
    ),
    path(
        "change_password/<str:pk>/", ChangePasswordView.as_view(), name="change_password"
    ),
]
