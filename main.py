test_lvl = 1

def test_print(text, lvl=1):
    if __name__ == "__main__":
        if lvl == 1 or test_lvl == 0:
            print(text)

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





def eruse_run(data):
    test_print("erasure work...", 0)

    test_print("convert to byte", 0)
    byte_data = convert_to_bytes(data)

    test_print("erasure starting", 0)
    erasure_data = make_erasure(byte_data)

    test_print("give a parity for erasure", 0)
    erasure_with_parity_data = make_parity(erasure_data)

    test_print("[DONE] return to back", 0)
    return erasure_with_parity_data
  


# -------------------------------------------------

def check(data):
    error = 0
    for i in data:
        if i is None:
            error += 1

    if error >= 2:
        return 2
    
    return error


def generate_back(data):
    generate = data.pop(3)
    for i in data:
        if i is not None:
            generate = XOR(i, generate)

    return generate

def generate_data_put(data, generate):
    for i in range(len(data)):
        if data[i] is None:
            data[i] = generate
            return data

def put(data):
    for i in range(3):
        if data[i][-1] == 0:
            test_print(data[i][-1], 0)
            it = data[i].pop(-1)
            test_print(it, 0)

    test_print(data, 0)
    return data[0] + data[1] + data[2]

def eruse_back_run(data):
    test_print("eruse back work...", 0)
    error = check(data)
    if error == 2:
        return None

    if data[3] != None and error == 1:
        generate_data = generate_back(data)
        data = generate_data_put(data, generate_data)

    
    share = put(data)

    return decode_from_bytes(share)
        

        

        


if __name__ == "__main__":
    original = "Hello, World!"

    response = eruse_run(original)
    test_print(decode_from_bytes(response[3]), 0)
    
    test_print(response, 0)

# ------------------------------------------------------------
    
    need = 4
    for_test = response.copy()
    for i in range(need):
        for_test[i] = None
        na = eruse_back_run(for_test)
        if na == original:
            print(f"[Nice] 4/{i+1}")
        else:
            print(f"[ERROR] 4/{i+1}", na, "<-->", original)

        for_test = response.copy()


