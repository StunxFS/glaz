module main

import os

const old_version = "MacroCallExpr"
const new_version = "BuiltinCallExpr"


const old_version2 = "(/.*/s) as (/.*/s)"
const new_version2 = r"cast(\\1, \\2)"

// sed -i -E "s/(<username>.+)name(.+<\/username>)/\1something\2/" file.xml

fn main() {
	mut files := os.walk_ext("./compiler/src/", ".glaz")
	//files << os.walk_ext("./src/", ".glaz")
	//files << os.walk_ext("./tests/", ".glaz")
	//files << os.walk_ext("./lib/", ".glaz")
	for file in files {
		//cmd := "sed -i -e 's/$old_version/$new_version/g' \"$file\""
		cmd := "sed -i -e 's/$old_version2/$new_version2/g' \"$file\""
		println(cmd)
		res := os.execute(cmd)
		if res.exit_code != 0 {
			panic(res.output)
		}
	}
}
