# Исследование скачанного файла фигур стр.69
import osgeo.ogr

shapefile = osgeo.ogr.Open('Data/Task1/tl_2014_us_state.shp')

layer =shapefile.GetLayer(0)
feature = layer.GetFeature(12)
print(f'Геообъект № {12} имеет следующие атрибуты:')
print()

attributes = feature.items()
for key,value in attributes.items():
    print(f'{key} = {value}')

geometry = feature.GetGeometryRef()
geometryName = geometry.GetGeometryName()

print()
print(f'Геометрия заданного геообъекта представляет  собой {geometryName}')