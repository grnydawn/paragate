"paragate setup module."

def main():

    from setuptools import setup
    from paragate.main import Paragate as pgate

    console_scripts = ["paragate=paragate.__main__:main"]
    install_requires = ["microapp>=0.3.9"]

    setup(
        name=pgate._name_,
        version=pgate._version_,
        description=pgate._description_,
        long_description=pgate._long_description_,
        author=pgate._author_,
        author_email=pgate._author_email_,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "Topic :: Scientific/Engineering",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        keywords="paragate",
        packages=[ "paragate" ],
        include_package_data=True,
        install_requires=install_requires,
        entry_points={ "console_scripts": console_scripts,
            "microapp.projects": "paragate = paragate"},
        project_urls={
            "Bug Reports": "https://github.com/grnydawn/paragate/issues",
            "Source": "https://github.com/grnydawn/paragate",
        }
    )

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
