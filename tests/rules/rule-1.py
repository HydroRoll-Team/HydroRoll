from HydroRollCore import Rule

class Rule_1(Rule):
    """规则包示例1
    
    """
    
    priority = 1
    
    async def check(self) -> None:
        ...