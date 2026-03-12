# Files and I/O

- Using Jupyter notebooks, we can create a text file and add text to it
- In this example, the `myfile.txt` is the name of the text file we are creating
- This will save the file in the working directory of the Jupyter notebook
```python
%%writefile myfile.txt
Hello, this is my first file with Jupyter Notebooks
this is the second line of my testing file
this will be the third line of my file

Writing myfile.txt
```

### Open and Work with Files

- To be able to work with files, you will need to first open them, as if they were variables, from there you can run methods and such
- Open the file and assign it a Variable name
```python
file = open("myfile.txt")
```

- Open up a file to work with it, in this case under the Variable `file`, and then print the contents of that "file" under that Variable
- We are still using `myfile.txt` and the method `.read()` inside of the `print()` Function
```python
with open("myfile.txt", mode='r') as file:
	print(file.read())

>>>Hello, this is my first file with Jupyter Notebooks
this is the second line of my testing fi...
```

### Read the contents of a File

- Method `.read()` to return a giant String of the contents of your file (make sure it is already opened up)
```python
file.read()

>>>'Hello, this is my first file with Jupyter Notebooks\nthis is the second line of my testing file\nthis will be the third line of my file\n'
```

- To be able to re-read the contents of your file again you will need to reset the cursor
- We use the `.seek()` to be able to reset it at index zero and be able to read the file again
```python
file.seek(0)
file.read()

>>>'Hello, this is my first file with Jupyter Notebooks\nthis is the second line of my testing file\nthis will be the third line of my file\n'
```

- Now we read each line in the file as a separate object, like in a List-form for example
- To do this we use the `.readlines()` method
```python
file.readlines()

>>>['Hello, this is my first file with Jupyter Notebooks\n',
 'this is the second line of my testing file\n',
 'this will be the third line of my file\n']
```

- Close the file when you are done working with it, otherwise your operating system may consider it as "still open" and you run into errors with that file
```python
file.close()
```

### Write and Overwrite with Files

- Open up the file with `with` so you do not have to worry about closing it, and keeps it open for modifications or changes
- Example syntax working with the `myfile.txt` text file, assigning `file` as the random Variable name to open it
```python
with open("thefile.txt") as file:
	content = file.read()

text
>>>'Hello, this is my first file with Jupyter Notebooks\nthis is the second line of my testing file\nthis will be the third line of my file\n'
```

### Appending to Files

- When appending new text to existing files, make sure they are already opened and writing
```python
with open("myfile.txt", mode='r+') as file:
  text = file.read()
```

- Then you can append new text to a existing file with `-a`
```python
%%writefile -a myfile.txt
NEW text with appending for testing

>>>Appending to myfile.txt
```

- Another example, append a new line with the "mode" to append
- This will work in a single block of code, and it will not provide any output, so just read the file again
```python
with open("myfile.txt", mode='a') as file:
  file.write("LAST LINE to be appended")
```

#### "Modes" for Files

- `mode='r'` is read only
- `mode='w'` is write only (will overwrite files or create new)
- `mode='a'` is append only (will add on to existing files)
- `mode='r+'` reading and writing
- `mode='w+'` is writing and reading (overwrites existing files or create new ones)

- Example with "Reading" mode
```python
with open("myfile.txt", mode='r') as file:
  text = file.read()
```

### Quick exercise

- This exercise will require several lines of code
- Write a script that opens a file named `'test.txt'` , writes `'Hello World'`  to the file, then closes it
```python
file = open("test.txt", "w")
file.write("Hello World")
file.close()
```
