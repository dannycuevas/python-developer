# 1) Core built-in types (at a glance)

| Category | Type        | Literal Example    | Main Uses                                            |
| -------- | ----------- | ------------------ | ---------------------------------------------------- |
| Numeric  | `int`       | `42`               | Counting, indexes, arithmetic without decimals       |
| Numeric  | `float`     | `3.14`             | Real numbers/decimals, measurements                  |
| Numeric  | `complex`   | `2+3j`             | Complex math (rare in beginner work)                 |
| Text     | `str`       | `"hello"`          | Human-readable text, file paths, JSON keys, messages |
| Binary   | `bytes`     | `b"hi"`            | Raw bytes, networking, files                         |
| Binary   | `bytearray` | `bytearray(b"hi")` | Mutable bytes; modify binary data                    |
| Logic    | `bool`      | `True` / `False`   | Conditions, flags                                    |
| Null     | `NoneType`  | `None`             | “No value”, missing/optional                         |

>“Ordered” and “mutable” don’t apply to scalars like `int`/`float`; they apply to _collections_.


# 2) Core collection types

| Type    | Literal Example    | Ordered?          | Mutable? | Duplicates? | Indexable? | Typical Operations               | Main Uses                            |
| ------- | ------------------ | ----------------- | -------- | ----------- | ---------- | -------------------------------- | ------------------------------------ |
| `list`  | `[1, 2, 3]`        | **Yes**           | **Yes**  | **Yes**     | **Yes**    | append, pop, sort, slice         | General-purpose ordered collection   |
| `dict`  | `{"a": 1, "b": 2}` | **Yes** (Py 3.7+) | **Yes**  | Keys unique | Key access | get, update, keys/values/items   | Mappings, config, lookup tables      |
| `tuple` | `(1, 2, 3)`        | **Yes**           | No       | **Yes**     | **Yes**    | indexing, unpacking              | Fixed groups, function returns       |
| `set`   | `{1, 2, 3}`        | No                | **Yes**  | No          | No         | add, remove, union, intersection | Membership tests, remove duplicates  |
| `range` | `range(5)`         | **Yes**           | No       | Yes         | **Yes**    | iterate, len, indexing           | Efficient integer sequences in loops |

>In Python 3.7+ and up, `dict` will be "ordered" by language guarantee.


# 3) Numbers—key differences

|Type|Precision|Common Pitfalls|When to Use|
|---|---|---|---|
|`int`|Arbitrary precision|None for normal use|Counts, loop indexes, exact arithmetic|
|`float`|IEEE-754 double|Rounding issues (e.g., `0.1+0.2!=0.3`)|Measurements, averages; format for display|
|`complex`|Two floats (real+imag)|Rare in general dev|Signal processing, math/engineering|


# 4) Text & bytes—what to pick?

|Type|What it Holds|Good For|Example|
|---|---|---|---|
|`str`|Unicode text|UI messages, file paths, JSON|`"México"`, `"logs/app.log"`|
|`bytes`|Immutable bytes|Network protocols, file I/O|`b"\xFF\xA0"`|
|`bytearray`|Mutable bytes|In-place binary edits|`ba = bytearray(b"\x00\x01")`|


# 5) Collections - Choose the right one

| You need…                                             | Pick    | Why                                                         |
| ----------------------------------------------------- | ------- | ----------------------------------------------------------- |
| An **ordered** list you can grow/shrink               | `list`  | Flexible, sliceable, sortable                               |
| **Key → value** lookups                               | `dict`  | Readable mappings; natural for configs/records              |
| A **fixed** group of items                            | `tuple` | Immutable; safe as dict keys if elements are hashable       |
| **Fast membership** and deduplication                 | `set`   | Hash-based; `x in s` is fast; set math (union/intersection) |
| A large **integer sequence** without storing them all | `range` | Lazy, memory-efficient iteration                            |


# 6) Common operations & (typical) time costs

> Big-O is rough/typical for CPython; good enough for beginner intuition.

|Structure|Operation|Typical Cost|Notes|
|---|---|---|---|
|`list`|Index `lst[i]`|O(1)|Random access by index|
|`list`|Append `lst.append(x)`|Amortized O(1)|Occasional resize|
|`list`|Insert/Delete (middle)|O(n)|Shifts elements|
|`set` / `dict`|Membership / Get|O(1) average|Hash based|
|`set` / `dict`|Insert/Delete|O(1) average|May rehash/resize|
|`tuple`|Index|O(1)|Immutable; fewer ops|
|`range`|Iterate|O(n) total|Constant memory|


# 7) Hashability & keys (quick rules)

| Concept                            | Rule of Thumb                                                    |
| ---------------------------------- | ---------------------------------------------------------------- |
| Lists are **not** hashable         | Don’t use `list` as a dict key or put it in a `set`              |
| Dict/set keys must be **hashable** | Immutable types like `int`, `str`, `tuple` (of hashables) are OK |
| Tuples can be hashable             | Only if all their elements are hashable                          |


# 8) “Mini cheat-sheet” (tiny examples)

| Task                  | Snippet                           |
| --------------------- | --------------------------------- |
| Create list & append  | `nums = [1, 2]; nums.append(3)`   |
| Slice list            | `nums[1:] # from index 1`         |
| Dict get with default | `cfg.get("timeout", 30)`          |
| Dict comprehension    | `{k: len(k) for k in ["a","bb"]}` |
| Tuple unpacking       | `x, y = (10, 20)`                 |
| Set union             | `{1,2}                            |
| Range loop            | `for i in range(5): ...`          |
| String format         | `f"Hello {name}"`                 |
