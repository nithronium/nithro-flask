import os
import importlib
from flask import Blueprint

def get_blueprints():
    blueprints = []
    directory = os.path.dirname(os.path.abspath(__file__))
    for file_name in os.listdir(directory):
        if file_name.endswith('.py') and file_name != '__init__.py':
            module_name = file_name[:-3]
            module_path = f'{__name__}.{module_name}'
            module = importlib.import_module(module_path)
            for obj_name in dir(module):
                obj = getattr(module, obj_name)
                if isinstance(obj, Blueprint):
                    blueprints.append(obj)
    return blueprints
