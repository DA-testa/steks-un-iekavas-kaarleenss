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
        
            opening_brackets_stack.append(Bracket(next,i))
            
            

        if next in ")]}":
            # Prss closing bracket, write your code here
            if opening_brackets_stack == [] or are_matching(opening_brackets_stack[-1].char,next) == False :
                
                return i + 1
            else:
                opening_brackets_stack.pop()
                
            

    if opening_brackets_stack == []:
        return  "Success"
    else:
        return opening_brackets_stack[-1].position + 1
    
def main():
    text = input()
    if text == "I":
        text = input()
        mismatch = find_mismatch(text)
        # Printing answer, write your code here
        print(mismatch)
    
if __name__ == "__main__":
    main()

#jauns teksts prieks parbaudem
