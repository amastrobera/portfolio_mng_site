import asset
import mktdta

import datetime

class Portfolio(object):
    def __init__(self, pid, mds, name=None, shortSelling=False):
        self.pid = pid
        self.mds = mds
        self.name = name
        self.shortSelling = shortSelling
        self.assets = {} # DICT(yid, position)
        #todo: DICT(yid, DICT(yyyy-mm-dd,position)). Think! 
        self.lastUpdate = None  
        
    def addSecurity(self, security, position):
        if not isinstance(security, asset.Security):
            raise Exception("failed addSecurity: " + str(security) + 
                        " is not a security type")
        if security.yid in self.assets:
            return
        if not security.yid in self.mds.store:
            self.mds.store[security.yid] = security
        self.assets[security.yid] = position
        
    def increasePosition(self, yid, delta_pos):
        if delta_pos < 0:
            raise Exception("failed to increasePosition: neative increase")
        if not yid in self.assets:
            return
        self.assets[yid] = self.assets[yid] + delta_pos

    def reducePosition(self, yid, delta_pos):
        if delta_pos < 0 :
            raise Exception("failed to reducePosition: positive decrease")
        if not yid in self.assets:
            return
        if delta_pos > self.assets[yid] and not self.shortSelling:
            raise Exception("failed to reducePosition: short sale not allowed")
        self.assets[yid] = self.assets[yid] - delta_pos
    
    def removeSecurity(self, yid):
        if yid in self.assets:
            self.assets.pop(yid,None)
            #todo:  
           
    def value(self):
        self.mds.pricePortfolio(self.assets)
        val = 0
        for s in self.assets:
            val = val + self.assets[s] * self.mds.store[s].price
        return val
        
    def valueAsOf(self, dt_str_1, dt_str_2=None):
        #format dt_str_1,2 = yyyy-mm-dd
        try:
            if (dt_str_2 == None):
                return self.__computeValue1Date(dt_str_1)
            else:
                return self.__computeValueRangeDates(dt_str_1, dt_str_2)
        except Exception as e:
            raise e
        except:
            raise
 
       
    def __checkDate(self, dt_str):
        d = dt_str.split("-")
        if len(d) != 3:
            raise Exception("date in wrong format")
        dt = datetime.date(int(d[0]), int(d[1]), int(d[2]))
        if not type(dt) is datetime.date:
            raise Exception("date in wrong format")

    def __computeValue1Date(self, dt_str):
        self.mds.pricePortfolioAsOf(self.assets, dt_str)
        val = 0
        for s in self.assets:
            val = val + self.assets[s] * self.mds.store[s].history[dt_str]['Close']
        return val

    def __computeValueRangeDates(self, dt_str_1, dt_str_2):
        dt = datetime.datetime.strptime(dt_str_1, "%Y-%m-%d")
        dt_end = datetime.datetime.strptime(dt_str_2, "%Y-%m-%d")
        self.mds.pricePortfolioAsOf(self.assets, dt_str_1, dt_str_2)
        val = {}        
        while dt <= dt_end:
            temp = 0
            dt_str = datetime.datetime.strftime(dt, "%Y-%m-%d")
            for s in self.assets:
                if dt_str in self.mds.store[s].history:
                    temp = temp + self.assets[s] * self.mds.store[s].history[dt_str]['Close']
                    val[dt_str] = temp
            dt = dt + datetime.timedelta(days=1)
        return val

