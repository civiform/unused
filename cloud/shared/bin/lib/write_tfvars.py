"""
Writes a tfvars file with the format
name="value"\n 

If we want to store non string values here we will need to add in the variables
and do a lil more advanced file writing
"""
import json

from cloud.shared.bin.lib.variables import Variables


class TfVarWriter:

    def __init__(self, filepath):
        self.filepath = filepath

    # a json of key: vals to turn into a tfvars
    def write_variables(self, config_vars: dict):
        with open(self.filepath, "w") as tf_vars_file:
            print("CONFIG VARS")
            print(config_vars.items())
            for name, definition in config_vars.items():
                # Special key that has a dict value.
                if name == Variables.CIVIFORM_SERVER_VARIABLES_KEY:
                    tf_vars_file.write(
                        f"{Variables.CIVIFORM_SERVER_VARIABLES_KEY} = {{\n")
                    for key, value in definition.items():
                        if value is not None:
                            if type(value) is list:
                                print("LIST TYPE")
                                tf_vars_file.write(f'{key.lower()}={value}\n')
                            else:
                                tf_vars_file.write(f'  "{key}"="{value}"\n')
                    tf_vars_file.write("}\n")
                    continue

                # # Special handling for "list" type variables
                # if name == Variables.TERRAFORM_LIST_VARIABLES_KEY:
                #     print("THIS IS THE DEF")
                #     print(definition)
                #     print("DEF ITEMS")
                #     print(definition.items())
                #     for key, value in definition.items():
                #         print("THIS IS THE KEY")
                #         print(key)
                #         print("THIS IS THE VALUE")
                #         print(value)
                #         if value is not None:
                #             tf_vars_file.write(f'{key.lower()}={value}\n')
                else:
                    print("GOT TO ELSE IN WRITE TF VARS")
                    print("NAME")
                    print(name)
                    print("DEFINITION")
                    print(definition)
                    print("TYPE DEF")
                    print(json.loads(definition))
                    if type(json.loads(definition)) is list:
                        print("LIST TYPE")
                        tf_vars_file.write(f'{name.lower()}="{definition}"\n')

                    if definition is not None:
                        tf_vars_file.write(f'{name.lower()}="{definition}"\n')
