a_string = "Hello world!"
a_string2 = "Hello World!"

a_string="Hello world!"
print("single quotes are ''")
print(len(a_string))

a_string="Hello world!"
print(a_string.index("o"))

a_string = "Hello world!"
print(a_string.count("l"))

a_string = "Hello world!"
print(a_string[3:7])

a_string = "Hello world!"
print(a_string[3:7:2])

a_string = "Hello world!"
print(a_string[3:7])
print(a_string[3:7:1])

a_string = "Hello world!"
print(a_string[::-1])

a_string = "Hello world!"
print(a_string.upper())
print(a_string.lower())

a_string = "Hello world!"
print(a_string.startswith("Hello"))
print(a_string.endswith("asdfasdfasdf"))

a_string = "Hello world!"
afewwords = a_string.split(" ")

#Exercise

s = "Hey, so afterwards.."
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Hey"):
    print("String starts with 'Hey'. Good!")

# Check how a string ends
if s.endswith("wards.."):
    print("String ends with 'wards..'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))