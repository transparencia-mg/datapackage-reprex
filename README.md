# Data packages for Reproducible Examples

Para entender o objetivo e funcionamento desse repositório leia o arquivo README do branch main disponível [aqui](https://github.com/dados-mg/datapackage-reprex/blob/main/README.md).

## Testa a existência do arquivo datapackage.json na raiz do dataset para sistemas operacionais diferentes de linux

- Teste necessário para fechamento do [issue 21 do repositório dpkgckanmg](https://github.com/dados-mg/dpkgckanmg/issues/21)
- 1° teste - Verificar existência do arquivo datapackage.json
```
# Clonar e acessar o projeto
$ git clone git@github.com:dados-mg/datapackage-reprex.git
$ cd datapackage-reprex

# Acessar o branch do teste
$ git co os-datapackage-identification

# Acessar pasta dataset
$ cd dataset

# Ativar ambiente
source venv/bin/activate

# Instalar pacote dpkgckanmg de teste armazenado neste branch
# Prestar atenção no window para necessidade de instalar utilizando "..\dpkgckanmg"
(venv) ➜ dataset git:(windows-datapackage-identification): pip install -e ../dpkgckanmg

# Testar função publish
$ python
>>> from dpkgckanmg.publish import publish
>>> publish()
```

- Resposta esperada
```
Datapackage.json existe
Fim da Função Publish
```

- 2° teste - Verificar a não existência do arquivo datapackage.json

```
# Sair do console python
>>> exit()

# Excluir o arquivo datapackage.json
$ rm datapackage.json

# Testar função publish
$ python
>>> from dpkgckanmg.publish import publish
>>> publish()
```

- Resposta esperada
```
Datapackage.json não existe
Fim da Função Publish
```

- 3° desconsiderando modificações na branch (**não commitar estas modificações no repositório online**)
```
# Sair do console python
>>> exit()

# Desativar e limpar ambiente
(venv) ➜  dataset git:(os-datapackage-identification) ✗ deactivate
$ rm -rf venv && python3.9 -m venv venv

# Voltar para pasta raiz datapackage-reprex
cd ..

# Desconsidere todas as modificações realizadas
$ git restore .




