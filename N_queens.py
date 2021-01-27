import numpy as np
class Solution(object):

    def everyThingOkay(self, box, i, j):
        boxCopy = np.zeros(box.shape)
        boxCopy[:] = box[:]
        n = boxCopy.shape[0]
        boxCopy[i,:]= 0
        boxCopy[:,j] = 0
        # print(boxCopy)
        tempI = i
        tempJ = j
        while(tempI+1<n and tempJ+1<n):
            boxCopy[tempI+1,tempJ+1]=0
            tempI+=1
            tempJ+=1
        tempI = i
        tempJ = j
        while(tempI+1<n and tempJ-1>=0):
            boxCopy[tempI+1,tempJ-1]=0
            tempI+=1
            tempJ+=-1
        for a in range(i+1, n):
            nextQueen = boxCopy[a, :]
            if 1 in nextQueen:
                continue
            else:
                return False, boxCopy
        return True, boxCopy



    def allocateAndPropagate(self, box, i):
        n = box.shape[0]
        # print(n)
        if i==n-1:
            if 1 in box[i, :]:
                return 1
            else:
                return 0

        remianPlaces = box[i,:]
        Sols = 0
        for j in range(0, n):
            if remianPlaces[j]==0:
                continue
            #Queen is placed at I,J, Now explore contraints and update box
            box[i,j] = -1
            f, boxCopy = self.everyThingOkay(box, i, j)
            if f==False:
                boxCopy = box
                box[i,j] = 1
            else:
                Sols+=self.allocateAndPropagate(boxCopy, i+1)
                box[i,j] =1
        return Sols


    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n<=3 and n!=1:
            return 0
        rows = [1]*n
        box = [rows]*n
        # print(cols)
        box = np.array(box)
        num = self.allocateAndPropagate(box,0)
        return num


        
