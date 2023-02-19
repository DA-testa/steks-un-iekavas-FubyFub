#Andrejs Vasiljevs 221RDB441 12 grupa
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append( Bracket( next, i + 1 ))
            pass

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            pass
            high = opening_brackets_stack.pop()
            if not are_matching( high.char, next ):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    


def main():
    text = input()
    
    if "I" in text:
        text = input()
    elif "F" in text:
        path = input()
        with open( path ) as f:
            text = f.read()
    mismatch = find_mismatch(text)
    
    if not mismatch :
        print ( "Success" )
    else:
        print ( mismatch )

if __name__ == "__main__":
    main()
