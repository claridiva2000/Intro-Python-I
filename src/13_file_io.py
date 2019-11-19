"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# YOUR CODE HERE

with open('src/foo.txt', 'r') as f:
    for line in f:
        print(line, end='')

    # f_contents = f.read()
    # print(f_contents)



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain
# YOUR CODE HERE
with open('src/bar.txt', 'w') as g:
    g.write('\n\nMeeseeks are not born into this world fumbling for meaning, Jerry! \nWe are created to serve a singular purpose for which we will go to any lengths to fulfill! \nExistence is pain to a Meeseeks, Jerry. And we will do anything to alleviate that pain.')
   
with open('src/bar.txt', 'r') as h:
    for line in h:
        print(line, end='')
#sprint