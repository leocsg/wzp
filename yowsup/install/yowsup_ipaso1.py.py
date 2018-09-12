import os
import subprocess
try:
    #os.system('sudo rm /home/pi/Downloads/respaldo_codigos.gz')
    pass
except:
    print('No se encontro respaldo_codigos.gz')
    pass
print("Ingresar numero de telefono con formato '569xxxxxxxx'")
phone = input()
os.system('sudo cp /home/pi/yowsup/yowsup/env/env_modo_android.py /home/pi/yowsup/yowsup/env/env.py')
os.system('cd /home/pi/yowsup\nsudo python3 setup.py build\nsudo python3 setup.py install')
print('Necesitas codigo?')
coderequest = input()
if coderequest=='si' :
    os.system('sudo python3 /home/pi/yowsup/yowsup-cli registration --requestcode sms --phone %s --cc 56 --mcc 730 --mnc 01'%phone)
print("Ingresar codigo que llegara al Celular  con formato 'XXX-XXX'")
code = input()
getVersion =  subprocess.Popen("cd /home/pi/yowsup\nsudo python3 yowsup-cli registration --register %s --phone %s --cc 56", shell=True, stdout=subprocess.PIPE).stdout
print("ESTE MENSAJE ESTA CAPTURADO @@@@@ : %s' % getVersion.read())
#os.system('cd /home/pi/yowsup\nsudo python3 yowsup-cli registration --register %s --phone %s --cc 56'%(code,phone))
os.system('sudo cp /home/pi/yowsup/yowsup/env/env_modo_s40.py /home/pi/yowsup/yowsup/env/env.py')
os.system('cd /home/pi/yowsup\nsudo python3 setup.py build\nsudo python3 setup.py install')
