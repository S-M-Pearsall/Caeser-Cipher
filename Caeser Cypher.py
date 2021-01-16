#Created by Scott Pearsall

 
#Variable for holding the encrypted word to output it once put together
encryptedWord = ''
#Variable for holding the decrypted word to output it once put together
decryptedWord = ''
#Variable for holding the menu choice the user has made
choice = ()
#Variable holding a mutable offset number for use in brute force
autoOffset = 1


#A while loop to bring back the menu options
#after an option is chosen and completed.
#It exits the loop when choice 4 is chosen.
while choice != 4:
    #Set of basic print commands to show the options a user may take
    #Could be coded in one line but looks far cleaner and more efficient when
    #organised as so.
    print()
    print("*** MENU *** \n")
    
    print("1. Encrypt string")
    print("2. Decrypt string")
    print("3. Brute force decryption")
    print("4. Quit \n")

    #a line requesting the user to make a menu choice
    choice = int(input("What would you like to do? [1,2,3,4]? "))

    #If a choice is invalid, it tells the user it's invalid and requests it again
    while choice not in [1, 2, 3, 4]:
        print("Invalid choice, please enter either 1, 2, 3, or 4.")
        choice = int(input("What would you like to do? [1,2,3,4]?"))
    print()

    #Asks the user to input the string to be encrypted and what to offset
    #it by if they pick option 1
    if choice == 1:
        encryption = input("Please enter string to encrypt: ")
        offset = int(input("Please enter offset value (1 to 94): "))
        #If the offset number is invalid, it requests again for an offset number
        while offset < 1 or offset > 94:
            offset = int(input("Please enter offset value (1 to 94): "))
        print()
        #Takes each letter, grabs the ASCII character of it, then adds the
        #offset
        for letter in encryption:
            numEncrypted = ord(letter)
            numEncrypted = numEncrypted + offset
            #Makes sure the character doesn't exceed 126 with the offset
            if numEncrypted > 126:
                numEncrypted = numEncrypted - 95
            #Takes the encrypted character and adds it to the encrypted Word
            #Variable
            encryptedWord += chr(numEncrypted)
        #Outputs the encrypted word
        print("Encrypted string:")
        print(encryptedWord)
    
    #Asks the user to input the encrypted word so it may be decrypted
    elif choice == 2:
        decryption = input("Please enter string to decrypt: ")
        offset = int(input("Please enter offset value (1 to 94): "))
        print()
        #Takes the letter, grabs the ASCII of it then removes the offset
        for letter in decryption:
            numDecrypted = ord(letter)
            numDecrypted = numDecrypted - offset
            #Makes sure the character doesn't dip below 32 without the offset
            if numDecrypted < 32:
                numDecrypted = numDecrypted + 95
            #Takes the ASCII numbers and changes them into the original
            #letters
            decryptedWord += chr(numDecrypted)
        #Outputs the decrypted string
        print("Decrypted string:")
        print(decryptedWord)

    #Choice 3 for brute forcing, askes the user for the encrypted word to decrypt              
    elif choice == 3:
        decryption = input("Please enter string to decrypt: ")
        print()
        autoOffset = 1
        #Sets a loop to repeat while the autooffset is less than 95
        while autoOffset < 95:
            #Takes the letter, grabs the ASCII of it then removes the offset
            for letter in decryption:
                numDecrypted = ord(letter)
                numDecrypted = numDecrypted - autoOffset
                #Makes sure the character doesn't dip below 32 without the offset
                if numDecrypted < 32:
                    numDecrypted = numDecrypted + 95
                #Takes the ASCII numbers and changes them into the original
                #letters
                decryptedWord += chr(numDecrypted)
            #Outputs the decrypted string and the offset assigned to it
            print("Offset: ", autoOffset, "= Decrypted string: ", decryptedWord)
            decryptedWord = ''
            autoOffset = autoOffset + 1
    #If choice 4 is chosen, exits the program.    
    elif choice == 4:
        print("Goodbye.")
