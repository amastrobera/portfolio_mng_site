#! /usr/bin/python

from asset import SecurityType, createSecurity
from mktdta import Mds
from portfolio import Portfolio

def run():

    #1. load data store
    mds = Mds()
    
    #2. load portfolio list per user
    # todo

    #3. load default portfolio
    #todo: get one from the list instead
    mainPort = Portfolio(123, mds, 'mainAppPort')

    goog = createSecurity('GOOG', SecurityType.stock)
    aapl = createSecurity('AAPL', SecurityType.stock)

    mainPort.addSecurity(goog, 10)
    mainPort.addSecurity(aapl, 20)

    ref_dt = '2015-12-16'
    ref_ht_1 = '2015-03-12'
    ref_ht_2 = '2015-03-18'

    mds.pricePortfolio(mainPort.assets)
    mds.descriptionPortfolio(mainPort.assets)
    mds.pricePortfolioAsOf(mainPort.assets, ref_ht_1, ref_ht_2)
    
    histo = mainPort.valueAsOf(ref_ht_1, ref_ht_2)

    val = mainPort.valueAsOf(ref_dt)  

    #print results
    print 'portfolio current value: ' + str(val)
    print 'portfolio history:\n' + str(histo)
    print 'portfolio mainPort statement:'
    i = 1
    for s in mainPort.assets:
        print (str(i) + ': ' + str(mainPort.assets[s]) + 
                ', prc='+ str(mds.store[s].price) +
                ', updated at ' +str(mds.store[s].lastUpdate))
        print 'info: ' + str(mds.store[s].info)
        print ('History: from ' + mds.store[s].historyDates['first'] + 
               ' to ' + mds.store[s].historyDates['last'])
        print mds.store[s].history


    #4. display grid
    #todo

    #5. display on the screen
    #todo

    #6. wait for events and update history, value, compo   
    


if __name__ == '__main__':
    run()
