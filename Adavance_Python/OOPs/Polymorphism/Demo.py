#  polymorphism - in python  is an ability of python object to take many forms
#  if a variable, object and method perform different behavior according to situation is called as polymorphism
# Example --> + symbole is python object and when it comes in between two integer it acts as plus operator and
# perform additon when it comes in between two strings it acts as concatenation

# Example2 --> len function is also best example for polymorphism
var1 = "Dinakar"
var2 = ["dinakar", "ashu", "bikas"]
print(len(var1))
print(len(var2))

# Example 3 - reversed function

emp = ["jay", "viru", "ram"]
compnays = "infosys"

for i in  reversed(emp):
    print(i)

for j in reversed(compnays):
    print(j)
