def vimBrain(code):
    array, starts, loops, i, pointer = [0], [], {}, 0, 0
    for index, instruction in enumerate(code):
        match instruction:
            case "q": starts.append(index)
            case "@": start = starts.pop(); loops[start] = index; loops[index] = start
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
            case 'q': i = loops[i] if not array[pointer] else i
            case '@': i = loops[i] if array[pointer] else i
        i += 1


vimBrain("""
lkkkkkkkkqhkkkkkkkkklj@hplkkkkqhkkkkkkklj@hkpkkkkkkkppkkkpllkkkkkkqhkkkkkkklj@hkkpjjjjjjjjjjjjplkkkkkkqhkkkkkkkkklj@hkphpkkkpjjjjjjpjjjjjjjjplllkkkkqhkkkkkkkklj@hkp
""")
