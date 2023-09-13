# Исследование скачанного файла фигур стр.68
import osgeo.ogr

shapefile = osgeo.ogr.Open('Data/Task1/tl_2014_us_state.shp')
numLayers = shapefile.GetLayerCount()
print("Файл фигур содержит {} слой(-ев)".format(numLayers))
print('- - - - - - - - - -')

for layerNum in range(numLayers):
    layer = shapefile.GetLayer(layerNum)
    spatialRef = layer.GetSpatialRef().ExportToProj4()
    numFeatures = layer.GetFeatureCount()
    print("Слой {} имеет пространственную привязку {}".format(layerNum, spatialRef))
    print('- - - - - - - - - -')
    print("Слой {} содержит {} геообъектов".format(layerNum, numFeatures))
    print('- - - - - - - - - -')

    for featureNum in range(numFeatures):
        feature = layer.GetFeature(featureNum)
        featureName = feature.GetField("NAME")

        print("Геообъект {} называется {}".format(featureNum, featureName))

