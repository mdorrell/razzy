# content of test_unittest_db.py

import unittest
import pytest
import logging

from matcher import Matcher
from testHandler import TestHandler
from mock_mouth import MockMouth

from ..razzy import Razzy

class MyTest(unittest.TestCase):
  razzy = ""

  @classmethod
  def setUpClass(self):
    self.handler = TestHandler(Matcher())
    self.razzy = Razzy()
    self.razzy.getLogger().addHandler(self.handler)
    self.razzy.mouth = MockMouth(self.razzy.getLogger())


  @classmethod
  def tearDownClass(self):
    print "all done"

  def test_init_speak(self):
    self.razzy.init(self)
    self.assertTrue(self.handler.matches(msg="Hello, my name is Razzy"))
    assert 1 == 1

  def test_method2(self):
    assert 1 == 1
