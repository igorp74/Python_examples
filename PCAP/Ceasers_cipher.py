# PCAP preparation
# ===================
# 📆 2022-07-05 11:13:15

# Caesar cipher enhanced...

text  = 'The die is cast' #input("Enter your message: ")
shift = '25' #input("Enter the shift: ")
cipher = ''

# For sucessfull rotating under the limited pool of characters
# let's define two pools for upper and lower case letters exclusively
char_upper = [u for u in range(65,91)]
char_lower = [l for l in range(97,123)]

# Create a function for rotating a list
def rotate_list(l,n):
    return [l[(i + n) % len(l)] for i, x in enumerate(l)]

for char in text:
    if not char.isalnum():
        cipher += str(char)

    if char.isnumeric():
        cipher += str(char)

    if char.isalpha():
        if char.isupper():
            char_index = char_upper.index(ord(char))
            upper_index = rotate_list(char_upper, int(shift))[char_index]
            cipher += chr(upper_index)
        else:
            char_index = char_lower.index(ord(char))
            lower_index = rotate_list(char_lower, int(shift))[char_index]
            cipher += chr(lower_index)

print(cipher)