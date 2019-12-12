#!/usr/bin/env python
# -*- coding: utf-8 -*-

# example 1
try:
    1 / 0
except:
    print("[1] You cannot divide by zero!")

# example 2
try:
    1 / 0
except ZeroDivisionError:
    print("[2] You cannot divide by zero!")

# example 3
my_dict = {"a":1, "b":2, "c":3}
 
try:
    value = my_dict["d"]
except KeyError:
    print("[3] That key does not exist!")

# example 4
my_list = [1, 2, 3, 4, 5]
 
try:
    my_list[6]
except IndexError:
    print("[4] That index is not in the list!")

# example 5
my_dict = {"a":1, "b":2, "c":3}
 
try:
    value = my_dict["d"]
except IndexError:
    print("[5] This index does not exist!")
except KeyError:
    print("[5] This key is not in the dictionary!")
except:
    print("[5] Some other error occurred!")

# example 6	
try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("[6] An IndexError or KeyError occurred!")


# example 7
my_dict = {"a":1, "b":2, "c":3}
 
try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement has executed!")