from django.urls import include, re_path
from app_1 import views

# SET THE NAMESPACE!
app_name = 'app_1'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),
]
