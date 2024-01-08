# (C) 2021 Glaz Developers. All rights reserved. Use of this source code
# is governed by an MIT license that can be found in the LICENSE file.

# script used to run the bad tests

import os
import sys
import glob
import subprocess

ARGS = sys.argv[1:]
assert len(ARGS) == 1

IS_INOUT = ARGS[0] == "inout"
files = glob.glob(f"tests/{ARGS[0]}/*.glaz")
files_len = len(files)

exit_code = 0


def filename(path):
    return os.path.splitext(os.path.basename(path))[0]


if IS_INOUT:
    for i, file in enumerate(files):
        print(f"[{i+1}/{files_len}] {file} -> ", end="")
        try:
            with open(file.replace(".glaz", ".out"), "r") as out_content:
                res = subprocess.run(
                    [
                        "./compiler/glazc",
                        "--src-name",
                        filename(file),
                        file,
                    ],
                    capture_output=True,
                )
                if res.returncode == 0:
                    res = subprocess.run(
                        [
                            f"./{filename(file)}",
                            file,
                        ],
                        capture_output=True,
                    )
                    res_stderr = res.stderr.decode()
                    out_content_str = out_content.read()
                    if res.returncode != 0 and res_stderr != out_content_str:
                        print("FAIL")
                        print("Expected:\n", out_content_str)
                        print("Got:\n", res_stderr)
                        exit_code = 1
                    else:
                        print("OK")
                    os.remove(filename(file))
                else:
                    print("FAIL [failed compilation]")
        except FileNotFoundError:
            print("FAIL [.out file not found]")
            exit_code = 1
else:
    for i, file in enumerate(files):
        print(f"[{i+1}/{files_len}] {file} -> ", end="")
        try:
            with open(file.replace(".glaz", ".out"), "r") as out_content:
                res = subprocess.run(
                    [
                        "./compiler/glazc",
                        "--src-name",
                        filename(file),
                        file,
                    ],
                    capture_output=True,
                )
                res_stderr = res.stderr.decode()
                out_content_str = out_content.read()
                if res.returncode != 0 and res_stderr != out_content_str:
                    print("FAIL")
                    print("Expected:\n", out_content_str)
                    print("Got:\n", res_stderr)
                    exit_code = 1
                else:
                    print("OK")
        except FileNotFoundError:
            print("FAIL [.out file not found]")
            exit_code = 1

exit(exit_code)
