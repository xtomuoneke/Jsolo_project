from django.urls import path
from .views import blog_home, login, sign_up
from .about import about_us, admin_dashboard


urlpatterns = [
    path('', blog_home, name='home'),
    path('about_us', about_us, name='about_us'),
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),
    path('login', login, name='login'),
    path('sign_up', sign_up, name='sign-up')
    

]