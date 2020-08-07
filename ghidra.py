# TODO: clean this up some more post DEFCON

def get_ascii(hex_value):
    return (bytes.fromhex(hex(hex_value)[2:])).decode("ASCII")


def string_obfuscation(param_1):
    return param_1 ^ 0x123456789abcdef


def stronger_obfuscation(param_1):
    uVar1 = (param_1 ^ 0xafafafafafafafaf) + 0xf
    return uVar1 >> 0x38 | (uVar1 & 0xff000000000000) >> 0x28 | (uVar1 & 0xff0000000000) >> 0x18 | \
           (uVar1 & 0xff00000000) >> 8 | (uVar1 & 0xff000000) << 8 | (uVar1 & 0xff0000) << 0x18 | \
           (uVar1 & 0xff00) << 0x28 | uVar1 << 0x38


if __name__ == '__main__':
    print("String Obfuscation: " + get_ascii(string_obfuscation(0x1412c13efc7a49f)))
    print("stronger Obfuscation: " + get_ascii(stronger_obfuscation(0xd9dddaccdccdc0af)))
