# Example file for Programming Foundations: Algorithms by Joe Marini
# use a set to count unique items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a set to perform a filter
unique_items = set()

# TODO: loop over each item and add to the set
# for item in items:
#   unique_items.add(item)
# print(unique_items)

# TODO: Count the unique letters in a sentence
sentence = "The quick brown fox jumps over the lazy dog."
counter = 0
unique_items = {c for c in sentence.lower() if c.isalnum()}
for item in unique_items:
  counter += 1
print(unique_items)
print(f'{counter} unique items.')