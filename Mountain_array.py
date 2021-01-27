# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        low = 0
        high = mountain_arr.length()-1
        mount = 0
        while(low<=high):
            mid = int((low+high)/2)
            mid_n = mountain_arr.get(mid)
            bef_n = mountain_arr.get(mid-1)
            aft_n = mountain_arr.get(mid+1)
            # if mid_n==target:
            #     return mid
            # elif bef_n
            if bef_n<mid_n and mid_n>aft_n:
                mount = mid
                break
            elif bef_n<mid_n and mid_n<aft_n:
                low = mid
            else:
                high = mid
        if target==mountain_arr.get(mount):
            return mount
        low = 0
        high = mount
        while(low<=high):
            # print("here1")
            mid = int((low+high)/2)
            mid_n = mountain_arr.get(mid)
            if mid_n==target:
                return mid
            elif mid_n<target:
                low = mid+1
            else:
                high = mid-1
        low = mount+1
        high = mountain_arr.length()-1
        while(low<=high):
            # print("here2")
            mid = int((low+high)/2)
            mid_n = mountain_arr.get(mid)
            if mid_n==target:
                return mid
            elif mid_n>target:
                low = mid+1
            else:
                high = mid-1
        return -1








            
