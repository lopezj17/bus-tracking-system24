from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),# Landing page
    path('login/', views.login_page, name='login'),# Login page
    path('signup/', views.sign_up_page, name='signup'),
    path('main/', views.main_page, name='main'), #Main map page
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
