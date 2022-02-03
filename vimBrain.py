def vimBrain(code):
    array, starts, user, loops, i, pointer = [0], [], [], {}, 0, 0
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
            case 'i': list(input() + "\n") if user == [] else 0; array[pointer] = ord(user.pop(0))
            case 'q': i = loops[i] if not array[pointer] else i
            case '@': i = loops[i] if array[pointer] else i
        i += 1


vimBrain("""
lkkkkkkkkqhkkkkkkkkklj@hplkkkkqhkkkkkkklj@hkpkkkkkkkppkkkpllkkkkkkqhkkkkkkklj@hkkpjjjjjjjjjjjjplkkkkkkqhkkkkkkkkklj@hkphpkkkpjjjjjjpjjjjjjjjplllkkkkqhkkkkkkkklj@hkp
""")
