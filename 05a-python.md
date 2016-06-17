# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

The similarities between lists and tuples are as follows:
1. Both contain sequence of values that do not have to be of a certain type.
2. We can  do add elements to both and also multiply them with a scaler
3. They can be sliced to get a certain number of elements from the whole.
4. One can check if element/s are in either with the use of 'in'

The main difference between the two is the tuples are immutable but lists are not. 

Tuples will work as keys in dicitonaries owing to the one reason that they are immutable. The reason is keys have to be made of a data structure that is hashable. In python dictionaries are set up with a hashtable hence the requirement that keys be hashable. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

The similarities between list and sets are that the same as between as between lists and tuples mentioned above.
The difference between lists and sets is that sets cannot have duplicate entries (values). 

For writing up an example for both I thought it would be interesting if I could solve the same problem using sets and list to showcase how sets not having duplicates is an advantage. The problem statement [taken from HackerRank.com] is given two list M and N, print out elements that are either in M or N, but not in both. 

Here are the lists M and N:
M = [2,4,5,9]
N = [2,4,11,12]

Here is solution using set and its methods:
set_M = set(M)
set_N = set(N)

union = set_M.union(set_N)
intersection = set_M.intersection(set_N)
sym_diff = list(union.difference(intersection))

Here is solution using lists methods:
same = []
diff = []
for m in M:
    for n in N:
        if m not in N and m not in diff:
            diff.append(m)
        if m in N and m not in same:
            same.append(m)

for n in N:
    if n not in same:
        diff.append(n)

# the result in both cases is [5,9,11,12]

In terms of performance in finding elements in a set they are on average O(1) and worst case scanario O(n). This is due to it having the same implementation as dictionaries using hastables. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Answer:
It is Pythons' version of an anonymous function, which is a function that is not bound to a name such as with def. This is created at runtime and does not need a return statement, unlike a normal function, and always contains an expression which is returned. Lamdba functions are mainly used in situations which require one requires use of a compact, readible code. A good example is its use in Python standard functions such as filter(), map() and reduce() each of which require in input a list and a function to add to list. We could use a standard function, but if the use case is temporary and to make code readible we resort to using lambda functions. An illustrative example is below:

>>> from functools import reduce
>>> foo = [2,56,3,6,8]
>>> reduce(lambda x,y: x+y, foo)
75

An example where we use lambda function as the key argument to 'sorted' is as follows:
>>> student_details = [
			('Alice', 'A', 16),
			('Mark', 'C', 15),
			('Abe', 'B', 13)
	]
>>> sorted(student_details, key=lambda student: student[2]) # here we are sorting by student age
[('Abe', 'B', 13), ('Mark', 'C', 15), ('Alice', 'A', 16)]

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

Answer:
List comprehension allows one to create lists in a concise way. It is a design pattern that is borne off of the requirement to run loops efficiently, and in a human readible form. 

Below are two examples where list comprehension is used followed by equivalent 'map' and 'filter' expressions:

# given inList 'squares_list_comp' makes an list of squares of this list. 'squares_map' does the same with 'map' expression

intList = [1,2,3,4,5]

squares_list_comp = [x**2 for x in intList]
squares_map = list(map(lambda x: x**2, intList))

# 'filter_list_comp' filters out values from list 'squares_list_comp' elements that are less than 10. 
# 'filter_function' does the same with 'filter expression'

filter_list_comp = [x for x in squares_list_comp if x < 10]
filter_function = list(filter(lambda x: x < 10, squares_list_comp))

By capabilities I am assuming efficiency of the code being in terms ot time taken to complete execution. It seems list comprehension for squaring is slightly more efficient then using the 'map' expression quite simply since map uses lambda function. In the case of the filtering portion the list comprehension is an order of magniture faster using the 'filter' expression when compared to it list comprehension counterpart. This might be due to the fact that 'filter' is more optimized of the two. In order to determine the time taken to execute each code piece above I used the following:

import time

start_time = time.clock()

# run function under consideration

print('time taken: %s seconds' % (time.clock() - start_time))

Example of set comprehension:
{x for x in range(50)}

For example of dictionary comprehension I decided to try to have a little fun. I have taken a known tongue twister and counted the word frequencies. In the example below word_count shows the example of dictionary comprehension:

tongue_twister = '''Peter Piper picked a peck of pickled peppers.
A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers,
Where's the peck of pickled peppers Peter Piper picked?'''

for ch in ['.', ',', '?', "\'s"]:
    if ch in tongue_twister:
        tongue_twister = tongue_twister.replace(ch, '')

tongue_twister = tongue_twister.lower()   
tongue_twister_list = tongue_twister.split()

word_count = {item: tongue_twister_list.count(item) for item in set(tongue_twister_list)}

print(word_count)

# result:
# {'the': 1, 'piper': 4, 'if': 1, 'a': 3, 'picked': 4, 'pickled': 4, 'where': 1, 'peck': 4, 'of': 4, 'peter': 4, 'peppers': 4}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
Answer:
Solution is in file 'q5_datetime.py' under heading (a). The output is 937 days.

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

Answer:
Solution is in file 'q5_datetime.py' under heading (b). The output is 513 days. 

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

Answer:
Solution is in file 'q5_datetime.py' under heading (c). The output is 7850 days.

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





