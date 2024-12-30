with open("books/frankenstein.txt") as f:
        file_contents = f.read()

## Counts the amount of words in the entire book text
def count_words():
    words = len(file_contents.split())
    return words
## prints the entire book to the console
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(file_contents)
        
 
 
def count_char():
    book_lower = file_contents.lower()
    chars = {}
    
    for x in book_lower:
        
        if x == " ":
            pass
        elif x in chars:
            chars[x] += 1
        else:
            chars[x] = 1

    return chars



def book_report(dict):
    
    ## prints the name of the book to the console
    print("-- Begin Report of Frankenstein.txt --")
    
    ## prints the total amount of words in the book to the console
    print(f"{count_words()} words found in total within the book")
    
    for x in dict:
        print(f"The Character {x} was found {dict[x]} Times!" )
    
    print("------------End Report----------")
    


book_report(count_char())