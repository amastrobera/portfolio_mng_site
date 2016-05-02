from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import User, Portfolio, Security, Asset

def index(request):    
    #return HttpResponse("Hello, world. You're at the port mng APP index.")
    template = 'portfolio_mng_app/index.html'
    return render(request, template)

def popup_add_port(request, userId, portfolioName):
    context = {'userId': userId, 'portfolioName': portfolioName}
    template = 'portfolio_mng_app/popup_add_port.html'
    return render(request, template, context)

def popup_delete_port(request, portfolioId, userId):
    context = {'userId': userId, 'portfolioId': portId}
    template = 'portfolio_mng_app/popup_delete_port.html'
    return render(request, template, context)



def popup_add(request, yid, portfolioId):
    portfolioName = Portfolio.objects.filter(id=portfolioId).first().name
    context = {'yid': yid, 
               'portfolioId': portfolioId, 
               'portfolioName': portfolioName}
    print "content: " + str(content)
    template = 'portfolio_mng_app/popup_add.html'
    return render(request, template, context)



def popup_edit(request, portfolioId, yid):
    context = {'yid': yid, 'portfolioId': portfolioId}
    template = 'portfolio_mng_app/popup_edit.html'
    print "content: " + str(content)
    #return HttpResponseRedirect(reverse())
    #checkout https://www.google.co.uk/search?client=ubuntu&channel=fs&q=django+href+to+url+kwargs&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=5JckV4GkNdeFaNrvlIAD#channel=fs&q=django+view+url+template+kwargs
    return render(request, template, context)



def popup_delete(request, yid, portId):
    context = {'yid': yid, 'portfolioId': portfolioId}
    template = 'portfolio_mng_app/popup_delete.html'
    return render(request, template, context)



def portfolios(request):
    #returns all portfolios in database
    context = {}
    try:
        all_port = Portfolio.objects.order_by('-last_update_date')
        context['portfolios'] = all_port
    except Portfolio.DoesNotExist:
        raise Http404("no portfolio found")
    template = 'portfolio_mng_app/portfolios.html'
    return render(request, template, context)

def portfolios_per_user(request, ownerId):
    #returns all portfolios owned by a user.id
    context = {}
    try:
        all_port = Portfolio.objects.all().filter(
                    owner__id=ownerId).order_by('-last_update_date')
        context['portfolios'] = all_port
    except Portfolio.DoesNotExist:
        raise Http404("no portfolio found")
    template = 'portfolio_mng_app/portfolios.html'
    return render(request, template, context)
    
def assets_in_port(request, portfolioId):
    #return all assets in a portfolio, given pk=portfolio.id
    context = {}
    try:
        all_assets = Asset.objects.all().filter(
                    portfolio__id=portfolioId).order_by('-yid')
        context['assets'] = all_assets
    except Asset.DoesNotExist:
        raise Http404("no portfolio found")
    template = 'portfolio_mng_app/assets.html'
    return render(request, template, context)

