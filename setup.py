from setuptools import setup, find_packages


setup(
    name='shum',
    version='0.1.0',
    description="Vulyk Speech Utterance Markup",
    long_description="""
    """,
    author="Vol Kyrylov",
    author_email='vol@wilab.org.ua',
    url='https://github.com/proger/shum',
    packages=find_packages(include=["shum.*"]),
    install_requires=[
        "wandb",
        "vulyk"
    ],
    license="MIT",
    keywords='vulyk',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Ukrainian',
        'Programming Language :: Python :: 3.8',
    ],
)
