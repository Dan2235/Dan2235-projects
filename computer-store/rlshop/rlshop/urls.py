from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from main import views as mv
from products import views as pv

sign = [
    path('-in', mv.sign_in),
    path('-in-2', mv.try_sign_in),
    path('-up', mv.sign_up),
    path('-up-2', mv.try_sign_up),
    path('-out', mv.sign_out),
]

products = [
    path('videocards', pv.videocards),
    path('processors', pv.processors),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', mv.index),
    path('about', TemplateView.as_view(template_name="about.html")),
    path('contacts', TemplateView.as_view(template_name="contacts.html",
            extra_context={"email": "compstore@example.com"}
        )
    ),
    path('sign', include(sign)),
    path('user-data', mv.user_data),
    path('products/', include(products)),
    path('put-to-cart/<str:product>', pv.put_to_cart),
    path('del-from-cart/<str:product>', pv.del_from_cart),
    path('pulse', mv.pulse_animation),     
]
