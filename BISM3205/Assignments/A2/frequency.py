from collections import Counter

sentence = "Tsi qsmseuci zbv tq fzyke il fhp jlmtgiiyk zpwjpiyeqfa"
normalized_sentence = ''.join(filter(str.isalpha, sentence.lower()))

letter_frequency = Counter(normalized_sentence)

for letter, frequency in letter_frequency.most_common():
    print(f"{letter}: {frequency}")

# from collections import Counter
# from itertools import permutations

# # Given sentence
# sentence = "Tsi qsmseuci zbv tq fzyke il fhp jlmtgiiyk zpwjpiyeqfa"

# # Normalize the sentence by converting to lowercase and removing non-letter characters
# normalized_sentence = ''.join(filter(str.isalpha, sentence.lower()))

# # Count the frequency of each letter
# letter_frequency = Counter(normalized_sentence)

# # Sort the letters by frequency (descending) and handle ties
# sorted_letters = sorted(letter_frequency.items(), key=lambda item: item[1], reverse=True)

# # List of most frequent letters in English
# most_frequent_english = "etaoinshrdlcumfywgbpkvxjqz"

# # Create frequency mapping
# frequency_mapping = {}
# for i, (letter, freq) in enumerate(sorted_letters):
#     if i < len(most_frequent_english):
#         frequency_mapping[letter] = most_frequent_english[i]

# # Handle tie-breakers
# # Collect letters with the same frequency
# frequency_groups = {}
# for letter, freq in sorted_letters:
#     if freq not in frequency_groups:
#         frequency_groups[freq] = []
#     frequency_groups[freq].append(letter)

# # Create a list of substitutions with permutations for tie-breakers
# substitution_permutations = []
# for group in frequency_groups.values():
#     if len(group) > 1:
#         # Generate permutations if there are ties
#         perms = [''.join(p) for p in permutations(group)]
#         substitution_permutations.append(perms)
#     else:
#         substitution_permutations.append([group[0]])

# # Create the list of final substitutions
# final_substitutions = [''.join(perm) for perm in permutations(most_frequent_english[:len(sorted_letters)])]

# # Create the substitution cipher
# substitution_cipher = {}
# for letters in substitution_permutations:
#     for letter in letters:
#         if letters.index(letter) < len(most_frequent_english):
#             substitution_cipher[letter] = most_frequent_english[letters.index(letter)]

# # Substitute the letters in the original sentence
# ciphered_sentence = ''.join(substitution_cipher.get(char.lower(), char) for char in sentence)

# # Output the results
# print("Frequency Mapping:")
# for original, substituted in substitution_cipher.items():
#     print(f"{original} -> {substituted}")

# print("\nCiphered Sentence:")
# print(ciphered_sentence)

# print("\nAll Substitution Permutations for Tie-breakers:")
# for group in substitution_permutations:
#     if len(group) > 1:
#         print(f"Group: {group}")
#         for perm in permutations(group):
#             print(''.join(perm))