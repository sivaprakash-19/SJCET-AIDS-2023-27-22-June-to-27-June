
s = "1233"
num = 0
for i in s :
    num = (num * 10) + int(i)
    print(num)
print(num)


# s = 'hello_good_morning_how_are_you?'

words = s.split("_") # Returns a list of words, where splitted by separator. T.C -> O(n)

# print(words, type(words))


# s1 = s.strip() # Returns a string after removing trailing spaces on right side. 

# s1 = s.rstrip() # Returns a string after removing trailing spaces on right side. 

# s1 = s.lstrip() # Returns a string after removing trailing spaces on left side. 

# print(s1, len(s1))

# print(s.lower()) # Returns a string, after converting all characters into lowercase. T.C -> O(n)

# print(s.upper()) # Returns a string, after converting all characters into uppercase. T.C -> O(n)

# print(s.isalnum()) # Returns True, if string is of alphabets and numbers, false otherwise. T.C -> O(n)

# print(s.isalpha()) # Returns True, if string is of alphabets, false otherwise. T.C -> O(n)

# print(s.capitalize()) # Returns a string, where first word's first character is capatilized. 

# print(s.index('o')) # Returns the index of first occurrence of the string, if substring is not found -> Throws ValueError. T.C -> O(n)

# print(s.count("llo")) # Return the number of occurrences of string - int. T.C -> O(n)

# print(s[ :: -1]) # Return a string in reversed

# print(s[ 2 : ]) # Return a substring from si  to end. si -> inclusive

# print(s[ : 4]) # Return a substring from 0 to ei.  ei -> exclusive

# print(s[0 : 5]) # Return a substring from si to ei. si -> inclusive, ei -> exclusive

# print(s[1]) # Returns the char(string) at index, if index is not valid -> Throws IndexError. 

# print(len(s)) # Return the length of string

print(s, len(s))