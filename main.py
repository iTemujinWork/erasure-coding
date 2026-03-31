def convert_to_bytes(data):
    return [ord(c) for c in data]


def decode_from_bytes(byte_data): 
    text = "".join(chr(c) for c in byte_data)
    return text


def make_erasure(byte_data):
    size = len(byte_data)
    by_how_much = size // 3

    part1 = byte_data[:by_how_much] 
    part2 = byte_data[by_how_much:by_how_much*2]
    part3 = byte_data[by_how_much*2:]

    return [part1, part2, part3]


def XOR(data1, data2):
    response = []
    for i in range(len(data1)):
        response.append(data1[i] ^ data2[i])

    return response

def complement(erause_data):
    how_mach_take = len(erause_data[2]) - len(erause_data[1])

    for i in range(how_mach_take):
        erause_data[0].append(0)
        erause_data[1].append(0)

    return erause_data

def make_parity(erause_data):
    
    erause_plus_data = complement(erause_data)
    

    ep1 = XOR(erause_plus_data[0], erause_plus_data[1])
    ep2 = XOR(ep1, erause_plus_data[2])

    erause_data.append(ep2)

    return  erause_data





def run(data):    
    byte_data = convert_to_bytes(data)

    erasure_data = make_erasure(byte_data)

    erasure_with_parity_data = make_parity(erasure_data)

    return erasure_with_parity_data
  

if __name__ == "__main__":
    print(run("Hello, world!"))


