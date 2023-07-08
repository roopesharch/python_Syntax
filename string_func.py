print("Python string functions \n----------------------------\n")

st="string"

# can iterate string.like list , single line for loop with reversed
# for i in reversed(st): print(i) 

# print string riverse
print(st[::-1])

# print string  with index
print(st[2:4])

# convert string to list and voice versa
lst=list(st)
print(lst)
st="".join(lst)
print(st)

# replace a character in string
st1=st.replace('r','#')
print(st1)

# delete string 
# del st1

# Formatting of Strings
 
# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)
 
# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)
 
# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)



