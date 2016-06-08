# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

Answer:
Here is a discription of what each ls command does:
ls: this will list all the files in the current working directory.

ls -a: list all files including entries that start with '.''

ls -l: list files in 'long format'. In this format we get a lot of useful information such as size of the file, owner of file, when it was last modified, etc.

ls -lh: same as 'ls -l' except in a human readible form.

ls -lah: same as above except now we also have all files even containing those that start with '.'

ls -t: show list of files / directory sorted by modified time.

ls -Glp: Here we list all file but without the list group with '/' appended to directories


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

Answer:

ls -m

ls -r

ls -d

ls -o: like -l, but do not list group information

ls -s: print size of each file


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

Answer:
 
xargs will read the items from standard input and excute the command one or more times with the initial-arguments followed by the items that are read from standard input. 

Take for example, we have the following files in a directory:
$ ls

one.c one.h one.c two.h

We would like to remove all the file that have extension '.c'. Using command such as: 
$ rm -rf find . -name '.c' 

will not work since in this case we have a long list of parameters passed to a command. A better alternative is to apply xargs in the following way:

$ find . -name '.c' | xargs rm -rf
