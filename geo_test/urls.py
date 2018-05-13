"""geo_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from geo_test.views.choose_quiz import ChooseQuiz
from geo_test.views.load_feature import LoadFeatureWFS
from geo_test.views.load_wfs import LoadWFSView

urlpatterns = [
    path('load_wfs/', LoadWFSView.as_view()),
    path('load_feature/', LoadFeatureWFS.as_view(), name='load_feature'),
    path('quiz/<int:quiz_id>/', ChooseQuiz.as_view(), name='quiz'),
    path('admin/', admin.site.urls),
    path('', ChooseQuiz.as_view()),
]
