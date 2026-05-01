# Dictionary practice solutions for 10 exercises

def main():
    # 1. Create a Dictionary
    print("1. Create a Dictionary")
    student_grades = {
        "Alice": "A",
        "Bob": "B",
        "Charlie": "C",
        "David": "A",
        "Eve": "B",
    }
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

    # 2. Accessing Values
    print("\n2. Accessing Values")
    student = {"name": "Alice", "age": 16, "grade": "A"}
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")

    # 3. Updating Values
    print("\n3. Updating Values")
    student["grade"] = "A+"
    print(student)

    # 4. Adding New Key-Value Pairs
    print("\n4. Adding New Key-Value Pairs")
    favorite_movies = {
        "The Matrix": 1999,
        "Toy Story": 1995,
        "Inception": 2010,
    }
    new_movie = input("Enter a new movie title: ").strip()
    new_year = input("Enter the release year for that movie: ").strip()
    if new_movie:
        if new_year.isdigit():
            favorite_movies[new_movie] = int(new_year)
        else:
            favorite_movies[new_movie] = new_year
    print("Updated movie dictionary:")
    print(favorite_movies)

    # 5. Removing Key-Value Pairs
    print("\n5. Removing Key-Value Pairs")
    fruit_prices = {
        "apple": 1.20,
        "banana": 0.50,
        "orange": 0.80,
        "grape": 2.50,
        "pear": 1.00,
    }
    remove_fruit = input("Enter the name of a fruit to remove: ").strip().lower()
    if remove_fruit in fruit_prices:
        del fruit_prices[remove_fruit]
        print(f"Removed {remove_fruit}.")
    else:
        print(f"{remove_fruit} was not found in the dictionary.")
    print("Updated fruit prices:")
    print(fruit_prices)

    # 6. Looping Through a Dictionary
    print("\n6. Looping Through a Dictionary")
    inventory = {"apples": 10, "bananas": 5, "oranges": 8}
    for fruit, quantity in inventory.items():
        print(f"We have {quantity} {fruit}.")

    # 7. Counting Occurrences
    print("\n7. Counting Occurrences")
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    print(word_counts)

    # 8. Nested Dictionaries
    print("\n8. Nested Dictionaries")
    books = {
        "book1": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
        "book2": {"title": "1984", "author": "George Orwell", "year": 1949},
        "book3": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    }
    for key, info in books.items():
        print(f"{info['title']} by {info['author']} ({info['year']})")

    # 9. Dictionary Comprehension
    print("\n9. Dictionary Comprehension")
    squares = {i: i * i for i in range(1, 11)}
    print(squares)

    # 10. Finding Maximum Value
    print("\n10. Finding Maximum Value")
    salaries = {
        "Alice": 55000,
        "Bob": 62000,
        "Charlie": 59000,
        "Dana": 68000,
        "Eve": 61000,
    }
    highest_paid = max(salaries, key=salaries.get)
    print(f"{highest_paid} has the highest salary: {salaries[highest_paid]}")


if __name__ == "__main__":
    main()
