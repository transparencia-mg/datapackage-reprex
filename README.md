# Data packages for Reproducible Examples

Esse repositório armazena exemplos de [data packages](https://specs.frictionlessdata.io/) para construção de [minimal, reproducible examples (reprex)](https://stackoverflow.com/help/minimal-reproducible-example)

Ao identificar um data package com algum caso de uso específico que merece ser testado faça as alterações necessárias e, após realizar os commits, crie uma tag.

```bash
# alterações necessárias
git add .
git commit -m "Foobar"
git tag reprexid
git push origin --tags
```

Você pode acessar essa versão do repositório na URL

- <https://github.com/dados-mg/datapackage-reprex/tree/reprexid>