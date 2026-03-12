# Escape Sequence in Python

- We would not be able to use apostrophes inside of strings when using single quotes 
```python
weather = 'It's raining out there'
```
- Python is reading it as the beginning and end of a string

- One way to fix it, is using double quotes
```python
weather = "It's raining"
```
- But then, we would not be able to use double quotes inside the starting double quotes of the string, so that is another issue

- **To fix this issues with syntax and quotes, we can use an "escape sequence", by simply adding an slash symbol `\` right before the apostrophe

- Example code using an escape sequence
```python
>>> weather = "It\'s \"kind of\" raining out there"
>>> print(weather)
It's "kind of" raining out there
```


# Add a Tab with `\t`

- Now, we can add a "tab space" by using the `\t` in a string
```python
>>> weather = "\t It\'s \"kind of\" raining out there"
>>> print(weather)
         It's "kind of" raining out there
```


# Add a new line with `\n`

- We can an entire new line in a string by adding `\n`  so you can break down text or give it a better format
```python
>>> weather = "\t It\'s \"kind of\" raining out there \n so bring an umbrella or something"
>>> print(weather)
         It's "kind of" raining out there 
 so bring an umbrella or something
```
