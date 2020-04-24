from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='tracksvc/login.html')),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/login/', template_name='tracksvc/logout.html')),
    path('', include('django.contrib.auth.urls')),
    path('', views.default, name='default'),
    path('tracksvc/', views.index, name='index'),
    path('<int:firearm_id>/', views.fdetail, name='fdetail'),
    path('<int:firearm_id>/add/', views.get_check_data, name='get_check_data'),
]
