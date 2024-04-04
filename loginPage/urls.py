from django.urls import path
from loginPage.views import login_user

urlpatterns = [
    path("login_user", login_user, name="login"),
]
