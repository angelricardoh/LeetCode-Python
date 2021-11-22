# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
# Example 4:

# Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can pick from trees [1,2,1,1,2].
 
# Constraints:

# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def len_types(list):
            list_set = set()
            for item in list:
                list_set.add(item)
            return len(list_set)
        
        if len(fruits) == 1:
            return 1
        
        left = 0
        right = 1
        baskets = set()
        baskets.add(fruits[0])
        baskets.add(fruits[1])
        
        prev = None
        prev_index = None
        if fruits[0] != fruits[1]:
            prev = fruits[1]
            prev_index = 1
        else:
            prev = fruits[0]
            prev_index = 0
            
        max_length = 0
        n = len(fruits)
        
        for i in range(2, n):
            right = i
            baskets.add(fruits[i])
            
            if len(baskets) > 2:
                length = right - left
                if length > max_length:
                    max_length = length
                
                left = prev_index
                item_to_remove = None
                for item in baskets:
                    if item != fruits[i] and item != prev:
                        item_to_remove = item
                baskets.remove(item_to_remove)
                    
            if prev != fruits[i]:
                prev = fruits[i]
                prev_index = i
                    
        length = right - left + 1           
        if length > max_length:
            max_length = length
        return max_length