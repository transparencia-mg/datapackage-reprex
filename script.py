import yaml
import json
import ipdb

with open('schema_novo.yaml', 'r') as file:
    configuration = yaml.safe_load(file)

with open('schema_novo.json', 'w') as json_file:
    json.dump(configuration, json_file)

with open('schema_velho.yaml', 'r') as file:
    configuration = yaml.safe_load(file)

with open('schema_velho.json', 'w') as json_file:
    json.dump(configuration, json_file)

output = json.dumps(json.load(open('schema_novo.json')), indent=2)
output_json = json.loads(output)

for field in output_json['fields']:
    if field['name'] == 'cd_fonte':
        constraints = field['constraints']
        for num in constraints['enum']:
            print(num)

