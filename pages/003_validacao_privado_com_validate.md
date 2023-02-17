# Validação conjunto público com método validate

Validação testada na [instância projeto ckan](http://projetockan.cge.mg.gov.br/), [ckanext-datapackage-creator 0.0.38](https://pypi.org/project/ckanext-datapackage-creator/)

- Conjunto: [teste17022023-privado](http://projetockan.cge.mg.gov.br/dataset/teste17022023-privado)
- Visibilidade: privado
- Metódo frictionless utilizado: Package.validate()
- Breve descrição do teste: 
	- Incluído campo `ano` do recurso `test-xlsx` (claramente texto) como `boolean`

- Resultado:
	- Validação campo `ano` do recurso `test-xlsx` falhou como era de se esperar (o mesmo não ocorreu no CKAN)

```yaml report
descriptor: validations/003_validacao_privado_com_validate.json
```
