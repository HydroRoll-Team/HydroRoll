from HydroRollCore import Rule, ConfigModel
# from ...plugins.HydroRoll.core import Rule, RuleLoadType

class ThePool(Rule):
    name: str = "池[The Pool]"
    tags = ["The Pool", "池", "合作", "叙事", "d6体系"]
    
    class Config(ConfigModel):
        __config_name__ = "ThePool"
    
    class DefaultDice:
        """默认骰池
        
        dice: 骰子数量
        sides: 骰子面数
        """
        
        def __init__(self):
            self._dice = 15
            self._sides = 6
            
        @property
        def dice(self):
            return self._dice
        
        @property
        def sides(self):
            return self._sides
    
class Wiki(ThePool):
    def __init__(self):
        self._intro = """《池》[The Pool]是一款合作叙事向的角色扮演游戏。
        你可以在游戏里使用任何你喜欢的设定。桌上的一人得成为游戏主持人（或者说 GM）并运作游戏。
        要玩这款 RPG，你需要许多 d6（有六个面的骰子），里面有一些得是GM 骰，它们的外表应该与其他骰子有所区别。
        在角色创建开始时，每个玩家在自己的起始骰池中有 15 颗骰子。剩下的骰子会被放到公共骰池中。
        """
        
        self._make_char = """创建角色很简单，写一段 50 个单词长的故事 [Story]（译者注：约为 80 个汉字）。
        想象你在写一本书，然后这一段就是对书中主角的介绍。你只有 50 个词，所以最好把重点放到两个地方：这个角色最重要的元素，以及他会如何融入到设定之中。
        角色的名字不算在词数限制之中。
        """
    
        self._char_example = """故事示例：
        这是我为《池》创造的第一个角色。我们所选的设定是一个充斥着黑暗魔法的奇幻世界。
        “受训于隐秘的失落之地教团，达马特是一位元素法师。他爱上了一位年轻的新晋门徒，而当法师试图教授一道她无法控制的法术时，她死了。
        达马特被逐出教团，如今，他正寻找着复活她的方法。”
        """
        
    @property
    def intro(self):
        return self._intro
    
    @property
    def make_char(self):
        return self._make_char
    
    @property
    def char_example(self):
        return self._char_example