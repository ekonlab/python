__author__ = 'albertogonzalez'




# from lxml import objectify
# import pprint
# import pandas as pd
#
# path = 'http://www.dgt.es/images/Tramos_INVIVE_20160501_v4.xml'
# xml = objectify.parse(path)
# root = xml.getroot()
# provincias = root.PROVINCIA
# for provincia in provincias:
#     pprint.pprint(provincia.NOMBRE)
#     for carretera in provincia.CARRETERA:
#         print("Carretera " + carretera.DENOMINACION)
#         for radar in carretera.RADAR:
#             print("Punto inicial: " + str(radar.PUNTO_INICIAL.LATITUD) + ", " + str(radar.PUNTO_INICIAL.LONGITUD))
#             print("Punto final: " + str(radar.PUNTO_FINAL.LATITUD) + ", " + str(radar.PUNTO_FINAL.LONGITUD))
#


###########################################################################


from lxml import objectify
import pprint
import pandas as pd

# Read Data
path = 'http://www.dgt.es/images/Tramos_INVIVE_20160501_v4.xml'

# Objectify Data
xml = objectify.parse(path)

# Get Root of object
root = xml.getroot()
print root

# Loop to get geo data (Raiz - Provincia - Carretera - Radar)

provincias = root.PROVINCIA

for provincia in provincias:
    for carretera in provincia.CARRETERA:
        car = str(carretera.DENOMINACION)
        for radar in carretera.RADAR:
            punto_inicial_lon = str(radar.PUNTO_INICIAL.LONGITUD)
            punto_inicial_lat = str(radar.PUNTO_INICIAL.LATITUD)
            punto_final_lon = str(radar.PUNTO_FINAL.LONGITUD)
            punto_final_lat = str(radar.PUNTO_FINAL.LATITUD)
            df = pd.DataFrame([car,punto_inicial_lon,punto_inicial_lat,punto_final_lon,punto_final_lat])
            df_1 = df.transpose()
            df_1.columns = ["carretera","init_lon","init_lat","end_lon","end_lat"]
            print df_1
            #print df_1
            #df_1.to_csv("loco.csv", sep = ',')







###########################################################################

































































