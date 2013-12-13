from setuptools import setup, find_packages
import os

version = '1.1dev'

setup(name='silva.pageactions.printfriendly',
      version=version,
      description="Display a simple printable version of the content in Silva CMS",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='silva pageactions print',
      author='Infrae',
      author_email='info@infrae.com',
      url='https://github.com/silvacms/silva.pageactions.printfriendly',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['silva', 'silva.pageactions'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'five.grok',
          'grokcore.chameleon',
          'setuptools',
          'silva.core.views',
          'silva.pageactions.base',
          ],
      )
