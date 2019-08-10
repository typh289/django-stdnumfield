#!/usr/bin/env python
"""
This is a dirty little script that parses stdnum and finds it's supported
formats. It is unfortunate that this information is not available in a
readable way from stdnum itself.

This should be executed before making a new release and / or after updating
stdnum.
"""
import importlib
import operator
import pkgutil
import os
from dataclasses import dataclass

import stdnum


def get_submodules(module):
    if not module.__file__.endswith('__init__.py'):
        return []
    path = os.path.join(os.path.dirname(module.__file__))
    submodule_names = [
        f'{module.__name__}.{info.name}'
        for info in pkgutil.iter_modules([path])
    ]
    seen_names = set()
    for submodule_name in submodule_names:
        submodule = importlib.import_module(submodule_name)
        if submodule.__name__ not in seen_names:
            seen_names.add(submodule.__name__)
            yield submodule


@dataclass
class Validator:
    module: object

    @property
    def doc(self):
        first_line = next(filter(None, self.module.__doc__.split('\n')))
        first_line = first_line.strip('.')
        return first_line

    @property
    def depth(self):
        move = 0
        if self.relative_name.startswith('iso'):
            move = -1
        return -1 * max(1, self.name.count('.') + move)

    @property
    def name(self):
        return self.module.__name__

    @property
    def relative_name(self):
        return self.name[len('stdnum.'):]


def find_validators(module):
    for submodule in get_submodules(module):
        if hasattr(submodule, 'validate'):
            yield Validator(submodule)
        else:
            yield from find_validators(submodule)


def prepate_formats(validators):
    validators = list(validators)
    validators.sort(key=operator.attrgetter('depth', 'relative_name'))

    def quote(val):
        return val.replace('"', r'\"')

    formatted = '{{\n{}\n}}'.format('\n'.join(
        f'    "{validator.relative_name}": u"{quote(validator.doc)}",'
        for validator in validators
    ))
    return formatted


TEMPLATE = '''# coding=utf-8
"""
This file is auto-generated via `bin/update_formats.py`.
"""

# fmt: off
formats = {formatted_formats}
# fmt: on
'''


def write_to_file(formatted_formats):
    target = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '../stdnumfield/_formats.py'))
    content = TEMPLATE.format(formatted_formats=formatted_formats)
    with open(target, 'w') as f:
        f.write(content)


def main():
    validators = find_validators(stdnum)
    formats = prepate_formats(validators)
    write_to_file(formats)


if __name__ == '__main__':
    main()
