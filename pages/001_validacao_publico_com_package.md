# Validação conjunto público com Objeto Frictionless Package

Validação testada na [instância projeto ckan](http://projetockan.cge.mg.gov.br/), [ckanext-datapackage-creator 0.0.38](https://pypi.org/project/ckanext-datapackage-creator/)

- Conjunto: [teste17022023](http://projetockan.cge.mg.gov.br/dataset/teste17022023/)
- Visibilidade: pública
- Metódo frictionless utilizado: Package.validate()
- Breve descrição do teste: 
	- Incluído campo `NATUREZA` do recurso `crimes-violentos-2022` (claramente texto) como `number`
	- Incluído campo `ano` do recurso `test-xlsx` (claramente texto) como `boolean`

- Resultado:
	- Validação campo `NATUREZA` do recurso `crimes-violentos-2022` falhou como era de se esperar (o mesmo não ocorreu no CKAN)
	- recurso `test-xlsx` não foi altualizado no datapackage.json após update de seus metadados, o que impediu a falha na validação.


```yaml report
descriptor: validations/001_validacao_publico_com_package.json
```
