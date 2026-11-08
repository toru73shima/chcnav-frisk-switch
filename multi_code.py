import time, board, digitalio, usb_hid
from adafruit_hid.mouse import Mouse


def move_and_click(mouse, x, y, click=True):
    mouse.move(x, y)
    if click:
        mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(1)


tact_pins = [board.GP0, board.GP1, board.GP3, board.GP4, board.GP5, board.GP6]
tact_switches = [digitalio.DigitalInOut(pin) for pin in tact_pins]
for tact in tact_switches:
    tact.switch_to_input(pull=digitalio.Pull.DOWN)

mouse = Mouse(usb_hid.devices)

time.sleep(15)
move_and_click(mouse, 238, 150, click=False)

before_states = [0] * len(tact_pins)

while True:
    for i, tact in enumerate(tact_switches):
        now_state = tact.value
        before_state = before_states[i]

        if now_state == 1 and before_state == 0:
            if i == 0:
                move_and_click(mouse, 0, 0)
            elif i == 1:
                move_and_click(mouse, 0, -90)
                move_and_click(mouse, 0, 90, click=False)
            elif i == 2:
                move_and_click(mouse, -110, 0)
                move_and_click(mouse, 110, 0, click=False)
            elif i == 3:
                move_and_click(mouse, -155, 0)
                move_and_click(mouse, 155, 0, click=False)
            elif i == 4:
                move_end = (-400, -90)
                move_and_click(mouse, -400, -90)
                move_and_click(mouse, 400, 90, click=False)
            elif i == 5:
                move_and_click(mouse, -210, -110)
                move_and_click(mouse, 210, 110, click=False)

        before_states[i] = now_state