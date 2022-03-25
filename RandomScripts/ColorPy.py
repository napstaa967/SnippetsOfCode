import os, typing, sys

reset = False

def init():
    os.system('')

class _Back:
    def from_rgb(self, red, green, blue):
        return f'\x1b[48;2;{red};{green};{blue}m'

    def from_hex(self, hex):
        h = hex.lstrip('#')
        h = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        return f'\x1b[48;2;{h[0]};{h[1]};{h[2]}m'
    RED = '\x1b[48;2;255;0;0m'
    GREEN = '\x1b[48;2;0;255;0m'
    BLUE = '\x1b[48;2;0;0;255m'
    YELLOW = '\x1b[48;2;255;255;0m'
    CYAN = '\x1b[48;2;0;255;255m'
    MAGENTA = '\x1b[48;2;255;0;255m'
    BLACK = '\x1b[48;2;0;0;0m'
    WHITE = '\x1b[48;2;255;255;255m'
    LIGHT_GRAY = '\x1b[48;2;191;191;191m'
    DARK_GRAY = '\x1b[48;2;63;63;63m'
    GRAY = '\x1b[48;2;127;127;127m'
    RESET = '\x1b[49m'

class _Fore:
    def from_rgb(self, red, green, blue):
        return f'\x1b[38;2;{red};{green};{blue}m'

    def from_hex(self, hex):
        h = hex.lstrip('#')
        h = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        return f'\x1b[38;2;{h[0]};{h[1]};{h[2]}m'
    RED = '\x1b[38;2;255;0;0m'
    GREEN = '\x1b[38;2;0;255;0m'
    BLUE = '\x1b[38;2;0;0;255m'
    YELLOW = '\x1b[38;2;255;255;0m'
    CYAN = '\x1b[38;2;0;255;255m'
    MAGENTA = '\x1b[38;2;255;0;255m'
    BLACK = '\x1b[38;2;0;0;0m'
    WHITE = '\x1b[38;2;255;255;255m'
    LIGHT_GRAY = '\x1b[38;2;191;191;191m'
    DARK_GRAY = '\x1b[38;2;63;63;63m'
    GRAY = '\x1b[38;2;127;127;127m'
    RESET = '\x1b[39m'

class _Text:
    BOLD = '\x1b[1m'
    THIN = '\x1b[2m'
    ITALIC = '\x1b[3m'
    UNDERLINE = '\x1b[4m'
    SLOW_BLINK = '\x1b[5m'
    FAST_BLINK = '\x1b[6m'
    INVERT = '\x1b[7m'
    HIDE = '\x1b[8M'
    STRIKE = '\x1b[9m'
    DOUBLE_UNDERLINE = '\x1b[21m'
    SPACING = '\x1b[26m'
    OVERLINED = '\x1b[53m'
    RESET = '\x1b[22m\x1b[23m\x1b[24m\x1b[25m\x1b[27m\x1b[28m\x1b[29m\x1b[50m\x1b[55m'

Reset_All = '\x1b[22m\x1b[23m\x1b[24m\x1b[25m\x1b[27m\x1b[28m\x1b[29m\x1b[39m\x1b[49m\x1b[50m\x1b[55m'
Fore = _Fore()
Back = _Back()
Text = _Text()