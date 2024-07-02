from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),# Landing page
    path('main/', views.main_page, name='main'), #Main map page
    path('users/', include('users.urls')), # Signup and login pages
    path('settings/', views.settings_page, name='settings'),# Settings page
    path('account/', views.account_page, name='account'),# About page
    path('support/', views.support_page, name='support')# Support page
    # Sign up page

    #
    # Account page
    # Mobile ID

]

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs
    path('', include('home.urls'))
]
'''
