[![CircleCI](https://circleci.com/gh/frnhr/django-stdnumfield/tree/master.svg?style=shield)](https://circleci.com/gh/frnhr/django-stdnumfield/tree/master)
[![codecov](https://codecov.io/gh/frnhr/django-stdnumfield/branch/master/graph/badge.svg)](https://codecov.io/gh/frnhr/django-stdnumfield)

version: 0.1.5

## Usage:

    from stdnumfield.models import StdNumField


    class SomeMode(models.Model):
        field = StdNumField(
            'hr.oib',  # stdnum format
        )


    class SampleModelForm(ModelForm):
        class Meta:
            model = SomeModel
            fields = ('field',)
            error_messages = {
                'field': {
                    'stdnum_format':_("Not maching format %(format_list)s"),  # you can override exception message
                },
            }

## What's an stdnum?

See [python-stdnum](https://arthurdejong.org/python-stdnum/doc/1.5/index.html)
