from cos_sim import cosSim
import numpy as np

texts = [
    "你好 HydroRoll",
    "你好 水系",
    "水系你好",
    "HydroRoll hi~",
    "水系, hola"
    "你好呀 水系",
    "hi 水系",
    "hi HydroRoll",
    "hello 水系",
    "hello HydroRoll",
    "hola 水系",
    "hola HydroRoll",
]

# print(model.corpuss)

# print(model.vocabulary)



model = cosSim(
    simple=texts,
    test_data=[
        # 'Hi! HydroRoll is a roll system.', 
        # 'Hello, this is a system which named HydroRoll',
        # '短文本匹配技术应用是很广泛的，包括搜索、问答、推荐、计算广告等领域，相关技术也沉淀多年，从无监督方法到有监督方法层出不穷，工业界也是都有应用，短文本匹配算是自然语言处理领域的重要技术了，虽然任务简单，但是想要做好并不是那么容易的事情。', 
        # '短文本匹配技术在搜索、问答、推荐和计算广告等领域有广泛的应用。这项技术已经发展多年，从无监督方法到有监督方法层出不穷。在工业界，短文本匹配技术已经得到了广泛的应用。虽然短文本匹配任务看起来简单，但要做好并不容易。',
        # '你好~水系。',
        # 'hola~~~~~~~hola水系！'
        ]
)

# print(model.vectors) 

# print(model.input_vector)

# print(model.input_vocabulary)

# print(cosSim.cos_sim(vector_a=model.input_vector[4], vector_b=model.input_vector[5]))


print(model.similarities)

print(model.inputs)

# model.append(['你好水'])

# model.append(['你好'])

print(model.inputs)

print(model.similarities)

model.reload()

print(model.input_corpuss)

print(model.similarities)