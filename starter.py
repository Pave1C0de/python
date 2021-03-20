import os

layer1 = 'my_project'
layer2 = ['settings', 'mainapp', 'adminapp', 'authapp']

def create_starter(layer1, layer2):
   for layer2_i in layer2:
      dir_path = os.path.join(layer1, layer2_i)
      if not os.path.exists(dir_path):
         os.makedirs(dir_path)
      else:
         print(f"WARNING: '{dir_path}' this directory already exist! This directory did not rewrited")
         return 1
   return 0


create_starter(layer1, layer2)
