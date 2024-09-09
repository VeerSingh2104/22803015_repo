import string
def rent_movie(name,cust_name):
    price=0
    movie_name=find(name) in  movies
    customer_name=find(cust_name) in customer["Name"]
    for i in range(len(movies)):
        if movies[i]==name:
           price=movies[i].price
    print("Please pay "+price+"to rent "+movie)
    movie.remove(movie_name)
    customer_name["Rented Movies"]=movie_name


def return_movie(name,cust_name):
    for i in range(len(movies)):
        if(movies[i]==name):
            print("Movie already present!")
            break
    cust_name["Rented Movies"]=""
    movies.append(name)

def rental_report(name):
    curr_name=find(name)in customer["Name"]
    print(customer[curr_name])

movies=["Avengers","The boys","Avatar","Transformers"]
customer = {
    "ID" : [],
    "Name" : [],
    "Age" : [],
    "Rented Movies" : []
    }
customer["ID"].append(1)
customer["ID"].append(2)
customer["ID"].append(3)
customer["ID"].append(4)
customer["Name"].append("Veer")
customer["Name"].append("Phalak")
customer["Name"].append("Pranav")
customer["Name"].append("Divyansh")
customer["Age"].append(20)
customer["Age"].append(20)
customer["Age"].append(19)
customer["Age"].append(20)
customer["Rented Movies"].append("")
customer["Rented Movies"].append("")
customer["Rented Movies"].append("")
customer["Rented Movies"].append("")

c=0
print("Menu:")
print("1. Show Customers.")
print("2. Rent a movie.")
print("3. Return a movie.")
print("4. Generate Rental Report.")
print("5. Show available movies.")
c=int(input("Enter choice: "))
if c==1:
    print(customer["Name"])
elif c==2:
    cust_name=string(input("Enter customer name: "))
    name=string(input("Enter the name of movie you want to rent: "))
    rent_movie(name,cust_name)
    print("Renting Successful")
elif c==3:
    cust_name=string(input("Enter customer name: "))
    name=string(input("Enter the name of movie you want to return: "))
    return_movie(name,cust_name)
    print("Movie Successfully Returned")
elif c==4:
    name=string(input("Enter name: "))
    rental_report(name)
elif c==5:
    print(movies)
else:
    print("Invalid input")
