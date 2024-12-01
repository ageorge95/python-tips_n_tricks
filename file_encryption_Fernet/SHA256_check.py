import hashlib
import os

def generate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    # Open the file in binary mode and read chunks to avoid memory overload for large files
    with open(file_path, "rb") as f:
        # Read the file in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    # Return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

def check_integrity(file_path, expected_hash):
    # Generate the SHA256 hash of the file
    current_hash = generate_sha256(file_path)

    # Compare the generated hash with the expected hash
    if current_hash == expected_hash:
        print("The file's integrity is intact.")
    else:
        print("The file has been modified or is corrupt.")

# Example usage
file_paths = ["my_file.txt",
              "my_file_encrypted.txt",
              "key"]  # Replace with your files path

for file_path in file_paths:
    if os.path.isfile(file_path):
        current_hash_value = generate_sha256(file_path)
        print(f"SHA256 Hash for {file_path}: {current_hash_value}")

        if not os.path.isfile(file_path+'.SHA256'):
            print(f'No prior SHA256 checks detected for {file_path}, no check will be done !!!')
            with open(file_path+'.SHA256', 'w') as out_file_handle:
                out_file_handle.write(current_hash_value)
        else:
            print(f'Prior SHA256 checks detected for {file_path}, checking integrity ...')
            with open(file_path+'.SHA256', 'r') as in_file_handle:
                prior_hash_value = in_file_handle.read()
            if prior_hash_value != current_hash_value:
                print('SHA256 MISMATCH !!!')
            else:
                print('SHA256 match')