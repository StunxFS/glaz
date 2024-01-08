# The Glaz programming language

## Overview

Glaz is a general purpose programming language designed for the development
of stable and safe software. The syntax of the language is inspired by Rust.

Glaz uses the C programming language as its main backend.

> **NOTE:** The compiler currently only supports Linux (I work on an Ubuntu
based distro).

> **NOTE:** Currently the language is in alpha state, and therefore its syntax
and the language API is not stable, and may change in the long term.

Before continuing, I assume you know how to use a console, otherwise you can
read this tutorial:
[The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview).

## Building Glaz from source

> **NOTE:** Only **linux** _for now_.

To build the compiler, we must have the following:

* Any C compiler (GCC, Clang, etc.).
* Python3 for bootstrapping/run scripts.
* [Git](https://git-scm.com/).

First we clone the repository:

```bash
$ git clone --depth 1 https://github.com/glaz-lang/glaz
```

Then we access the `glaz` folder and run the `bootstrap.py` script:

```bash
$ cd glaz
$ python3 bootstrap.py # or `python3 bootstrap.py --release` for optimized version
```

> **NOTE:** This script uses the
[nightly compiler](https://github.com/glaz-lang/glaz/releases/tag/nightly),
which is built with every commit, to generate the Glaz compiler.

Ready! :)

## Hello World!

Let's start with the typical `Hello World!`:

We create a file called `hello_world.glaz` with the following content:

```rs
use std::console;

fn main() {
    console::println("Hello World!");
}
```

Then we compile that file:

```bash
$ ./compiler/glazc hello_world.glaz -o hello_world
```

We'll get an executable called `hello_world` as output, so we run it:

```bash
$ ./hello_world
```

We should see this output:

```bash
Hello World!
```

Excellent! You have compiled your first program in Glaz!

## Hello World! with the Glaz project manager

The repository also comes with a
[project manager](https://github.com/glaz-lang/glaz/tree/main/src), this
too is compiled with the `bootstrap.py` script.

Let's use it! First, we create a project called `hello_world`:

```bash
$ ./glaz new hello_world
project `hello_world` (bin) was created successfully!
$ cd hello_world/
$ tree .
.
├── glaz.proj
└── src
    └── main.glaz

1 directory, 2 files
$ cat glaz.proj
name: "hello_world"
description: ""
version: "0.0.0"
type: "bin"
homepage: ""
authors: []
dependencies: []
$ cat src/main.glaz
use std::console;

fn main() {
	console::println("Hello World!");
}
```

Ready! That's it. As you can see, Glaz generates a basic structure for
our project.

Let's now compile and run the project:

```bash
$ ../glaz build
$ ./hello_world
```

We should see this output:

```bash
Hello World!
```

The 2 previous steps can be done with a single command:

```bash
$ ../glaz run
```

Ready!

## Creating a symbolic link for Glaz

Previously we did everything inside the `glaz` folder, and used compiler
and GPM relative paths, but this is not correct.

The ideal is to have both binaries as commands that we can use anywhere,
so GPM (**G**laz **P**roject **M**anager) has a command called `symlink`.

We return to the terminal and go to the root folder of the project:

```bash
$ cd ..
```

So we run:

```bash
$ sudo ./glaz symlink
```

This will create compiler and GPM symlinks in `/usr/local/bin`.
And, in order to do that, we need to give the GPM admin permissions via
`sudo`.

The process shouldn't take long, and if there weren't any errors, we'll
see the following output:

```bash
The project manager and compiler were successfully symlinked!
```

Ready! We can use the GPM anywhere:

```bash
$ glaz version
Glaz 0.1.0
```

## Editor/IDE support

* [LiteXL (the main editor I use :P)](https://github.com/lite-xl/lite-xl-plugins/blob/master/plugins/language_glaz.lua)
(Syntax highlighting only).

* * *

<div align="center">

[next](01_code_structure.md)

</div>
