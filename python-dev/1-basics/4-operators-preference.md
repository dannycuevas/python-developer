# Operator Preference in Python

- Different operators have precedence over different ones
- Math will work the same in any programming languages

- This is the order of precedence, from top to bottom:
```
()
** (to the poder of...)
* /
+ -
```


# Logic Operator Precedence

- You may remember from mathematics that when you have a complicated mathematical expression, there are rules about how it should be evaluated.

- For example, in mathematics if you have the following expression:
```
2+3×5
```
- Then the result is 17 because **multiplication** should be evaluated before **addition**.

- That is, when the expression is evaluated you evaluate it as 3×5 then add 2, rather than 2+3, then multiply by 5.

- Similarly, logic operators have an order of precedence. In this task, you need to research and find out the order of precedence of the logic operators OR, AND and NOT.


>Here’s the rule you want to remember:

# NOT → AND → OR

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
