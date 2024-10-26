def xor_with_key(hex_values, key):
    # Convert the hexadecimal values to integers
    byte_values = [int(hex_val, 16) for hex_val in hex_values]

    # XOR each byte with the key
    xor_result = [(byte ^ key) for byte in byte_values]

    # Convert back to hexadecimal or ASCII for readability
    xor_hex_result = [hex(x)[2:].zfill(2) for x in xor_result]  # Hexadecimal output
    xor_ascii_result = ''.join(chr(x) for x in xor_result if 32 <= x <= 126)  # ASCII printable characters

    return xor_hex_result, xor_ascii_result

# Define the hex values from the GIF and a sample key (0x20 for example)
hex_values = ["F5", "CA", "4F", "93", "5D", "44", "B8", "5C", "43", "1A", "8B", "F7", "88", "C0", "EA", "CA"]
key = 0x00  # Example XOR key, you can change this

# Run the XOR operation
hex_result, ascii_result = xor_with_key(hex_values, key)

# Display results
print("XOR Hex Result:", hex_result )
print("XOR ASCII Result:", ascii_result)
