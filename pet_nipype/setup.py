from distutils.core import setup
setup(
  name = 'petpipeline',         
  packages = ['petpipeline'],   
  version = '0.1',     
  license='MIT',       
  description = 'PET pre-processing pipeline built on Nipype workflows',
  author = 'Martin Norgaard, Avneet Kaur',
  url = 'https://github.com/openneuropet/PET_pipelines',
  keywords = ['PET', 'neuroimaging', 'nipype', 'preprocessing', 'BIDS'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
          'bids',
          'dataclasses',
          'config',
          'nibabel',
          'numpy',
          'argparse',
          'pyyaml',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
