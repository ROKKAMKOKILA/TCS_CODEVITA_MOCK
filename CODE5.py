#  Balancing stars
# CODU loves to play with string of brackets. He considers string as a good string if it is balanced with stars. A string is considered as balanced with stars if string contains balanced brackets and between every pair of bracket i.e. between opening and closing brackets, there are at least 2 stars(*) present. CODU knows how to check whether a string is balanced or not but this time he needs to keep a track of stars too. He decided to write a program to check whether a string is good or not. But CODU is not as good in programming as you are, so he decided to take help from you. Will you help him for this task? You need to print Yes and number of balanced pair if string satisfies following conditions(string is good if it satisfies following 2 conditions):
# 1. The string is balanced with respect to all brackets.
# 2. Between every pair of bracket there is at least two stars. However if string doesn't satisfies above conditions then print No and number of balanced pair in string as an output.
# Input Format
# The first and only line of input contains a string of characters(a-z,A-Z), numbers(0-9), brackets( '{', '[', '(', ')', ']', '}' ) and stars(*).
# Output Format
# Print space separated "Yes" (without quotes) and number of balanced pair if string is good. Else print "No" (without quotes) and number of balanced pair.
# Constraints
# 4 <= String length <= 1000
# Refer the sample output for formatting
# Sample Input:
# {**}
# Sample Output:
# Yes 1
def main():
    stack = []
    s = input()
    count = 0
    balanced = True

    i = 0
    while i < len(s):
        if s[i] in ['{', '[', '(']:
            stack.append(s[i])

        elif s[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                balanced = False
                break

        elif s[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break

        elif s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break

        elif s[i] == '*':
            if i + 1 < len(s) and s[i + 1] == '*':
                if stack and stack[-1] in ['(', '{', '[']:
                    count += 1
                i += 1  

        i += 1

    if balanced and not stack:
        print("Yes",end=" ")
        print(count)
    else:
        print(f"No {count}")

if __name__ == "__main__":
    main()
