from pathlib import Path
import os, sys, subprocess


def eprint(s, end="\n"):
    print(s, end=end, file=sys.stderr)


if sys.platform != "linux":
    eprint(
        f"[ERROR] {sys.platform} is not supported. NOTE: Only linux is supported for now."
    )
    eprint("Aborting...")
    exit(1)

CC = "cc"
EXE = sys.argv[0]
ARGS = sys.argv[1:] if len(sys.argv) > 1 else []
RELEASE = "--release" if "--release" in ARGS else ""
HELP = f"""bootstrap.py - build the Glaz bootstrap-compiler

Usage: {EXE} [OPTIONS]

Available options:
   --release             Compile the compiler in release mode, where most optimizations
                         are enabled.
"""


def system(cmd):
    log(cmd)
    if os.system(cmd) != 0:
        log("    failed command")
        exit(1)


def chdir(path):
    log(f"chdir `{path}`")
    os.chdir(path)


def log(s):
    eprint(f">> {s}")


# ====================================== STAGE0 ====================================== #

log("bootstrapping Glaz")

# clone nightly compiler and unzip
system(
    "wget https://github.com/glaz-lang/glaz/releases/download/nightly/glazc-linux-nightly.zip"
)
system("unzip -q glazc-linux-nightly.zip")

# build standard library with nightly compiler
chdir("lib/std")
system("../../glazc --src-name std --no-std --lib src/*.glaz")

# build the Glaz compiler with nightly compiler
chdir("../../compiler/")
system("../glazc --src-name glazc src/*.glaz")
system("./glazc --src-name glazc src/*.glaz")

# ====================================== STAGE1 ====================================== #

# re-build standard library
chdir("../lib/std")
system("../../compiler/glazc --src-name std --no-std --lib src/*.glaz")

# re-build the Glaz compiler
chdir("../../compiler/")
system("./glazc --src-name glazc src/*.glaz")

chdir("../")

# remove basic compiler
system("rm glazc")

# compile the project manager
system(f"./compiler/glazc {RELEASE} --src-name glaz src/*.glaz")

# check Glaz version
system("./glaz version")

# OK!
log("Glaz has been successfully built!")
