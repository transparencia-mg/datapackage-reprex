from frictionless import Package

dp = Package("datapackage.json")

dp.get_resource("no-docs").to_pandas()
#    id  value
# 0   1    NaN
# 1   2    NaN


dp.get_resource("docs").to_pandas()
#    id     value
# 0   1  46563.48
# 1   2  49371.00
