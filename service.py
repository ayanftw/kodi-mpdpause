#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc
import xbmcaddon
from mpd import MPDClient

settings = xbmcaddon.Addon(id='service.xbmc.mpdpause')


def mpd_pause():
    mpd_host = settings.getSetting("mpd_host")
    mpd_pass = settings.getSetting("mpd_pass")
    mpd_port = int(settings.getSetting("mpd_port"))

    client = MPDClient()
    client.timeout = 10
    client.idletimeout = None
    client.connect(mpd_host, mpd_port)
    if mpd_pass:
        client.password(mpd_pass)

    status = client.status()
    if int(status.get('playlistlength', '0')) > 0:
        state = status.get('state')
        if state == 'play':
            client.pause()
    client.close()
    client.disconnect()


class MyPlayer(xbmc.Player):

    def __init__(self):
        xbmc.Player.__init__(self)

    def onPlayBackStarted(self):
        xbmc.log("PLAY!!!!")
        mpd_pause()

    def onPlayBackResumed(self):
        xbmc.log("RESUME!!!")
        mpd_pause()

player = MyPlayer()


while(1):
    xbmc.sleep(1000)
