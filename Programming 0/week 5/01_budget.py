
# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week5/1-On-Budget

def on_budget(books, budget):
    books.sort()
    total_cost = sum(books)
    books_cost = 0
    books_count = 0

    for book in books:
        books_cost += book
        
        if books_cost < budget:
            books_count += 1
        else:
            books_cost -= book
            break

    loan = total_cost - books_cost - (budget - books_cost)

    if loan < 0:
        loan = 0

    result = {'books_on_budget': books_count, 'loan': loan}

    return result

books = [0, 10, 100, 5, 3, 8, 25]
budget = 35

print(on_budget(books, budget))
