import re

"""
. => Any characters except the newline character
^ => Starts with
$ => Ends with
* => Zero or more occurrences
+ => One or more occurrences
? => Zero or one occurrences
{ } => Exactly the specified number of occurrences
[ ] => A set of characters
\ => Escape Sequence
| => Either or
( ) => group

"""


# match() - Determine if the RE matches at the beginning of the string
line="1,sagar mahajan,sagar@gmail.com,1231231232"
print(re.match("[0-9]+", line).group())

# search() - Scan through a string, looking for any location where this RE matches
print(re.search("[0-9]{10}", line).group())

# findall() - Find al substrings where RE matches and returns them as a list
print(re.findall("[0-9]+", line))

# finditer() - Find al substrings where RE matches and returns them as an iterator
for i in re.finditer("[0-9]+", line):
    print(i.group())


# Real-time Example

txt=input("Enter your email: ")
print("Is is an email? ")

isEmail = re.search("^[a-z0-9.]+@[a-z0-9]+(.com|.in)$", txt)

isEmail = re.search("^[a-z0-9.]{6,25}@[a-z0-9]+[a-z.]+", txt)
if isEmail:
    print("Yes it is!")
else:
    print("No its not!")
    
    
# https://docs.python.org/3/howto/regex.html#regex-howto
