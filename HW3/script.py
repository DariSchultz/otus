import csv
import json

with open('books.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    books = [row for row in reader]

with open('users.json', encoding='utf-8') as jsonfile:
    users = json.load(jsonfile)

num_users = len(users)
num_books = len(books)

books_per_user = num_books // num_users
remaining_books = num_books % num_users

result = []

books_to_distribute = list(range(num_books))

for i, user in enumerate(users):
    user_books = books_to_distribute[i * books_per_user:(i + 1) * books_per_user]

    if remaining_books > 0:
        user_books.append(books_to_distribute[num_users * books_per_user + remaining_books - 1])
        remaining_books -= 1

    new_user_dict = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": int(user["age"]),
        "books": [dict(title=b["Title"], author=b["Author"], pages=int(b["Pages"]), genre=b["Genre"]) for b in books if books.index(b) in user_books]
    }

    result.append(new_user_dict)

with open('result.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(result, jsonfile, indent=4)