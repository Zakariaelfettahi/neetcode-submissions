class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights or len(heights)==1:
            return 0    

        # O(N) time solution
        results =[]
        L = 0
        R = len(heights)-1

        while L<R:
            area = min(heights[L],heights[R]) *(R-L)
            results.append(area)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return max(results)

            