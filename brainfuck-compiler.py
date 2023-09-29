import os

def file():
    if os.path.exists("./main.bf"):
        with open("./main.bf", "r") as source_code:
            code = source_code.read()
    else:
        with open("./main.bf", "w+") as source_code:
            print("main.bf file generated, exiting now.")
            source_code.write("YOUR CODE HERE")
            quit()
    return list(code)

def main():
    code = file()
    LOWER_LIMIT = 1
    UPPER_LIMIT = 255
    fill_in = [0 for _ in range(UPPER_LIMIT)]
    cells = ["placeholder", *fill_in] # I want list indexes to start at 1 >:D
    del fill_in
    cell_index = 1
    ignore = False # Variable I'll use to add comments
    for instruction in code:
        match instruction:
            case "#":
                ignore = not ignore # Comments will be enclosed by # symbols
            case "+":
                if ignore:
                    continue
                cells[cell_index] += 1
            case "-":
                if ignore:
                    continue
                cells[cell_index] += 1
            case ">":
                if ignore:
                    continue
                cell_index += 1
                if cell_index > UPPER_LIMIT:
                    cell_index = UPPER_LIMIT
            case "<":
                if ignore:
                    continue
                cell_index -= 1
                if cell_index < LOWER_LIMIT:
                    cell_index = LOWER_LIMIT
            case ".":
                if ignore:
                    continue
                print(cells[cell_index], end="")
            case "!": # An instruction I invented :D (Print ASCII value of number in current cell, modified so letter a = 1)
                if ignore:
                    continue
                print(chr(cells[cell_index] + 96), end="")
            case ",":
                if ignore:
                    continue
                user_input = list(input("Input:\n"))
                """for i in range(len(user_input)): # Convert all letters to their ASCII value
                    if not user_input[i].isnumeric():
                        user_input[i] = ord(user_input[i])"""
                user_input = filter(lambda char: char.isnumeric(), user_input) # Filter out non-numeric characters
                cells[cell_index] = int("".join(user_input))

if __name__ == "__main__":
    main()