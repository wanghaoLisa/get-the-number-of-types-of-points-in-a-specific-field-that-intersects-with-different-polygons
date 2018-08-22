# get-the-number-of-types-of-points-in-a-specific-field-that-intersects-with-different-polygons
This code is used in QGIS to get the number of types of points in a specific field that intersects with different polygons

First please open the layers of point and polygon in QGIS.

Secondly, run this code first in QGIS.

Thirdly, usage example in qgis:
    statistics_by_type_intersection(point_layer, group_by_attribute, polygon_layer, polygon_attribute)
    statistics_by_type_intersection('landuse_revision', 'LandUseDiv', 'Fremantle_Areas_buffer800m', 'ORIG_FID')
