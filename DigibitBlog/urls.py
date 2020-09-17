from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from allauth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='base.html'))
]
