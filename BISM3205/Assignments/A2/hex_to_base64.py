import base64

def hex_to_base64(hex_string):
    # Convert the hexadecimal string to bytes
    bytes_data = bytes.fromhex(hex_string)
    # Encode the bytes in Base64
    base64_data = base64.b64encode(bytes_data)
    # Convert the Base64 bytes to a string and return
    return base64_data.decode('utf-8')

# Example usage
hex_string = "F5CA4F935D44B85C431A8BF788C0EACA"
base64_result = hex_to_base64(hex_string)
print("Base64 encoded result:", base64_result)
