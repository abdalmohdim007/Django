"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from capp import views

urlpatterns = [
    path('company/', views.company, name='company'),
    path('department/', views.department, name='department'),
    path('employee/', views.employee, name='employee'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('nameform/', views.get_name, name='nameform'),
    path('', views.main, name='main'),
    path('', include('capp.urls')),  # Direct root URLs to the capp app
    path('', include('capp.urls')),  # Direct root URLs to caap app
    path('admin/', admin.site.urls),
]
