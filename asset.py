from enum import Enum
class SecurityType(Enum):
    stock = 1


class Asset(object):
    #todo: position --> shares, notional, multiplier...
    def __init__(self, security, position):
        self.security = security
        self.position = position


def createSecurity(yid, type=SecurityType.stock):
    #strategy pattern
    if type == SecurityType.stock:
        return Stock(yid)
    else:
        raise Exception('failed to create security.Type '+str(type)+' unknown')


class Security(object):
    def __init__(self, yid, type):
        self.yid = yid
        self.type = type
        self.lastUpdate = None
        self.price = None
        self.volume = None
        self.history = {} # DICT(date, LIST(price, etc..))
        self.historyDates = {'first': None, 'last': None}
        self.info = None

    def priceAsOf(self, dt_str):
        #format dt_str yyyy-mm-dd
        if not dt_str in self.history:
            #todo: call to mktdta
            return 0
        return self.history[dt_str]
        

class Stock(Security):
    def __init__(self, yid):
        super(Stock,self).__init__(yid, SecurityType.stock)
        self.dividend = None
       
                
