# A utility to convert 24-bit RGB values into 2 byte GBA values
import sys

def main():
    rawRGB = input("Give me an RGB color to convert, separated by commas: ")
    try:
        RGB24 = rawRGB.split(",")
        BGR15 = [round(int(x) * 31 / 255) for x in RGB24]
        byteValue = (BGR15[2] << 10) + (BGR15[1] << 5) + BGR15[0]
        print(hex(byteValue))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        print("Press Ctrl-C to quit.")
        print("Keep in mind that all bytes need to be reversed for GBA.")
        while(True):
            main()
    except KeyboardInterrupt:
        sys.exit(0)
