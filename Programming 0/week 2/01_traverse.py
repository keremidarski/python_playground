# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week2/2-List-Problems

books = ["Learn You a Haskell", 
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"]

for i in books:
    print(i)

counter = 0

while counter < len(books):
    print(books[counter])
    counter += 1
