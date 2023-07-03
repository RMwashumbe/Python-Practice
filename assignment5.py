# write a function to create a palindrome
# create a function that gives you the longest string in a list of items
def create_palindrome(word):
    palindrome = word + word[::-1]
    return palindrome


word = input("Enter a word: ")
palindrome = create_palindrome(word)
print(f"The palindrome is: {palindrome}")


def find_longest_string(items):
    longest_string = ""
    for item in items:
        if isinstance(item, str) and len(item) > len(longest_string):
            longest_string = item
            return longest_string


my_list = ["apple", "banana", "kiwi", "orange", "pear"]
longest_string = find_longest_string(my_list)
print(f"The longest string in the list is: {longest_string}")
