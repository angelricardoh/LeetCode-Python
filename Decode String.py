class Solution:
    def decodeString(self, s: str) -> str:
        def getContent(s, global_mult = 1):
            result = ''
            current_string = ''
            stack = []
            current_mult = None
            for item in s:
                if item.isnumeric():
                    if current_string != '' and len(stack) == 0:
                        if current_mult is None:
                            result += current_string
                        else:
                            result += current_string * current_mult
                        current_string = ''
                    
                    if len(stack) != 0:
                        current_string += item
                    else:
                        if current_mult != None:
                            current_mult = (10 * current_mult) + int(item)
                        else:
                            current_mult = int(item)
                    
                    # if current string is not empty then add to result
                elif item == '[':
                    stack.append(item)
                    current_string += item
                elif item == ']':
                    stack.pop(0)
                    current_string += item
                    if len(stack) == 0:
                        result += getContent(current_string[1:-1], current_mult)
                        current_string = ''
                        current_mult = None
                else:
                    current_string += item 
                    
            # result += current_string
            if current_mult is None:
                result += current_string
            else:
                result += current_string * current_mult
            return result * global_mult    
        
        return getContent(s)