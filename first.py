# print ("hello, world!")

# how to deal with str and value to print.
#name = input("name: ")
#print (f"heloooooooooooooo {name}")





# conditions
#n =  int(input ("number: "))
#if n > 0:
#    print ("the number is greater 0")
#elif n < 0:
#    print ("the number is smaller 0")
#else :
#    print ("equal to 0")




# sequences
# name = ["harry", "baha" , "suhaib"]
# n = int(input ("enter a number : "))
# print(f" the {n} name is: {name[n]}")

# DATA STRUCTURE
# list      name = ["harry", "baha" , "suhaib"]
# tuple 
# set       name = set()
# dict      name = {"harry":"amman", "baha":"turkey" , "suhaib":"istanbul"}

# s = set ()
# #for the set we can add by :
# print (s)
# s.add(0)
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# # and delete by:
# s.remove(1)
# # to print the length of any set:
# print (f" the length for the set is: {len(s)}")


# for loops
# for i in (range(6)):
#     print(i)
# or
# names="abcdefghijklmnopqrstu"
# for name in names:
#     print(name)


# Dictionary 
# name = {"harry":"amman", "baha":"turkey" , "suhaib":"istanbul"}
# name ["musab"]="istanbul"
# print(name["musab"])


# function

# def square(x):
#     return x * x

# for i in range(10):
#     print(f"the square of {i} is {square(i)}")



# classes 
# class point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = point(2,4)
# print(p.x)
# print(p.y)

####### Another example #####

# class Flight():
#     def __init__(self, capacity):
#         self.capacity= capacity
#         self.passengers=[]

#     def add_passengers(self, name):
#         if not self.remaining_seats():
#             return False
#         self.passengers.append(name)
#         return True
    
#     def remaining_seats(self):
#         return self.capacity - len(self.passengers)

# flight = Flight(2)
# people = ["baha", "baha", "baha"]
# for name in people:
#     if flight.add_passengers(name):
#         print("done")
#     else:
#         print("no seats")






########### DECORATORS ##############
# def announce(f):
#     def wrapper():
#         print("about to run the function")
#         f()
#         print("done running the function")
#     return wrapper 


# @announce
# def hello():
#     print("hello world!")

# hello()





############### lambda ########################

people = [{"name" : "c", "house": "b"},
          {"name" : "b", "house": "a"},
          {"name" : "a", "house": "c"},
]

def f(person):
    return person ["name"]
    
people.sort(key=f)
print(people)

# better way to maintain the same result is by using lambda and there is how.

people = [{"name" : "c", "house": "b"},
          {"name" : "b", "house": "a"},
          {"name" : "a", "house": "c"},
]

people.sort(key=lambda person : person ["name"])
print(people)