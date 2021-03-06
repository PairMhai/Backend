from django.conf.urls import url
from catalog.views import *

urlpatterns = [
    url(r'^materials$',
        MaterialList.as_view(), name='material-list'),
    url(r'^material/(?P<pk>[0-9]+)$',
        MaterialDetail.as_view(), name='material-detail'),
    url(r'^designs$',
        DesignList.as_view(), name='design-list'),
    url(r'^design/(?P<pk>[0-9]+)$',
        DesignDetail.as_view(), name='design-detail'),
    url(r'^promotions$',
        PromotionList.as_view(), name='promotion-list'),
    url(r'^test$',
        TestView.as_view(), name='test'),

    # url(r'^promotion/(?P<pk>[0-9]+)$', PromotionDetail.as_view(), name='promotion-detail'),
]
