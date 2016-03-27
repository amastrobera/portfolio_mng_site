from django.conf.urls import url

from . import views


#you can visit  http://localhost:8000/portfolio_mng_app/
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all_portfolios/$', views.all_portfolios, name='all_portfolios'),
    url(r'^all_portfolios/(?P<ownerId>[0-9]+)/$',
        views.all_portfolios_per_user,
        name='all_portfolios_per_user'),
    url(r'^all_securities_in_port/(?P<portfolioId>[0-9]+)/$',
        views.all_securities_in_port,
        name='all_securities_in_port'),
    url(r'^\d+/popup_add/$', views.popup_add, name='popup_add'),
    url(r'^\d+/popup_edit/$', views.popup_edit, name='popup_edit'),
    url(r'^\d+/popup_delete/$', views.popup_delete, name='popup_delete'),
]
