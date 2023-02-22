from django.urls import path
from .views import MovieList,MovieDetail,my_login,register,logout_page

urlpatterns = [
    path("", MovieList.as_view(), name='movie_list'),
    path("<int:pk>", MovieDetail.as_view(), name='movie_detail'),
    path("login/",my_login, name="log"),
    path("logout/",logout_page, name="logout"),
    path("register/", register, name="reg")
]