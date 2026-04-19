
# Python Package Index

>**Find, install and publish Python packages with the Python Package Index**
https://pypi.org/

- Another super power of Python, and the reason that Python is such a big part of any and almost all companies, is, it empowers us all, all developers, to write any python code and be able to share everything with each other
	- so, instead of just having our own code written with just core functionality of the language, we also use any and all code from anyone around the world as our own, so we do not keep "reinventing the wheel"
	- we can download Modules from anyone around the world, and then import it, and just use it
- We do not always have to write something from absolute scratch, we can reuse code from around the world, use bits and pieces, Modules, and libraries, and combine our code so we can built something amazing and even faster
	- **bringing in the code other people write will need `pip`, and they will be called "packages" or "libraries", thus, "we are installing packages/libraries"**
	- and libraries are maintain by people too, by other programmers
	- and so, they are always improving, the libraries are always "increasing" in their versions

- This is why Python has amazing libraries like;
	- NumPy
	- Pandas
	- TernsorFlow
	- etc
	- all of these are libraries (also known as "packages") that were built by the outside developer community
	- meaning, not the python community, instead just developers like you and I, people around the world

### The `pip` Command

- The `pip` utility comes with Anaconda as well
- Check your version of `pip` installed (capital "V")
```python
pip -V
# or
pip3 -V

# the output
pip 25.1 from /home/user/anaconda3/lib/python3.13/site-packages/pip (python 3.13)
```

- Install a package / library
```python
pip install <package-name>
```

### Example Package / Library

https://pypi.org/project/pyjokes/
- Tested with this package to run "jokes" from a Jupyter notebook cell, it worked just fine
```python
import pyjokes

pyjokes.get_joke('en', 'neutral')

# the output
>>>"Why was the developer bankrupt? He'd used all his cache."
```

- And from the terminal it also worked
```python
(base) mitrandir@vivobook:~/repos/python-developer$ pyjoke

>>>"I'm not anti-social; I'm just not user friendly."
```

### The new `uv` package manager

[https://docs.astral.sh/uv/](https://docs.astral.sh/uv)

- There is a new tool called `uv` which is gaining popularity in the Python world. It helps you download packages like `pip` in the previous video, but it does it much faster
- I'll leave a link for you to explore it, but keep in mind it is still a fairly new technology so it's changing a lot and it's still much less popular than `pip`

- It's also a package manager that has a ton of other features (but we don't need to get into it now) 
	- Although it is still new, it is becoming the popular way to handle packages and create virtual environments in python
