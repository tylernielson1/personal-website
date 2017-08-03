from setuptools import setup

setup(name='flaskapp',
      version='1.0',
      description='Tyler Nielson\'s personal website.',
      author='Tyler Nielson',
      author_email='devemail@gmail.com',
      url='http://tylernielson.net',
      install_requires=[
          'Flask>=0.10.1', 'flask_wtf', 'flask_mail', 'Flask-Mail'
      ])
