from django.test import TestCase
from django.test.client import Client
from django.utils.html import escape

from stdnumfield.tests.forms import INVALID_OIB, VALID_OIB


class SampleFormViewTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_invalid_value(self):
        response = self.c.post(path='/sample_form/', data={'oib': INVALID_OIB})
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            escape('Value does not match with any of the formats: "hr.oib"'))

    def test_valid_value(self):
        response = self.c.post(path='/sample_form/', data={'oib': VALID_OIB})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/success/')
