# Glaz Tests

This directory contains all the compiler tests. Each of the subdirectories
is explained below:

* `bad` contains multiple Glaz source files, it can be run via
`python3 tests/run_out_tests.py bad`.

* `good` is a Glaz project, it can be run via `glaz test`.

* `inout` is a directory containing tests that have an output,
which must be the same as found in the respective `.out` file, it can be run
via `python3 tests/run_out_tests.py inout`.

The `gen_out_files.py` script can be used to generate the `.out` files used
in the tests.
 
