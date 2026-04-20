class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        
        # Keep track of the maximum heights seen so far from both sides
        left_max = height[left]
        right_max = height[right]
        
        total_water = 0
        
        while left < right:
            # Process the side with the smaller max height
            if left_max < right_max:
                left += 1
                # Update max height or add trapped water
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                # Update max height or add trapped water
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                
        return total_water