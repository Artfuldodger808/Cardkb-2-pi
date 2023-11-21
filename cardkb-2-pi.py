import smbus
import keyboard
import time

# Define I2C address for the CardKB module
CARDKB_I2C_ADDRESS = 0x5F

# Create an instance of the smbus.SMBus class
bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi Model B+

# Define a mapping of ASCII codes to corresponding keyboard characters
ascii_to_key = {
    32: 'Space',
    8: 'Backspace',
    13: 'Enter',
    27: 'Escape',
    44: 'Comma',
    46: 'Fullstop',
    181: 'up',
    182: 'down',
    180: 'left',
    183: 'right',
    
    # Add more mappings for other special characters
    48: '0',
    49: '1',
    50: '2',
    51: '3',
    52: '4',
    53: '5',
    54: '6',
    55: '7',
    56: '8',
    57: '9',
    
    # Add mappings for uppercase letters
    65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G',
    72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N',
    79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U',
    86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z',
    
    # Add mappings for lowercase letters
    97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g',
    104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n',
    111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u',
    118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z',
}

# Function to read a single byte from the CardKB module
def read_byte():
    return bus.read_byte(CARDKB_I2C_ADDRESS)

# Function to translate ASCII codes to keyboard actions
def translate_to_key(action):
    # Ignore unsigned characters (value of zero)
    if action == 0:
        return
    # Check if the ASCII code is in the mapping
    elif action in ascii_to_key:
        keyboard.press_and_release(ascii_to_key[action])
    # Do nothing for unhandled ASCII codes
    
# Main loop
while True:
    try:
        # Read a byte from the CardKB module
        ascii_code = read_byte()

        # Translate the ASCII code to a keyboard action
        translate_to_key(ascii_code)

        # Add a delay to avoid excessive key presses
        time.sleep(0.1)

    except KeyboardInterrupt:
        # Ignore a KeyboardInterrupt (Ctrl+C) and continue with the loop
        pass