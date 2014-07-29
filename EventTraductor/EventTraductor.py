import gtk
import pygame

keys = {
    "0": "K_0", "1": "K_1", "2": "K_2", "3": "K_3", "4": "K_4", "5": "K_5",
    "6": "K_6", "7": "K_7", "8": "K_8", "9": "K_9",
    "KP_0": "K_KP0", "KP_1": "K_KP1", "KP_2": "K_KP2", "KP_3": "K_KP3",
    "KP_4": "K_KP4", "KP_5": "K_KP5", "KP_6": "K_KP6", "KP_7": "K_KP7",
    "KP_8": "K_KP8", "KP_9": "K_KP9",
    "a": "K_a", "b": "K_b", "c": "K_c", "d": "K_d", "e": "K_e", "f": "K_f",
    "g": "K_g", "h": "K_h", "i": "K_i", "j": "K_j", "k": "K_k", "l": "K_l",
    "m": "K_m", "n": "K_n", "o": "K_o", "p": "K_p", "q": "K_q", "r": "K_r",
    "s": "K_s", "t": "K_t", "u": "K_u", "v": "K_v", "w": "K_w", "x": "K_x",
    "y": "K_y", "z": "K_z",
    "Up": "K_UP", "Down": "K_DOWN", "Right": "K_RIGHT", "Left": "K_LEFT",
    "Escape": "K_ESCAPE", "space": "K_SPACE", "Return": "K_RETURN",
    "Control_L": "K_LCTRL", "Control_R": "K_RCTRL",
    }


def KeyPressTraduce(event):
    nombre = gtk.gdk.keyval_name(event.keyval)
    unic = str.lower(nombre)
    if nombre in keys.keys():
        evt = pygame.event.Event(pygame.KEYDOWN,
            key=getattr(pygame, keys[nombre]), unicode=unic, mod=None)
        pygame.event.post(evt)


def KeyReleaseTraduce(event):
    nombre = gtk.gdk.keyval_name(event.keyval)
    unic = str.lower(nombre)
    if nombre in keys.keys():
        evt = pygame.event.Event(pygame.KEYUP,
            key=getattr(pygame, keys[nombre]), unicode=unic, mod=None)
        pygame.event.post(evt)


def MousemotionTraduce(event):
    x, y, state = event.window.get_pointer()
    rel = (x, y) # = (x - self.mouse_pos[0], y - self.mouse_pos[1])
    mouse_pos = (int(x), int(y))
    button_state = [
        state & gtk.gdk.BUTTON1_MASK and 1 or 0,
        state & gtk.gdk.BUTTON2_MASK and 1 or 0,
        state & gtk.gdk.BUTTON3_MASK and 1 or 0,
        ]
    evt = pygame.event.Event(pygame.MOUSEMOTION,
        pos=mouse_pos, rel=rel, buttons=button_state)
    pygame.event.post(evt)


def Traduce_button_press_event(event):
    evt = pygame.event.Event(pygame.MOUSEBUTTONDOWN,
        button=event.button, pos=(int(event.x), int(event.y)))
    pygame.event.post(evt)


def Traduce_button_release_event(event):
    evt = pygame.event.Event(pygame.MOUSEBUTTONUP,
        button=event.button, pos=(int(event.x), int(event.y)))
    pygame.event.post(evt)


'''
def Traduce_posiciones(VA, VH):
    eventos= pygame.event.get(pygame.MOUSEBUTTONDOWN)
    for event in eventos:
        x, y = event.pos
        xx= x/VA
        yy= y/VH
        event_pos= (xx, yy)
    for event in eventos:
        evt = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos= event_pos, button=event.button)
        pygame.event.post(evt)

    eventos= pygame.event.get(pygame.MOUSEMOTION)
    for event in eventos:
        x, y = event.pos
        xx= x/VA
        yy= y/VH
        event_pos= (xx, yy)
    for event in eventos:
        evt = pygame.event.Event(pygame.MOUSEMOTION, pos= event_pos, rel=event.rel, buttons=event.buttons)
        pygame.event.post(evt)
'''
