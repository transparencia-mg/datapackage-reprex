import os
from frictionless.plugins.ckan import CkanDialect
from frictionless import Package

dp = Package('datapackage.json')


dialect = CkanDialect(dataset = 'age7',
                      resource = '1dd02e18-ccdc-41b2-9a3f-39687d31d9bc',
                      apikey = os.getenv('CKAN_KEY'))

dp.to_ckan(target = os.getenv('CKAN_HOST'), dialect = dialect)

