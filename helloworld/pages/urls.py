from django.urls import path
from .views import homePageView, aboutPageView, momonaPageView

urlpatterns = [
    path("", homePageView, name="home"),
    path("about/",aboutPageView, name="about"),
    path("momona/", momonaPageView, name="momona"),
]