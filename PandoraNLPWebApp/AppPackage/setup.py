from setuptools import find_packages
from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
  name='PandoraNLP',
  version='1.0.0',
  description='Perform NLP Operations',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Ashwin Raj',
  author_email='rajashwin812@gmail.com',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Students',
    'Topic :: Software Development :: NLP Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
  ],
  packages==find_packages(exclude=('tests*',)),
  keywords='Pandora NLP',
  python_requires='>=3.6, <4',
  project_urls={  # Optional
    'Bug Reports': 'https://github.com/ashwinraj-in/Workspace/blob/main/.github/ISSUE_TEMPLATE/bug_report.md',
    'Feature Request': 'https://github.com/ashwinraj-in/Workspace/blob/main/.github/ISSUE_TEMPLATE/feature_request.md',
    'Say Hi!': 'http://github.com/ashwinraj-in',
    'Source': 'https://github.com/ashwinraj-in/Workspace/tree/main/PandoraNLPWebApp',
  },
)
