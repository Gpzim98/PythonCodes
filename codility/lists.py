list = [ [] ] * 5
print list  # [[],[],[],[],[]]
list[0].append(10)
print list  # [[10],[],[],[],[]]
list[1].append(20)
print list  # [[10],[20],[],[],[]]
list.append(30)
print list  # [[10],[20],[],[],[30]]

# The statement list = [ [ ] ] * 5 does NOT
# create a list containing 5 distinct lists; rather, 
# it creates a a list of 5 references to the same list.
