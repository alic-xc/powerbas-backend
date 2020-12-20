from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.urls import path
from .views import LoginView, HomepageView, DashboardView

app_name = 'dashboard'

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('settings', DashboardView.as_view(), name='settings'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]