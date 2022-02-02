def vimBrain(code):
    array, starts, ends, i, pointer = [0], [], [], 0, 0
    print(code)
    while i < len(code):
        match code[i]:
            case 'h': pointer -= 1 if pointer > 0 else 0
            case 'l': pointer += 1; array.append(0) if len(array) <= pointer else 0
            case 'k': array[pointer] += 1
            case 'j': array[pointer] -= 1 if array[pointer] > 0 else 0
            case 'p': print(chr(array[pointer]), end='')
            case 'i':
                x = input()
                try:
                    y = int(x)
                except ValueError:
                    y = ord(x)
                array[pointer] = y
            case 'q': starts.append(i) if array[pointer] != 0 else 0
            case '@':
                ends.append(i); i = starts[-1]
                if array[pointer] == 0: starts.pop(-1); i = ends[-1]
        i += 1


vimBrain("""
lkkkkkkkkqhkkkkkkkkklj@hplkkkkqhkkkkkkklj@hkpkkkkkkkppkkkpllkkkkkkqhkkkkkkklj@hkkpjjjjjjjjjjjjplkkkkkkqhkkkkkkkkklj@hkphpkkkpjjjjjjpjjjjjjjjplllkkkkqhkkkkkkkklj@hkp
""")
