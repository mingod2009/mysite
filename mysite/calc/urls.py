from django.conf.urls import url
import calc.views as cv

urlpatterns = [
    url(r'^$', cv.index, name='home'),
    url(r'^add/', cv.add, name="add"),
    url(r'add2/(\d+)/(\d+)/', cv.add2, name="add2"),
    url(r're_add/(\d+)/(\d+)/', cv.add3),
]