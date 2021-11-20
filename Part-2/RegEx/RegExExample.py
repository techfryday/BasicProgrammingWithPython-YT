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
txt=input("Enter your email: ")
print("Is is an email? ")
# isEmail = re.search("^[a-z0-9.]*@[a-z0-9]*\.com", txt)
# isEmail = re.search("^[a-z0-9.]+@[a-z0-9]+\.com", txt)
# print(re.match("^[a-z0-9.]+@[a-z0-9]+(.com|.in)$", txt)) 
isEmail = re.search("^[a-z0-9.]{6,25}@[a-z0-9]+[a-z.]+", txt)
if isEmail:
    print("Yes it is!")
else:
    print("No its not!")
# https://docs.python.org/3/howto/regex.html#regex-howto
