def xor_binary_strings(bin_str1, bin_str2):
    # Ensure both binary strings are of equal length by padding with zeros if necessary
    max_len = max(len(bin_str1), len(bin_str2))
    bin_str1 = bin_str1.zfill(max_len)
    bin_str2 = bin_str2.zfill(max_len)
    
    # XOR each bit and join the result into a new binary string
    result = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(bin_str1, bin_str2))
     # Convert the binary result to decimal
    decimal_result = int(result, 2)
    return result, decimal_result

# Example usage
bin_str1 = '10111010010010110'
bin_str2 = '10111010010100000'
xor_result, decimal_result = xor_binary_strings(bin_str1, bin_str2)
print("XOR result in binary:", xor_result)
print("XOR result in decimal:", decimal_result)