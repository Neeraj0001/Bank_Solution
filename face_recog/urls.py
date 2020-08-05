
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('registration/', views.registration, name="registration"),
    path('admin_dash/', views.a_dash, name="admin"),
    path('user_form/', views.user_form, name="update"),
    path('user/<str:pk_test>/', views.user, name="user"),
    path('logout/',views.logoutUser,name='logoutuser'),
]
