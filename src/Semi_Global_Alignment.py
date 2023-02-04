import numpy as np
from random import seed
from random import choice

S1 = input()
S2 = input()

# S1 = "HEAGAWGHE"
# S2 = "PAWHEA"

# S1 = "AAAAA"
# S2 = "AA"

PAM250 = {
'A': {'A':  2, 'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N':  0, 'P':  1, 'Q':  0, 'R': -2, 'S':  1, 'T':  1, 'V':  0, 'W': -6, 'Y': -3},
'C': {'A': -2, 'C': 12, 'D': -5, 'E':-5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S':  0, 'T': -2, 'V': -2, 'W': -8, 'Y':  0},
'D': {'A':  0, 'C': -5, 'D':  4, 'E': 3, 'F': -6, 'G':  1, 'H':  1, 'I': -2, 'K':  0, 'L': -4, 'M': -3, 'N':  2, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'E': {'A':  0, 'C': -5, 'D':  3, 'E': 4, 'F': -5, 'G':  0, 'H':  1, 'I': -2, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'F': {'A': -3, 'C': -4, 'D': -6, 'E':-5, 'F':  9, 'G': -5, 'H': -2, 'I':  1, 'K': -5, 'L':  2, 'M':  0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W':  0, 'Y':  7},
'G': {'A':  1, 'C': -3, 'D':  1, 'E': 0, 'F': -5, 'G':  5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N':  0, 'P':  0, 'Q': -1, 'R': -3, 'S':  1, 'T':  0, 'V': -1, 'W': -7, 'Y': -5},
'H': {'A': -1, 'C': -3, 'D':  1, 'E': 1, 'F': -2, 'G': -2, 'H':  6, 'I': -2, 'K':  0, 'L': -2, 'M': -2, 'N':  2, 'P':  0, 'Q':  3, 'R':  2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y':  0},
'I': {'A': -1, 'C': -2, 'D': -2, 'E':-2, 'F':  1, 'G': -3, 'H': -2, 'I':  5, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -5, 'Y': -1},
'K': {'A': -1, 'C': -5, 'D':  0, 'E': 0, 'F': -5, 'G': -2, 'H':  0, 'I': -2, 'K':  5, 'L': -3, 'M':  0, 'N':  1, 'P': -1, 'Q':  1, 'R':  3, 'S':  0, 'T':  0, 'V': -2, 'W': -3, 'Y': -4},
'L': {'A': -2, 'C': -6, 'D': -4, 'E':-3, 'F':  2, 'G': -4, 'H': -2, 'I':  2, 'K': -3, 'L':  6, 'M':  4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V':  2, 'W': -2, 'Y': -1},
'M': {'A': -1, 'C': -5, 'D': -3, 'E':-2, 'F':  0, 'G': -3, 'H': -2, 'I':  2, 'K':  0, 'L':  4, 'M':  6, 'N': -2, 'P': -2, 'Q': -1, 'R':  0, 'S': -2, 'T': -1, 'V':  2, 'W': -4, 'Y': -2},
'N': {'A':  0, 'C': -4, 'D':  2, 'E': 1, 'F': -3, 'G':  0, 'H':  2, 'I': -2, 'K':  1, 'L': -3, 'M': -2, 'N':  2, 'P':  0, 'Q':  1, 'R':  0, 'S':  1, 'T':  0, 'V': -2, 'W': -4, 'Y': -2},
'P': {'A':  1, 'C': -3, 'D': -1, 'E':-1, 'F': -5, 'G':  0, 'H':  0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N':  0, 'P':  6, 'Q':  0, 'R':  0, 'S':  1, 'T':  0, 'V': -1, 'W': -6, 'Y': -5},
'Q': {'A':  0, 'C': -5, 'D':  2, 'E': 2, 'F': -5, 'G': -1, 'H':  3, 'I': -2, 'K':  1, 'L': -2, 'M': -1, 'N':  1, 'P':  0, 'Q':  4, 'R':  1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
'R': {'A': -2, 'C': -4, 'D': -1, 'E':-1, 'F': -4, 'G': -3, 'H':  2, 'I': -2, 'K':  3, 'L': -3, 'M':  0, 'N':  0, 'P':  0, 'Q':  1, 'R':  6, 'S':  0, 'T': -1, 'V': -2, 'W':  2, 'Y': -4},
'S': {'A':  1, 'C':  0, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P':  1, 'Q': -1, 'R':  0, 'S':  2, 'T':  1, 'V': -1, 'W': -2, 'Y': -3},
'T': {'A':  1, 'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  0, 'H': -1, 'I':  0, 'K':  0, 'L': -2, 'M': -1, 'N':  0, 'P':  0, 'Q': -1, 'R': -1, 'S':  1, 'T':  3, 'V':  0, 'W': -5, 'Y': -3},
'V': {'A':  0, 'C': -2, 'D': -2, 'E':-2, 'F': -1, 'G': -1, 'H': -2, 'I':  4, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -6, 'Y': -2},
'W': {'A': -6, 'C': -8, 'D': -7, 'E':-7, 'F':  0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4, 'P': -6, 'Q': -5, 'R':  2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y':  0},
'Y': {'A': -3, 'C':  0, 'D': -4, 'E':-4, 'F':  7, 'G': -5, 'H':  0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W':  0, 'Y': 10}
}

L1 = len(S1)
L2 = len(S2)
Gamma = 9
seed(1)

Scores = np.zeros( (L1 + 1, L2 + 1) )
Arrows = np.array(["" for _ in range(L1)], dtype='object')
for i in range(L1):
  Arrows[i] = np.array(["" for _ in range(L2)], dtype='object')

for i in range(1, L1+1):
  for j in range(1, L2+1):
    temp = np.zeros(3) # 0 : left / 1 : up-left / 2 : up
    temp[0] = Scores[i,j-1] - Gamma
    temp[1] = Scores[i-1,j-1] + PAM250[S1[i-1]][S2[j-1]]
    temp[2] = Scores[i-1,j] - Gamma
    Scores[i,j] = max(temp)
    if(max(temp) == temp[0]):
      Arrows[i-1][j-1] += "0"
    if(max(temp) == temp[1]):
      Arrows[i-1][j-1] += "1"
    if(max(temp) == temp[2]):
      Arrows[i-1][j-1] += "2"

# print(Scores)
# print(Arrows)

Row_max_value = Scores[L1, : ].max()

Column_max_value = Scores[:, L2 ].max()

max_score = int(max(Row_max_value, Column_max_value))

Seq = np.array(["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                ], dtype='object')
count = 0

for _ in range(int(len(Seq))):
  if(count == len(Seq)-10):
    break
  for n in range(L2):
    if(int(Scores[L1,n]) == max_score):
      seq = np.array(["", ""], dtype='object')
      max_index = np.array([L1, n])
      if((max_index[0] != L1) | (max_index[1] != L2)):
        if(L2 > max_index[1]):
          for i in range(L2-max_index[1]):
            seq[0] += "-"             # First Seq
            seq[1] += S2[L2-1-i]      # Second Seq
        else:
          for i in range(L1-max_index[0]):
            seq[0] += S1[L1-1-i]    # First Seq
            seq[1] += "-"           # Second Seq
            

      while((max_index[0] != 0) & (max_index[1] != 0)):
        if(len(Arrows[max_index[0]-1][max_index[1]-1]) == 1):
          if(Arrows[max_index[0]-1][max_index[1]-1] == '0'):
            seq[0] += "-"
            seq[1] += S2[max_index[1]-1]
            max_index[1] -= 1
          elif(Arrows[max_index[0]-1][max_index[1]-1] == '1'):
            seq[0] += S1[max_index[0]-1]
            seq[1] += S2[max_index[1]-1]
            max_index[0] -= 1 
            max_index[1] -= 1 
          else:
            seq[0] += S1[max_index[0]-1]
            seq[1] += "-"
            max_index[0] -= 1
        elif(len(Arrows[max_index[0]-1][max_index[1]-1]) == 2):
          integer = choice(['0', '1'])
          if(Arrows[max_index[0]-1][max_index[1]-1][int(integer)] == '0'):
            seq[0] += "-"
            seq[1] += S2[max_index[1]-1]
            max_index[1] -= 1
          elif(Arrows[max_index[0]-1][max_index[1]-1][int(integer)] == '1'):
            seq[0] += S1[max_index[0]-1]
            seq[1] += S2[max_index[1]-1]
            max_index[0] -= 1 
            max_index[1] -= 1 
          else:
            seq[0] += S1[max_index[0]-1]
            seq[1] += "-"
            max_index[0] -= 1
        else:
          integer = choice(['0', '1', '2'])
          if(Arrows[max_index[0]-1][max_index[1]-1][int(integer)] == '0'):
            seq[0] += "-"
            seq[1] += S2[max_index[1]-1]
            max_index[1] -= 1
          elif(Arrows[max_index[0]-1][max_index[1]-1][int(integer)] == '1'):
            seq[0] += S1[max_index[0]-1]
            seq[1] += S2[max_index[1]-1]
            max_index[0] -= 1 
            max_index[1] -= 1 
          else:
            seq[0] += S1[max_index[0]-1]
            seq[1] += "-"
            max_index[0] -= 1


      if((max_index[0] != 0) | (max_index[1] != 0)):
        if(max_index[1] != 0):
          for i in range(max_index[1]):
            seq[0] += "-"                       # First Seq
            seq[1] += S2[max_index[1]-1-i]      # Second Seq
        else:
          for i in range(max_index[0]):
            seq[0] += S1[max_index[0]-1-i]    # First Seq
            seq[1] += "-"                     # Second Seq

      seq[0] = seq[0][::-1]
      seq[1] = seq[1][::-1]
      Seq[count] = seq[0] + seq[1]
      count += 1


  for m in range(L1+1):
    if(int(Scores[m,L2]) == max_score):
      seq = np.array(["", ""], dtype='object')
      max_index = np.array([m, L2])
      if((max_index[0] != L1) | (max_index[1] != L2)):
        if(L2 > max_index[1]):
          for i in range(L2-max_index[1]):
            seq[0] += "-"             # First Seq
            seq[1] += S2[L2-1-i]      # Second Seq
        else:
          for i in range(L1-max_index[0]):
            seq[0] += S1[L1-1-i]    # First Seq
            seq[1] += "-"           # Second Seq
            

      while((max_index[0] != 0) & (max_index[1] != 0)):
        if(len(Arrows[max_index[0]-1][max_index[1]-1]) == 1 ):
          if(Arrows[max_index[0]-1][max_index[1]-1] == '0'):
            seq[0] += "-"
            seq[1] += S2[max_index[1]-1]
            max_index[1] -= 1
          elif(Arrows[max_index[0]-1][max_index[1]-1] == '1'):
            seq[0] += S1[max_index[0]-1]
            seq[1] += S2[max_index[1]-1]
            max_index[0] -= 1 
            max_index[1] -= 1 
          else:
            seq[0] += S1[max_index[0]-1]
            seq[1] += "-"
            max_index[0] -= 1
        elif(len(Arrows[max_index[0]-1][max_index[1]-1]) == 2):
          integer = choice(['0', '1'])
          if(Arrows[max_index[0]-1][max_index[1]-1][int(integer)] == '0'):
            seq[0] += "-"
            seq[1] += S2[max_index[1]-1]
            max_index[1] -= 1
          elif(Arrows[max_index[0]-1][max_index[1]-1][int(integer)] == '1'):
            seq[0] += S1[max_index[0]-1]
            seq[1] += S2[max_index[1]-1]
            max_index[0] -= 1 
            max_index[1] -= 1 
          else:
            seq[0] += S1[max_index[0]-1]
            seq[1] += "-"
            max_index[0] -= 1
        else:
          integer = choice(['0', '1', '2'])
          if(Arrows[max_index[0]-1][max_index[1]-1][int(integer)] == '0'):
            seq[0] += "-"
            seq[1] += S2[max_index[1]-1]
            max_index[1] -= 1
          elif(Arrows[max_index[0]-1][max_index[1]-1][int(integer)] == '1'):
            seq[0] += S1[max_index[0]-1]
            seq[1] += S2[max_index[1]-1]
            max_index[0] -= 1 
            max_index[1] -= 1 
          else:
            seq[0] += S1[max_index[0]-1]
            seq[1] += "-"
            max_index[0] -= 1

      if((max_index[0] != 0) | (max_index[1] != 0)):
        if(max_index[1] != 0):
          for i in range(max_index[1]):
            seq[0] += "-"                       # First Seq
            seq[1] += S2[max_index[1]-1-i]      # Second Seq
        else:
          for i in range(max_index[0]):
            seq[0] += S1[max_index[0]-1-i]    # First Seq
            seq[1] += "-"                     # Second Seq

      seq[0] = seq[0][::-1]
      seq[1] = seq[1][::-1]
      Seq[count] = seq[0] + seq[1]
      count += 1

print(max_score)
Seq = list(set(Seq))
Seq.remove('')
Seq.sort()
for i in Seq:
    print(i[0:int(len(i)/2)])
    print(i[int(len(i)/2):])