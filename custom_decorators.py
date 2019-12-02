from functools import wraps


# 0=reset
# 1=bold
# 4=underline
# 30-37=normal fg colors
# 40-47=normal bg colors
# 90-97=bright fg colors
# 100-107=bright bg colors


def color_console(color):
    def funct(func):
        @wraps(func)
        def print_in_color(*args, **kwargs):
            print(get_color_string(color))
            try:
                func(*args, **kwargs)
            finally:
                print(get_color_string())

        return print_in_color
    return funct


def get_color_string(color='reset'):
    color_dict={
        'red':"\u001b[31m",
        'bred':"\u001b[91m",
        'green':"\u001b[32m",
        'yellow':"\u001b[33m",
        'magenta':"\u001b[35m",
        'reset':"\u001b[0m"
    }
    return color_dict[color]

def get_bgcolor_string(color='reset'):
    color_dict={
        'red':"\u001b[41m",
        'green':"\u001b[42m",
        'yellow':"\u001b[43m",
        'magenta':"\u001b[45m",
        'reset':"\u001b[0m"
    }
    return color_dict[color]

def get_text_style_string(style='reset'):
    color_dict={
        'bold':"\u001b[1m",
        'underline':"\u001b[4m",
        'reversed':"\u001b[7m",
        'reset':"\u001b[0m"
    }
    return color_dict[style]

def cursor_move(direction,n):
    color_dict={
            'up': '\u001b[{n}A'.format(n=n),
            'down': '\u001b[{n}B'.format(n=n),
            'right': '\u001b[{n}C'.format(n=n),
            'left': '\u001b[{n}D'.format(n=n)
    }
    return color_dict[direction]

def change_color(color='reset'):
    print(get_color_string(color),end="")

def delete_prev_line(n=1):
    for i in range(n):
        print(cursor_move('up',1),end="")
        print('\u001b[{n}K'.format(n=2),end="")
        print(cursor_move('left',1000),end="")
        