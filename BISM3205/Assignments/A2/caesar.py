from collections import Counter

# Function to decrypt a Caesar cipher with a given shift
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():  # Decrypt only alphabetic characters
            shift_base = ord('a') if char.islower() else ord('A')
            decrypted_text.append(chr((ord(char) - shift_base - shift) % 26 + shift_base))
        else:
            decrypted_text.append(char)  # Non-alphabet characters remain unchanged
    return ''.join(decrypted_text)

# Function to estimate the Caesar cipher shift by assuming the most frequent letter is 'E'
def estimate_caesar_shift(ciphertext, letter):
    # Count the frequency of each letter in the ciphertext
    filtered_text = [char.lower() for char in ciphertext if char.isalpha()]
    letter_frequency = Counter(filtered_text)
    
    # Find the most frequent letter in the ciphertext
    most_common_letter = letter_frequency.most_common(1)[0][0]
    
    # Calculate the shift assuming the most common letter is 'E'
    estimated_shift = (ord(most_common_letter) - ord(letter)) % 26
    return estimated_shift

# Example usage
ciphertext = """Tsi qsmseuci zbv tq fzyke il fhp jlmtgiiyk zpwjpiyeqfa: 
s9r51566bo6705j7bb6iv54nb9oiy449g795582l6529s0q22207b8981233pg58 ; 
jpl(qauc_wqvlwzt_yyjcmj,10). """

for letter in 'abcdefghijklmnopqrstuvwxyz':
    estimated_shift = estimate_caesar_shift(ciphertext, letter)

    # Decrypt the message using the estimated shift
    decrypted_message = decrypt_caesar_cipher(ciphertext, estimated_shift)
    
    print(f"Mapping most frequent letter to '{letter}'")
    print(f"Estimated Shift: {estimated_shift}")
    print(f"Decrypted Message: {decrypted_message}")
    print('-' * 60)  # Separator for readability