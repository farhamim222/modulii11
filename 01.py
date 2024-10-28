# Base class for publication
class Publication:
    def __init__(self, name):
        self.name = name

# Subclass for Book
class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def tulosta_tiedot(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Subclass for Magazine
class Magazine(Publication):
    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def tulosta_tiedot(self):
        print(f"Magazine Name: {self.name}")
        print(f"Editor-in-Chief: {self.editor_in_chief}")

# Main program
if __name__ == "__main__":
    # Create magazine and book objects
    aku_ankka = Magazine("Aku Ankka", "Aki Hyyppä")
    hytti_no6 = Book("Hytti n:o 6", "Rosa Liksom", 200)

    # Print the information
    aku_ankka.tulosta_tiedot()
    print()
    hytti_no6.tulosta_tiedot()
