import time
import os
import urllib
from subprocess import Popen, PIPE
import rumps

rumps.debug_mode(True)

class PicInPic(rumps.App):

	def __init__(self):
		super(PicInPic, self).__init__('PicInPic')
		self.menu = ['Open in VLC']

	def getCurrentUrl(self):
		script = '''
		    tell application "Firefox" to activate
			tell application "System Events"
				keystroke "l" using {command down}
				keystroke "c" using {command down}
				do shell script "pbpaste"
			end tell
		'''

		proc = Popen(['/usr/bin/osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
		stdout, stderr = proc.communicate(script)
		return stdout

	@rumps.clicked('Open in VLC')
	def openOverlay(self, _):
		os.system("/Applications/VLC.app/Contents/MacOS/VLC " + self.getCurrentUrl())

if __name__ == '__main__':
	PicInPic().run()