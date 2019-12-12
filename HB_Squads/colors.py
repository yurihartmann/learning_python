colors_availables = ('yellow', 'green', 'red', 'blue', 'purple', 'white')
bg_availables = ('yellow', 'green', 'red', 'blue', 'purple')


def key_color(name_color):

    name_color = name_color.strip().lower()

    if name_color not in colors_availables:
        raise Exception('Color is not avaliable, type one this', colors_availables)

    if name_color == 'yellow':
        return '33'
    elif name_color == 'green':
        return '32'
    elif name_color == 'red':
        return '31'
    elif name_color == 'blue':
        return '34'
    elif name_color == 'purple':
        return '35'
    elif name_color == 'white':
        return ''    


def key_bg(name_bg_color):

    name_bg_color = name_bg_color.strip().lower()

    if name_bg_color not in bg_availables:
        raise Exception('Backgroud is not avaliable, type one this', bg_availables)

    if name_bg_color == 'yellow':
        return '43'
    elif name_bg_color == 'green':
        return '42'
    elif name_bg_color == 'red':
        return '41'
    elif name_bg_color == 'blue':
        return '44'
    elif name_bg_color == 'purple':
        return '45' 

    
def color(text, color):

    color = color.strip().lower()    
    
    if color not in colors_availables:
        raise Exception('Color is not avaliable, type one this', colors_availables)

    return '\033[1;'+ key_color(color)+ 'm' + text + '\033[m'
    
    
def color_bg(text, color, bg):

    color = color.strip().lower()
    bg = bg.strip().lower() 

    if color not in colors_availables:
        raise Exception('Color is not avaliable, type one this', colors_availables)
    if bg not in bg_availables:
        raise Exception('Backgroud is not avaliable, type one this', bg_availables)

    return '\033[1;'+ key_color(color) + ';' +  key_bg(bg) + 'm' + text + '\033[m'

