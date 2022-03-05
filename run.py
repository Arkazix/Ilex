from main import read_line

filename = "test/test.lx"

if __name__ == '__main__':
    if filename[-3:] == ".lx":
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                read_line(line)
    else:
        print(f"File extenstion error '{filename[-3:]}'")