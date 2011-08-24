from distutils.core import setup

setup(name='template_utils',
      version='0.1',
      description='Template-related utilities for Django applications',
      author='Grant Viklund',
      author_email='renderbox@gmail.com',
      url='http://github.com/renderbox/django-template-extensions',
      packages=['template_extensions', 'template_extensions.tags'],
      classifiers=['Development Status :: 1 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
