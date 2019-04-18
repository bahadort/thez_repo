"""thez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import experiment.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', experiment.views.experiment),
    path('question-2', experiment.views.question_2),
    path('question-3', experiment.views.question_3),
    path('question-4', experiment.views.refresh),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
