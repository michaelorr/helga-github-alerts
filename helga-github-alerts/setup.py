from setuptools import setup, find_packages

version = '0.1'

setup(
    name="helga-github-alerts",
    version=version,
    description=('A helga plugin to handle webhook events from github.'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Software Development :: Version Control',
        'Intended Audience :: Developers',
        'Framework :: Twisted',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='helga github notifications pull requests irc bots xmpp hipchat',
    author='Michael Orr',
    author_email='michael@orr.co',
    url='https://github.com/morr/helga-github-alerts',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga_github_alerts'],
    zip_safe=True,
    entry_points = dict(
        helga_webhooks=[
            'github_alerts = helga_github_alerts:github_alerts',
        ],
    ),
)
