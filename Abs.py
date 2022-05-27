#!/usr/bin/python3

##################
# Kamil Pawlicki #
##################

# Input:
# 1 measurement A1-G1 [D5-D11], A2-G2 [E5-E11] and A3-G3 [F5-F11] -> Untitled1
# 2 measurement A4-G4 [D5-D11], A5-G5 [E5-E11] and A6-G6 [F5-F11] -> Untitled2
# 3 measurement A7-G7 [D5-D11], A8-G8 [E5-E11] and A9-G9 [F5-F11] -> Untitled3
# 4 measurement A10-G10 [D5-D11], A11-G11 [E5-E11] and A12-G12 [F5-F11] -> Untitled4
# 5 measurement H1-H7 [D5-D11] and H8-H12 [E5-E9] -> Untitled5

# Map:
#                           Plate
#       Untitled1   Untitled2   Untitled3   Untitled4
#       1   2   3   4   5   6   7   8   9   10  11  12
#   A   D5  E5  F5  D5  E5  F5  D5  E5  F5  D5  E5  F5
#   B   D6  E6  F6  D6  E6  F6  D6  E6  F6  D6  E6  F6
#   C   D7  E7  F7  D7  E7  F7  D7  E7  F7  D7  E7  F7
#   D   D8  E8  F8  D8  E8  F8  D8  E8  F8  D8  E8  F8
#   E   D9  E9  F9  D9  E9  F9  D9  E9  F9  D9  E9  F9
#   F   D10 E10 F10 D10 E10 F10 D10 E10 F10 D10 E10 F10
#   G   D11 E11 F11 D11 E11 F11 D11 E11 F11 D11 E11 F11
#                         Untitled5
#   H   D5  D6  D7  D8  D9  D10 D11 E5  E6  E7  E8  E9

# Core of name file
core_name = "Untitled"


# Read all file and extract data
def read_file_abs(core_name):
    rows = [[] for _ in range(0, 8)]
    for i in range(1, 6):
        with open(f"data//{core_name}{i}.txt", "rb") as ff:
            contents = ff.read().decode("utf-16")

        if len(contents) < 20:
            print("Error empty file!")
            exit()

        # uncomment to replace . with ,
        # contents = contents.replace(".", ",")

        table_body = False
        index = 0
        end_h = []

        for line in contents.split("\n"):
            if "Sample	Well	DilutionFactor	A260	A280	A230	260:280	260:230	Concentration (ng/uL)	Range	" in line:
                table_body = True
                continue
            if table_body:
                if line[0] == "0":
                    line = line[3:5] + line[7:]
                if i < 5:
                    rows[index].append(line.split()[4:6])

                    if "F" in line:
                        index += 1

                else:
                    if "D" in line:
                        rows[-1].append(line.split()[4:6])
                    elif "E" in line:
                        end_h.append(line.split()[4:6])

                if "F11" in line:
                    rows[-1].extend(end_h[0:5])
                    break
    return rows


# write data to output.tsv file
def write_output_file(rows):
    read260_280 = read260_230 = "\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\n"
    row_name = "ABCDEFGH"

    for rows, cols in enumerate(rows):
        r280 = [col[0] for col in cols]
        read260_280 += f"{row_name[rows]}\t" + '\t'.join(r280) + '\n'
        r230 = [col[1] for col in cols]
        read260_230 += f"{row_name[rows]}\t" + '\t'.join(r230) + '\n'

    output = read260_280 + "\n" + read260_230
    print(output)

    with open("output.tsv", "w") as ff:
        ff.write(output)


if __name__ == "__main__":
    columns = read_file_abs(core_name)
    write_output_file(columns)
