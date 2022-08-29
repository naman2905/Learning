Context managers allow you to allocate and release resources precisely when you want to. 


Managing Resources: In any programming language, the usage of resources like file operations or database connections is very common. But these resources are limited in supply. Therefore, the main problem lies in making sure to release these resources after usage. If they are not released then it will lead to resource leakage and may cause the system to either slow down or crash. It would be very helpful if users have a mechanism for the automatic setup and teardown of resources. In Python, it can be achieved by the usage of context managers which facilitate the proper handling of resources. The most common way of performing file operations is by using the keyword as shown below: 

# Python program showing
# a use of with keyword
 
with open("test.txt") as f:  
    data = f.read()
Let’s take the example of file management. When a file is opened, a file descriptor is consumed which is a limited resource. Only a certain number of files can be opened by a process at a time. The following program demonstrates it. 

file_descriptors = []
for x in range(100000):
    file_descriptors.append(open('test.txt', 'w'))
Output:

Traceback (most recent call last):
  File "context.py", line 3, in 
OSError: [Errno 24] Too many open files: 'test.txt'
An error message saying that too many files are open. The above example is a case of file descriptor leakage. It happens because there are too many open files and they are not closed. There might be chances where a programmer may forget to close an opened file. 

Managing Resources using context manager: Suppose a block of code raises an exception or if it has a complex algorithm with multiple return paths, it becomes cumbersome to close a file in all the places. Generally in other languages when working with files try-except-finally is used to ensure that the file resource is closed after usage even if there is an exception. Python provides an easy way to manage resources: Context Managers. The with keyword is used. When it gets evaluated it should result in an object that performs context management. Context managers can be written using classes or functions(with decorators).

Creating a Context Manager: When creating context managers using classes, user need to ensure that the class has the methods: __enter__() and __exit__(). The __enter__() returns the resource that needs to be managed and the __exit__() does not return anything but performs the cleanup operations. First, let us create a simple class called ContextManager to understand the basic structure of creating context managers using classes, as shown below: 

# Python program creating a
# context manager
 
class ContextManager():
    def __init__(self):
        print('init method called')
         
    def __enter__(self):
        print('enter method called')
        return self
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
 
with ContextManager() as manager:
    print('with statement block')
Output:

init method called
enter method called
with statement block
exit method called









Dunder methods are names that are preceded and succeeded by double underscores, hence the name dunder. They are also called magic methods and can help override functionality for built-in functions for custom classes.


