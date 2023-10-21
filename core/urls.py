from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='core'),
    path('contact/', views.contact, name='contact'),
    path('<int:pk>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('new/', views.new, name='new'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('about/', views.about, name='about'),
    path('browse/', views.browse, name='browse'),
    path('new/<int:item_pk>/', views.new_conversation, name='new_conversation'),
    path('inbox/', views.inbox, name='inbox'),
    path('<int:pk>/', views.reply, name='reply'),
]
