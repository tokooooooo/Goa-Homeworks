def even_index_numbers(lst):
    return lst[::2]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(even_index_numbers(numbers))
#2
games = ["Chess", "Poker", "Tetris", "Minecraft"]
programming_languages = ["Python", "Java", "C++", "JavaScript"]
games = programming_languages
print(games)
#3
def greet_user(name):
    print("Hello, {name}!")

greet_user("John")
