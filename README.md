<p align="center">
  <a href="https://turbo.build">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="image/readme/1682620162817.png">
      <img src="image/readme/1682620162817.png" height="128">
    </picture>
    <h1 align="center">HydroRoll'水系</h1>
  </a>
</p>

<p align="center">
  <a aria-label="Vercel Site" href="https://hydroroll.retrofor.space/">
    <img src="https://img.shields.io/badge/DOCS%20AND%20BLOGS-000000.svg?style=for-the-badge&logo=Vercel&labelColor=000">
  </a>
  <a aria-label="PYTHON version" href="https://pypi.org/project/hydroroll">
    <img alt="" src="https://img.shields.io/pypi/v/hydroroll.svg?style=for-the-badge&labelColor=000000">
  </a>
  <a aria-label="License" href="https://github.com/retrofor/hydroroll/blob/main/LICENSE">
    <img alt="" src="https://img.shields.io/pypi/l/hydroroll.svg?style=for-the-badge&labelColor=000000&color=">
  </a>
  <a aria-label="Join the community on GitHub" href="https://github.com/retrofor/hydroroll/discussions">
    <img alt="" src="https://img.shields.io/badge/Join%20the%20community-blueviolet.svg?style=for-the-badge&logo=data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8CAgL/CgoK/woKCv8GBgb/BgYG/woKCv8KCgr/AgIC/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/BgYG/0ZGRv9MTEz/JiYm/ygoKP9MTEz/RkZG/wYGBv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9ycnL/Li4u/1xcXP9eXl7/Li4u/3Jycv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP88PDz/cnJy/05OTv9OTk7/UFBQ/05OTv9wcHD/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Kioq/3Jycv9cXFz/TExM/05OTv9aWlr/cHBw/yoqKv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Pj4+/zg4OP+AgID/Pj4+/2ZmZv9oaGj/PDw8/4CAgP86Ojr/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/ywsLP9iYmL/enp6/zIyMv90dHT/dHR0/zAwMP98fHz/YmJi/ywsLP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9SUlL/PDw8/3Jycv9CQkL/UlJS/1RUVP9CQkL/cnJy/zw8PP9SUlL/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/VFRU/yIiIv9aWlr/PDw8/zw8PP8+Pj7/PDw8/1hYWP8iIiL/VFRU/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/zQ0NP9CQkL/ZmZm/yIiIv9WVlb/WFhY/yIiIv9mZmb/QkJC/zY2Nv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9QUFD/BgYG/0RERP9KSkr/JCQk/yYmJv9KSkr/RERE/wgICP9QUFD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/CgoK/wICAv8KCgr/CgoK/wYGBv8GBgb/CgoK/woKCv8CAgL/CgoK/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==&labelColor=000000&logoWidth=20&logoColor=white">
  </a>

水系是一个基于深度学习框架iamai的跨平台骰系，尽管只是作为iamai的插件示例，但它仍然有自己的创新之处与标准遵循:

- **语法高度严谨且自由**: 命令语法贴切实际，输入灵活方便。

- **概念继承但焕然一新**: 因为开发者混迹的骰系群以及使用过的骰系很多，因此继承学习了相当一部分各个骰系做的比较好的地方，同时也引入了诸多类似(规则模块、世界主、模型模块)等概念。

## 🎁 Getting

1. 安装库

在命令行输入。

``` shell
pip install HydroRoll
```

2. 创建机器人实例

``` shell
mkdir mybot && cd mybot && mkdir plugins 
echo.> config.toml && echo.> main.py :: 创建空的配置文件和python运行脚本
```

在 `main.py` 导入 `Bot` 类, 创建一个 `bot` 实例并开启热加载, 最后通过 `run` 方法启动水系骰娘。

``` python
from hydroroll import Bot

bot = Bot(hot_reload=True)

if __name__ == "__main__":
    bot.run()
```

3. 使用合适的适配器, 合理修改你的 `config.toml` 配置文件, 等待连接!

## 💕 Contributing

欢迎阅读 [CONTRIBUTING.md](./CONTRIBUTING.md)

## 🙋‍ Community

HydroRoll 水系 的论坛在 [GitHub Discussions](https://github.com/retrofor/HydroRoll/discussions), 你可以在这里提出任何问题, 分享任何想法。

目前你可以加入 [![](https://img.shields.io/badge/-QQ群126211793-002FA7?style=flat-square&logo=TencentQQ&logoColor=white)]() 和社区里的其它用户交流, 同时也能在里面体验到最新开发的水系骰子(krypton)。

我们的 [行为准则(Code of Conduct)](https://github.com/retrofor/HydroRoll/blob/main/CODE_OF_CONDUCT.md) 适用于 HydroRoll'水系 社区内的所有交流渠道。

## ✨ Updates

1. 使用 `pip` 更新

``` shell
pip install --upgrade hyrdroroll
```

## 👨‍🚀 Contributors

<a href="https://github.com/retrofor/HydroRoll/graphs/contributors">
  <img width="80" src="https://contrib.rocks/image?repo=retrofor/HydroRoll"/>
</1a>

## 📄 License

[GPL 3.0](https://github.com/HsiangNianian/OlivaBiliLive/blob/main/LICENSE) © 2023-PRESENT [简律纯](https://github.com/HsiangNianian)