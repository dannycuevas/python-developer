# FOR Loop example

For example, we will have a List with 3 Values, for each Value we will want to get their percentages, and we have a line of code for each value
But, we want to "iterate" instead of having to write code for each value manually, and just rather create a FOR loop and save lines and time on coding

- Here is what the code would look like without using FOR loops, when trying to get the percentages of each Value
- We call each Value by its index number from the List "scores"
```python
scores = [17, 14, 16]

percentage1 = scores[0] / 20 * 100
percentage2 = scores[1] / 20 * 100
percentage3 = scores[2] / 20 * 100

print(percentage1)
print(percentage2)
print(percentage3)

85.0
70.0
80.0
```

- To create our FOR loop, we will pick whatever name for a random variable in your loop (we will name it "s"), that will go "inside of your List" (in this case, the List name is "scores"), example:
```python
for s in scores:
```

- We then are able to substitute each line of the "percentage" with the loop action
- The "random variable" will go inside of the List, as mentioned before, by going value by value, and transforming itself into each of the Values of the List
```python
scores = [17, 14, 16]

for s in scores:
	s / 20 * 100
```

- To be able to print out the result of each iteration, we want to first stored the result of each iteration into another variable
- We can name that variable however we like as well, in this case we will call it "p"
- Then print out that variable that was storing the results
```python
scores = [17, 14, 16. 18]

for s in scores:
	p = s / 20 * 100
	print(p)

85.0
70.0
80.0
90.0
```
