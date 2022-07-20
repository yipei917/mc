# -*- coding: utf-8 -*-

from Preset.Model.PartBase import PartBase
from Preset.Model.GameObject import registerGenericClass

@registerGenericClass('CreatePart')
class CreatePart(PartBase):

    def __init__(self):
        super(CreatePart, self).__init__()
        self.name = '蓝图零件'
        self.description = '蓝图零件'
        self.bpFiles = ['CreatePart.bp']
        self.replicated = []

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
