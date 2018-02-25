# Program that randomizes Kirby: Nightmare in Dream Land for GBA
# Written by Aquova, 2017-2018
# http://github.com/Aquova/KNDL-Rando

from PyQt5 import QtWidgets
import os, random, sys, hashlib
from mainwindow import Ui_MainWindow

VERSION = '0.1.0'

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

class KirbyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(KirbyApp, self).__init__(parent)
        self.setupUi(self)
        self.findROMButton.clicked.connect(self.open_file)
        self.randomizeButton.clicked.connect(self.runRandomizer)
        self.title.setText(self.title.text() + VERSION)

        # Fades out starRodCheck if not clicked
        self.starRodCheck.setEnabled(False)
        self.enemyCheck.toggled.connect(self.starRodCheck.setEnabled)
        self.enemyCheck.toggled.connect(
            lambda checked: not checked and self.starRodCheck.setChecked(False))

    # Opens ROM selector window, clears the previous path text
    def open_file(self):
        self.romDisplay.clear()
        self.rom_file = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", os.path.dirname(__file__), "GBA ROMs (*.gba)")[0]
        if self.rom_file:
            self.romDisplay.setText(self.rom_file)

    def runRandomizer(self):
        try:
            rom = open(self.rom_file, 'rb').read()
            test_hash = hashlib.md5(rom).hexdigest()
            # Checks for the correct ROM
            if test_hash != "35ae64b0f27e60107c14ab956f6cdf70":
                raise HashError("Invalid checksum")
            rom_list = list(rom)

            # Uses given input as seed, else randomly picks a new seed to use
            # AFAIK you can't get what the default seed is, so it needs to be changed to one we know
            KNDL_seed = self.seedValue.text()
            if KNDL_seed == "":
                KNDL_seed = random.randint(0, 999999999)
            random.seed(KNDL_seed)

            if self.enemyCheck.isChecked():
                if self.starRodCheck.isChecked():
                    ability_values.append("19")

                # Gives enemies new abilities based on random selection from file
                for item in ability_locations:
                    address = int(item, 16)
                    new_enemy = random.choice(ability_values)
                    new_enemy = int(new_enemy,16)
                    rom_list[address] = new_enemy

            rom = bytes(rom_list)
            new_rom = open('.'.join(self.rom_file.split(".")[:-1]) + "_" + str(KNDL_seed) + ".gba", 'wb')
            new_rom.write(rom)
            new_rom.close()

            QtWidgets.QMessageBox.about(self, "Success", "Your copy of Nightmare in Dream Land has been randomized. Enjoy!")
        except AttributeError:
            QtWidgets.QMessageBox.about(self, "Error", "Error: Specify a ROM location")
        except FileNotFoundError:
            QtWidgets.QMessageBox.about(self, "Error", "Error: File not found")
        except HashError:
            QtWidgets.QMessageBox.about(self, "Error", "The given file is invalid. Please use a US GBA Kirby: Nightmare in Dream Land ROM.")
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "Error", "Some mysterious error has occurred. Please contact the developers with information about what happened. {}".format(e))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = KirbyApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
