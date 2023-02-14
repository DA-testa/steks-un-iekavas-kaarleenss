# python3
#Labd1

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
        
            opening_brackets_stack.append(next)
            

        if next in ")]}":
            # Prss closing bracket, write your code here
            if are_matching(opening_brackets_stack.pop(),next) == False :
                return i + 1
            

    if opening_brackets_stack == []:
        return "Success"
    
def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)
    
if __name__ == "__main__":
    main()

#jauns teksts prieks parbaudem
