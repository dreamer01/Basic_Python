
import fileinput

lines= fileinput.input()
N = int(lines[0])   # N is fucking need of the question
A = list(set(map(int,lines[1].split())))    # it will take infinite inputs from user in space and store i the listComprenshion
A.sort()
print(A[len(A)-2])