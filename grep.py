import os
import re
import sys


def search_string(text, pattern, flag=None):
    text = " " + text
    main_pattern = pattern.replace("*", "(.+)")
    if flag == "-w":
        main_pattern = r"\s" + main_pattern + r"\s"
    if flag == "-i":
        return re.compile(main_pattern, re.I).search(text)
    return re.compile(main_pattern).search(text)


def check_file(path, pattern, flag):
    with open(path) as f:
        lines = f.readlines()
        nums = []
        for i, line in enumerate(lines):
            if search_string(line, pattern, flag):
                nums.append(i)
        return [nums, lines]


def gen_file_paths(dir):
    paths = []
    for root, _, files in os.walk(dir):
        for file in files:
            paths.append(f"{root}\\{file}")
    return paths


def print_res(path, num, line):
    print(f"{path:<40} line {num:<3} {line[:40].strip():<40}")


def parse_args(args):
    try:
        if "-w" in args and "-i" in args:
            raise Exception("Argumen program anda tidak benar")
        if len(args) == 3:
            if args[-3] != "-w" and args[-3] != "-i":
                raise Exception("Argumen program anda tidak benar")
            return [args[-1], args[-2], args[-3]]
        else:
            return [args[-1], args[-2], None]

    except IndexError:
        print("Argumen program anda tidak benar")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        path, search_pattern, flag = parse_args(args)
        paths = gen_file_paths(path)
        if os.path.isdir(path):
            for p in paths:
                nums, lines = check_file(p, search_pattern, flag)
                for i in nums:
                    print_res(p, i+1, lines[i])
        else:
            nums, lines = check_file(path, search_pattern, flag)
            for i in nums:
                print_res(path, i+1, lines[i])
    except IndexError:
        print("Argumen program anda tidak benar")
    except FileNotFoundError as f:
        print(f"Path {f.filename} tidak ditemukan")


if __name__ == '__main__':
    main()
