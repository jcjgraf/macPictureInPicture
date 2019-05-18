# PicInPic - Picture In Picture Mode for all Browsers

This app provides an easy to use 'picture in picture' functionality for any browser for macOS. Inspired by Safari's picture in picture mode.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

This app requires [Python 3.x](https://www.python.org/downloads/mac-osx/) as well as the VLC player.

Get the current VLC version with `brew` or from the [official website](https://www.videolan.org/vlc/).
```
brew cask install vlc
```

Make VLC stay always on the top: VLC -> Preferences -> Video -> enable 'Float on top'

For building the app [py2app](https://pypi.org/project/py2app/) is required, which can be installed with `pip`.
```
pip install -U py2app
```

At the first run you have to grant `Accessibility` privileges to `PicInPic.app`

### Build

Build the app
```
python3 setup.py py2app -A

```

Launch it from `./dist/main.app`

### Usage

To open a video which is currently open in the topmost firefox tab, click on 'PicInPic' -> 'Open in VLC' in the statusbar.
