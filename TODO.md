* [ ] Improve and document the standard library.
* [ ] Convert the `switch` statement to an expression.
* [ ] Replace old `as` cast syntax with new `cast` in compiler code.
* [ ] If we have an immutable reference to a value, we must not be able to
take a mutable reference to that value as well.
* [ ] support a special function for each module called `init`, which is called
automatically when a program is executed or a library is initialized.

## Glaz TODOs list

* [X] `goto` (unsafe), labels.
* [X] Libraries.
* [X] `std` library.
* [X] Support `??` (null-coalescing operator): `optional_value ?? default_value`.
* [X] Variadic arguments (`fn join(base: str, dirs: ...str)`).
* [X] Array decompose syntax (`sum(...arr_i32)`).
* [X] comptime `if`: `$if (_LINUX_ or USE_LINUX_CODE) { ... } $elif (_WINDOWS_) { ... } $else { ... }`.
* [X] `if` expr: `let a = if (use_level > 1) 10 else 0;`.
* [ ] Function types: `type Matcher = fn(&str, i32);`.
* [ ] Lifetimes (`&^a i32`).
* [ ] Support `if (let x = res_or_opt_fn(); x.len == 1) { ... }`.

## Don't allocate optionals values on the heap

Optional types should not be allocated on the heap, instead a simple
structure should be used.

Both optionals pointers and optionals references are exempt from this rule.

```c
struct _Opt_T {
	T value;
	bool is_null;
};
```

## Don't allocate sumtypes values on the heap

Currently the values of sumtypes are allocated on the heap, this makes
unnecessary use of the heap.

## Rearrange arrays in Glaz

Currently the compiler has 2 types of arrays: dynamic and fixed. But this is
not appropriate, since the compiler cannot know when an array can be mutated
or not (and this does not help autodrop much).

The solution to this problem is the following:

* [X] Dynamic arrays become vectors (`vec[T]` would be the type syntax).
* [X] Fixed arrays would be converted to a normal array (and still have
the same type syntax: `[i32; 5]`).
* [X] A new array type would be added: Slices (whose type syntax would
be the same as for dynamic arrays: `[i32]`).

This way the compiler would know when to mark a value as moved or not, or
when it can be mutated or not.

The slices would be simple references to a array or vector (behind the scenes
they would be a struct with 2 fields: ptr and len). The slices would be immutable.

## Support mutable result of functions

This would be to check that the return value (either pointer or reference)
from a function can be mutable.

```rust
struct Ptr {
	mut ptr: rawptr
}

impl Ptr {
	/// Return the `ptr` field as an immutable pointer.
	@[unsafe]
	pub fn get_ptr(&self) rawptr {
		return self.ptr;
	}

	/// Return the `ptr` field as a mutable pointer.
	@[unsafe]
	pub fn get_mut_ptr(mut &self) mut rawptr {
		return self.ptr;
	}
}
```

This way the compiler can make sure that immutable values cannot be mutated
completely.

```rust
let mut ptr = Ptr{ptr: &math::PI}.get_ptr(); // ERROR: cannot mutate immutable value
```

## To implement

* [ ] `interface`s: `interface IPlugin { fn run(); }`.
* [ ] Closures: `let closure = fn (a: i32) { ... }; closure(5);`.
* [ ] Generics: `fn cast<T, F>(value: F) T { return value as T; }` -> `cast::<u8>(5)`.
