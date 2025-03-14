import secrets
from tkinter import font
import pyfiglet 
import helper 

def xor_cipher(txt_list, key_list): 
    xkey =  helper.get_repeating_key(txt_list, key_list) if len(txt_list) != len(key_list) else key_list   
    xor = []
    for i in range(len(txt_list)):
        xor.append(txt_list[i] ^ xkey[i])
    return bytes(xor)          

def xor_encrypt(): 
    try: 
        xuser_input = helper.xor_str_validation("\nXOR Plaintext: ")
    except ValueError as error: print(error)

    try: 
        xkey_input = helper.xor_str_validation("XOR key: ")   
        xencrypted_text = xor_cipher(list(xuser_input.encode()), xkey_input.encode()) #encode list of bytes 
        print(f"""
=============================================================================
                           ENCRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:                            
              
Ciphertext(hex):     {xencrypted_text.hex()}

=============================================================================

IMPORTANT NOTICE:

- Encrypted XOR output is raw binary data (random bytes), operating on UTF-8 characters.
- Copy-paste the encrypted plaintext (as hex values) for accurate decryption later.
- Ensure the key is handled securely.

=============================================================================\n""") #.hex() = normalize into a copy-able string
        
    except ValueError or IndexError as error: print(error)

def xor_decrypt(): 
    
    while True:
        try: 
            xduser_input = helper.xor_str_validation("\nXOR Ciphertext: ")                                         
            xhex_input = bytes.fromhex(xduser_input)                       #bytes.fromhex() = return from hex to original byte perfectly 
            break                                                          #exit loop if successful                   
        except ValueError:
            print("Please enter valid hex values.")                        #hex must be in even pairs

    while True:
        try:
            xkey_input = helper.xor_str_validation("XOR Key: ").encode()  
            xdecrypted_text = xor_cipher(xhex_input, xkey_input) 
            print(f"""
=============================================================================
                            DECRYPTION SUCCESSFUL 
=============================================================================
              
RESULTS:              
              
Decrypted Text:     {xdecrypted_text.decode(errors="replace")}

=============================================================================

SECURITY NOTE:

- Ensure the decrypted message is handled securely.
- XOR Encryption provides security, but responsibility lies with the user.
- Non UTF-8 characters will be printed as "?"

=============================================================================\n""") 
            #.decode(errors="replace") = validation for non utf-8 characters
            break
        except ValueError as error: print(error) 
    
def print_info():
    print("""\n=============================================================================
          \nVersion 1.0.0\n\nOrigin:

    The XOR encryption algorithm is based on the exclusive OR (XOR) logical operation, 
    a fundamental concept in Boolean algebra by George Boole. It is a simple cipher that 
    applies the exclusive OR (XOR) operation between plaintext and a key, making encryption and 
    decryption identical processes. Gilbert Vernam later built upon this concept in 1917, 
    introducing the Vernam cipher (One-Time Pad), which achieves perfect secrecy by using a truly 
    random, single-use key. Due to its simplicity, efficiency, and reversibility, XOR encryption 
    remains widely used in stream ciphers, data obfuscation, and lightweight encryption schemes.    
          
Use Case:         
          
    A secure file storage system encrypts sensitive text-only files using XOR encryption with 
    a unique key. When accessed, the same key is used to decrypt the file instantly,
    ensuring fast and lightweight security.

Pros:
          
    - Uses basic bitwise operations, making it fast.
    - Encryption and decryption use the same process.
    - Requires minimal computational power, ideal for embedded systems.
          
Cons:

    - Reusing keys makes it vulnerable to known-plaintext attacks.
    - Secure key storage is crucial for maintaining encryption security.
    - Needs additional techniques (e.g., random key generation) for robustness, created as One-Time pad (or Vernam)
            
=============================================================================\n""")

def run_xor():

    banner = pyfiglet.figlet_format("XOR Encryption", font="cybermedium")
    print(f"""\n=============================================================================

{banner}\nSelect an option below to proceed:\n""")

    while True:
        
        choice = helper.get_menu_choice()
        
        if choice == 1:
            xor_encrypt()    
        elif choice == 2:
            xor_decrypt()       
        elif choice == 3: 
            print_info()
        elif choice == 4:
            print("""\nReturning to the Main Menu...\n
=============================================================================\n""")
            break

if __name__ == "_main_":
    run_xor()