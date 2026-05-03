# file handling => it is the process of reading and writing files in python. 
# it is used to store data permanently on the disk. we can use the built-in open() function to open a file and perform various operations on it such as reading, writing, and closing the file.


# p= open(r"./dictionary.py")
# print(p.read())  # reads the entire content of the file 

# modes 
# r => read mode (default) => it is used to read the content of the file. if the file does not exist, it raises a FileNotFoundError.
# w => write mode => it is used to write content to the file. if the file does not exist, it creates a new file. if the file already exists, it overwrites the existing content.
# a => append mode => it is used to write content to the file. if the file does not exist, it creates a new file. if the file already exists, it appends the new content to the existing content.
# x => exclusive creation mode => it is used to create a new file. if the file already exists, it raises a FileExistsError.
# r+ => read and write mode => it is used to read and write content to the file. if the file does not exist, it raises a FileNotFoundError. if the file already exists, it allows us to read and write content to the file.



# p= open("./dictionary.py", "r")
# print(p.read())  # reads the entire content of the file
# p.close()  # closes the file


# p= open("../test.py", "w") # opens the file in write mode. if the file does not exist, it creates a new file. if the file already exists, it overwrites the existing content.
# p.write("hello World3") # writes the content to the file
# p.close() # closes the file


# p= open("../test.txt", "a") # opens the file in append mode. if the file does not exist, it creates a new file. if the file already exists, it appends the new content to the existing content.
# p.write("\nhello World3") # writes the content to the file
# p.close() # closes the file





