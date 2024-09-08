# MyRule
import math

from typing import Union
from dataclasses import dataclass

from hrc.rule import Rule
from hrc.rule.BaseRule import CharacterCard

aliases = Rule.aliases

@dataclass
class Attributes(CharacterCard.Attribute):

    @aliases(["luck", "运气"], ignore_case=True)
    def LUK(self) -> Union[str, int, None]: ...

    @aliases(["伤害加值", "DamageBonus"], ignore_case=True)
    def DB(self) -> Union[str, int, None]:
        sum = self.STR() + self.SIZ()
        return (
            str(math.ceil((sum - 164) / 80)) + "D6"
            if sum > 164
            else "1D4"
            if sum > 124
            else "0"
            if sum > 84
            else "-1"
            if sum > 64
            else "-2"
            if sum > 0
            else None
        )

    @aliases(["年龄", "age"], ignore_case=True)
    def AGE(self) -> Union[str, int, None]: ...

    @aliases(["HitPoints", "生命值", "生命"], ignore_case=True)
    def HP(self) -> Union[str, int, None]:
        return self.MAX_HP

    @aliases(["最大生命值", "HitPointTotal", "总生命值"], ignore_case=True)
    def MAX_HP(self) -> Union[str, int, None]:
        if hasattr(self, "CON") and hasattr(self, "SIZ"):
            return (self.CON() + self.SIZ()) // 10
        else:
            return None

    @aliases(["理智", "Sanity", "SanityPoint", "理智值", "san值"], ignore_case=True)
    def SAN(self) -> Union[str, int, None]:
        return self.POW()

    @aliases(["最大理智值", "MaximumSanity"], ignore_case=True)
    def MAX_SAN(self) -> Union[str, int, None]:
        return 99 - self.player_card.CM()

    @aliases(["魔法", "魔法值", "MagicPoints"], ignore_case=True)
    def MP(self) -> Union[str, int, None]:
        if hasattr(self, "POW"):
            return math.floor(self.POW() / 5)
        else:
            return None

    @aliases(["伤害加值", "DamageBonus"], ignore_case=True)
    def DB(self) -> Union[int, str, None]:  # noqa: F811
        sum = self.STR() + self.SIZ()
        return (
            str(math.ceil((sum - 164) / 80)) + "D6"
            if sum > 164
            else "1D4"
            if sum > 124
            else "0"
            if sum > 84
            else "-1"
            if sum > 64
            else "-2"
            if sum > 0
            else None
        )

    @aliases(["体格", "build"], ignore_case=True)
    def BUILD(self) -> Union[str, int, None]:
        sum = self.STR() + self.SIZ()
        return (
            math.ceil((sum - 84) / 80)
            if sum > 164
            else 1
            if sum > 124
            else 0
            if sum > 84
            else -1
            if sum > 64
            else -2
            if sum > 0
            else None
        )

    @aliases(["移动速度"], ignore_case=True)
    def MOV(self) -> Union[str, int, None]:
        mov = 8
        siz = self.player_card.SIZ()
        str_val = self.player_card.STR()
        dex = self.player_card.DEX()
        age = self.AGE()

        if age >= 40:
            mov -= math.floor(age / 10 - 3)

        if str_val > siz and dex > siz:
            mov += 1
        elif siz > str_val and siz > dex:
            mov -= 1

        return mov

    @aliases(["兴趣技能点", "PersonalInterests"], ignore_case=True)
    def PI(self) -> Union[str, int, None]:
        return self.player_card.INT() * 2

    @aliases(["闪避", "Dodge"], ignore_case=True)
    def DODGE(self) -> Union[str, int, None]:
        if hasattr(self.player_card, "DEX"):
            return math.floor(self.player_card.DEX / 2)
        return None

    @aliases(["锁匠", "开锁", "撬锁", "Locksmith"], ignore_case=True)
    def LOCKSMITH(self) -> Union[str, int, None]:
        return 1

    @aliases(["动物驯养", "驯兽", "AnimalHandling"], ignore_case=True)
    def ANIMAL_HANDLING(self) -> Union[str, int, None]:
        return 1
