from iamai import ConfigModel


class Config(ConfigModel):
    __config_name__ = "draft_bottles"

    usage: str = """\
    指令：
        扔漂流瓶 [文本/图片]
        捡漂流瓶
        查看漂流瓶 [漂流瓶编号]
        点赞漂流瓶 [漂流瓶编号]
        评论漂流瓶 [漂流瓶编号] [文本]
        举报漂流瓶 [漂流瓶编号]
        删除漂流瓶 [漂流瓶编号]
        我的漂流瓶
    SUPERUSER指令：
        清空漂流瓶
        恢复漂流瓶 [漂流瓶编号]
        删除漂流瓶评论 [漂流瓶编号] [QQ号]
        漂流瓶白名单 [QQ / 群聊 / 举报] [QQ号 / 群号]
        漂流瓶黑名单 [QQ / 群聊] [QQ号 / 群号]
        漂流瓶详情 [漂流瓶编号]
    """.strip()

    command_list: dict = {
        "test": "/dfb",
        "throw": "扔漂流瓶",
        "get": "捡漂流瓶",
        "report": "举报漂流瓶",
        "comment": "评论漂流瓶",
        "check": "查看漂流瓶",
        "remove": "删除漂流瓶",
        "listb": "我的漂流瓶",
        "like": "点赞漂流瓶",
        "resume": "恢复漂流瓶",
        "clear": "清空漂流瓶",
        "delete": "删除漂流瓶评论",
        "details": "漂流瓶详情",
    }

    ban_list: dict = {
        "groups": [],
        "users": [],
    }

    white_list: dict = {
        "groups": [],
        "users": [],
    }

    max_content_length: int = 1024
