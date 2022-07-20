# -*- coding: utf-8 -*-

from common.mod import Mod


@Mod.Binding(name="Script_NeteaseModV7K3ql6C", version="0.0.1")
class Script_NeteaseModV7K3ql6C(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModV7K3ql6CServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModV7K3ql6CServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModV7K3ql6CClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModV7K3ql6CClientDestroy(self):
        pass
