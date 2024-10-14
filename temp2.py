import string

def base64_decode_to_base10(base64_str):
    # Base64 character set (standard base64 set)
    base64_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    base = len(base64_chars)  # Base-64

    # Initialize base 10 value
    base10_value = 0

    # Iterate through the base-64 string
    for char in base64_str:
        if char in base64_chars:
            # Find the value of the character in base-64
            value = base64_chars.index(char)
            # Update the base-10 value by multiplying the previous total by 64
            base10_value = base10_value * base + value
        else:
            raise ValueError(f"Character '{char}' is not a valid base-64 character.")

    return base10_value

# Example usage:
encoded_str = "s9r51566bo6705j7bb6iv54nb9oiy449g795582l6529s0q22207b8981233pg58"
try:
    decoded_value = base64_decode_to_base10(encoded_str)
    print(f"Base-10 decoded value: {decoded_value}")
except ValueError as e:
    print(e)
