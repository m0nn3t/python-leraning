

with open("symbols.txt", 'r') as file:
    with open('ex2 - results.txt','a') as results:
        results.write(f"2.1\n")
        for f in file:
            line = f.strip()
            if line == line[::-1]:
                print(line)
                results.write(f"{line}\n")


print()


with open("symbols.txt", 'r') as file:
    with open('ex2 - results.txt','a') as results:
        results.write(f"2.2\n")
        count = 0
        res = []
        pos = []
        lines = [line.strip() for line in file]
        for y in range(1, len(lines) - 1):
            for x in range(1, len(lines[y]) -1):
                center = lines[y][x]
                if ((lines[y-1][x-1]) == (lines[y-1][x]) == (lines[y-1][x+1]) == (lines[y][x-1]) == center == (lines[y][x+1]) == (lines[y+1][x-1]) == (lines[y+1][x]) == (lines[y+1][x+1])):
                    print(f"line: {y+1}  position: {x+1}")
                    count += 1
                    res.append(count)               
                    pos.append(f"{count} {y+1} {x+1}\n")
        results.write(f"{res[-1]}\n")
        for i in pos:
            results.write(i)
                  
        print(f"total amount of 3x3 squares: {count}")