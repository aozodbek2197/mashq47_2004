# 1-mashq
def is_valid_parentheses(s):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

print(is_valid_parentheses("({[]})"))
print(is_valid_parentheses("({[})"))
# 2-mashq
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates([1,2,2,3,4,4,5,1]))
# 3-mashq
def second_largest(arr):
    if len(arr) < 2: return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

print(second_largest([10, 5, 8, 20, 15]))
