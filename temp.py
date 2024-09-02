import hashlib

def hash_file(file_path, algorithm='sha256'):
    """
    Hashes a file using the specified algorithm and returns the hexadecimal digest.
    
    Args:
        file_path (str): The path to the file to be hashed.
        algorithm (str): The hashing algorithm to use (default is 'sha256').
    
    Returns:
        str: The hexadecimal hash of the file.
    """
    # Create a new hash object
    hash_obj = hashlib.new(algorithm)
    
    try:
        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            # Read the file in chunks to avoid memory issues with large files
            while chunk := file.read(8192):
                hash_obj.update(chunk)
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"Error: {e}"
    
    # Return the hexadecimal digest of the hash
    return hash_obj.hexdigest()

# Prompt the user for the file path
file_path = 'build.sh'

# Compute the hash of the file
file_hash = hash_file(file_path)

print(f"Hash of the file: {file_hash}")
