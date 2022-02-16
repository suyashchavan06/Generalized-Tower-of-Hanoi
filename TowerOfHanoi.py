from typing import List

class Disk:

    size: int

    def __init__(self,s):
        self.size=s

class Rod:

    state: List[Disk]

    def __init__(self):
        self.state=[]

    def popDisk(self) :
        if len(self.state)<0:
            return None
        else:
            d = self.state.pop()
        return d

    def pushDisk(self,d:Disk):
        self.state.append(d)
        return True

class TowerOfHanoi:


    def __init__(self,no_disk:int,no_rods:int):
        self.orientation=[]
        for i in range(no_rods):
            self.orientation.append(Rod())
        
        for j in reversed(range(no_disk)):
            self.orientation[0].pushDisk(Disk(j+1))

        self.steps=[]

    def displayOrientation(self):
        print("Step "+str(len(self.steps)+1))
        for r in range(len(self.orientation)):
            print("Rod ["+str(r)+"]:",end="")
            for d in self.orientation[r].state:
                print(str(d.size)+",",end="")
            print()
        print()
    
    def moveDisk(self,start,end):
        temp_disk=self.orientation[start].popDisk()
        self.orientation[end].pushDisk(temp_disk)
        temp_step={}
        temp_step["disk"]=temp_disk
        temp_step["start"]=start
        temp_step["end"]=end
        # If you wish to see visual Representation, uncomment the following statement
        self.displayOrientation()
        self.steps.append(temp_step)
    


    def getEmptyRod(self):
        for l in range(len(self.orientation)):
            if len(self.orientation[l].state)==0:
                return l
    
    def recursiveTOH(self,n,start,end,aux):
        if n == 1:
            self.moveDisk(start,end)
            return 
        self.recursiveTOH(n-1,start,aux,end)
        self.moveDisk(start,end)
        self.recursiveTOH(n-1,aux,end,start)
        return 
    
    def threerod(self,start,aux,end):
        n=len(self.orientation[start].state)
        self.recursiveTOH(n,start,end,aux)
        
    
    def run(self,d,r):
        rempty=r-1
        k=rempty

        #Phase 1: Distributing disks from original pile to empty rods, ensuring number of empty rods remains more than two
        doTOH=True
        while rempty>2:
            for i in range(k):
                place=self.getEmptyRod()
                self.moveDisk(0,place)

            for j in range(1,k):
                self.moveDisk(place-j,place) 
            rempty=rempty-1
            k=rempty    
            if len(self.orientation[0].state)==0:
                doTOH=False
                target=place
    
        #Phase 2: Applying recursive Tower of Hanoi solution on the original rod, and the two empty rods, to shift all the
        # disks on original rod to new rod(target)
        if doTOH==True:
            self.threerod(0,1,2)
            target = 2
        
        #Phase 3: Distributing all piles of disks created in Phase 1, and accumalating them on the target rod for solution
        for i in range(target+1,r):
            while len(self.orientation[i].state)>1:
                place=self.getEmptyRod()
                self.moveDisk(i,place)
            for j in range(i+1):
                if i-j==target:
                    continue
                self.moveDisk(i-j,target)

        return target




def takeInput():
    while True:
        print("How many rods in the problem?")
        r=int(input())
        if r> 10:
            print("Max no. of rods allowed is 10")
            continue
        else:
            break

    while True:
        print("How many disks in the original rod?")
        d=int(input())
        if d>40:
            print("Max no. of disks allowed is 40")
        else:
            break
    
    return r,d

def main():
    r,d=takeInput()
    toh=TowerOfHanoi(d,r)
    if d < 2:
        print("1) Disk 1 was moved from Rod 1 to Rod 2")
        return
    if r < 3:
        print("No Solution is possible")
        return
    target = toh.run(d,r)
    print("All Disks will be shifted to Rod "+str(target+1))

    print("\n--------------STEPS--------------")
    for s in range(len(toh.steps)):
        print(str(s+1)+") Disk "+str(toh.steps[s]["disk"].size)+" was moved from Rod "+str(toh.steps[s]["start"]+1)+" to Rod "+str(toh.steps[s]["end"]+1))




if __name__ == "__main__":
    main()
