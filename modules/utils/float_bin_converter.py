#----------------------------------------------------------recebe numero e retorna string binaria
def float_bin_converter(float_num: float) -> str:
    part_int = int(float_num)
    part_frac = str(float_num - part_int)[2:]
    if part_frac == '0':
        string_bin = bin(part_int)[2:] 
    else:
        string_bin = bin(part_int)[2:] + "#" + bin(part_frac)[2:]

    return string_bin

#----------------------------------------------------------recebe string binaria e retorna numero
def bin_float_converter(string_bin: str) -> float:
    if "#" in string_bin:
        part_int, part_frac = string_bin.split("#")
        int_num = int(part_int, 2)
        frac_num = int(part_frac, 2) / (2 ** len(part_frac))
        float_num = int_num + frac_num
    else:
        float_num = int(string_bin, 2)

    return float_num