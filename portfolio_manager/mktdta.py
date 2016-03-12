import asset

from yahoo_finance import Share
#todo: Currency, and other if any

class Mds(object):
    def __init__(self):
        self.store = {} #DICT(yid, security)

    def addSecurity(self, security):
        if not isinstance(security, asset.Security):
            raise Exception("failed addSecurity: " + str(security) +
                        " is not a security type")
        if not security.yid in self.store:
            self.store[security.yid] = security

    def pricePortfolio(self, assets={}):
        #prices all MDS securities in the portfolio DICT(yid, position)
        #adds securities to MDS if the portfolio has more
        for s in assets:
            try:
                ySec = self.__getYahooHandler(s, self.store[s].type)
                self.store[s].price = float(ySec.get_price())
                self.store[s].volume = int(ySec.get_volume())
                self.store[s].lastUpdate = ySec.get_trade_datetime()
            except:
                raise

    def pricePortfolioAsOf(self, assets={}, dt_str_1=None, dt_str_2=None):
        if assets == {} or (dt_str_1 == None and dt_str_2 == None):
            return
        try: 
            if dt_str_2 == None:
                self.__dateCheck(dt_str_1)
                for s in assets:
                    sec = self.store[s]
                    ySec = self.__getYahooHandler(s, sec.type)
                    self.__fillPointWithData(sec, ySec, dt_str_1)
            else:
                self.__dateCheck(dt_str_1)
                self.__dateCheck(dt_str_2)
                
                for s in assets:
                    sec = self.store[s]
                    ySec = self.__getYahooHandler(s, sec.type)
                    if (sec.historyDates['first'] == None and 
                        sec.historyDates['last'] == None):
                        self.__fillHistoryWithData(sec, ySec, dt_str_1, 
                                                    dt_str_2)
                        sec.historyDates['first'] = dt_str_1
                        sec.historyDates['last'] = dt_str_2
                    else:
                        if sec.historyDates['first'] > dt_str_1:
                            self.__fillHistoryWithData(sec, ySec, 
                                        dt_str_1, sec.historyDates['first'])
                            sec.historyDates['first'] = dt_str_1
    
                        if sec.historyDates['last'] < dt_str_2:
                            self.__fillHistoryWithData(sec, ySec, 
                                        sec.historyDates['last'], dt_str_2)
                            sec.historyDates['last'] = dt_str_2
        except Exception as e:
            raise e
        except:
            raise
 
    def descriptionPortfolio(self, assets={}):
        try:
            for s in assets:
                if not s in self.store:
                    raise Exception('failed to get description.' + 
                            'Security not in mds')
                ySec = Share(s)
                self.store[s].info = ySec.get_info()
        except Exception as e:
            raise e
        except:
            raise
           
    #todo: cache in Redis


    #private functions 
    def __getYahooHandler(self, yid, type):
        #type is asset.SecurityType
        if type == asset.SecurityType.stock:
            return Share(yid)
            #todo: other types
        else:
            raise Exception('failed to get y-handler. Unknown asset type')

    def __dateCheck(self, dt_str):
        import datetime
        d = dt_str.split("-")
        if len(d) != 3:
            raise Exception("date in wrong format")
        dt = datetime.date(int(d[0]), int(d[1]), int(d[2]))
        if not type(dt) is datetime.date:
            raise Exception("date in wrong format")
    
    def __fillHistoryWithData(self, sec, ySec, dt_str_1, dt_str_2):        
        from datetime import datetime, timedelta
        dt = datetime.strptime(dt_str_2, "%Y-%m-%d")
        dt = dt + timedelta(days=1)
        dt_str_2 = datetime.strftime(dt, "%Y-%m-%d")
        yHist = ySec.get_historical(dt_str_1, dt_str_2)    
        for h in yHist:
            sec.history[h['Date']] = \
                                     {'Close': float(h['Close']),
                                      'Volume': int(h['Volume'])}
             #todo: add also the others, Low, High ...
             #todo: make an object Price = {High, Low, Close...}

    def __fillPointWithData(self, sec, ySec, dt_str_1):
        yHist = ySec.get_historical(dt_str_1, dt_str_1)
        if len(yHist) == 0:
            sec.history[dt_str_1] = \
                                 {'Close': 0.0,
                                 'Volume': 0}
            #todo: implement a failure case here None or null...
        else:
            for h in yHist:
                sec.history[h['Date']] = \
                                     {'Close': float(h['Close']),
                                      'Volume': int(h['Volume'])}
                 #todo: add also the others, Low, High ...
                 #todo: make an object Price = {High, Low, Close...}

