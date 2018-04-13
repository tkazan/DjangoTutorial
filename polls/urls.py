from django.conf.urls import url

from polls.views import *

# app_name = 'polls'
# urlpatterns = [
#     url(r'^$', index, name='index'),
#     url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
#     url(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
# ]

app_name = 'polls'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
]