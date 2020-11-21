# We're linking against '../build/bin/libhumon-d.a' which is built by `../build.py`.

from setuptools import setup, Extension

setup(name="humon",
      version="0.0.0",
      packages=["humon"],
      ext_package="humon",
      ext_modules=[Extension("humon",
                             include_dirs = ['./clib/include/humon', './clib/src'],
                             #libraries = ['humon'],
                             #library_dirs = ['./humon/build/bin'],
                             extra_compile_args = ['-ggdb3', '-O0'],
                             sources = ["./clib/src/ansiColors.c",
                                        "./clib/src/encoding.c",
                                        "./clib/src/node.c",
                                        "./clib/src/parse.c",
                                        "./clib/src/printing.c",
                                        "./clib/src/tokenize.c",
                                        "./clib/src/trove.c",
                                        "./clib/src/utils.c",
                                        "./clib/src/vector.c",
                                        "./humon/cpkg/enumConsts.c",
                                        "./humon/cpkg/humonModule.c", 
                                        "./humon/cpkg/node-py.c",
                                        "./humon/cpkg/token-py.c",
                                        "./humon/cpkg/trove-py.c",
                                        "./humon/cpkg/utils.c"])
                   ])
      