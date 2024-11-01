import hashlib

def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


md5_result = calculate_md5('plane.jpg')
print(f"MD5 hash of the image plane: {md5_result}")
md5_result = calculate_md5('ship.jpg')
print(f"MD5 hash of the image ship: {md5_result}")
md5_result = calculate_md5('number.gif')
print(f"MD5 hash of the number gif: {md5_result}")