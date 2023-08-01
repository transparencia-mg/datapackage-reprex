from frictionless import Package

package = Package("datapackage.yaml")
mega = package.get_resource("mega-sena")
df = mega.to_pandas()

print(df)
