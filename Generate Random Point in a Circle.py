'''
Given the radius and the position of the center of a circle, implement the function randPoint which generates a uniform random point inside the circle.

Implement the Solution class:

Solution(double radius, double x_center, double y_center) initializes the object with the radius of the circle radius and the position of the center (x_center, y_center).
randPoint() returns a random point inside the circle. A point on the circumference of the circle is considered to be in the circle. The answer is returned as an array [x, y].

Example 1:

Input
["Solution", "randPoint", "randPoint", "randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
Output
[null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
'''

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        # Initializing the variables at class level

        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        ang = random.uniform(0, 1) * 2 * math.pi 
        hyp = sqrt(random.uniform(0, 1)) * self.radius
        adj = cos(ang) * hyp
        opp = sin(ang) * hyp
        return [self.x_center + adj, self.y_center + opp]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()