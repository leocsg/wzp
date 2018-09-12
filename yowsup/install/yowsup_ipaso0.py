import os 
descarga_wzp = '/home/padmin/Descargas/WhatsApp.apk'
carpeta_destino='/home/padmin/wzp/yowsup/install/'
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)
os.system('sudo cp %s %sWhatsApp.apk' % (descarga_wzp,carpeta_destino))
os.system('sudo python3 %sdexMD5.py %sWhatsApp.apk' %(carpeta_destino,carpeta_destino))
