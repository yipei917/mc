# -*- coding: utf-8 -*-

from Preset.Model.PartBase import PartBase
from Preset.Model.GameObject import registerGenericClass

@registerGenericClass('MissionPart')
class MissionPart(PartBase):

    def __init__(self):
        super(MissionPart, self).__init__()
        self.name = '蓝图零件'
        self.description = '蓝图零件'
        self.bpFiles = ['MissionPart.bp']
        self.replicated = ['v_location']
        self.v_fire = 0
        self.v_isbig = False
        self.v_hurt = 0

    def TickClient(self):
        return PartBase.TickClient(self)

    def DestroyServer(self):
        return PartBase.DestroyServer(self)

    def TickServer(self):
        return PartBase.TickServer(self)

    def InitClient(self):
        return PartBase.InitClient(self)

    def DestroyClient(self):
        return PartBase.DestroyClient(self)

    def ProjectileDoHitEffectEvent(self, *args, **kwargs):
        pass

    def PlayerHurtEvent(self, *args, **kwargs):
        pass

    def f_small(self, *args, **kwargs):
        pass

    def f_boom(self, *args, **kwargs):
        pass

    def f_fire(self, *args, **kwargs):
        pass

    def f_big(self, *args, **kwargs):
        pass

    def f_shoot(self, *args, **kwargs):
        pass
