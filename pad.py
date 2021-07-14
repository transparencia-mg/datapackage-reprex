from frictionless import Package
from frictionless_ckan_mapper import frictionless_to_ckan as f2c
import dpckan
import os

dp = Package('datapackage.json')
dp = Package('/Users/fjunior/Local/cge/dados-mg/datapackage-reprex/datapackage.json')
dp = Package('https://raw.githubusercontent.com/dados-mg/datapackage-reprex/data-types/datapackage.json')

dp.basepath