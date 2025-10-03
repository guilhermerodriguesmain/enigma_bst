# Binary Converter Module

class BinaryConverter:
    def __init__(self):
        pass
    
    # Inteiros
    def encrypt(self, numbers):
        return [format(int(num), '08b') for num in numbers]
    
    def decrypt(self, binaries):
        return [int(b, 2) for b in binaries]
    
    # Floats
    def float_bin_converter(self, numbers, precision=10):
        binaries = []
        for float_num in numbers:
            int_part = int(float_num)
            frac_part = float_num - int_part
            
            # Parte inteira
            bin_int = bin(int_part)[2:]
            
            # Parte fracionária
            bin_frac = []
            frac = frac_part
            for _ in range(precision):   # limite de precisão binária
                frac *= 2
                bit = int(frac)
                bin_frac.append(str(bit))
                frac -= bit
                if frac == 0:
                    break
            
            if bin_frac:
                binaries.append(bin_int + "#" + "".join(bin_frac))
            else:
                binaries.append(bin_int)
        
        return binaries

    def bin_float_converter(self, binaries):
        floats = []
        for string_bin in binaries:
            if "#" in string_bin:
                part_int, part_frac = string_bin.split("#")
                int_num = int(part_int, 2)
                frac_num = sum(int(bit) * (2 ** -(i+1)) for i, bit in enumerate(part_frac))
                floats.append(int_num + frac_num)
            else:
                floats.append(int(string_bin, 2))
        return floats


# exemplo de uso
if __name__ == "__main__":
    converter = BinaryConverter()
    
    original_numbers = [32.5, 132.0, 301.5]
    print(f"Original Numbers: {original_numbers}")
    
    encrypted_binaries = converter.float_bin_converter(original_numbers)
    print(f"Encrypted Binaries: {encrypted_binaries}")
    
    decrypted_numbers = converter.bin_float_converter(encrypted_binaries)
    print(f"Decrypted Numbers: {decrypted_numbers}")
