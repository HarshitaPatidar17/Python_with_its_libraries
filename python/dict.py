info={
    "name":"ram",
    "age":11
}
print(info)
print(info.keys())
print(len(info))
print(info.values())
print(info.items())
print(info.get("name2"))
# print(info["name2"]) #gives erroe but get method give none if key is not occur
info1={"city":1}
info.update(info1)
print(info)