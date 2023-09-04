class Book:
    def __init__(self, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year


book = Book("", "", "")


class Bookstore:
    def __init__(self, lib):
        self.lib = lib
        self.book = book

    def add_book(self):
        self.book.title = input("Enter the title: ")
        self.book.author = input("Enter the author: ")
        self.book.pub_year = input("Enter the year of publication: ")
        operative = (self.book.title, self.book.author, self.book.pub_year)
        self.lib.append(operative)
        print(self.lib)
        fork = int(input("Would tou like to add one more else book? 1 - Yes; 2 - No "))
        match fork:
            case 1:
                self.add_book()
            case 2:
                if_del = int(input("Would tou like to delete some book? 1 - Yes; 2 - No "))
                match if_del:
                    case 1:
                        self.remove_from_lib()
                    case 2:
                        print("Thank you, good bye")
                    case _:
                        print("Incorrect input")
            case _:
                print("Incorrect input")

    def remove_from_lib(self):
        search = input("Enter the title to search and delete: ")
        for item in self.lib:
            try:
                item.index(search)
                self.lib.remove(item)
                print(self.lib)
            except ValueError:
                pass

    def get_lib(self):
        if not self.lib:
            print("The library is empty.")
        else:
            for bk in self.lib:
                res = list(bk)
                print(f'Title: {res[0]}, Author: {res[1]}, Year of publishing: {res[1]}')


def main():
    bookstore = Bookstore(lib=[])

    while True:
        print("Options:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Display library")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            bookstore.add_book()
        elif choice == '2':
            bookstore.remove_from_lib()
        elif choice == '3':
            bookstore.get_lib()
        elif choice == '4':
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()


# class User:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#
# user = User("Stepan", "Bandera", 114)
#
# print(user.full_name)

