# Glaz Changelog

## [Unreleased]

* add `unreachable` builtin function.

## [v0.1.10b] (2022-04-01)

* `extern` blocks for extern C code.
* Disallow references types (`&T`) in `extern` blocks.
* Check missing return in functions.
* Check unreachable code.
* Deprecate `[]T`/`[EXPR]T`, use `[T]`/`[T; EXPR]` instead.
* Disallow return address of local value.
* Add basic `autodrop` system (experimental).
* Implement native test framework, add command `test`, add `test` blocks.
* Support `compile` flag for C files (`#compile "some_thing.c"`).
* `test_framework`: colorize output.
* Remove `map_len!()` macro, use field `map.len` instead.
* Remove `{ ... }` map syntax, use `map<str, VType>{ ... }` instead.
* Check mutable values in `for (mut k, mut v in expr) { ... }`.
* Struct update syntax: `Account{ ...old_people, banned: true }`.
* Support `?i32`(`fn x() ?i32 { return 1; }`).
* Disallow expressions evaluated but not used.
* Support labels and `goto`.
* Support dot enum syntax (`.EnumField`).
* Add `Box` struct, a smart pointer type for heap allocation.
* Add `drop` macro for dropping a value early.
* Auto-generate `drop` methods.
* Add `std::conv` module.
* Support tuple assignment (`let (a, b) = (1, true);`).
* Add `typeof!()` macro (`typeof!(true) == "bool"`).
* Support blank ident (`_ = 1;`).
* Add `breakpoint!()` macro.
* Use `Self` as an alias for `T` in `impl T {}`.
* Deprecate `#[]` syntax, use `@[]` instead for attributes.
* Support `??` (the null-coalescing operator).
* Add `new` command (`glaz new project-name`).
* Support opaque C structs (`struct OpaqueType;`).
* Support `boxed_value.*` and `boxed_value.method_from_t()`.
* Add `box` macro, for boxed values (`box!(5)`).
* Check uninitialized struct fields.
* Support field attributes, add `@[required]` attribute.
* Support escaped keywords (`struct Crash { @break: i32 }`).
* Support default values for sum types (`type StrOrInt = str | i32 = 0;`).
* Support `noinit` attribute for struct fields.
* Support struct inheritance!
* Remove `map_deinit` macro.
* Check attributes.
* Support multi-line reports.
* `rt`: print current type name with sum-types/base structs `cast`s.
* Support boxed values passed directly to references.
* Full support for polymorphism!
* Support protected fields and methods with `@[protected]` attribute.
* Full support for virtual methods.
* Full support for abstract methods.
* Variadic arguments (`fn join(base: str, dirs: ...str)`).
* Support libraries!
* Split compiler and project manager (`compiler/` and `src/` folders).
* Support `noreturn` attribute.
* Change ternary expression syntax (`(cond)? expr : expr2` => `if (cond) expr else expr2`).
* Array decompose syntax (`sum(...arr_i32)`).
* Support default values in enums.
* Support comptime `if`!
* Add `std::strings` and `std::path` modules.
* Exhaustive `switch`.
* Add `run` command (`glaz run`).
* Support `union` types.
* Support `fixed_array[:]`.
* Support comptime `if` expression.
* Unify `std`, `rt` and `test_framework` libraries under a single library called `std`.

## [v0.1.0b] (2021-12-14)

* First release (We generate the self-hosted compiler :D!).

[Unreleased]: https://github.com/glaz-lang/glaz/compare/v0.1.10b...HEAD
[v0.1.0b]: https://github.com/glaz-lang/glaz/releases/tag/v0.1.0b
[v0.1.10b]: https://github.com/glaz-lang/glaz/releases/tag/v0.1.10b
