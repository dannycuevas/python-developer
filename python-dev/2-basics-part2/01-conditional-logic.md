# 🧠 CONDITIONAL LOGIC (Python)

## 🔹 What is Conditional Logic?

- **Conditional logic** allows us to control **when** certain code runs.
- This is called **control flow**.
- Control flow means:
  > *“Run this code only if a condition is met.”*

- In Python, conditions are based on **True / False** values (booleans).

---

## 🔹 Control Flow Keywords in Python

Python uses **three main keywords** for conditional logic:

| Keyword | Purpose |
|------|--------|
| `if` | Check a condition |
| `elif` | Check another condition if previous ones failed |
| `else` | Catch-all when nothing else matched |

### ⚠️ Important Python Rule
- Python uses:
  - **colons `:`**
  - **indentation (whitespace)**  
to define blocks of code (not `{}` like other languages).

---

## 🔹 How `if` Statements Work

- An `if` statement checks a **condition**
- If the condition is `True` → the indented code **runs**
- If the condition is `False` → the code is **skipped**

### Basic Syntax
```python
if condition:
    # code runs only if condition is True
```

## IF Statement (Simple Example)

Example: Check if a person is old enough to drive.
```python
is_old = True

if is_old:
    print("You are old enough to drive")
```

Output
```python
You are old enough to drive
```

### Why this works
- `is_old` is `True`    
- Python enters the `if` block    
- Indented code executes

---

## ELSE Statement

- `else` runs **only when the `if` condition is False**    
- It acts as the **final fallback**

Example
```python
is_old = False

if is_old:
    print("You are old enough to drive")
else:
    print("You are not old enough to drive")
```

Output
```python
You are not old enough to drive
```

### Key Rule
> `else` runs **only if all previous conditions fail**

---

## ELIF Statement (Else If)

- `elif` lets you check **multiple conditions**    
- Python checks conditions **top to bottom**    
- The **first True condition wins**    
- After a match, Python **stops checking**    

### Syntax
```python
if condition1:
    # action 1
elif condition2:
    # action 2
else:
    # action 3
```

ELIF Example (Location Check)
```python
loc = "Bank"

if loc == "Auto Shop":
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool")
elif loc == "Store":
    print("Welcome to the store")
else:
    print("I do not know much")
```

Output
```python
Money is cool
```

### Why that output?
- `"Bank"` matches the second condition    
- Python runs that block and stops

ELIF Example (Multiple Conditions)
```python
is_old = False
is_licensed = True

if is_old:
    print("You are old enough to drive")
elif is_licensed:
    print("You have a license to drive")
else:
    print("No check here")
```

Output
```python
You have a license to drive
```

### Important Correction (Conceptual Fix ✅)
- `elif` does **not** run the `else` block    
- `else` runs **only if all `if` and `elif` conditions are False**    

---

# Execution Flow (Very Important Table)

| Step | What Python Does               |
| ---- | ------------------------------ |
| 1    | Checks `if` condition          |
| 2    | If True → runs block and stops |
| 3    | If False → checks first `elif` |
| 4    | Continues until one is True    |
| 5    | If all are False → runs `else` |

## Conditions Are Usually Comparisons

Most conditions use **comparison operators**:

|Operator|Meaning|Example|
|---|---|---|
|`==`|equal|`age == 18`|
|`!=`|not equal|`x != 0`|
|`>`|greater than|`age > 18`|
|`<`|less than|`age < 65`|
|`>=`|greater or equal|`score >= 90`|
|`<=`|less or equal|`temp <= 0`|

---

## Using Logical Operators in Conditions

Conditions are often combined using:

|Operator|Meaning|
|---|---|
|`and`|both must be True|
|`or`|at least one True|
|`not`|reverses True/False|

### Example Complete Real-World Pattern
```python
if condition1:
    perform_action_1
elif condition2:
    perform_action_2
elif condition3:
    perform_action_3
else:
    perform_default_action
```

---

## Common Beginner Mistakes (Watch Out!)

|Mistake|Why It’s Wrong|
|---|---|
|Missing indentation|Python relies on indentation|
|Forgetting `:`|Syntax error|
|Using `=` instead of `==`|Assignment vs comparison|
|Assuming all conditions are checked|Python stops at first True|

---

## One-Line Memory Rules 🧠

- **`if`** → _check first_    
- **`elif`** → _check another_    
- **`else`** → _nothing else worked_    
- **Indentation = code block**    
- **First True wins**
