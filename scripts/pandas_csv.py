from frictionless import Package

package = Package("datapackage_csv.yaml")
mega = package.get_resource("mega-sena")
df = mega.to_pandas()

print(df)
