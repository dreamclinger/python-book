import os

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

print os.path.abspath('.')
print os.name
print os.uname
print os.environ
print os.getenv('PATH')
