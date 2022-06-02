### Change word with another

# var to change the prog

#This is the menu or the home.

print("4 to show the menu")
fo = input(">>> ")
fo = int(fo)
if fo == 4:
    var = print("""
    This prog is to encript the text, but there is two way:
    1) The option: wuo.
    2) The option: ouw.
    3) No play.
    
    Chosse one: 
        """)
    
the = input(">>> ")
the = int(the)

#Here use while to call the code.
while the == 2:
    import rsa
    pubkey, privkey = rsa.newkeys(512)
    print("The second way text: ") 
    ho = input(">>> ")

    enctex = rsa.encrypt(ho.encode(), pubkey)
    dectex = rsa.decrypt(enctex, privkey).decode()
    print("The text: ", ho)
    print("The secret messege crypted: 👇 ")
    print(">>>")
    print(enctex)
    print("<<<")

    print("""Do you want to see the messege that it was incript?
        1) Yes.
        2) No.
        3) Play again.
        """)

    op = input(">>> ")
    op = int(op)
    if op == 1:
        print("The descrypted: ", dectex)
    if op == 3:
        the = 2
    if op == 2:
        print("Bye 👍")
        break
    else:
        print("🤔")

while the == 1:
    the = int(the)
    if the == 1:
        cara_chose = "x"
        def encript(sente, cara_chose):
            ense = ""
            for word in sente:
                if word.lower() in "aeiou":
                    if word.isupper():
                        ense = ense + cara_chose.upper
                    else:
                        ense = ense + cara_chose
                else:
                    ense = ense + word
            return encript 
            
        print(encript(input("This is the firt way, Give a sentences\n> "), cara_chose))
        
        print("""Already, 👆 This was your sentences. Do you want?
        A) Finishes the game.
        B) Play again.
        """)

        hii = input(">>> ")
        hii = hii.upper
        if hii == ("B") or ("b"):
            the = 1
        if hii == ("A") or ("a"):
            break
        
