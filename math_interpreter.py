from src import read_line
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Not enough argument.")
    filename = sys.argv[1]
    if filename[-3:] == ".lx":
        with open(filename, "r") as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                read_line(line, idx)
    else:
        print(f"File extenstion error '{filename[-3:]}'")
