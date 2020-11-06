"""ase_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views
from homechef import views as homechef_views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
# from users.views import login_view

router1=routers.DefaultRouter()
router1.register('homechef',homechef_views.VendorList)

router2=routers.DefaultRouter()
router2.register('homechef',homechef_views.FoodItemList)

router3=routers.DefaultRouter()
router3.register('homechef',homechef_views.IngredientsList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homechef.urls')),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',user_views.login_view,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('Buy/',homechef_views.Buy,name='Buy'),
    path('Vendor/',homechef_views.Vendor,name='Vendor'),
    path('display/',homechef_views.display,name='display'),
    path('product/',homechef_views.product,name='product'),
    path('food/',homechef_views.food,name='food'),
    path('vendorlist/',homechef_views.vendorlist,name='vendorlist'),
    path('about/',homechef_views.about,name='about'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/',include('payment.urls',namespace="payment")),
    path('Vendor1/',include(router1.urls)),
    path('FoodItem1/',include(router2.urls)),
    path('Ingredients1/',include(router3.urls)),
    path('activate/<uidb64>/<token>',user_views.activate,name='activate'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)