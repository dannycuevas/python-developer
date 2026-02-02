# Comparisons VS Logicals

They’re related, but they are **not the same thing**.
Let’s break it down very clearly.

### 1) Comparison operators (they _compare_ values)

**Purpose:**  
They compare two values and return a **boolean** (`True` or `False`).

#### Common comparison operators

|Operator|Meaning|Example|Result|
|---|---|---|---|
|`==`|equal to|`5 == 5`|`True`|
|`!=`|not equal to|`5 != 3`|`True`|
|`>`|greater than|`5 > 3`|`True`|
|`<`|less than|`2 < 5`|`True`|
|`>=`|greater or equal|`5 >= 5`|`True`|
|`<=`|less or equal|`3 <= 2`|`False`|

**Key idea:**  
➡️ _Comparison operators produce booleans._

### 2) Logical operators (they _combine_ or _modify_ booleans)

**Purpose:**  
They work **on boolean values** (often produced by comparisons).

#### Logical operators in Python

|Operator|Meaning|Example|Result|
|---|---|---|---|
|`and`|both must be true|`5 > 3 and 2 < 4`|`True`|
|`or`|at least one true|`5 > 10 or 2 < 4`|`True`|
|`not`|negates|`not (5 > 3)`|`False`|

**Key idea:**  
➡️ _Logical operators combine or invert booleans._

### 3) How they work together (very important)

Most real conditions use **both**:
```python
age = 25
age > 18 and age < 65
```

Step-by-step:

1. `age > 18` → `True` (comparison)
    
2. `age < 65` → `True` (comparison)
    
3. `True and True` → `True` (logical)

### 4) Side-by-side comparison

|Feature|Comparison Operators|Logical Operators|
|---|---|---|
|What they do|Compare values|Combine booleans|
|Output|Boolean|Boolean|
|Operate on|Numbers, strings, objects|Booleans|
|Examples|`>`, `==`, `<=`|`and`, `or`, `not`|

### 5) Common beginner confusion (you’re not alone)

❌ Incorrect thinking:
> “`and` compares two values”

✅ Correct thinking:
> “`and` combines the **results** of comparisons”

Example:
```python
# WRONG idea
age and salary # this is not a comparison

# RIGHT
age > 18 and salary > 50000
```

# Precedence of Logical Operators

>Here’s the rule you want to remember:

### NOT → AND → OR

(highest) (middle) (lowest)

- In most languages (Python, JavaScript, and Bash’s `[[ … ]]`) the logical operators are evaluated in this order:

1. **NOT** (`not`, `!`) first
    
2. **AND** (`and`, `&&`) next
    
3. **OR** (`or`, `||`) last   

- So an expression like:
```
A or B and not C
```

- Is read as:
```
A or (B and (not C))
```

- not (false or (not false and false))
- not(false or(true and false))
- not(false or false)
- not(false)
