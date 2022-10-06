import pandas as pd
import matplotlib as plt
from datetime import timedelta
data_gps = pd.read_csv('data7.csv',parse_dates=['fechaMensaje'])
fallas = pd.read_csv('Historico De Respuestos.csv' ,parse_dates=['FECHASOLICITUD','FECHAENTREGA'])
fallas['FECHASOLICITUD'] = pd.to_datetime(fallas.FECHASOLICITUD, format="%Y-%m-%d")
fallas['FECHAENTREGA'] = pd.to_datetime(fallas.FECHAENTREGA, format="%Y-%m-%d")
data_gps['fechaMensaje'] = pd.to_datetime(data_gps.fechaMensaje, format="%Y-%m-%d")
data_gps['fechaMensaje'] = data_gps['fechaMensaje'].dt.date
#data_gps['fechaMensaje'] = data_gps['fechaMensaje'].dt.strftime('%Y-%m-%d')
data_gps.sort_values(by=['placa','fechaMensaje'], inplace=True)
placa_modelo = pd.read_csv('placa_modelo.csv')
def listToString(s):
   
    # initialize an empty string
    str1 = ""
   
    # traverse in the string 
    for ele in s:
        str1 += str(ele)
        str1 += ',' 
   
    # return string 
    return str1
#se requiere hacer una funcion que modifique la linea que tenga Nan cuando el carro ha estado parado y tenemos fallas
#itero por indicies
#for ind in placa_modelo.index:
    
#Cada linea se imprime con:
#print(placa_modelo['marca-modelo'][ind], placa_modelo['placa'][ind]
#fecha1 = data_gps.fechaMensaje.min()
#fecha1 = fecha1 + timedelta(days=11)
#fecha1 = pd.to_datetime('2020-03-31', format="%Y-%m-%d").date()#si no le pongo .date, queda con hh:mm:ss:mmms
#print(fecha1 + timedelta(days=11))
#test = data_gps.loc[(data_gps['fechaMensaje'] == fecha1)]
#print(test)
#placa='EQP620'
#ruta=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].referenciaPos.unique()
#mindist=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].odometro.min()  
#maxdist=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].odometro.max()
#print(placa)
#print(ruta)
#print(maxdist)
#print(fecha1)
#fecha1 = fecha1 + timedelta(days=1)
#df = pd.DataFrame(columns=['fecha','placa','modelo','ruta','dist_dia','odometro','avg_bat','avg_vel','avg_rpm','avg_tempaceite','avg_presionaceite','avg_temprefrigerante','avg_tempmultiple','avg_nivelcombustible','avg_nivleaceite','avg_pedalaceleracion','avg_torquemotor','horas_motor','fallas_d','SISTEMA_MOTOR', 'NEUMATICA', 'CABINA', 'TREN_POTENCIA','ELECTRICO', 'CHASIS', 'DIRECCION', 'FRENOS', 'LUBRICACION','MOTOR', 'SUSPENSION', 'LLANTAS', 'ESTRUCTURA_CISTERNA','LATONERIA_Y_PINTURA','SERVICIOS','NEUMATICO','ESTRUCTURA_TANQUE','QUINTA_RUEDA','ENGANCHE','ESTRUCTURA_TRAILER'])
#df = pd.DataFrame(columns=['fecha','placa','modelo','ruta','dist_dia','odometro','avg_bat','avg_vel','avg_rpm','avg_tempaceite','avg_presionaceite','avg_temprefrigerante','avg_tempmultiple','avg_nivelcombustible','avg_nivleaceite','avg_pedalaceleracion','avg_torquemotor','horas_motor','fallas_d'])
counter=0
data = []
for ind in placa_modelo.index:
 placa =  placa_modelo['placa'][ind]
 modelo =  placa_modelo['marca-modelo'][ind]
 fecha1 = data_gps.fechaMensaje.min()
 #print(placa_modelo['marca-modelo'][ind], placa_modelo['placa'][ind]
 #ruta=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == '2020/03/31')].referenciaPos.unique()#['2014-01-01':'2014-02-01']para rango
 
 while fecha1 < data_gps.fechaMensaje.max():
  
  ruta=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].referenciaPos.unique().tolist()
  #print(ruta,len(ruta))
  if(len(ruta)<2):
   ruta='stopped-day'
  else:
   ruta=str(ruta[0])+'-'+str(ruta[len(ruta)-1])
  #print(ruta,len(ruta),type(ruta))
  
  ########ruta=str(ruta[0])+'-'+str(ruta[len(ruta)-1])
  mindist=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].odometro.min()  
  odometro=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].odometro.max()
  avg_bat=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].bateria.mean()
  dist_dia=odometro-mindist
  avg_vel=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].velocidad.mean()
  avg_rpm=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].rpm.mean()
  avg_combustibletotal=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].combustibletotal.mean()
  avg_tempaceite=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].tempaceite.mean()
  avg_presionaceite=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].presionaceite.mean()
  avg_temprefrigerante=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].temprefrigerante.mean()
  avg_tempmultiple=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].tempmultiple.mean()
  avg_nivelcombustible=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].nivelcombustible.mean()
  avg_nivleaceite=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].nivleaceite.mean()
  avg_pedalaceleracion=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].pedalaceleracion.mean()
  #####ojo agregar funcion de altitud#####################
  avg_torquemotor=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].torquemotor.mean()
  horas_motor=data_gps[data_gps['placa']==placa].loc[(data_gps['fechaMensaje'] == fecha1)].horasmotor.mean()
  #fallas_d=fallas[fallas['IDPLACA']==placa].loc[(fallas['FECHAENTREGA'] == fecha1)].REPUESTO.unique()
  end_date = fecha1 + timedelta(days=1)
  mask = (fallas['FECHASOLICITUD'] > fecha1.strftime("%Y-%m-%d")) & (fallas['FECHASOLICITUD'] <= end_date.strftime("%Y-%m-%d"))
  fallas_d = fallas[fallas['IDPLACA']==placa].loc[mask].SISTEMA.unique()
  ##fallas_d = listToString(fallas_d)
  if(len(fallas_d) == 0):
   fallas_d='no_failures'
   line = [fecha1.strftime("%Y-%m-%d"),placa,modelo,ruta,dist_dia,odometro,avg_bat,avg_vel,avg_rpm,avg_tempaceite,avg_presionaceite,avg_temprefrigerante,avg_tempmultiple,avg_nivelcombustible,avg_nivleaceite,avg_pedalaceleracion,avg_torquemotor,horas_motor,fallas_d,'auto']
   print(line[0],line[1],line[2],counter)
   counter = counter + 1
   data.append(line)
  else:
    for indx in range(len(fallas_d)):
      line = [fecha1.strftime("%Y-%m-%d"),placa,modelo,ruta,dist_dia,odometro,avg_bat,avg_vel,avg_rpm,avg_tempaceite,avg_presionaceite,avg_temprefrigerante,avg_tempmultiple,avg_nivelcombustible,avg_nivleaceite,avg_pedalaceleracion,avg_torquemotor,horas_motor,fallas_d[indx],'manual']
      print(line[0],line[1],line[2],counter)
      counter = counter + 1
      data.append(line)  
  fecha1 = fecha1 + timedelta(days=1)
df = pd.DataFrame(data, columns=['fecha','placa','modelo','ruta','dist_dia','odometro','avg_bat','avg_vel','avg_rpm','avg_tempaceite','avg_presionaceite','avg_temprefrigerante','avg_tempmultiple','avg_nivelcombustible','avg_nivleaceite','avg_pedalaceleracion','avg_torquemotor','horas_motor','fallas_d','method'])
print(' FIN  ')
df.to_csv('hdv2_data7.csv') 

"""
  #fecha1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d") + datetime.timedelta(days=1)

 
#####ITERA CON TUPLAS #############
#for row in placa_modelo.iterrows():
#   print(row)





#for placa in placa_modelo.placa:
 # min_day_gps = data_gps[data_gps['placa']==placa] & data_gps[data_gps['fechaMensaje']=='2020-03-20T22']
#for i in range(1,len(placa_modelo)):
"""