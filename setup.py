from setuptools import setup, find_packages

setup (
       name='razzy',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['SpeechRecognition', 'pyaudio', 'selenium'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='mdorrell',
       author_email='',

       #summary = 'Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )
