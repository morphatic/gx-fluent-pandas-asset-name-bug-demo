"""
Simple reproduction of the inability to get the "Asset Name"
to show up in the Data Docs for validations that use Fluent
datasources.
"""

import great_expectations as gx

context = gx.get_context()

# Configuration
datasource_name = "demo"
asset_name = "iris"
suite_name = f"{asset_name}_expectations"

asset = context.get_datasource(datasource_name).get_asset(asset_name)
batch = asset.build_batch_request()

checkpoint = context.add_or_update_checkpoint(
  name=f"{datasource_name}_{suite_name}",
  run_name_template="%Y-%m-demo", # REQUIRED to make data docs work on GitHub Pages
  validations=[{
    "batch_request": batch,
    "expectation_suite_name": suite_name,
  }]
)
checkpoint.run()
