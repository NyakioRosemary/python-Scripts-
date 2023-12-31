"""Write a function called generate_password that selects three
random words from the list of words word_list and concatenates them
into a single string. Your function should not accept any arguments and
should reference the global variable word_list to build the password. To help with this,
check out the choice function associated with the random module in the Standard Library."""
# TODO: First import the `random` module
import random
# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# TODO: Add your function generate_password below
def generate_password():
    return ""
# It should return a string consisting of three random words
# concatenated together without spaces

# Now we test the function
password = generate_password()
def generate_password():
    return ''.join(random.sample(word_list, 3))

"""Create a function that opens the flowers.txt, reads every line in it, and
 saves it as a dictionary. The main (separate) function should take
  user input (user's first name and last name) and parse the user input 
  to identify the first letter of the first name. It should then use it to print 
  the flower name with the same first letter (from dictionary created in the first function).

Sample Output: >>> Enter your First [space] Last name only: Bill Newman >>> Unique
 flower name with the first letter: Bellflower"""

## function that creates a flower_dictionary from filename
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower()
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

## Main function that prompts for user input, parses out the first letter
## includes function call for create_flowerdict to create dictionary
def main():
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
## print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()