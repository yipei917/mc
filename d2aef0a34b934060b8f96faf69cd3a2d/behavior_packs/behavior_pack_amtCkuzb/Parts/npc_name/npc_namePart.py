# -*- coding: utf-8 -*-

from Preset.Model.PartBase import PartBase
from Preset.Model.GameObject import registerGenericClass

@registerGenericClass('npc_namePart')
class npc_namePart(PartBase):

    def __init__(self):
        super(npc_namePart, self).__init__()
        self.name = '蓝图零件'
        self.description = '蓝图零件'
        self.bpFiles = ['npc_namePart.bp']
        self.replicated = []
        self.v_PartVariable_1 = ''

    def DestroyServer(self):
        return PartBase.DestroyServer(self)

    def InitClient(self):
        return PartBase.InitClient(self)

    def DestroyClient(self):
        return PartBase.DestroyClient(self)

    def TickServer(self):
        return PartBase.TickServer(self)

    def InitServer(self):
        return PartBase.InitServer(self)

    def TickClient(self):
        return PartBase.TickClient(self)
