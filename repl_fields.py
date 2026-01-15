age = 24
print("My age is " + str(age) + " years")
# or
print("My age is {0} years. ".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}.".format(31, "Jan", "Mar", "May", "Jul",
                                                                           "Aug", "Oct", "Dec"))

print("There are {0} days in {1} months.".format(31, 7))

print("the goal by player: John - {0} , Andrew {0} , Peter - {1} , Tim - {1} , Tom - {2} , Mike - {2}, Frank - {1}"
      .format(0, 1, 2))

print("""the goal by player: 
John - {0} , 
Andrew {0} , 
Peter - {1} , 
Tim - {1} , 
Tom - {2} , 
Mike - {2}, 
Frank - {1}""".format(0, 1, 2))