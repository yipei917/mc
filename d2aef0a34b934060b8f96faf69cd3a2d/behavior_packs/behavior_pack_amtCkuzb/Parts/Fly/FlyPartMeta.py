# -*- coding: utf-8 -*-

from Meta.TypeMeta import PInt
from Meta.ClassMetaManager import sunshine_class_meta
from Preset.Model import PartBaseMeta

@sunshine_class_meta
class FlyPartMeta(PartBaseMeta):
    CLASS_NAME = 'FlyPart'
    PROPERTIES = {'v_fly_to': PInt(sort=10000, group='蓝图零件', text='v_PartVariable_1')}
