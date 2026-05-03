
import os

print("press 1 for creating a file: ")
print("press 2 for reading file: ")
print("press 3 for updating file: ")
print("press 4 for deleting file: ")
print("press 5 for view all files: ")


choice = int(input("Enter your choice: "))

try:
    if choice==1:
        filename= input("Enter the file name: ")
        if os.path.exists(filename):
            print("File already exists")
        else:
            p= open(filename, "w")
            content= input("Enter the content: ")
            p.write(content)
            p.close()
            print("File created successfully")
    elif choice==2:
        filename= input("Enter the file name: ")
        if os.path.exists(filename):
            with open(filename, "r") as p:
                content= p.read()
                p.close()
        else:
            print("File does not exist")
    elif choice==3:
        filename= input("Enter the file name: ")
        if os.path.exists(filename):
            p= open(filename, "a")
            content= input("Enter the content: ")
            p.write(content)
            p.close()
            print("File updated successfully")
        else:
            print("File does not exist")
    elif choice==4:
        filename= input("Enter the file name: ")
        if os.path.exists(filename):
            os.remove(filename)
            print("File deleted successfully")
        else:
            print("File does not exist")
    elif choice==5:
        files= os.listdir()
        print("Files in the current directory:")
        for file in files:
            print(file)
    else:
        print("Invalid choice")

except Exception as err:
    print(f"An error occured: {err}")
    
        

    


