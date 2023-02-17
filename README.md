# Test ckan-next-validation versão 0.0.38

Objetivos: mostrar divergências entre resultado de validação apresentado no [dataset teste17022023](http://projetockan.cge.mg.gov.br/dataset/teste17022023) e a validação local.

- Setup linux:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Atualizar relatório de validação

```
make all
```

- Visualizar relatório de validação:

```
livemark start
```
Deverá abrir automaticamente servidor rodando no endereço  http://localhost:7000/. Também é gerado arquivo `index.html` que poderá ser acessado localmente no browser caso não queira trabalhar com servidor ligado.

