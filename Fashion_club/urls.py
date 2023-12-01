"""
URL configuration for Fashion_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
import authentication.views
import core.views
from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import get_object_or_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", authentication.views.LoginPageView.as_view(), name="login"),
    path("logout/", authentication.views.logout_user, name="logout"),
    path("home/", core.views.home, name="home"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="authentication/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "profile-photo/upload/",
        authentication.views.upload_profile_photo,
        name="upload_profile_photo",
    ),
    path(
        "change-password-done/",
        PasswordChangeDoneView.as_view(
            template_name="authentication/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path("signup/", authentication.views.signup_page, name="signup"),
    path("modules/", core.views.view_modules, name="view_modules"),
    path("mentorship_forum/", core.views.mentorship_forum, name="mentorship_forum"),
    path('request_mentorship/<int:mentor_id>/', core.views.request_mentorship, name='request_mentorship'),
    path("products/", core.views.product_list, name="product_list"),
    path('add_product/', core.views.add_product, name='add_product'),
    path('', core.views.index, name='index'),
    path('about_us/', core.views.about_us, name='about_us'),
    path('contact_us/', core.views.contact_us, name='contact_us'),
    path('privacy_and_policy/', core.views.privacy_and_policy, name='privacy_and_policy'),
    path('services/', core.views.services, name='services'),
    path('fashion_courses1/', core.views.fashion_courses1, name='fashion_courses1'),
    path('fashion_courses2/', core.views.fashion_courses2, name='fashion_courses2'),
    path('fashion_courses3/', core.views.fashion_courses3, name='fashion_courses3'),
    path('wellness1/', core.views.wellness1, name='wellness1'),
    path('wellness2/', core.views.wellness2, name='wellness2'),
    path('trends/', core.views.trends, name='trends'),
    path('comments/', core.views.CommentView.as_view(), name='comments'),
    path('comments/<int:comment_id>/delete/', core.views.DeleteCommentView.as_view(), name='delete_comment')



         
]
urlpatterns += staticfiles_urlpatterns()