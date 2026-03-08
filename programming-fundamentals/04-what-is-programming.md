
- When you write code, it is not machine code, it is "source code", like writing code with C# or python for example
- Machines and computers do not understand "source code"
	- They only understand "Machine Code"

- To convert your source code into machine code you have 2 options:
	- Compile
	- Interpret


# Compiling code

- When you write your source code, your machine will also convert that source code into machine code using a "compiler"
- A "compiler" is a program, that goes through your source code file instruction by instruction, and convert them into machine code
- Your source code will then convert into a new file containing machine code
- Thus, with machine code, this is something that the CPU can actually understand and run, or execute


- The result of the whole "compilation" is called: "executable", or executable file
- So now, I can give you that file, and you can run my program


- With compiling you do not get my source code, that stays on my machine, you do not even know what programming language I used


# Using an Interpreter

- With this, I would just give you a copy of my source code
- Meaning, you need to do the conversion to machine code, not me (like when "compiling") 
- For you to convert my source code into machine code with the copy I gave you, you will need an "interpreter"
	- so "interpreted languages" are often cross-platform, because as long as the person you are sending your source code to has the interpreter, you do not care what operating system they use


- "Interpreters" are usually bundled inside web browsers or even operating systems themselves, and they will be used automatically
	- example, there is a `javascript` interpreter inside every web browser
- Note that the conversion from source code into machine code does not happen automatically
	- in fact, it does not happen until you decide to run the program on your computer 
	- at that time, the interpreter will go through that source code instructions line by line and converts them into machine code as needed
	- then it runs that machine code, it does not save it as a separate file
