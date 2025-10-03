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
            #-----------------------------------verifica se não é um inteiro em formato float
            if frac_part == 0:
                binaries.append(bin(int_part)[2:])
            else:
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
                binaries.append(bin_int + "#" + "".join(bin_frac))
        
        return binaries

    def bin_float_converter(self, binaries):
        floats = []
        for string_bin in binaries:
            if "#" in string_bin:
                part_int, part_frac = string_bin.split("#")
                # refactor usando join
                int_num = int(part_int, 2)
                frac_num = sum(int(bit) * (2 ** -(i+1)) for i, bit in enumerate(part_frac))
                floats.append(int_num + frac_num)
            else:
                floats.append(int(string_bin, 2))
        return floats




