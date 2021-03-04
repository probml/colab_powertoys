import setuptools

setuptools.setup(name="colab_powertoys",
version="1.0.0",
description="A set of python functions that enhances your experience with Google's Colab",
packages=setuptools.find_packages("src"),
package_dir={"":"src"}
)