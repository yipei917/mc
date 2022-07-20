# -*- coding: utf-8 -*-

from Meta.TypeMeta import PInt, PBool
from Meta.ClassMetaManager import sunshine_class_meta
from Preset.Model import PartBaseMeta

@sunshine_class_meta
class MissionPartMeta(PartBaseMeta):
    CLASS_NAME = 'MissionPart'
    PROPERTIES = {'v_fire': PInt(sort=10000, group='蓝图零件', text='v_PartVariable_1'), 'v_isbig': PBool(sort=10000, group='蓝图零件', text='v_PartVariable_1'), 'v_hurt': PInt(sort=10000, group='蓝图零件', text='v_PartVariable_1')}
