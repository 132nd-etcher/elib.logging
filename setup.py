# coding=utf-8
"""
Logging library
"""

from setuptools import find_packages, setup

requirements = [
]

test_requirements = [
    'epab',
]

"""
Development Status :: 1 - Planning
Development Status :: 2 - Pre-Alpha
Development Status :: 3 - Alpha
Development Status :: 4 - Beta
Development Status :: 5 - Production/Stable
Development Status :: 6 - Mature
Development Status :: 7 - Inactive
"""

CLASSIFIERS = filter(None, map(str.strip,
                               """
Development Status :: 1 - Planning
Environment :: Win32 (MS Windows)
Intended Audience :: End Users/Desktop
Natural Language :: English
Operating System :: Microsoft :: Windows :: Windows 7
Operating System :: Microsoft :: Windows :: Windows 8
Operating System :: Microsoft :: Windows :: Windows 8.1
Operating System :: Microsoft :: Windows :: Windows 10
License :: OSI Approved :: MIT License
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
""".splitlines()))

entry_points = '''
[console_scripts]
elib_logging=elib_logging.__main__:main
'''

# noinspection SpellCheckingInspection
setup(
    name='elib_logging',
    zip_safe=False,
    entry_points=entry_points,
    package_dir={'elib_logging': 'elib_logging'},
    package_data={},
    test_suite='pytest',
    packages=find_packages(),
    install_requires=requirements,
    tests_require=test_requirements,
    python_requires='>=3.6',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    license='MIT',
    classifiers=CLASSIFIERS,
)
