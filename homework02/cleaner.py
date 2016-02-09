# This file cleans up the data
import os

def main():
    parsed_lines = []
    with open(os.path.join("data", "adult.data"), "r") as data_file:
        lines_read = 0
        for line in data_file:
            lines_read += 1
            elems = [word.strip() for word in line.strip().split(",")]
            if len(elems) > 14:
                last = "g" if elems[-1] == ">50K" else "l"
                elems = [elems[0], elems[2], elems[4]] + elems[10:13]
                try:
                    int_elems = list(map(int, elems))
                except:
                    continue
                parsed_lines.append(", ".join(elems) + ", " + last)
        print("Read {} lines.".format(lines_read))
    with open(os.path.join("data", "clean.data"), "w+") as data_file:
        for line in parsed_lines:
            data_file.write(line + "\n")
    print("Wrote {} lines.".format(len(parsed_lines)))

if __name__ == "__main__":
    main()
