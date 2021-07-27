from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('register/',views.signup, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('profile/', views.user_profile, name='profile'),
    path('list/', views.polls_list, name='list'),
    path('add/', views.polls_add, name='add'),
    path('edit/<int:poll_id>/', views.polls_edit, name='edit'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)