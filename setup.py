from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
ext_module_file_1 = Extension('Python_Code.file_1',['Python_Code/file_1.py'])
ext_module_file_2 = Extension('Python_Code.file_2',['Python_Code/file_2.py'])
cython_ext_modules = [
    ext_module_file_1,
    ext_module_file_2
]
setup (
    name = "Python_Code",
    ext_modules = cythonize(cython_ext_modules),
    packages=find_packages(),
)