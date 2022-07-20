# -*- coding: utf-8 -*-

from Preset.Model.PartBase import PartBase
from Preset.Model.GameObject import registerGenericClass

@registerGenericClass('FlyPart')
class FlyPart(PartBase):

    def __init__(self):
        super(FlyPart, self).__init__()
        self.name = '蓝图零件'
        self.description = '蓝图零件'
        self.bpFiles = ['FlyPart.bp']
        self.replicated = ['v_fly_to']
        self.v_fly_to = 0

    def InitServer(self):
        return PartBase.InitServer(self)

    def TickClient(self):
        return PartBase.TickClient(self)

    def DestroyServer(self):
        return PartBase.DestroyServer(self)

    def InitClient(self):
        return PartBase.InitClient(self)

    def DestroyClient(self):
        return PartBase.DestroyClient(self)

    def TickServer(self):
        return PartBase.TickServer(self)

    def f_fly(self, *args, **kwargs):
        pass

    def f_shoot(self, *args, **kwargs):
        pass
