# -*- coding: utf-8 -*-

from Meta.TypeMeta import PStr
from Meta.ClassMetaManager import sunshine_class_meta
from Preset.Model import PartBaseMeta

@sunshine_class_meta
class npc_namePartMeta(PartBaseMeta):
    CLASS_NAME = 'npc_namePart'
    PROPERTIES = {'v_PartVariable_1': PStr(sort=10000, group='蓝图零件', text='自定义名称')}
