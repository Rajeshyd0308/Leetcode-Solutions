class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        while(i<=len(nums1) or j<=len(nums2)):
            # print(nums1)
            if i==len(nums1):
                if j==len(nums2):
                    break
                nums1.insert(i,nums2[j])
                j+=1
                i+=1
            # print(nums1)
            elif j==len(nums2):
                break
            elif nums1[i]>=nums2[j]:
                nums1.insert(i,nums2[j])
                j+=1
                i+=1
            else:
                i+=1
            
        if len(nums1)%2==0:
            # print(nums1)
            # print(nums1[len(nums1)/2 -1], nums1[len(nums1)/2])
            a = nums1[len(nums1)/2 -1] + nums1[len(nums1)/2]
            # print(float(a)/2)
            return float(a)/2
        else:
            return nums1[len(nums1)//2]
