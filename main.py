def bits_to_text(bitstream):
    # Ellenőrizni, hogy a bitfolyam 8-mal osztható legyen
    if len(bitstream) % 8 != 0:
        raise ValueError("A bitfolyam hossza nem osztható 8-cal!")

    chars = []
    for i in range(0, len(bitstream), 8):
        byte = bitstream[i:i+8]          # 8 bites csoport
        decimal = int(byte, 2)           # binárisból decimálissá
        chars.append(chr(decimal))        # decimálisból karakter
    return ''.join(chars)


def XOR(part1, part2):
    partOne = ''
    for _ in range(len(part1)):
        if int(part1[_]) == int(part2[_]):
            partOne += '1'
        else:
            partOne += '0'
    return partOne

def run():
    with open("original", 'rb') as rb:
        data = rb.read()
    
    bit = ''.join(f'{b:08b}' for b in data)

    # Output: '00000001111111111000000000000111'
    
    bit_length = len(bit)
    bit_ = len(bit) // 3

    part1 = bit[:bit_]
    part2 = bit[bit_:bit_*2]
    part3 = bit[bit_*2:]

    print("part1", bits_to_text(part1))
    print("part2", bits_to_text(part2))
    print("part3", bits_to_text(part3))
    
    partOne = XOR(part1, part2)
    print('partOne', bits_to_text(partOne))

    perty = XOR(partOne, part3)
    print("perty", bits_to_text(perty))

    b = int(perty, 2).to_bytes(len(perty) // 8, byteorder="big")

    with open("part1.bin", "wb") as wb:
        wb.write(b)





    


run()
