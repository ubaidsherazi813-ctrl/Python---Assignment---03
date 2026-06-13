# Create a class book with Attributes & Methods

class Book:

    def __init__(self , title , author):
        self.title = title
        self.author = author
        self.list_of_review = []

    def add_review(self , new_review):
        self.list_of_review.append(new_review)

    def count_review(self):
        return len(self.list_of_review)

    def deiplay(self):
        print(f"title: {self.title}")
        print(f"Author: {self.author}")
        print("Reveiws:")

        for review in self.list_of_review:
            print(f"- {review}")

        

b1 = Book("Harry Potter" , "Jk Rowling")

b1.add_review("Excellent Story")
b1.add_review("Amazing plot Twist")
b1.add_review("Must read for everyone")

b1.deiplay()
print(f"Number of Reviews: {b1.count_review()}")
