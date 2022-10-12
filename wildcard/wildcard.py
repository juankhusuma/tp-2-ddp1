from typing import Union


def search(pattern: str, line: str, flag: Union[bool, None] = None) -> bool:
    if flag == "-i":
        line = line.lower()
        pattern = pattern.lower()
    if flag == "-w":
        pattern = " " + pattern + " "
        line = " " + line + " "
    if "*" in pattern:
        pattern = pattern.split("*")
        head = False
        tail = False
        for i in range(len(line) - len(pattern[0]) + 1):
            if line[i:i+len(pattern[0])] == pattern[0]:
                head = True
                line = line[i+len(pattern[0]):]
        print(line)
        for i in range(len(line)-len(pattern[1]) + 1):
            if line[i:i+len(pattern[1])] == pattern[1]:
                tail = True
        return head and tail
    return pattern in line


line = "Halo semua, selamat pagi"

print(search(
    "selamat pagi",
    line,
))

print(search(
    "selamat pagi",
    line,
    "-w"
))

print(search(
    "Selamat pagi",
    line,
    "-w"
))

print(search(
    "se*gi",
    line,
    "-i"
))
