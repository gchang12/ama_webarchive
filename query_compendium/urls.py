#!/usr/bin/python3
"""
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.content_creator_index, name="content_creator_index"),
    path("<str:cc_name>", views.qa_listing, name="qa_listing"),
]


if __name__ == '__main__':
    pass
