import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='replreports',
	version='0.8.14',
	author='codemonkey51',
	author_email='contact@codemonkey51.dev',
	description='A fork of mat\'s repltalk module',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/codemonkey51-org/repl-talk-api',
	packages=setuptools.find_packages(),
	install_requires='aiohttp',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Framework :: AsyncIO'
	],
)
