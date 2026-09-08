TYPE=input("ARE YOU GIVING NUMBER OR WORD TO GET ASCII VALUE:")

if TYPE=="NUMBER":
    NUMBER=int(input("ENTER THE NUMBER TO GET ASCII VALUE IN WORD:"))
    ascii_value_NUMBER=chr(NUMBER)
    print(f"THE ASCII VALUE OF {NUMBER} IS:",ascii_value_NUMBER)

elif TYPE=="WORD":
    WORD = input("ENTER THE WORD TO GET ASCII VALUE IN NUMBER:")
    ascii_value_WORD =ord(WORD)
    print(f"THE ASCII VALUE OF {WORD} IS:",ascii_value_WORD)