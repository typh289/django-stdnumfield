# coding=utf-8
from django.core.exceptions import ValidationError
from django.test.testcases import TestCase

from stdnumfield.validators import StdnumFormatValidator


class ValidatorsTets(TestCase):

    def test_invalid_format(self):
        validator = StdnumFormatValidator(formats=['damn'])
        self.assertRaisesMessage(
            ValueError,
            'Unknown stdnum format: "damn"',
            validator,
            '123456',
        )

    def test_valid_format_valid_value(self):
        validator = StdnumFormatValidator(formats=['hr.oib'])
        validator('69435151530')

    def test_valid_format_invalid_value(self):
        validator = StdnumFormatValidator(formats=['hr.oib'])
        self.assertRaises(
            ValidationError,
            validator,
            '69435151531',
        )
