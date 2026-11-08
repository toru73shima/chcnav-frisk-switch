# CHCNAV フリスクスイッチで自動操舵ON/OFF（RP2040-Zero）

北海道の島貫農園さんのブログ記事を参考に作成した、RP2040-Zeroを用いたCHCNAV自動操舵用のフリスクスイッチ（マウスエミュレーター）のプログラムとメモです。

- 記事元: [島貫農園ブログ](https://www.shimanuki-farm.net/archives/2159/)
- 使用マイコン: RP2040-Zero (CircuitPython)

## 必要なパーツ・リンク
- マルチコアボードモジュール RP2040-Zero
- 押しボタンスイッチ（キャップ付き）
- ユニバーサル基板
- はんだメッキ線 0.6mm

## 参考リンク
- [CircuitPython ファームウェア](https://circuitpython.org/board/raspberry_pi_pico/)
- [Adafruit HID ライブラリ](https://docs.circuitpython.org/projects/hid/en/latest/)
- [Mu Editor](https://codewith.mu/en/download)