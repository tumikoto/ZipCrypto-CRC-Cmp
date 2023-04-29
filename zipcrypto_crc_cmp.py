#
# Script to ID plaintext contents of text file in a ZipCrypto'd ZIP via the CRC32 in order to conduct a subsequent KPA
# python zipcrypto_crc_cmp.py <crc_32> wordlist.txt
#

import binascii
import sys


def main():
    # Get the CRC32 value from the command-line argument
    target_crc32 = sys.argv[1].upper()
    # Get the filename of the list of strings from the command-line argument
    filename = sys.argv[2]
    # Open the file and read the contents into a list of strings
    with open(filename, 'r') as f:
        strings = f.read().splitlines()
    print(f"\nLoaded {len(strings)} strings from wordlist\n")
    # Print table headers
    print(f"CRC32{' '*11}STRING")
    print(f"-----{' '*11}------")
    for s in strings:
        crc32 = str(hex(binascii.crc32((s + "\n").encode())))[2:].upper()
        # Pad the output as needed
        if len(crc32) == 6:
            print(f"{crc32}\t\t{s}")
        elif len(crc32) == 7:
            print(f"{crc32} \t{s}")
        else:
            print(f"{crc32}\t{s}")
        if crc32 == target_crc32:
            print("\nMatch found!\n")
            return
    # End of loop reached with no match
    print("\nCRC match not found in wordlist\n")


if __name__ == '__main__':
    main()
