# Binary Converter Module

class BinaryConverter:
    def __init__(self):
        pass
    
    def encrypt(self, numbers):
        return [format(num, '08b') for num in numbers]
    
    def decrypt(self, binaries):
        return [float(b, 2) for b in binaries]
    
# exemplo de uso

if __name__ == "__main__":
    converter = BinaryConverter()
    
    original_numbers = [32.5, 132.0, 301.5]
    print(f"Original Numbers: {original_numbers}")
    
    encrypted_binaries = converter.encrypt(original_numbers)
    print(f"Encrypted Binaries: {encrypted_binaries}")
    
    decrypted_numbers = converter.decrypt(encrypted_binaries)
    print(f"Decrypted Numbers: {decrypted_numbers}")