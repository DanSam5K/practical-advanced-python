import re

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base) + convert_string[n % base]
    
print(to_str(10, 2))

# Recursively reverse str
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[:1]
    
def clean_str(s):
    return re.sub('[^A-Za-z0-9]+', '', s)

def is_pal(s):
    return clean_str(s) == reverse(clean_str(s))

print(reverse("hello"), "olleh")
print(clean_str("Dani. el"), "Daniel")


print(is_pal("Wassamassaw – a town in South Dakota"))
print(is_pal("kayak"))