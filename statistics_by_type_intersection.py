# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 17:34:58 2018
This code is used in QGIS to get the number of types of points in a specific field that intersects with different polygons
@author: hao
usage example in qgis:
    statistics_by_type_intersection(point_layer, group_by_attribute, polygon_layer, polygon_attribute)
    statistics_by_type_intersection('landuse_revision', 'LandUseDiv', 'Fremantle_Areas_buffer800m', 'ORIG_FID')
"""

import collections



def statistics_by_type_intersection(point_layer, group_by_attribute, polygon_layer, polygon_attribute):
    if QgsMapLayerRegistry.instance().mapLayersByName(point_layer):
        point = QgsMapLayerRegistry.instance().mapLayersByName(point_layer)[0]
    else:
        print('{}{}{}'.format('Layer ', point_layer, ' does not exist.'))
        return False
    index = point.fieldNameIndex(group_by_attribute)
    if index == -1:
        print('{}{}{}'.format('Field ', group_by_attribute, ' does not exist.'))
        return False
    else:
        pass
    if QgsMapLayerRegistry.instance().mapLayersByName(polygon_layer):
        poly = QgsMapLayerRegistry.instance().mapLayersByName(polygon_layer)[0]
    else:
        print('{}{}{}'.format('Layer ', polygon_layer, ' does not exist.'))
        return False
    index = poly.fieldNameIndex(polygon_attribute)
    if index == -1:
        print('{}{}{}'.format('Field ', polygon_attribute, ' does not exist.'))
        return False
    else:
        pass
    list = []
    dic={}
    for b in poly.getFeatures():
        for a in point.getFeatures():
            if a.geometry().intersects(b.geometry()):
                list.append(a[group_by_attribute])
        s=set(list)
        s.remove('else')
        dic[b.id()]=len(s)
    d=collections.OrderedDict(sorted(dic.items()))
    _sum=0
    for k, v in d.items():
        _sum+=v
#        print(k,":", v)
    print('mean:',_sum*1.000/len(d))
