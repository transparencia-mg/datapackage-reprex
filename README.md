# Data packages for Reproducible Examples

Esse repositório armazena exemplos de [data packages](https://specs.frictionlessdata.io/) para construção de [minimal, reproducible examples (reprex)](https://stackoverflow.com/help/minimal-reproducible-example)

Ao identificar um data package com algum caso de uso específico que merece ser testado, crie um novo branch, faça as alterações necessárias e, após realizar os commits, faça push das mudanças.

```bash
git checkout -b reprex-example
# alterações necessárias
git add .
git commit -m "Altera algo significativo para esse exemplo"
git push --set-upstream origin reprex-example
```

Você pode acessar essa versão do repositório na URL

- <https://github.com/dados-mg/datapackage-reprex/tree/reprex-example>

_Não faça commits em branches que você não criou antes de expressamente conversar com o autor_. Além disso, atualize a lista abaixo:

- [root-datapackage](https://github.com/dados-mg/datapackage-reprex/tree/root-datapackage): Data package [mínimo](https://specs.frictionlessdata.io/data-package/#illustrative-structure) com arquivos armazenados na raiz do diretório (ie. sem pasta `data/`)
- [pdf-resource](https://github.com/dados-mg/datapackage-reprex/tree/pdf-resource): Data package com um arquivo `.pdf` como recurso
- [pdf-resource-sha256](https://github.com/dados-mg/datapackage-reprex/tree/pdf-resource-sha256): Data package com um arquivo `.pdf` como recurso e algoritmo de [checksum sha256](https://en.wikipedia.org/wiki/SHA-2)
- [xlsx-resource](https://github.com/dados-mg/datapackage-reprex/tree/xlsx-resource): Data package com um arquivo `.xlsx` como recurso
- [foreign-key-constraint](https://github.com/dados-mg/datapackage-reprex/tree/foreign-key-constraint): Data package com múltiplos recursos e [restrição de chave estrangeira](https://specs.frictionlessdata.io/table-schema/#foreign-keys)
- [git-lfs](https://github.com/dados-mg/datapackage-reprex/tree/git-lfs): Data package configurado para utilização do [git LFS](https://git-lfs.github.com/) na pasta `data/`
- [Conferindo existência de datapackage.json na raiz do dataset em sistemas operacionais distintos](https://github.com/dados-mg/datapackage-reprex/tree/os-datapackage-identification)
- [Typo Material frictionless - teste sem corrigir o erro](https://github.com/dados-mg/datapackage-reprex/tree/frictionless-online-validate-whith-folder-typo)
- [Typo Material frictionless - teste corrigindo erro](https://github.com/dados-mg/datapackage-reprex/tree/frictionless-online-validate-whith-folder-typo-correction)
- [ftp-resource](https://github.com/dados-mg/datapackage-reprex/tree/ftp-resource): Data package com recurso utilizando FTP para armazenamento de arquivos
- [data-types](https://github.com/dados-mg/datapackage-reprex/tree/data-types): Data package utilizando colunas com tipos variados
- [yaml-schema](https://github.com/dados-mg/datapackage-reprex/tree/yaml-schema): Data package utilizando um table schema em um arquivo yaml externo
- [bad-dialect-delimiter](https://github.com/dados-mg/datapackage-reprex/tree/bad-dialect-delimiter): Data package utilizando dialect com separador incorreto
- [external-dialect](https://github.com/dados-mg/datapackage-reprex/tree/external-dialect): Data package utilizando dialect armazenado em arquivo json externo
- [gzip](https://github.com/dados-mg/datapackage-reprex/tree/gzip): Data package com recursos com compressão gzip
- [utf-8-bom](https://github.com/dados-mg/datapackage-reprex/tree/utf-8-bom): Data package com recursos com encoding UTF-8 with BOM
- [invalid-decimal-char](https://github.com/dados-mg/datapackage-reprex/tree/invalid-decimal-char): Data package com separador de decimal `,` no table schema mas usando `.` no csv
- [json-data](https://github.com/dados-mg/datapackage-reprex/tree/json-data): Data package com dados armazenados em json
- [foreign-key-data-package](https://github.com/dados-mg/datapackage-reprex/tree/foreign-key-data-package): Data package com _pattern_ [Foreign Keys to Data Packages](https://specs.frictionlessdata.io/patterns/#table-schema-foreign-keys-to-data-packages)
- [frictionless-describe-dataset-template](https://github.com/dados-mg/datapackage-reprex/tree/frictionless-describe-dataset-template)
- [generate-erd-pictures](https://github.com/dados-mg/datapackage-reprex/tree/generate-erd-pictures)
- [test-frictionless-describe](https://github.com/dados-mg/datapackage-reprex/tree/test-frictionless-describe)
- [test-frictionless-describe](https://github.com/dados-mg/datapackage-reprex/tree/test-datapackage-creator-datapackage.json)
- [test-validation-038](https://github.com/dados-mg/datapackage-reprex/tree/test-validation-038)
- [list-comprehension](https://github.com/dados-mg/datapackage-reprex/tree/list-comprehension)
- [frictionlessPandas](https://github.com/dados-mg/datapackage-reprex/tree/frictionlessPandas)
- [create_df_using_ckan_datapackage](https://github.com/dados-mg/datapackage-reprex/tree/create_df_using_ckan_datapackage)
