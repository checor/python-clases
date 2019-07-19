import os

print("-" * 40)
for _file in os.listdir('.'):
    print("{:.<35}{:5}".format(_file, os.path.getsize(_file)))
print("-" * 40)