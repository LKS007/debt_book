from django.test import TestCase

from debts.models import Debt
from django.urls import reverse

class DebtViewTestCase(TestCase):

  def set_up(self):
    print("YAH!!! Let's do it")

  def test_false_is_false(self):
    print("Method: test_false_is_false.")
    self.assertFalse(False)

  def test_view_url_exists_at_desired_location(self): 
    response = self.client.get('/debts/') 
    self.assertEqual(response.status_code, 200)

  def test_should_fail(self):
    self.assertTrue(5 == 5)

