import wikipedia
from wikipedia import WikipediaPage


search = input("Enter your search term ")
while search != "":
    try:
        print(wikipedia.search(search))
    except wikipedia.exceptions.DisambiguationError as error:
        print(error.options)
    search = input("Enter your search term ")

