'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    5 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    import string
    import math

    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)


    if letter == " ":
        return(" ")
    
    elif shift == _:
        return(letter)

    else:
        i = alphabet_list.index(letter) #position of letter

        if (i+shift) < len(alphabet_list):
            return(alphabet_list[i+shift])

        elif (i+shift) >= len(alphabet_list):
            i = i - len(alphabet_list)
            x = shift/len(alphabet_list)
            z = math.ceil(x)
            alphabet_list = alphabet_list*z
            return(alphabet_list[i+shift])

        
def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   
    import string
    import math

    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)

    message_list = list(message)
    i = 0
    max = len(message_list)

    caesar_list = list()

    while i < max:
        letter = message_list[i]

        if letter == " ":
            caesar_list.append(" ")
            i += 1   

        elif letter != " ":
            j = alphabet_list.index(letter)

            if (j+shift) < len(alphabet_list):
                caesar_list.append(alphabet_list[j+shift])
                i += 1  

            elif (j+shift) >= len(alphabet_list):
                x = (j+shift)/len(alphabet_list)
                z = math.ceil(x)
                j = j - len(alphabet_list)
                alphabet_list2 = alphabet_list*z
                caesar_list.append(alphabet_list2[j+shift])
                i += 1 

    return("".join(caesar_list))


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    import string
    import math

    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)

    if letter == " ":
        return(" ")

    elif letter_shift == _:
        return(letter)

    else:
        i = alphabet_list.index(letter) #position of letter
        j = alphabet_list.index(letter_shift) #position of letter_shift

        if (i+j) < len(alphabet_list):
            return(alphabet_list[i+j])

        elif (i+j) >= len(alphabet_list):
            i = i - len(alphabet_list)
            return(alphabet_list[i+j])

        
def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    15 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    import string
    import math

    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)

    message_list = list(message)

    k = 0
    key_ext = list()

    if len(key) < len(message):
        key_multiplier = math.ceil(len(message)/len(key))
        key_2 = key*key_multiplier
        while k != len(message):
            key_ext.append(key_2[k])
            k += 1
        key_list = key_ext
    
    else:
        key_list = list(key)

        
    cipher_list = list()
    i = 0
    max = len(message_list)

    while i < max:
        letter = message_list[i]
        shift_key = key_list[i]

        if letter == " ":
            cipher_list.append(" ")
            i += 1   

        elif letter != " ":
            x = alphabet_list.index(letter) #position of letter in message
            y = alphabet_list.index(shift_key) #position of shift_letter in key

            if (x+y) < len(alphabet_list):
                cipher_list.append(alphabet_list[x+y])
                i += 1  

            elif (x+y) >= len(alphabet_list):
                x = x - len(alphabet_list)
                cipher_list.append(alphabet_list[x+y])
                i += 1  

    return("".join(cipher_list))


def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    
    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    import string

    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)

    is_multiple = len(message) % shift

    if is_multiple != 0:

        message_list = list(message)
        m = len(message_list)

        while (m % shift)  != 0:
            message_list.append("_")
            m += 1
            new_message = message_list

    else:
        new_message = list(message)

    i = 0
    scytale = list()

    while i < len(new_message):
        cipher = (i // shift) + (len(new_message) // shift) * (i % shift)

        if cipher == "_":
            scytale.append("_")
            i += 1

        else:
            s_letter = new_message[cipher]
            scytale.append(s_letter)
            i += 1  

    return("".join(scytale))

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    i = 0
    message_list = list(message)
    scytale_decipher = list()

    while i < len(message):
        multiple = int(len(message)/shift)  #5

        de_cipher = (i // multiple) + (len(message) // multiple) * (i % multiple)

        sd_letter = message_list[de_cipher]
        scytale_decipher.append(sd_letter)
        i += 1  

    return("".join(scytale_decipher))