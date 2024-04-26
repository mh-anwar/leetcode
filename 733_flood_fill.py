# 733. Flood Fill (Grind75 #9)
# 2024-04-26

# Approach
# Use depth-first-search, start (fill) at the first coordinate, get it's neighbours and call fill function on them - Beats 18.33%
# ! Come back to this and improve this sol

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image

        self.fill(image, sr, sc, image[sr][sc], color)
        return image
        
    def fill(self, image, sr, sc, color, newColor):
        # To prevent index out of bounds check image[sr][sc] at the end
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != color:
            return
            
        image[sr][sc] = newColor
        self.fill(image, sr -1, sc, color, newColor), 
        self.fill(image, sr, sc -1, color, newColor), 
        self.fill(image, sr +1, sc, color, newColor), 
        self.fill(image, sr, sc+1, color, newColor)