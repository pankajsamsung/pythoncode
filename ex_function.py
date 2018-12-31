#! /usr/bin/env python
def greet(name):
    """This function greets to the person passed in as parameter"""
    print("Hello, " + name + ". Good morning!")

print "Enter the name for greet: "
name1 = raw_input ("name: ")

greet(name1)