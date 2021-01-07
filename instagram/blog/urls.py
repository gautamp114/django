from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('visit_pofile/<int:id>', views.visit_pofile, name="visit_pofile"),
    path('delete_post/<int:id>', views.delete_post, name="delete_post"),
    path('add_comment/<int:id>', views.add_comment, name="add_comment"),
    path('delete_comment/<int:id>', views.delete_comment, name="delete_comment"),

    path('change-profile-pic/<int:id>', views.change_profile_pic, name='change_profile_pic'),
    path('search/', views.search, name='search'),
    path('follow/<str:username>/', views.follow, name='follow'),
]
