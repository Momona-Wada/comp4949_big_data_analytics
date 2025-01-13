from django.urls import path
from .views import homePageView, aboutPageView, momonaPageView, homePost, results

urlpatterns = [
    path("", homePageView, name="home"),
    path("about/",aboutPageView, name="about"),
    path("momona/", momonaPageView, name="momona"),
    path("homePost/", homePost, name="home_post"),
    path("results/<int:choice>/<str:gmat>", results, name="results")
]