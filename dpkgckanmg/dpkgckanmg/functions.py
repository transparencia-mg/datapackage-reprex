import os

def datapackage_existence():
  '''
  Verifica a existência do arquivo datapackage.json na raiz do dataset
  '''
  if os.path.isfile('datapackage.json'):
    print("Datapackage.json existe")
  else:
    print("Datapackage.json não existe")
