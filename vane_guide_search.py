import random
import time

# File Format:
# Each line format should be "Order,A,B"
# Ex.
# 1,0.43,0.52
# 2,0.59,0.678
# 3,0.023,0.134
# ...

#--------- Classes -----------#

class Vane:

    def __init__(self, order, A, B):
        self.order = order
        self.A = A
        self.B = B

#-------- Functions ---------#

def compute_avg_area(vanes):
    totalArea = 0.0
    numVanes = len(vanes)
    
    for i in range(numVanes):
        totalArea += vanes[i].A + vanes[i].B
        
    return totalArea / numVanes
    
def compute_score(vanes, avgArea):
    score = 0.0
    numVanes = len(vanes)
    
    for i in range(numVanes - 1):
        score += abs(avgArea - vanes[i].A - vanes[i+1].B)
        
    score += abs(avgArea - vanes[numVanes - 1].A - vanes[0].B)
    
    score = score * -1
    
    return score

#--------- Program ----------#

print("Enter input file name (press enter to default to \"input.txt\"):")
input = input()

if input == "":
    input = "input.txt"

fin = open(input)

vanes = []

for line in fin:
    spline = line.split(",")
    vanes.append(Vane(int(spline[0]), float(spline[1]), float(spline[2])))

numVanes = len(vanes)
fin.close()

start = time.perf_counter()

avgArea = compute_avg_area(vanes)

bestVanes = vanes
random.shuffle(bestVanes)
bestScore = compute_score(bestVanes, avgArea)

done = False

while not(done):
    done = True
    
    nextVanes = list(bestVanes)
    
    for i in range(numVanes):
        for j in range(i + 1, numVanes):
            tmp = nextVanes[i]
            nextVanes[i] = nextVanes[j];
            nextVanes[j] = tmp;
            
            nextScore = compute_score(nextVanes, avgArea);

            if nextScore > bestScore:
                bestVanes = nextVanes;
                bestScore = nextScore;
                done = False;
                break;
                
            tmp = nextVanes[i]
            nextVanes[i] = nextVanes[j];
            nextVanes[j] = tmp;
            
        if not(done):
            break;

end = time.perf_counter()

elapsed = "%.12f" % (end - start);

fout = open("output.txt", "wt")
fout.write("Elapsed Time: " + elapsed + " sec\n")

for i in range(numVanes):
    fout.write(str(bestVanes[i].order) + "," + str(bestVanes[i].A) + "," + str(bestVanes[i].B) + "\n")
    
fout.close()