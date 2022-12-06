from frictionless import describe
import os

package = describe('data/*')
package.get_resource("users").schema.primary_key = ["id"]
package.get_resource("orders").schema.primary_key = ["id"]
package.get_resource("orders").schema.foreign_keys.append(
    {"fields": ["user_id"], "reference": {"resource": "users", "fields": ["id"]}}
)
package.to_er_diagram(path='erd.dot')
os.system("dot -Tpng erd.dot > package_erd.png")
package.to_yaml("datapackage.yaml")