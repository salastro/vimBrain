def vimBrain(code):
    array = [0]
    pointer = 0
    i = 0
    print(code)
    while i < len(code):
        match code[i]:
            case 'h': pointer -= 1 if pointer > 0 else 0
            case 'l': pointer += 1; array.append(0) if len(array) <= pointer else 0
            case 'k': array[pointer] += 1
            case 'j': array[pointer] -= 1 if array[pointer] > 0 else 0
            case 'p': print(chr(array[pointer]), end='')
            case 'i':
                x = input("Input:")[0]
                try:
                    y = int(x)
                except ValueError:
                    y = ord(x)
                array[pointer] = y
            case 'q':
                if array[pointer] == 0:
                    loop = 1
                    while loop > 0:
                        i += 1
                        match code[i]:
                            case 'q': loop += 1
                            case '@': loop -= 1
            case '@':
                loop = 1
                while loop > 0:
                    i -= 1
                    match code[i]:
                        case 'q': loop -= 1
                        case '@': loop += 1
                i -= 1
        i += 1


vimBrain("""
lkkkkkkkkqhkkkkkkkkklj@hplkkkkqhkkkkkkklj@hkpkkkkkkkppkkkpllkkkkkkqhkkkkkkklj@hkkpjjjjjjjjjjjjplkkkkkkqhkkkkkkkkklj@hkphpkkkpjjjjjjpjjjjjjjjplllkkkkqhkkkkkkkklj@hkp
""")
