from django.conf.urls import url

from . import views


#you can visit  http://localhost:8000/portfolio_mng_app/
urlpatterns = [
    url(r'^$', 
            views.index, 
            name='index'),
    url(r'^portfolios/$', 
            views.portfolios, 
            name='portfolios'),
    url(r'^portfolios/(?P<ownerId>[0-9]+)/$', 
            views.portfolios_per_user,
            name='portfolios_per_user'),
    url(r'^assets/(?P<portfolioId>[0-9]+)/$', 
            views.assets_in_port,
            name='assets_in_port'),

    url(r'^popup_add_port/(?P<userId>\d+)/(?P<portfolioName>[A-Za-z .=^]+)/$', 
            views.popup_add_port, 
            name='popup_add_port'),

    url(r'^popup_delete_port/(?P<userId>\d+)/(?P<portfolioName>[A-Za-z .=^]+)/$', 
            views.popup_delete_port, 
            name='popup_delete_port'),

    url(r'^popup_edit/(?P<portfolioId>[0-9]+)/(?P<yid>[A-Za-z .=^]+)/$', 
            views.popup_edit,
            name='popup_edit'),
            
]
