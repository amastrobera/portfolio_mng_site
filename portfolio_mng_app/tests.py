from django.test import TestCase
from django.utils import timezone

from .models import User, Security, Portfolio

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
        self.assertIn(self.goog,Security.objects.all())
        self.assertIn(self.port1,Portfolio.objects.all())
        self.assertIn(self.franky,User.objects.all())
    
    def test_portfolio_created(self):
        self.assertLess(self.port1.creation_date, timezone.now())
        self.assertEqual(len(self.port1.security_set.all()),0)

    def test_portfolio_add(self):
        self.port1.security_set.add(self.goog)
        self.assertIn(self.goog,self.port1.security_set.all())
        
    def test_portfolio_remove(self):
        #add a security to port, test, remove it, test, remove it from db, test
        self.yhoo = Security.objects.create(yid="YHOO",name="Yahoo")
        id = self.yhoo.id
        yhoo = self.yhoo
        self.port1.security_set.add(self.yhoo)
        self.assertIn(self.yhoo,self.port1.security_set.all())
        self.port1.security_set.remove(self.yhoo)
        self.assertNotIn(self.yhoo,self.port1.security_set.all())
        self.assertIn(yhoo,Security.objects.all())
        Security.objects.filter(id=id).delete()
        self.assertNotIn(yhoo,Security.objects.all())
        
