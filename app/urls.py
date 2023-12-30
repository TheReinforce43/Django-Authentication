from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='sign_up'),
    path('login/',views.user_login,name='log_in'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('PasswordChange/',views.password_change,name='pass_change'),
    path('pass_change_without_validation/',views.pass_change_without_validation,name='pass_change_without_validation'),
    # path('ChangeData/',views.ChangeDataUser,name='change_data'),

    
]
