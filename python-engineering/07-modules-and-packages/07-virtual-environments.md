# Virtual Environments

- Keeping in mind that packages and libraries are always improving, like "increasing" in their versions, you are still "installing the packages" or Modules, and they will come with their own "current versions"
- What happens when the libraries or Modules are out of date to work with Python at a certain point?
	- one option is to reinstall them
	- this will get you the latest version

```python
pip uninstall <package-name>

pip install <package-name>
```

### Different versions of a Library

- Now, what happens when you want your projects to use different versions of a library?
	- maybe a project that you started 5 years ago will not be compatible with the current version of the library you want to use
	- and then you are also starting a new project on the side too, and this one will require the current version of the library
	- thus, you will need to run 2 different projects with different versions of a library you would want to use
	- for this, we use "virtual environments"

### Enter Virtual Environments

- Virtual Environments answers the question of being able to have "different versions" of your packages and modules on your same machine
	- and also be able to have different projects using different versions of them
	- each project will have its own packages

- This is a common situations in the industry, as packages and libraries are constantly being updated, and we have packages that depend on other packages that need to have certain versions
	- thus, making Virtual Environments a reliable system in companies
