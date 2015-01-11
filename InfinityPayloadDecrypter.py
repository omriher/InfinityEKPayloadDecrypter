import sys

table = []
decoded_payload = []
input_file = ""
output_file = ""
key = ""

def create_00_FF_array():
    print "[+] Creating 00-FF array"
    for i in range(0,256):
        table.append(i)

def create_initial_s_box():
    print "[+] Creating s-box array"
    ECX = 0
    BL = 0
    EBP = len(key)
    for i in range(0,256):
        AL = ECX                # AL and ECX are byte counters
        DL = (int)(AL % EBP)    # DL is AL modulo key length (key index)

        BL = BL + ord(key[DL])  # Sums BL with KEY's current index
        BL = BL % 256           # Makes sure BL stay's within boundaries ( <= FF)
        AH = table[ECX]         # AH is s-box current location

        BL = BL + AH            # Sums BL with s-box's current value
        BL = BL % 256           # Makes sure BL stay's within boundaries ( <= FF)
        AL = table[BL]          # AL is a position in the table set by BL

        table[ECX] = AL         # Swaps positions in the table
        table[BL] = AH

        ECX += 1

def decrypt():
    print "[+] Decrypting Payload"
    f = open(input_file, 'rb')
    try:
        ECX = 0
        DL = 0
        byte = f.read(1)
        while byte != "":
            EDI = ECX           # EDI and ECX are byte counters
            EDI += 1

            EDI = EDI % 256     # Makes sure EDI stay's within boundaries ( <= FF)

            AL = table[EDI]     # AL is current location in the table

            DL = DL + AL        # Sums DL with current location in the table
            DL = DL % 256       # Makes sure DL stay's within boundaries ( <= FF)

            BL = table[DL]      # Takes the value from table when DL says

            table[EDI] = BL     # Swaps (AGAIN) position in table
            table[DL] = AL

            AL = AL + BL        # Sums AL with BL [this process is the stream decoding]
            AL = AL % 256       # Makes sure AL stay's within boundaries ( <= FF)

            AL = table[AL]      # Takes new position from the table
            decoded_payload.append(ord(byte) ^ AL)          # XOR with new position

            ECX += 1
            byte = f.read(1)
    finally:
        f.close()

def save_to_file():
    print "[+] Writing Decrypted File to disk"
    with open (output_file, "wb") as out:
        bytes = bytearray(decoded_payload)
        out.write(bytes)

def main():
    create_00_FF_array()
    create_initial_s_box()
    decrypt()
    save_to_file()
    print "Done! Exiting."

if __name__ == '__main__':
    print "Infinity Payload Decrypter"
    if len(sys.argv) < 4:
        print "Usage: InfinityPayloadDecrypter.py <encoded_file> <output_file> <key>"
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        key = sys.argv[3]
        main()
