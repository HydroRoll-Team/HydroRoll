HydroRoll'水系
============

|ruff| |python_v| |community| |docs|

水系是一个基于机器学习框架iamai的跨平台骰系，尽管只是作为iamai的插件示例，但它仍然有自己的创新之处与标准遵循:

-  **语法高度严谨且自由**: 命令语法贴切实际，输入灵活方便。

-  **概念继承但焕然一新**:
   因为开发者混迹的骰系群以及使用过的骰系很多，因此继承学习了相当一部分各个骰系做的比较好的地方，同时也引入了诸多类似(规则模块、世界主、模型模块)等概念。

.. _getting:

Getting
----------

1. 安装库

推荐局部安装，使用 ``pdm`` 创建一个虚拟环境后在命令行输入。

.. code:: shell

   pdm add hydroroll[all]

2. 创建机器人实例

.. code:: shell

   mkdir mybot && cd mybot && mkdir plugins 
   echo.> config.toml && echo.> main.py :: 创建空的配置文件和python运行脚本

在 ``main.py`` 导入 ``Bot`` 类, 创建一个 ``bot`` 实例并开启热加载,
最后通过 ``run`` 方法启动水系骰娘。

.. code:: python

   from hydroroll import Bot

   bot = Bot(hot_reload=True)

   if __name__ == "__main__":
       bot.run()

3. 使用合适的适配器, 合理修改你的 ``config.toml`` 配置文件, 等待连接!

.. code:: python

   pdm run main.py

.. _contributing:

Contributing
---------------

欢迎阅读 `CONTRIBUTING.md <./CONTRIBUTING.md>`__

.. _community:

Community
----------

HydroRoll 水系 的论坛在 `GitHub
Discussions <https://github.com/orgs/HydroRoll-Team/discussions>`__,
你可以在这里提出任何问题, 分享任何想法。

目前你可以加入 |image1| 和社区里的其它用户交流,
同时也能在里面体验到最新开发的水系骰子(krypton)。

我们的 `行为准则(Code of Conduct) <./CODE_OF_CONDUCT.md>`__ 适用于
HydroRoll'水系 社区内的所有交流渠道。

.. _update:

Update
---------

1. 使用 ``pdm`` 局部更新

.. code:: shell

   pdm update hyrdroroll

🔺Structure
-----------

|Structure|

.. _license:

License
----------

`MIT <https://github.com/HydroRoll-Team/HydroRoll/blob/main/LICENSE>`__
© 2023-PRESENT `简律纯 <https://github.com/HsiangNianian>`__

.. |Structure| image:: https://images.repography.com/39938419/HydroRoll-Team/HydroRoll/structure/ZbjPFFiNYq0UR3cTqEwQHLzqWSn3SeO30n9Nk3SwmVU/-8GQ3jezs4jjRVX5ZbACiuiSwmPbkzEdEQAyP2ednF0_table.svg
   :target: https://github.com/HydroRoll-Team/HydroRoll
   :alt: Structure
.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff
   :alt: Ruff
.. |logo| image:: https://mirror.ghproxy.com/https://raw.githubusercontent.com/HydroRoll-Team/HydroRoll/main/site/src/assets/image/logo.png
   :target: https://hydroroll.team/
   :alt: HydroRoll Logo
   :height: 128
   :align: right
.. |docs| image:: https://img.shields.io/badge/DOCS%20AND%20BLOGS-000000.svg?logo=Vercel&labelColor=000&style=flat-square
   :target: https://docs.hydroroll.team/
   :alt: Documentation
.. |python_v| image:: https://img.shields.io/pypi/v/hydroroll.svg?labelColor=000000&style=flat-square
   :target: https://pypi.org/project/hydroroll/
.. |community| image:: https://img.shields.io/badge/Join%20the%20community-blueviolet.svg?logo=data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8CAgL/CgoK/woKCv8GBgb/BgYG/woKCv8KCgr/AgIC/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/BgYG/0ZGRv9MTEz/JiYm/ygoKP9MTEz/RkZG/wYGBv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9ycnL/Li4u/1xcXP9eXl7/Li4u/3Jycv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP88PDz/cnJy/05OTv9OTk7/UFBQ/05OTv9wcHD/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Kioq/3Jycv9cXFz/TExM/05OTv9aWlr/cHBw/yoqKv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Pj4+/zg4OP+AgID/Pj4+/2ZmZv9oaGj/PDw8/4CAgP86Ojr/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/ywsLP9iYmL/enp6/zIyMv90dHT/dHR0/zAwMP98fHz/YmJi/ywsLP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9SUlL/PDw8/3Jycv9CQkL/UlJS/1RUVP9CQkL/cnJy/zw8PP9SUlL/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/VFRU/yIiIv9aWlr/PDw8/zw8PP8+Pj7/PDw8/1hYWP8iIiL/VFRU/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/zQ0NP9CQkL/ZmZm/yIiIv9WVlb/WFhY/yIiIv9mZmb/QkJC/zY2Nv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9QUFD/BgYG/0RERP9KSkr/JCQk/yYmJv9KSkr/RERE/wgICP9QUFD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/CgoK/wICAv8KCgr/CgoK/wYGBv8GBgb/CgoK/woKCv8CAgL/CgoK/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==&labelColor=000000&logoWidth=20&logoColor=white&style=flat-square
   :target: https://github.com/orgs/HydroRoll-Team/discussions
   :alt: Join The Community