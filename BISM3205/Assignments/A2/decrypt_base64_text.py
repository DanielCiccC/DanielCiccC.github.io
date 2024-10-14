from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

# Load your public key (replace YOUR_PUBLIC_KEY_HERE)
public_key_pem = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAucU+u7phfIspqebNE+LR0pZYb0Waa
NaX5WNTamO41MdSExiSuG7vTVIb+P4Vw0+BE+ElYFE7oYxyr+BPmsnNA986D3+RwrrELkfohL
UDkhETGzE7hwl4FHTgQ0o3RLDFsjjAqiqoQVQpItWAo4JYWi09C0MvfaclZLll3wL20FnZc867Tnd
Mhr11qw68HB9daW0BLkZk/loJy0FFjl1nU/ujBhVPkOvCCrZOLT0ZUXZnIST4kV5bVJ5kniIEOAmZ
VMo893gDAXTkrCJrPwYGheTSNwzbyXtbuSvPV/C+YBhBTV2sdTA0WTYckFE6FYxLzjt9OMehIy
MeXWFmT/TLKQIDAQAB 
-----END PUBLIC KEY-----"""

# Load the public key
public_key = serialization.load_pem_public_key(
    public_key_pem,
    backend=default_backend()
)

# Base64 encoded message to decrypt
base64_encrypted_message = """
iE0E5eO/QYgiTuYiiHlTv60nxr1Q6gKV2LjVWca4Qbp4uw98qjpdxJV+trQO+ZRG2WZBGDQg/kR
MVShVy/AEaG4TGK9SZL1elbmLrVn0+AXCAwJaPovYhV7c62eg67XKO/Fk+ThQc/0PnulIJgu7AL
OXr3aULuvIVGUm5u030fi2vwrjaCFfQl4QtxlfhFSP1/p0ftDsJPuj3NNx7ylIuAkTmcSc8fZ3/12xyz1
a72y+ASG3OTLwNACci/mZcr2gq7p/LkNFeHAYmUMh+ty5cijH9m+hgNWfw3TL0p2GMhLjNsD
MdjTonqBKZhFLsnCRj2z+ggBF88ay4L/XVlMjzA==
"""

# Decode the base64 encrypted message
encrypted_message = base64.b64decode(base64_encrypted_message)

try:
    # Decrypt the message
    decrypted_message = public_key.decrypt(
        encrypted_message,
        padding.PKCS1v15()
    )
    print("Decrypted message:", decrypted_message.decode('utf-8'))
except Exception as e:
    print(f"Error during decryption: {e}")
