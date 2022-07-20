# -*- coding: utf-8 -*-

from common.mod import Mod


@Mod.Binding(name="Script_NeteaseModafitLOTn", version="0.0.1")
class Script_NeteaseModafitLOTn(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModafitLOTnServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModafitLOTnServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModafitLOTnClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModafitLOTnClientDestroy(self):
        pass
