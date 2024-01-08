# (C) 2021 Glaz Developers. All rights reserved. Use of this source code
# is governed by an MIT license that can be found in the LICENSE file.

# script used to generate the `.out` files

import os
import glob
import subprocess


def filename(path):
    return os.path.splitext(os.path.basename(path))[0]


files = glob.glob("tests/bad/*.glaz")
for i, file in enumerate(files):
    out_name = file.replace(".glaz", ".out")
    res = subprocess.run(
        ["./compiler/glazc", "--src-name", filename(file), file],
        capture_output=True,
    )
    if res.returncode != 0:
        with open(out_name, "w") as f:
            f.write(res.stderr.decode())
    else:
        print(f"[BAD: exit_code == 0] {file}")
        os.remove(filename(file))

files = glob.glob("tests/inout/*.glaz")
for i, file in enumerate(files):
    file_name = filename(file)
    out_name = file.replace(".glaz", ".out")
    res = subprocess.run(
        ["./compiler/glazc", "--src-name", file_name, file],
        capture_output=True,
    )
    if res.returncode == 0:
        res = subprocess.run(
            [f"./{file_name}"],
            capture_output=True,
        )
        with open(out_name, "w") as f:
            f.write(res.stderr.decode())
        os.remove(file_name)
    else:
        print(f"[BAD: failed compilation] {file}")
