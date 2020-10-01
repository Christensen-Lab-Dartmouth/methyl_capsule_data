from setuptools import setup
with open('README.md','r', encoding='utf-8') as f:
      long_description = f.read()
setup(name='methyl_capsules',
      version='0.1',
      description='Data used for capsule-related projects.',
      url='https://github.com/Christensen-Lab-Dartmouth/methyl_capsule_data',
      author='Joshua Levy',
      author_email='joshualevy44@berkeley.edu',
      license='MIT',
      scripts=[],
      entry_points={
            'console_scripts':[]
      },
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['methyl_capsules'],
      install_requires=['pandas'],
      package_data={'methyl_capsules': ['data/*']})
