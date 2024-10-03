# Holes and Balls
# A man is doing an experiment with the device that he built newly. The structure of the device is as below diagram.
 
# B to E is a sloping surface with n holes, labelled H1, H2, ... Hn, on it. Holes are of different diameters and depths. The man is releasing m number of balls of different diameters from the point B one after the other. He needs to ﬁnd the positions of each ball after the experiment.  
# The specialties of the device are: 
# 1. A ball will fall into a hole, if its diameter is less than or equal to the diameter of the hole. 
# 2. A hole Hi will become full, if i numbers of balls fall into it. For example hole labelled H3 will become full if 3 balls fall into it. 
# 3. If a hole is full, then no more balls fall into it.  
# 4. A ball will reach the bottom point E from B, if and only if it is not falling into any one of the holes.
# Please help him in ﬁnding the eventual position of the balls. If a ball is in hole Pi, then take its position as i. If a ball reached the bottom point E, then take its position as 0. 
# Constraints
# 0 < N <= 50
# 0 < Diameter of holes <= 10^9
# 0 < M <= 1000
# 0 < Diameter of balls <= 10^9
# Input Format
# Line 1: total number of holes, N
# Line 2: N space separated integers denoting the diameters of N holes, from bottom to top
# Line 3: total number of balls, M
# Line 4: M space separated integers denoting the diameters of balls in the order of release.
# Output Format
# Line 1: Positions of each ball in the order of ball release separated by space.
# Refer the sample output for formatting
# Sample Input:
# 3
# 21 3 6
# 11
# 20 15 5 7 10 4 2 1 3 6 8
# Sample Output:
# 1 0 3 0 0 3 3 2 2 0 0
# Explanation:
# 3 holes are there labelled H1, H2, H3 of diameters 21, 3 and 6 respectively.   
def main():
    n = int(input())      
    h = list(map(int, input().split()))
    cap = [i + 1 for i in range(n)]  

    m = int(input())
    b = list(map(int, input().split()))

    for i in range(m):
        found = False  # Flag to check if we found a suitable index
        for j in range(n - 1, -1, -1):
            if b[i] <= h[j] and cap[j] != 0:
                print(j + 1, end=" ") 
                cap[j] -= 1 
                found = True
                break  

        if not found:
            print(0, end=" ")


if __name__== "_main_":
    main()
