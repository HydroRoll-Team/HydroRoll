
from iamai import Plugin
from iamai.log import logger as _logger
from HydroRoll.models.cos_sim import cosSim
import jieba

logger = _logger


texts = [
    "你好 HydroRoll",
    "你好 水系",
    "hi 水系",
    "hi HydroRoll",
    "hello 水系",
    "hello HydroRoll",
    "hola 水系",
    "hola HydroRoll",
]

cos_Sim = cosSim(texts)
logger.info(f"{cos_Sim.calcuSim('你好')}")

cos_Sim.save('cos.h5')

model = cosSim.load('cos.h5')

logger.info(f"{model}")

# class Sim(Plugin):
#     async def handle(self) -> None:
#         try:

#             txt_list = eval(self.event.message.get_plain_text()[5:])
#             if len(txt_list) == 1:
#                 await self.event.reply(f"{cos_Sim.CalcuSim(txt_list)}")
#             elif len(txt_list) == 2:
#                 corpuss = [" ".join(jieba.cut(text))
#                            for text in eval(self.event.message.get_plain_text()[5:])]
#                 await self.event.reply(str(corpuss))
#                 vocabulary = cos_Sim.getVocabulary(corpuss)
#                 v = cos_Sim.getVectors(corpuss, vocabulary=vocabulary)
#                 await self.event.reply(f"weight\n=========\n{v}")
#                 await self.event.reply(f"相似度\n=========\n{cos_Sim.cos_sim(v[0], v[1])}")
#         except Exception as e:
#             await self.event.reply(f"{e!r}")

#     async def rule(self) -> bool:
#         return self.event.type == "message" and self.event.message.startswith(".cos")



