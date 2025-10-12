import yaml
import os

# folder YAML modular
yaml_folder = os.path.join(os.path.dirname(__file__), "yaml")

# load input
with open(os.path.join(yaml_folder, "input.yaml")) as f:
    inputs = yaml.safe_load(f)

# load output
with open(os.path.join(yaml_folder, "output.yaml")) as f:
    outputs = yaml.safe_load(f)

# logic cleanup entitas unavailable
# contoh pseudo-code:
# for ent in inputs + outputs:
#     if ent['state'] == 'unavailable':
#         hapus_entitas(ent['entity_id'])

print("Loaded inputs:", len(inputs))
print("Loaded outputs:", len(outputs))
