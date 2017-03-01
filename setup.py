from setuptools import setup

url = ""
version = "0.1.0"
readme = open('README.rst').read()

setup(name="datademo",
      packages=["datademo"],
      version=version,
      description="Package to demonstrate dapi functionality",
      long_description=readme,
      include_package_data=True,
      author="Tjelvar Olsson",
      author_email="tjelvar.olsson@jic.ac.uk",
      url=url,
      install_requires=[
        "click",
        "dtool",
        "pygments",
      ],
      entry_points={
          'console_scripts': ['datademo=datademo.cli:cli']
      },
      download_url="{}/tarball/{}".format(url, version),
      license="MIT")
