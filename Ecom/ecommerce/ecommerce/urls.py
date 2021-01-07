from django.contrib import admin
from django.conf.urls import url
from products import views
from django.conf import settings
from django.conf.urls.static import static
from user import views as user
from carts import views as usercart

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^s/$', views.search, name='search'),
    url(r'^products/(?P<slug>[\w-]+)/$', views.single, name='single'),
    url(r'^register/$', user.register, name='register'),
    url(r'^register_process/$', user.register_process, name='register_process'),
    url(r'^login_page/$', user.login_page, name='login_page'),
    url(r'^user_login/$', user.user_login, name='user_login'),
    url(r'^cart/$', usercart.cartview, name='cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', usercart.update_cart, name='update_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
