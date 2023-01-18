from django.urls import path
from . import views
from .views import home, profile, RegisterView, CustomLoginView, LoginForm, paint

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('catalog/ishop',views.ishop,name="ishop"),
    path('catalog/smarket',views.smarket,name='smarket'),
    path('catalog/shopping',views.shopping,name='shopping'),
    path('catalog/fshop',views.fshop,name='fshop'),
    path('catalog/icompany',views.icompany,name='icompany'),
    path('catalog/edu',views.edu,name='edu'),
    path('catalog/<int:pk>/details',views.company_detail,name='company_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('addnew',views.addnewcomp,name='addnew'),
    path('children',views.children,name='children'),
    path('catalog/<int:pk>/edit',views.editcompany,name='editcompany'),
    path('video/', views.upload_display_video, name='upload_display_video'),
    #path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/',views.profile, name='users-profile'),
    path('paint/',views.paint, name='paint'),
]