print("Pakistan Zindabad")
myname: str = "muhammad Kamran"
hisname: str = "700" 

# to install mytype in anaconda please check this repository
# https://github.com/conda-forge/mypy-feedstock
# conda install mypy mypyc

name: str = "muhammad Kamran"
# name = 700 # there will be error as name is string type
print(name)
print(type(name))
print(id(name))
print([i for i in dir(name) if "__" not in i]) # method attributes

