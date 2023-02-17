import json
from frictionless import Package
from frictionless import validate
import requests


# Test 001
datapackage_url = 'http://projetockan.cge.mg.gov.br/datapackage-creator/show-datapackage-json/afaa60dd-edc4-4c84-ab6c-842d5519e309'
test_001 = '001_validacao_publico_com_package'
datapackage_json = requests.get(datapackage_url).json()
package = Package(datapackage_json)
validation = package.validate(skip_errors=["byte-count-error"])
with open(f'validations/{test_001}.json', 'w', encoding='utf-8') as file:
	json.dump(validation, file, ensure_ascii=False, indent=4)

# Test 002
datapackage_url = 'http://projetockan.cge.mg.gov.br/datapackage-creator/show-datapackage-json/afaa60dd-edc4-4c84-ab6c-842d5519e309'
test_002 = '002_validacao_publico_com_validate'
datapackage_json = requests.get(datapackage_url).json()
validation = validate(datapackage_json, skip_errors=["byte-count-error"])
with open(f'validations/{test_002}.json', 'w', encoding='utf-8') as file:
	json.dump(validation, file, ensure_ascii=False, indent=4)
