from main import read_line

filename = "test/test.lx"

if __name__ == '__main__':
    if filename[-3:] == ".lx":
        with open(filename, "r") as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                read_line(line, idx)
    else:
        print(f"File extenstion error '{filename[-3:]}'")
        