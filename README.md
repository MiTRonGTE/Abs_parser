# Abs_parser is a simple parser for absorbance data.

```
Scanning plate:
 |BLANK|--------------SAMPLE---------------|
 |  D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11|
 |EMPTY| E5 | E6 | E7 | E8 | E9 | E10 | E11|
 |EMPTY| F5 | F6 | F7 | F8 | F9 | F10 | F11|
 |-----------------------------------------|

Input:
    1 measurement A1-G1 [D5-D11], A2-G2 [E5-E11] and A3-G3 [F5-F11] -> Untitled1.txt
    2 measurement A4-G4 [D5-D11], A5-G5 [E5-E11] and A6-G6 [F5-F11] -> Untitled2.txt
    3 measurement A7-G7 [D5-D11], A8-G8 [E5-E11] and A9-G9 [F5-F11] -> Untitled3.txt
    4 measurement A10-G10 [D5-D11], A11-G11 [E5-E11] and A12-G12 [F5-F11] -> Untitled4.txt
    5 measurement H1-H7 [D5-D11] and H8-H12 [E5-E9] -> Untitled5.txt

Map:
                          Plate
      Untitled1   Untitled2   Untitled3   Untitled4
      1   2   3   4   5   6   7   8   9   10  11  12
  A   D5  E5  F5  D5  E5  F5  D5  E5  F5  D5  E5  F5
  B   D6  E6  F6  D6  E6  F6  D6  E6  F6  D6  E6  F6
  C   D7  E7  F7  D7  E7  F7  D7  E7  F7  D7  E7  F7
  D   D8  E8  F8  D8  E8  F8  D8  E8  F8  D8  E8  F8
  E   D9  E9  F9  D9  E9  F9  D9  E9  F9  D9  E9  F9
  F   D10 E10 F10 D10 E10 F10 D10 E10 F10 D10 E10 F10
  G   D11 E11 F11 D11 E11 F11 D11 E11 F11 D11 E11 F11
                        Untitled5
  H   D5  D6  D7  D8  D9  D10 D11 E5  E6  E7  E8  E9

Output:
    tsv with data abs 260/280 and 260/230.
```