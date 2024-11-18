#  storing objects in lists

class Movies(object):

    def __init__(self, title, min, hero):
        self.title = title
        self.min = min
        self.hero = hero

    def printer(self):
        print(f"Title is : {self.title}\nruntime is :{self.min}\nhero is :{self.hero}")

list_of_movies =[]
while True:

    title = input("Enter the title of the movie : ")
    runtime = input("Enter the runtime of the movie : ")
    hero = input("Enter the hero of the movie : ")
    obj = Movies(title,runtime,hero)
    list_of_movies.append(obj)
    print("Movie is added into the list")
    ans = input("Do you want to add another movie (y/n)")
    if ans!= 'y':
        break

print("All the movies information ")
print("********\n***********")
for obj in list_of_movies:
    obj.printer()
    print("---------------")


