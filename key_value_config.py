#!/usr/bin/env python3
"""
ConfigParser snippets to:
-> Using keys and values from config files
-> Using a comma separated value list from config files
"""

# Python 3 import (all lowercase configparser)
import configparser

# Create object and open config file
config = configparser.ConfigParser()
config.read("key-value-config.conf")

my_list = []

print(f">> Using Key and Values from a config file")
for mykey, myvalue in config.items("keys-values"):
    my_list.append({"mykey_id": mykey, "myvalue_description": myvalue})

for line in my_list:
    print(
        f"MyKey Id and MyValue Description is: {line['mykey_id']} - {line['myvalue_description']}"
    )


print(f"\n>> Using multiple values comma separated from a config file")
my_var_list = config.get("general-settings", "my_vars")
my_var_list = my_var_list.replace(" ", "").split(",")
print(f"My Var List is: {my_var_list}")
