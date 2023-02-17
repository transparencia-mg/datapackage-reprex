import json
import frictionless
from frictionless import Package
from frictionless import validate
import requests
from dotenv import dotenv_values

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


# Test 003
datapackage_url = 'http://projetockan.cge.mg.gov.br/datapackage-creator/show-datapackage-json/adc66acf-4e14-414a-a862-01d0fbf20aff'
test_003 = '003_validacao_privado_com_validate'
ckan_token = dotenv_values(".env")['CKAN_TOKEN']
session = requests.Session()
session.headers['Authorization'] = ckan_token
with frictionless.system.use_http_session(session) as ctx:
    validation = frictionless.validate(datapackage_url)
    with open(f'validations/{test_003}.json', 'w', encoding='utf-8') as file:
    	json.dump(validation, file, ensure_ascii=False, indent=4)

# Test 003
datapackage_url = 'http://projetockan.cge.mg.gov.br/datapackage-creator/show-datapackage-json/adc66acf-4e14-414a-a862-01d0fbf20aff'
test_003 = '003_validacao_privado_com_validate'
datapackage_json = requests.get(datapackage_url).json()
ckan_token = dotenv_values(".env")['CKAN_TOKEN']
session = requests.Session()
session.headers['Authorization'] = ckan_token
with frictionless.system.use_http_session(session) as ctx:
	validation = validate(datapackage_json, skip_errors=["byte-count-error"])
	with open(f'validations/{test_003}.json', 'w', encoding='utf-8') as file:
		json.dump(validation, file, ensure_ascii=False, indent=4)