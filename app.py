def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("find - Find movie(s) by year")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

# formatting
def list(movie_list):
    if len(movie_list) == 0:
        print("Empty Movie List.\n")
        return # if empty, return to terminate
    else: # if not empty, get to work
        i = 1
        for movie in movie_list: # loop through movie list
            row = movie
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")" + " @ $" + str(row[2]))
            i += 1
        print()

# search feature
def find(movie_list):
  # check to see if movie list has any data in it
  if len(movie_list) == 0: # if empty, tell user no movies to search. add some
    print("There are no movies to search. Please add some")
  else:
    year = int(input("enter a year: "))
    found = 0 # keeps track of movies found
    
    for movie in movie_list:
      if movie[1] == year:
        # 0 is title, 
        # 1 is year
        # 2 is price
        print(movie[0] + " was released in " + str(year))
        found += 1 # if match, increment found
    # a grammar check    
    if found == 1:
      print(str(found) + " movie found.")
    else:
      print(str(found) + " movies found.")
    print()

# add to database    
def add(movie_list): # we pass in movie_list so we have something to add to
    name = input("Name: ")
    year = int(input("Year: "))
    price = float(input("Price: "))
    movie = [] # we build the movie to add to movies list
    movie.append(name)
    movie.append(year)
    movie.append(price)
    movie_list.append(movie) # we append the movie we built, to the movies list.
    print(movie[0] + " was added.\n") # we tell user the title that has been added
    
# delete from our movie list that we pass in so we have something to delete
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list): # we can't delete nothing and we can't delete something that exceeds our list
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie[0] + " was deleted.\n")
        
def main():
    movie_list = [
      ["Monty Python and the Holy Grail", 1975, 9.99],
      ["On the Waterfront", 1954, 9.99],
      ["Cat on a Hot Tin Roof", 1958, 9.99]
      ]
    print("Movie List For Cool Kids\n")
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "find":
            find(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
