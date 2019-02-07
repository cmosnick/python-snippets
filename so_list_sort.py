import re


def convert(text): int(text) if text.isdigit() else text
def alphanum_key(key): [convert(c) for c in re.split('([0-9]+)', key)]


books = [
    ['Max', 'Harry Potter 3', '908374'],
    ['Max', 'Harry Potter', '98347'],
    ['Max', 'Harry Potter 2', '93874'],
    ['Stan', 'Volume 55', '4354'],
    ['Stan', 'Volume 7', '3527'],
    ['brad', 'bible', '7386'],
    ['brad', 'bible 2', '564651'],
    ['frank', 'sailing 101', '1234'],
    ['frank', 'Sailing 101', '2341'],
    ['frank', 'sailing 101', '3412']
]

basic = sorted(books)
# print basicpages

sorted_case = sorted(books, key=lambda l: [i.lower() for i in l])
print sorted_case

# Sort titles only as test for chaining
# titles = [l[1] for l in books]

# titles_sorted = sorted(titles)
# print titles_sorted

# titles_sorted_case = sorted(titles, key=lambda title: title.lower())
# print titles_sorted_case

# titles_sorted_numeric = sorted(titles, key=alphanum_key)
# print titles_sorted_numeric  # Deosn't work

