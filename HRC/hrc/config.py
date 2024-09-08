from typing import Set, Union

from pydantic import BaseModel, ConfigDict, DirectoryPath, Field


class ConfigModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    __config_name__: str = ""


class LogConfig(ConfigModel):
    level: Union[str, int] = "DEBUG"
    verbose_exception: bool = False


class CoreConfig(ConfigModel):
    rules: Set[str] = Field(default_factory=set)
    rule_dirs: Set[DirectoryPath] = Field(default_factory=set)
    log: LogConfig = LogConfig()


class RuleConfig(ConfigModel):
    """rule configuration."""


class MainConfig(ConfigModel):
    core: CoreConfig = CoreConfig()
    rule: RuleConfig = RuleConfig()
