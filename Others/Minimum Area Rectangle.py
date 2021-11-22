# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

# Example 1:

# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:

# Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: (x[0], x[1]))
        # sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        possible_areas = []
        for p1 in range(n):
            for p2 in range(p1 + 1, n):
                for p3 in range(p2 + 1, n):
                    for p4 in range(p3 + 1, n):
                        point1 = points[p1]
                        point2 = points[p2]
                        point3 = points[p3]
                        point4 = points[p4]
                        if point1[0] == point2[0] and point1[1] == point3[1] and point3[0] == point4[0] and point2[1] == point4[1]:
                            if (point1,point2,point3,point4) not in possible_areas:
                                possible_areas.append((point1,point2,point3,point4))
                                
        result = float('inf')
        for item in possible_areas:
            area = abs(item[0][0] - item[2][0]) * abs(item[0][1] - item[1][1])
            if area < result:
                result = area
        if result == float('inf'):
            result = 0
        return result

    def minAreaRectLeetCode(self, points):
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            seen.add((x1, y1))
        return res if res < float('inf') else 0