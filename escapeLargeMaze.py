class Solution(object):
#     def inblocked(self, blocked, pt):
        
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        visit = {}
        q = []
        # print(len(q))
        q.append(source)
        bl = {}
        for l in blocked:
            bl[str(l)] = True
        # print(bl)
        # visit[str(source)] = True
        directions = [[0,-1], [0,1], [-1,0], [1,0]]
        dist = 0
        while(len(q)>0):
            # print(q)
            u = q.pop(-1)
            if not visit.get(str(u)):
                # print("herrrrr")
                for d in directions:
                    temp = [u[0]+d[0], u[1]+d[1]]
                    if temp[0]>=0 and temp[0]<1e+6 and temp[1]>=0 and temp[1]<1e+6:
                        if not bl.get(str(temp)):
                            if temp[0]==target[0] and temp[1]==target[1]:
                                return True
                            else:
                                q.append(temp)
                visit[str(u)] = True
                dist = abs(source[0]-u[0]) + abs(source[1]-u[1])
                if dist>201:
                    break
        if dist<200:
            return False
        visit = {}
        q = []
        q.append(target)
        dist = 0
        while(len(q)>0):
            # print(q)
            u = q.pop(-1)
            if not visit.get(str(u)):
                # print("herrrrr")
                for d in directions:
                    temp = [u[0]+d[0], u[1]+d[1]]
                    if temp[0]>=0 and temp[0]<1e+6 and temp[1]>=0 and temp[1]<1e+6:
                        if not bl.get(str(temp)):
                            if temp[0]==source[0] and temp[1]==source[1]:
                                return True
                            else:
                                q.append(temp)
                visit[str(u)] = True
                dist = abs(target[0]-u[0]) + abs(target[1]-u[1])
                if dist>201:
                    break
        if dist<200:
            return False
        return True
            
            
            
