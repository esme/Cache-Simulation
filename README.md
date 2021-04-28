# Computer Architecture Project 2 - Cache Simulation
Details:
- Software simulation of a cache memory subsystem
- Main memory of 2k array
- Direct-mapped, write-back cache
- Supports three types of requests from the terminal: (R)ead, (W)rite, or (D)isplay Cache
- If a Read is requested: Ff the address is in the cache, display the value found for it in cache AND indicate that a cache hit took place. If not, go to your main memory instead, bring the entire block into the cache, display the value found AND indicate a cache miss
- If a write is to be performed on a block that is not already in the cache, bring the entire block into the cache, perform the write and consider it a cache miss
- Display Cache will display the contents of each slot in the cache

Output:
```
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
5
Copying data from main mem to cache...
At that byte there is the value 5 (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
6
At that byte there is the value 6 (Cache Hit)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
7
At that byte there is the value 7 (Cache Hit)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
14c
Copying data from main mem to cache...
At that byte there is the value 4c (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
14d
At that byte there is the value 4d (Cache Hit)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
14e
At that byte there is the value 4e (Cache Hit)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
14f
At that byte there is the value 4f (Cache Hit)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
150
Copying data from main mem to cache...
At that byte there is the value 50 (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
151
At that byte there is the value 51 (Cache Hit)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
3A6
Copying data from main mem to cache...
At that byte there is the value a6 (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
4C3
Copying data from main mem to cache...
At that byte there is the value c3 (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
D
        Slot Valid   Tag Dirty  Data
           0     1     0     0     0     1     2     3     4     5     6     7     8     9     A     B     C     D     E     F
           1     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           2     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           3     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           4     1     1     0    40    41    42    43    44    45    46    47    48    49    4A    4B    4C    4D    4E    4F
           5     1     1     0    50    51    52    53    54    55    56    57    58    59    5A    5B    5C    5D    5E    5F
           6     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           7     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           8     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           9     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           A     1     3     0    A0    A1    A2    A3    A4    A5    A6    A7    A8    A9    AA    AB    AC    AD    AE    AF
           B     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           C     1     4     0    C0    C1    C2    C3    C4    C5    C6    C7    C8    C9    CA    CB    CC    CD    CE    CF
           D     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           E     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           F     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
---
(R)ead, (W)rite, or (D)isplay Cache?
W
What address would you like to write to?
14C
What data would you like to write at that address?
99
Value 99 has been written to address 14c. (Cache Hit)
---
(R)ead, (W)rite, or (D)isplay Cache?
W
What address would you like to write to?
63B
What data would you like to write at that address?
7
Copying data from main mem to cache...
Value 7 has been written to address 63b. (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
582
Copying data from main mem to cache...
At that byte there is the value 82 (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
D
        Slot Valid   Tag Dirty  Data
           0     1     0     0     0     1     2     3     4     5     6     7     8     9     A     B     C     D     E     F
           1     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           2     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           3     1     6     1    30    31    32    33    34    35    36    37    38    39    3A     7    3C    3D    3E    3F
           4     1     1     1    40    41    42    43    44    45    46    47    48    49    4A    4B    99    4D    4E    4F
           5     1     1     0    50    51    52    53    54    55    56    57    58    59    5A    5B    5C    5D    5E    5F
           6     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           7     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           8     1     5     0    80    81    82    83    84    85    86    87    88    89    8A    8B    8C    8D    8E    8F
           9     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           A     1     3     0    A0    A1    A2    A3    A4    A5    A6    A7    A8    A9    AA    AB    AC    AD    AE    AF
           B     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           C     1     4     0    C0    C1    C2    C3    C4    C5    C6    C7    C8    C9    CA    CB    CC    CD    CE    CF
           D     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           E     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           F     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
348
Updating main mem starting at 140...
Copying data from main mem to cache...
At that byte there is the value 48 (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
3F
Updating main mem starting at 630...
Copying data from main mem to cache...
At that byte there is the value 3f (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
D
        Slot Valid   Tag Dirty  Data
           0     1     0     0     0     1     2     3     4     5     6     7     8     9     A     B     C     D     E     F
           1     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           2     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           3     1     0     0    30    31    32    33    34    35    36    37    38    39    3A    3B    3C    3D    3E    3F
           4     1     3     0    40    41    42    43    44    45    46    47    48    49    4A    4B    4C    4D    4E    4F
           5     1     1     0    50    51    52    53    54    55    56    57    58    59    5A    5B    5C    5D    5E    5F
           6     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           7     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           8     1     5     0    80    81    82    83    84    85    86    87    88    89    8A    8B    8C    8D    8E    8F
           9     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           A     1     3     0    A0    A1    A2    A3    A4    A5    A6    A7    A8    A9    AA    AB    AC    AD    AE    AF
           B     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           C     1     4     0    C0    C1    C2    C3    C4    C5    C6    C7    C8    C9    CA    CB    CC    CD    CE    CF
           D     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           E     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           F     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
14b
Copying data from main mem to cache...
At that byte there is the value 4b (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
14c
At that byte there is the value 99 (Cache Hit)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
63F
Copying data from main mem to cache...
At that byte there is the value 3f (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
R
What address would you like to read?
83
Copying data from main mem to cache...
At that byte there is the value 83 (Cache Miss)
---
(R)ead, (W)rite, or (D)isplay Cache?
D
        Slot Valid   Tag Dirty  Data
           0     1     0     0     0     1     2     3     4     5     6     7     8     9     A     B     C     D     E     F
           1     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           2     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           3     1     6     0    30    31    32    33    34    35    36    37    38    39    3A     7    3C    3D    3E    3F
           4     1     1     0    40    41    42    43    44    45    46    47    48    49    4A    4B    99    4D    4E    4F
           5     1     1     0    50    51    52    53    54    55    56    57    58    59    5A    5B    5C    5D    5E    5F
           6     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           7     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           8     1     0     0    80    81    82    83    84    85    86    87    88    89    8A    8B    8C    8D    8E    8F
           9     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           A     1     3     0    A0    A1    A2    A3    A4    A5    A6    A7    A8    A9    AA    AB    AC    AD    AE    AF
           B     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           C     1     4     0    C0    C1    C2    C3    C4    C5    C6    C7    C8    C9    CA    CB    CC    CD    CE    CF
           D     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           E     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
           F     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0     0
---
```