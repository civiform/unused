"""
Writes a tfvars file with the format
name="value"\n 

If we want to store non string values here we will need to add in the variables
and do a lil more advanced file writing
"""

import json


class TfVarWriter:

    def __init__(self, filepath):
        self.filepath = filepath

    # a json of key: vals to turn into a tfvars
    def write_variables(self, config_vars: dict):
        with open(self.filepath, "w") as tf_vars_file:
            for name, definition in config_vars.items():
                # Special key that has a dict value.
                if name == Variables.CIVIFORM_SERVER_VARIABLES_KEY:
                    tf_vars_file.write(
                        f"{Variables.CIVIFORM_SERVER_VARIABLES_KEY} = {{\n")
                    for key, value in definition.items():
                        if value is not None:
                            tf_vars_file.write(f'  "{key}"="{value}"\n')
                    tf_vars_file.write("}\n")
                    continue

                if definition is not None:
                    try:
                        parsed_definition = json.loads(definition)
                    except json.JSONDecodeError as e:
                        parsed_definition = definition
                    formatted_value = definition if isinstance(
                        parsed_definition, list) else f'"{definition}"'
                    tf_vars_file.write(f'{name.lower()}={formatted_value}\n')
