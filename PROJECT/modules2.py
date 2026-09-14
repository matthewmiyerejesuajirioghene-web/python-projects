from pathlib import Path

# Absolute path
# Relative path

# path = Path("emails")
# print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)