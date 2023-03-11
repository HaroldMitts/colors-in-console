# list of colors
colors = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white" ]

# list of color codes
codes = [
    "0;30", "0;31", "0;32", "0;33", "0;34", "0;35", "0;36", "0;37",
    "1;30", "1;31", "1;32", "1;33", "1;34", "1;35", "1;36", "1;37" ]

# dictionary of colors and codes
color_codes = dict(zip(colors, codes))

# function to print colored text
def print_color(text, color, bold=False):
    if bold:
        bold_text = "\033[1m" + text + "\033[0m"
    else:
        bold_text = text
    color_code = color_codes[color]
    print("\033[" + color_code + "m" + bold_text + "\033[0m")


# print colored text
print_color("Hello World!", "red", bold=False)

# print bold red text
print_color("Hello World!", "red", bold=True)

def print_multicolor(text, color):
    color_code = color_codes[color]
    print("\033[" + color_code + "m" + text + "\033[0m", end="")

# print multiple colors on the same line using escape sequences
print("\033[31mred\033[0m and \033[34mblue\033[0m")

# print multiple colors on the same line using function
print_multicolor("red", "red") 
print_multicolor(" and ", "black")
print_multicolor("blue", "blue")
print()

# basic hard code color codes for text
print("\033[32mThis text is green via color code 0 32\033[0m")
print("\033[31mThis text is red via color code 0 31\033[0m")