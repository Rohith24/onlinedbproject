"""onlinedbproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import views
import collegeviews
urlpatterns = [
    url(r'^text/(?P<location>[A-Za-z]+)', views.text, name="text"),
    url(r'^college/(?P<id>[0-9]+)', views.college_details_id, name="details based on id"),
    url(r'^college/(?P<acronym>[A-Za-z]+)', views.college_details_acronym, name="details based on acronym"),
    url(r'^$',views.index),
    url(r'^collegedetails/(?P<pk>[0-9]+)',view=collegeviews.CollegeDetailsView.as_view()),
    url(r"^colleges/create$",view=collegeviews.CollegeCreateView.as_view()),
    url(r"^colleges/update/(?P<pk>[0-9]+)",view=collegeviews.CollegeUpdateView.as_view(),name='update-data'),
    url(r'^colleges/delete/(?P<pk>[0-9]+)',view=collegeviews.CollegeDeleteView.as_view(),name="delete-data"),
    url(r"^colleges/", view=collegeviews.CollegeListView.as_view(), name="college-list-view"),
    url(r"^colleges/(?P<location>[A-Za-z]*)$",view=collegeviews.CollegeListView.as_view(),name="college-list"),
]
