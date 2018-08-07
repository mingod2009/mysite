
from django.conf.urls import url
import learn.views as lv
urlpatterns = [
    url(r'^$', lv.home)
]