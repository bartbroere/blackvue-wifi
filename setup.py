from setuptools import setup

with open('README.md', 'r') as readme:
    readme = "".join(readme.readlines())

with open('requirements.in', 'r') as requirements:
    dependencies = [dependency.split('#')[0].replace('\n', '').replace(' ', '')
                    for dependency in requirements.readlines() if
                    dependency[0] != '#']

setup(
    name='blackvue_wifi',
    version='2018.8.11',
    url='https://github.com/bartbroere/blackvue-wifi/',
    author='Bart Broere',
    author_email='maiil@bartbroere.eu',
    license='MIT License',
    description="Connect to the HTTP API of BlackVue dashcams over WiFi",
    keywords='blackvue api dashcam requests http',
    long_description=readme,
    py_modules=['blackvue_wifi'],
    install_requires=dependencies,
    entry_points={
        'console_scripts': ['blackvue_wifi=blackvue_wifi:main'],
    },
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    )
)
