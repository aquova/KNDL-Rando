# Program that randomizes the abilities of swallowed enemies in Kirby: Nightmare in Dream Land
# Written by Aquova, 2017-2018
# Usage: python3 KNDL-Simple.py
# http://github.com/Aquova/KNDL-Rando

import os, random, hashlib

VERSION = "0.1.0 CLI"

# Valid byte values for Kirby's ability
ability_values = ["00","01","02","03","04","05","06","07","08","09","0A","0B","0C",
                "0D","0E","0F","10","11","12","13","14","15","16","17","18"]

# ROM locations of enemy abilities
ability_locations = ["7417C4", "7429F4", "740C38", "743344", "742A20", "7417F0", "742A4C",
                     "7418A0", "740C64", "740C90", "7418F8", "742B28", "741924", "741950",
                     "740CE8", "740D14", "741A58", "741A84", "740D6C", "740D98", "740DC4"]

# Creating a custom exception, how fancy
class HashError(Exception):
    pass

if __name__ == "__main__":
    try:
        print("Thanks for using the Kirby: Nightmare in Dream Land Randomizer, version " + VERSION)
        rom_name = input("Give the name of the ROM (must be in same folder as this program): ")
        rom_name = os.path.join(os.path.dirname(__file__), rom_name)

        # If seed is blank, generate a random seed
        # Python will generate one by default, but you can't access it
        KNDL_seed = input("Now give a seed to be used (or leave blank): ")
        if KNDL_seed == "":
            KNDL_seed = random.randint(0, 999999999)
        random.seed(KNDL_seed)

        rom = open(rom_name, 'rb').read()
        test_hash = hashlib.md5(rom).hexdigest()
        if (test_hash != "35ae64b0f27e60107c14ab956f6cdf70"):
            raise HashError("Invalid checksum")
        rom_list = list(rom)

        star_rod = input("Should the Star Rod be an available ability? Warning: Very Experimental. (Y/N): ")

        if star_rod.upper() == 'Y':
            # Add 0x19, the value of Star Rod
            ability_values.append("19")

        # Gives enemies new abilities based on random selection from file
        for item in ability_locations:
            address = int(item, 16)
            rand_ind = random.randint(0,len(ability_values) - 1)
            new_enemy = ability_values[rand_ind]
            new_enemy = int(new_enemy,16)
            rom_list[address] = new_enemy

        rom = bytes(rom_list)
        new_rom = open('.'.join(rom_name.split(".")[:-1]) + "_" + str(KNDL_seed) + ".nes", 'wb')
        new_rom.write(rom)
        new_rom.close()

        input("Your copy of Kirby: Nightmare in Dream Land has been randomized, enjoy! Press Enter to close.")

    except FileNotFoundError:
        input("No file of that name was found. Make sure your .gba ROM is in the same folder as this program. Press Enter to close.")
    except HashError:
        input("The file given is invalid. Please use a US NES Kirby: Nightmare in Dream Land ROM. Press Enter to close.")
    except Exception as e:
        print("ERROR: {}".format(e))
        input("Press Enter to close.")
