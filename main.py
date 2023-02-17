import json
from frictionless import Package
import requests


# private dataset 
datapackage_url = 'http://projetockan.cge.mg.gov.br/datapackage-creator/show-datapackage-json/afaa60dd-edc4-4c84-ab6c-842d5519e309'
datapackage_json = requests.get(datapackage_url).json()
package = Package(datapackage_json)
validation = package.validate()
with open('validation.json', 'w', encoding='utf-8') as file:
	json.dump(validation, file, ensure_ascii=False, indent=4)
