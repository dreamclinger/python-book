import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
}

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88)

print(json.dumps(s, default=student2dict))

json_str = '{"age": 26, "score": 88, "name": "chen"}' #Dict

print(json.loads(json_str, object_hook=dict2student)) # return obj <__main__.Student object at 0x10ebc7e10>
