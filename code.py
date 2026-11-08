import time, board, digitalio, usb_hid
from adafruit_hid.mouse import Mouse

# GPO0,GPO1ピンを入力に設定します
tactA = digitalio.DigitalInOut(board.GP0)
tactA.switch_to_input(pull=digitalio.Pull.DOWN)

tactB = digitalio.DigitalInOut(board.GP1)
tactB.switch_to_input(pull=digitalio.Pull.DOWN)

# キーボード・マウスのオブジェクトを作成します
mouse = Mouse(usb_hid.devices)

# 前回値用の変数を初期化します。
beforeA = 0
beforeB = 0

time.sleep(15)  # 15秒待ちます
# カーソルを自動操舵ONOFFアイコンの場所に移動します
mouse.move(238, 150)  # CHCNAV510(238,150) 610(255,172) FJD(265,170) TrimbleGFX750(280，-198）

while True:
    # タクトスイッチA,Bが押されているか取得
    nowA = tactA.value
    nowB = tactB.value

    # タクトスイッチAが押された(立ち上がり)
    if nowA == 1 and beforeA == 0:
        mouse.click(Mouse.LEFT_BUTTON)

    # タクトスイッチBが押された(立ち上がり)
    if nowB == 1 and beforeB == 0:
        mouse.move(0, -90)  # カーソルを塗りつぶしボタンに移動
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(1)
        mouse.move(0, 90)  # カーソルを自動操舵ONOFFアイコンに戻す

    # 前回値として現在のスイッチの状態を保存します。
    beforeA = nowA
    beforeB = nowB