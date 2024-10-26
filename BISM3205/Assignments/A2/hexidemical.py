# Given hex pairs
# hex_pairs = [
#     "F5", "CA", "4F", "93", "5D", "44", "B8", "5C",
#     "43", "1A", "8B", "F7", "88", "C0", "EA", "CA"
# ]

hex_pairs = ['0a', '35', 'b0', '6c', 'a2', 'bb', '47', 'a3', 'bc', 'e5', '74', '08', '77', '3f', '15', '35']

# Convert the hexadecimal pairs to ASCII characters
ascii_string = ''.join(chr(int(pair, 16)) for pair in hex_pairs)

print(ascii_string)
