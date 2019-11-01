""" Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number
1111 0000 1111 0000 1111 0000 1111 0000,
return 0000 1111 0000 1111 0000 1111 0000 1111."""

def reverse_bits(binary: str):
    decimal = int(binary,2)
    one_inverted = (decimal ^ 0x00000000)
    return ~one_inverted& 0xFFFFFFFF


if __name__ == '__main__':
    binary = '11110000111100001111000011110000'
    print(reverse_bits(binary))