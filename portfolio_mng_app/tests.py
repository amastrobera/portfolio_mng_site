from django.test import TestCase
from django.utils import timezone

from .models import User, Security, Asset, Portfolio

#run only these webserver tests : ./manage.py test --pattern="tests.py"
#run also the backend unit tests: ./manage.py test 

class PortfolioModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.franky = User.objects.create(name="Franky Morello",
                                         email="fmorello@gmail.com")
        cls.port1 = Portfolio.objects.create(name="Franky's best", 
                                        owner=cls.franky)
        cls.goog = Security.objects.create(yid="GOOG", name="Google")
    
    @classmethod
    def tearDownClass(cls):
        Security.objects.filter(id=cls.goog.id).delete()
        User.objects.filter(id=cls.franky.id).delete()
        Portfolio.objects.filter(id=cls.port1.id).delete()

    def test_setup_created(self):
        self.assertIn(self.goog, Security.objects.all())
        self.assertEqual(len(Asset.objects.all()), 0)
        self.assertIn(self.port1, Portfolio.objects.all())
        self.assertIn(self.franky, User.objects.all())
    
    def test_portfolio_created(self):
        self.assertLess(self.port1.creation_date, timezone.now())
        self.assertEqual(len(self.port1.asset_set.all()),0)

    def test_portfolio_add_edit_remove(self):
        #create asset
        asset_goog = Asset.objects.create(yid=self.goog.yid, position=100,
                                           portfolio=self.port1)
        self.assertEqual(asset_goog.position, 100)
        self.assertIn(asset_goog, Asset.objects.all())
        
        #edit
        temp_asset = Asset.objects.filter(id=asset_goog.id).first()
        temp_asset.position = 120
        temp_asset.save()
        self.assertEqual(temp_asset.position, 120)

        #add to portfolio
        self.port1.asset_set.add(asset_goog)
        self.assertIn(asset_goog,self.port1.asset_set.all())
        
        #edit in portfolio
        temp_asset_port = self.port1.asset_set.filter(id=asset_goog.id).first()
        temp_asset_port.position=80
        temp_asset_port.save()
        temp_asset = Asset.objects.filter(id=asset_goog.id).first()
        self.assertEqual(temp_asset.position, temp_asset_port.position)
        
        # remove from DB, then from portfolio
        Asset.objects.filter(id=asset_goog.id).delete()
        self.assertNotIn(asset_goog, Asset.objects.all())
        self.assertNotIn(asset_goog, self.port1.asset_set.all())
                
