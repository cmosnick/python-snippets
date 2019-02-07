import re
from operator import itemgetter


def list_explode(l):
    return [item.split("-") for item in l]


def print_list(l):
    for item in l:
        print item


def remove_chars(s):
    return re.sub('[^A-Za-z0-9]+', ' ', s)


def sorted_nicely(l):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)[]

# fnames_list = [
#     "Max-Across From House 3-1-908374",
#     "Max-Across From House-1-98347",
#     "Max-Across From House 2-1-93874",
#     "Stan-Voorhis 55-1-4354",
#     "Stan-Voorhis 7-1-3527",
#     "brad-field-1-7386",
#     "brad-field 2-1-564651",
#     "farm-fieldname-1-1234",
#     "farm-Fieldname-1-2341",
#     "farm-fieldname-1-3412"
# ]


fnames_list = [
    "Max-Harry Potter 3-908374",
    "Max-Harry Potter-98347",
    "Max-Harry Potter 2-93874",
    "Stan-Volume 55-4354",
    "Stan-Volume 7-3527",
    "brad-bible-7386",
    "brad-bible 2-564651",
    "frank-sailing 101-1234",
    "frank-Sailing 101-2341",
    "frank-sailing 101-3412"
]



# basic = sorted(fnames_list)
# print "_______________________\nBasic: \n"
# print_list(basic)

# lower = sorted(fnames_list, key=lambda s: s.lower())
# print "___________________________\nIgnore Case: \n"
# print_list(lower)

# specialchars_removed = sorted(fnames_list, key=lambda x: re.sub('[^A-Za-z]+', '', x).lower())
# print "_________________________\nIgnore Case and Special Characters:\n"
# print_list(specialchars_removed)


# spaces_only = map(remove_chars, fnames_list)
# print "___________________________\nSpaces Replaced:\n"
# print_list(spaces_only)

# spaces_only_sorted = sorted(spaces_only, key=lambda s: s.lower())
# print "______________________\nSpaces only sorted ignore case:\n"
# print_list(spaces_only_sorted)

# Explode strings into multiple


# Sort by numbers as well
# s = ["18 hello-1", "hello 1-1", "hello 2-1", "hello-1-1", "1 hello-1", "2hello-1", "hello 55-1", "hello 7-1"]
# s_sorted = sorted_nicely(s)
# print "___________________\nSort numbers experiment:\n"
# print_list(s_sorted)


# print "_________________\nExplode strings in list: \n"
# for l in list_explode(fnames_list):
#     print_list(l)

fnames_list_expl = list_explode(fnames_list)
# print fnames_list_expl

# convert to tuples
fnames_tuples = [tuple(l) for l in fnames_list_expl]
# for t in fnames_tuples:
# 	print t

# basic = sorted(fnames_list_expl, key=lambda l:  (l[0].lower(), l[1].lower(), l[2].lower(), l[3].lower()))
# basic = sorted(fnames_list_expl, key=lambda l:  (l[i].lower() for i in l))
basic = sorted(fnames_list_expl, key= itemgetter(0, 1, 2, 3))
# print "____________________________\nSorted exploded:\n"
# for l in basic:
#     print l



basic_sorted_tuples = sorted(fnames_tuples)
# for t in basic_sorted_tuples:
#     print t

sorted_tuples = sorted(fnames_tuples, key=lambda t: (t[0].lower(), t[1].lower()))
# for t in sorted_tuples:
# 	print t

pythonic_sorted_tuples = sorted(fnames_tuples, key=lambda t: (t[i].lower() for i in t))
# for t in pythonic_sorted_tuples:
# 	print t



