#!/usr/bin/python

import asset
import portfolio
import mktdta

import unittest

class TestAsset(unittest.TestCase):

    def test_creation(self):
        sec = asset.createSecurity("GOOG", asset.SecurityType.stock)
        self.assertEqual(sec.yid, "GOOG")
      
        a = asset.Asset(sec, 150)
        self.assertEqual(a.position, 150)
        self.assertEqual(a.security.yid, "GOOG")

        with self.assertRaises(Exception):
            b = asset.createSecurity("UNKW", -1)


class TestMktDta(unittest.TestCase):

    def setUp(self):
        self.mds = mktdta.Mds()
        goog = asset.createSecurity("GOOG", asset.SecurityType.stock)
        yhoo = asset.createSecurity("YHOO", asset.SecurityType.stock)
        self.assets = {'GOOG': 100, 'YHOO': 40}
        self.mds.addSecurity(goog)
        self.mds.addSecurity(yhoo)
   
    def test_price(self):
        self.mds.pricePortfolio(self.assets)
        for s in self.assets:
            sec = self.mds.store[s]
            print str(s) + " " + str(sec.price) + " " + str(sec.lastUpdate) 
  
    def test_price_as_of(self):
        self.mds.pricePortfolioAsOf(self.assets, '2015-06-30', '2015-07-12')
        for s in self.assets:
            sec = self.mds.store[s]

        self.assertEqual(self.mds.store['GOOG'].history['2015-06-30']['Close'],
                       520.51001)
         
        self.assertEqual(self.mds.store['YHOO'].history['2015-06-30']['Close'],
                       39.290001)

    def test_description(self):
        self.mds.descriptionPortfolio(self.assets)

        self.assertEqual(self.mds.store['GOOG'].info['start'], '2004-08-19')
        self.assertEqual(self.mds.store['YHOO'].info['start'], '1996-04-12')


class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.mds = mktdta.Mds()
        self.port = portfolio.Portfolio(666, self.mds, "Devil wears Prada")
        goog = asset.createSecurity('GOOG',asset.SecurityType.stock)
        aapl = asset.createSecurity('AAPL',asset.SecurityType.stock)
        self.mds.store[goog.yid] = goog
        self.mds.store[aapl.yid] = aapl
        self.port.assets[goog.yid] = 100
        self.port.assets[aapl.yid] = 40

    def test_add(self):
        yhoo = asset.createSecurity('YHOO',asset.SecurityType.stock)
        self.port.addSecurity(yhoo,30)
        self.assertTrue(yhoo.yid in self.port.assets)
        self.assertTrue(yhoo.yid in self.mds.store)
    
    def test_increase(self):
        self.port.assets['GOOG'] = 100
        self.port.increasePosition('GOOG',20)
        self.assertTrue(self.port.assets['GOOG'] == 120)

    def test_reduce(self):
        self.port.assets['GOOG'] = 100
        self.port.reducePosition('GOOG',20)
        self.assertTrue(self.port.assets['GOOG'] == 80)

    def test_remove(self):
        self.port.removeSecurity('AAPL')
        self.assertTrue('AAPL' not in self.port.assets)
        self.assertTrue('AAPL' in self.mds.store)

    def test_value(self):
        val = self.port.value()
        print 'current portfolio value : ' + str(val)
   
    def test_value_as_of(self):
        ref_dt = '2015-12-16'
        val = self.port.valueAsOf(ref_dt)
        self.assertEqual(round(val,2), 80262.60)

    def test_histo(self):
        ref_dt_1 = '2015-12-10'
        ref_dt_2 = '2015-12-15'
        val = self.port.valueAsOf(ref_dt_1, ref_dt_2)
        self.assertEqual(val, {'2015-12-14': 79276.20212, '2015-12-15': 78759.60231999999, '2015-12-10': 79592.80212000001, '2015-12-11': 78414.1995})


if __name__ == '__main__':
    unittest.main()
