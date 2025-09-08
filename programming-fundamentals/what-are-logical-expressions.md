
# Simple definitions you can keep forever 🙂

# What is a Proposition?

- Proposition is a statement (or "expression") that can either be True or False
- Computers make decisions using logical propositions

- **Proposition (logic):** A statement that is **unambiguously True or False**.  
    _Example:_ “It is raining.” (either True or False right now)

- **Logical expression (programming):** An expression your program can **evaluate to True/False** _given current values_.  
    _Example:_ `temp > 30 && isRaining`

# Connectives / Logical Operators

- We can create complex logic propositions using **connectives** (aka logical operators):
	- and
	- or
	- not
	- etc


# What’s a **conditional**?

A **conditional** is a decision point in your code.  
It says: “**If** this is true, do X; **else** do Y.”

- It’s the **if / else** (or switch) in any language.
    
- It doesn’t decide by itself—it **uses the result** of a logical expression (below) to choose a path.

Tiny example (Python):
```python
if window_is_open and is_raining:
    close_window()
else:
    open_window()
```


# What’s a **logical expression**?

A **logical expression** is a yes/no question your code can evaluate.  
When the computer checks it, it becomes **True** or **False**—no maybes.

- Built from **comparisons** and **logical operators**.
    
- You feed this into a conditional.

**Building blocks**
- Comparisons: `==` (equal), `!=` (not equal), `>` `<` `>=` `<=`
    
- Logical operators: `AND` (`and`, `&&`), `OR` (`or`, `||`), `NOT` (`not`, `!`)
    
- Example: 
```
window_is_open AND is_raining
```

**Tiny examples**
- Python: `age >= 18 and country == "MX"`
    
- Bash: `[ "$temp" -gt 30 ] && [ "$raining" = "no" ]`
    
- JavaScript: `(items.length > 0) || isAdmin`

#### How they work together
1. **Logical expression** → “Is the condition true?”    
2. **Conditional** → “Based on that answer, which path do we run?”

Think: **question → answer → action**

#### Quick cheatsheet
- **Conditional** = `if (…) { … } else { … }`
    
- **Logical expression** = the stuff inside `if (…)` that evaluates to True/False
    
- Use **parentheses** to make intent clear: `(A && B) || C`
    
- Don’t mix up **assignment** vs **comparison**:
    
    - Python/JS: `=` sets a value, `==` compares (and `===` in JS for strict compare)
        
    - Bash: strings `[ "$a" = "$b" ]`, numbers `[ "$x" -eq "$y" ]`

If you remember: **“Conditionals choose; logical expressions decide,”** you’re golden.

#### Quick view
- **Proposition (logic):** A statement that is **unambiguously True or False**

- _Example:_ “It is raining.” (either True or False right now)
    
- **Logical expression (programming):** An expression your program can **evaluate to True/False** _given current values_.  
    _Example:_ `temp > 30 && isRaining`

#### How they connect
- A **logical expression becomes a proposition once all its variables have concrete values**.
    
    - `x > 5` by itself isn’t yet a proposition (it depends on `x`).
        
    - With `x = 7`, it becomes the proposition **“7 > 5”**, which is **True**.

Think of it like this:
> **Template (logical expression)** + **actual data (variable values)** → **concrete statement (proposition)**
