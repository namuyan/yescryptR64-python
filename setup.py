from distutils.core import setup, Extension

yescryptr64_module = Extension('yescryptr64',
                            sources = ['yescrypt.c'],
                            extra_compile_args=['-march=native', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'yescryptr64',
       version = '1.0',
       description = 'Bindings for yescryptr64 proof of work.',
       ext_modules = [yescryptr64_module])
