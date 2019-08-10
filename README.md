[![CircleCI](https://circleci.com/gh/frnhr/django-stdnumfield/tree/master.svg?style=shield)](https://circleci.com/gh/frnhr/django-stdnumfield/tree/master)
[![codecov](https://codecov.io/gh/frnhr/django-stdnumfield/branch/master/graph/badge.svg)](https://codecov.io/gh/frnhr/django-stdnumfield)

version: 0.1.5

## What's an stdnum?

See [python-stdnum](https://arthurdejong.org/python-stdnum/doc/1.5/index.html)


## Local development and testing

There is a gazillion ways of managing Python versions these days. I prefer 
pip and [pyenv](https://github.com/pyenv/pyenv):
``` bash
pyenv install --skip-existing 3.7.4
pyenv install --skip-existing 3.6.9
pyenv install --skip-existing 3.5.7
pyenv install --skip-existing 3.4.10
pyenv install --skip-existing 2.7.16
pyenv virtualenv 3.7.4 django-stdnumfield
echo 'django-stdnumfield:2.7.16:3.6.9:3.5.7:3.4.10' > .python-version
pip install -e .[dev]
```
