# Trade Viewer

Trade viewer is a GUI application written in PyQt5, to visualize crypto currency trading from Bitmex websocket api. Currently the app supports following topics:
* topic: instrument, action: update
* topic: orderbookL2, action: insert

https://www.bitmex.com/app/wsAPI#subscriptions

![Trade Viewer](trade_viewer.gif)

## Getting started

```
pip install -r requirements.txt
python main.py

```
