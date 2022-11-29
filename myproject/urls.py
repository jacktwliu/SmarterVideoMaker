"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from myapp import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

app_name = "myapp"

urlpatterns = [
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
    path('',views.index),
    path('hello2/<str:name>',views.hello2),
    path('hello3/<str:name>',views.hello3),
    path('index/', views.index),
    path('news/', views.news),
    path('messageboard/',views.messageboard),
    path('messageboardpost/',views.messageboardpost),
    path('messageboard/edit/<int:id>/',views.messageboardedit),
    path('messageboard/edit/<int:id>/<str:mode>',views.messageboardedit),
    path('messageboard/delete/<int:id>/',views.messageboarddelete),
    path('sendfeedback/', views.sendfeedback),
    path('sendfeedback_successful/', views.sendfeedback_successful),
    path('accounts/sign_up/',views.sign_up, name="sign_up"),
    path('accounts/login/', views.login,name='login'),
    path('accounts/logout/', views.logout,name='logout'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('accounts/userinfoedit/', views.userinfoedit),
    path('accounts/userinfo/', views.userinfo),
    path('accounts/profile/', views.index),
    path("uploadFile/", views.uploadFile, name = "uploadFile"),
    #path('del/<int:id>',views.deleteFile,name='delete'),
    path('makevideo/', views.makevideo),
    path('smartrecord/',views.smartrecord),
    path('recordingvideo/', views.recordingvideo),
    path('ytcomments/',views.ytcomments),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )