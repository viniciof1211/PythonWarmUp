# palindrome.py implementation
# function arg "line" is dynamically-types assumed to be string

def palindrome(line):
    s = str(line) # Enforce "static" typed to avoid issues down the road
    return s == s[::-1]