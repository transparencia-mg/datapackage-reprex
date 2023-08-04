import locale
from frictionless import Package
from requests import get
import calendar

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
ckan_datapackage = get('http://projetockan.cge.mg.gov.br/datapackage-creator/show-datapackage-json/fd3619b2-db62-45c2-8c15-52cba375a290')
package = Package(ckan_datapackage.json())
resource = package.get_resource('crimes-violentos-2022-1')
df = resource.to_pandas()
for mes in range(1,13):
    df = df.loc[(df['ANO'] >= 2022) & (df['MES'] >= mes )]
    numero_registros = df['REGISTROS'].sum()
    numero_registros = format(numero_registros, "6,d").replace(",", ".")
    print(f'O número de registro de crimes violentos em todo Estado de Minas (RISP) em {calendar.month_name[mes].capitalize()} de 2022 foi de {numero_registros}.')
