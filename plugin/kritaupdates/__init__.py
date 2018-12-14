from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from krita import *
from .requests import requests
import re
import webbrowser


def downloadLatestVersion(ver):
	webbrowser.open('https://download.kde.org/stable/krita/%s/krita-x64-%s-setup.exe' % ((ver,)*2))

def getLatestVersion():
	ver_list = re.findall('\d+\.\d+\.\d+', requests.get('https://download.kde.org/stable/krita/').content)
	return '.'.join([str(n) for n in sorted([[int(v) for v in ver.split('.')] for ver in ver_list]).pop()])

def checkForUpdates():
	current_version = Krita.instance().version()
	latest_version = getLatestVersion()

	if current_version == latest_version:
		return

	response = QMessageBox.question(QWidget(),
		'',
		'Version '+current_version+' is outdated. A new version, '+latest_version+', is available, would you like to download it?',
		QMessageBox.Yes, QMessageBox.No)

	if response == QMessageBox.Yes:
		downloadLatestVersion(latest_version)

checkForUpdates()