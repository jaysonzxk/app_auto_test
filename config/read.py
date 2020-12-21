import yaml
import os

with open('./desired_caps', 'r') as f:
    f = f.read()
    f = yaml.load(f)
    print(type(f))