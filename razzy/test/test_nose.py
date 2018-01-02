# content of test_unittest_db.py

import unittest
import pytest

from razzy import Razzy

class MyTest(unittest.TestCase):
  razzy = ""
  
  @classmethod
  def setUpClass(self):
    self.razzy = Razzy()

  @classmethod
  def tearDownClass(self):
    self.razzy.init()
    print "all done"
    
  def test_method1(self):
      assert 1 == 1

  def test_method2(self):
      assert 1 == 1
