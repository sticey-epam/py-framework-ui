from bs4 import BeautifulSoup




with open("parsing/library.xml", "r") as library:


    soup = BeautifulSoup(library, features="xml")

    book_attribute = ['author', 'title', 'genre', 'price', 'publish_date', 'description']

    all_books = soup.find_all('book')
 

    counter = 0
    while counter < len(all_books):

        if "the" in all_books[counter].text:
            print(all_books[counter].text)

        counter += 1

  


