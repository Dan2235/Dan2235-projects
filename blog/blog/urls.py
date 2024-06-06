from django.contrib import admin
from django.urls import path, include
from main import views as mv

sign = [
    path('-in', mv.sign_in),
    path('-in-2', mv.try_sign_in),
    path('-up', mv.sign_up),
    path('-up-2', mv.try_sign_up),
    path('-out', mv.sign_out),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.index),
    path('sign', include(sign)),
    path('mychannel', mv.my_channel),
    path('user/<str:user_name>', mv.user),
    path('edit/<str:type>', mv.edit),
    path('edit-2/<str:type>', mv.try_edit),
]