|official site| |community| |ruff| |python_v| |crates_v| |release_img| |docs_status| |CodeQL| 

跨平台、多模态、高度自定义的骰系开发框架 |Structure2|
==================================

.. start-index

欢迎来到 *HydroRoll* [水系]，一个依据科学架构并由多模态模型赋能，使用 *Rust* 与 *Python* 编写的高性能、跨平台骰系开发框架。

  🌏 此框架主要用于解决 **“如何更好的为冷门规则书做适配”** 与 **“如何更好的实现人机交互”** 两个问题。如果你是世界主、规则书作者、人工智能（自然语言处理方向）爱好者，那么水系或许是你的不二之选。

- 🦀 核心由 *Rust* 编写，性能优异、速度惊人。
- 🐍 *Python* 编写的顶层业务逻辑，方便使用、更快入门。
- 📕 基于规则书的架构，名副其实的骰系（制造）工场。
- ⚡ 仅需三条指令即可快速安装运行已有的规则包，或开发自己的骰系。
- 🛠️ 灵活的配置，高度自定义，就像搭积木与拼拼图一样简单高效。
- 🔌 可选的拓展模块，兼容 *shiki* 的 *lua* 模块、兼容青果 *onedice* 标准的骰子表达式解析模块等...
- 👍 跨平台，对接 *onebot* 协议、 *kook* 平台、 *dingtalk* 软件、 *telegram*、 *discord*、 *minecraft*...与自研 *IM* 平台。
- 🧩 兼容的插件设计，可编写 *lua*、 *python*、 *javascript* 脚本，为附加功能赋能， *Blockly* 傻瓜式在线可视化编写水系脚本插件。
- 🎲 *Meta* 级别的掷骰表达式解析库，可自定义任何解析规则，或可用于一条指令执行多个操作~>学习 `oneroll <https://github.com/HydroRoll-Team/DiceParser>`_。
- 🤖 内嵌 *AI* 工具——水系模型工作流， *webui* 管理各个单一任务模型的输入输出与嵌套关系，低成本实现媲美大模型的多任务功能。
- 🎢 渐进式学习框架，从编写简单的 *nivis reply* 脚本，到编写满足小需求的 *lua*、 *python* 脚本，再到成为世界主编写自己的规则包模块，甚至训练水系模型，层层递进，轻松学习。
- 🔓 更多特性等你发掘！

.. end-index

----

安装与使用
----------

在安装 **3.9+** 版本的 *Python* 之后，请先全局安装 *pdm* 依赖，接着全局安装 *hydro_roll* 包。

.. code:: shell

  pip install hydro-roll
  # pip install hydro-roll[all] 安装所有组件
  # pip install hydro-roll[basemodel] 安装基础模型
  # pip install hydro-roll[dev] 安装开发包

接着使用 ``atien`` 命令搭建机器人模板并运行。

.. code:: shell

  atien new -b coc-example "HydroRollBot"
  cd HydroRollBot
  atien run

更多详细的使用方法请参考 `官方文档`_。

----

开发示例
--------

你可以选择从框架端开始开发水系骰子。

.. code:: shell

  pip install iamai
  iamai new "HydroRollDevBot"

  iamai install hydro-roll --dist HydroRollDevBot
  # cd HydroRollDevBot
  # iamai install hydro-roll

接着你需要自行修改 *config.toml* 中的相关适配器与 *hydro-roll* 插件的配置。

最后你可能需要一个启动锚点—— ``main.py``。

.. code:: python

  from iamai import Bot

  bot = Bot(hot_reload=True)

  if __name__ == '__main__':
      bot.run()

.. code:: shell

  python main.py

----

知识问答
--------

“谁适合水系？”
~~~~~~~~~~~~~~~~~

:世界主: 规则书作者。水系基于通用规则包（规则书的 *Python* 实现）标准架构，可以为你一键生成规则书
  的 *pdf* 版本与一个在线规则书浏览站点，同时允许你在规则包内自定义高优先级的骰系内建指令。一个规则
  包，便是一个骰系。
:插件爱好者: 下游插件开发者。水系插件可用 *lua*、 *python*、 *javascript* 编写，同时，支持在线将其他骰
  系的插件文件（如 *shiki* 的 *lua* 脚本，青果的 *python* 插件，海豹的 *js* 插件等）转换为水系对应语言的插
  件脚本实现，另有使用 *Blockly* 搭建的可视化编程站点，轻松编写插件脚本。
:机器学习爱好者: 水系继承自多模态机器学习框架 *iamai*，能够同时训练与推理多个模型，试想你的骰子拥有
  自己的独特人格...
:*kp* 与 *pl*: 水系丰富的规则包生态以及骰系生态允许渴望游玩冷门规则的他们在各种遵循水系 *GRPS* 标准的骰系
  中安装游玩同一个规则包文件。 

“水系是什么？水系不是什么？”
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 水系是一个骰系开发框架: 允许你方便快捷的开发自己的骰系。抛开人工智能模块的水系的第一用户是世界主。
#. 水系不是一个具体的骰系: 但是水系有一个官方的规则书与骰系实现(`传送门`_)。在水系社区，骰系概念是被弱化的，一个加载了独特的规则包的骰子，便是一个骰系（针对此规则包所对应的规则书而言）。

----

`MIT`_ © 2023-PRESENT `简律纯`_ & `HydroRoll-Team`_.

|license icon|

|FOSSA Status|

.. uri list above:
.. _传送门: https://github.com/HydroRoll-Team/examples-hydro
.. _自动热重载: https://docs.hydroroll.team/addons/hot-reload
.. _调度任务: https://docs.hydroroll.team/addons/apscheduler
.. _基础模型: https://docs.hydroroll.team/addons/base-model
.. _规则包: https://docs.hydroroll.team/advanced/rule-package
.. _官方文档: https://docs.hydroroll.team/
.. _MIT: https://github.com/HydroRoll-Team/HydroRoll/blob/main/LICENSE
.. _简律纯: https://github.com/HsiangNianian
.. _HydroRoll-Team: https://github.com/HydroRoll-Team

.. image list above:
.. |docs_status| image:: https://readthedocs.org/projects/hydro-roll-docs/badge/?version=latest
    :target: https://docs.hydroroll.team/zh-cn/latest/?badge=latest
    :alt: Documentation Status
.. |Structure| image:: https://images.repography.com/39938419/HydroRoll-Team/HydroRoll/structure/ZbjPFFiNYq0UR3cTqEwQHLzqWSn3SeO30n9Nk3SwmVU/-8GQ3jezs4jjRVX5ZbACiuiSwmPbkzEdEQAyP2ednF0_table.svg
   :target: https://github.com/HydroRoll-Team/HydroRoll
   :alt: Structure
   :align: right
.. |Structure2| image:: https://images.repography.com/39938419/HydroRoll-Team/HydroRoll/structure/ZbjPFFiNYq0UR3cTqEwQHLzqWSn3SeO30n9Nk3SwmVU/P3iLPoavAOE9FSLe1r5_jJObx8LljYhDBCDfkumyDY0_table.svg
   :width: 60
.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff
   :alt: Ruff
.. |logo_icon| image:: https://cdn.jsdelivr.net/gh/HydroRoll-Team/HydroRoll@main/site/src/assets/image/logo.png
   :target: https://hydroroll.team/
   :align: bottom
   :alt: HydroRoll Logo
   :height: 128
.. |docs| image:: https://img.shields.io/badge/DOCS%20AND%20BLOGS-000000.svg?logo=Vercel&labelColor=000&style=flat-square
   :target: https://docs.hydroroll.team/
   :alt: Documentation
.. |python_v| image:: https://img.shields.io/pypi/v/hydro_roll.svg?&style=flat-square&logo=python&color=blue
   :target: https://pypi.org/project/hydro_roll/
.. |community| image:: https://img.shields.io/badge/论坛-002fa7.svg?logo=github&labelColor=gray&logoWidth=20&logoColor=white&style=flat-square
   :target: https://github.com/orgs/HydroRoll-Team/discussions
   :alt: Join The Community
.. |official site| image:: https://img.shields.io/badge/官网-2255aa.svg?logo=data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8CAgL/CgoK/woKCv8GBgb/BgYG/woKCv8KCgr/AgIC/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/BgYG/0ZGRv9MTEz/JiYm/ygoKP9MTEz/RkZG/wYGBv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9ycnL/Li4u/1xcXP9eXl7/Li4u/3Jycv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP88PDz/cnJy/05OTv9OTk7/UFBQ/05OTv9wcHD/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Kioq/3Jycv9cXFz/TExM/05OTv9aWlr/cHBw/yoqKv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Pj4+/zg4OP+AgID/Pj4+/2ZmZv9oaGj/PDw8/4CAgP86Ojr/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/ywsLP9iYmL/enp6/zIyMv90dHT/dHR0/zAwMP98fHz/YmJi/ywsLP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9SUlL/PDw8/3Jycv9CQkL/UlJS/1RUVP9CQkL/cnJy/zw8PP9SUlL/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/VFRU/yIiIv9aWlr/PDw8/zw8PP8+Pj7/PDw8/1hYWP8iIiL/VFRU/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/zQ0NP9CQkL/ZmZm/yIiIv9WVlb/WFhY/yIiIv9mZmb/QkJC/zY2Nv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9QUFD/BgYG/0RERP9KSkr/JCQk/yYmJv9KSkr/RERE/wgICP9QUFD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/CgoK/wICAv8KCgr/CgoK/wYGBv8GBgb/CgoK/woKCv8CAgL/CgoK/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==&labelColor=gray&logoWidth=20&logoColor=white&style=flat-square
   :target: https://hydroroll.team/
.. |crates_v| image:: https://img.shields.io/crates/v/hydro_roll?logo=rust&color=red
   :target: https://crates.io/crates/hydro_roll
.. |release_img| image:: https://github.com/HydroRoll-Team/HydroRoll/actions/workflows/release.yml/badge.svg
   :target: https://github.com/HydroRoll-Team/HydroRoll/actions/workflows/release.yml
.. |license icon| image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2FHydroRoll-Team%2FHydroRoll.svg?type=shield&issueType=license
   :target: https://app.fossa.com/projects/git%2Bgithub.com%2FHydroRoll-Team%2FHydroRoll?ref=badge_shield&issueType=license
.. |FOSSA Status| image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2FHydroRoll-Team%2FHydroRoll.svg?type=large&issueType=license
   :target: https://app.fossa.com/projects/git%2Bgithub.com%2FHydroRoll-Team%2FHydroRoll?ref=badge_large&issueType=license
.. |CodeQL| image:: https://github.com/HydroRoll-Team/HydroRoll/actions/workflows/github-code-scanning/codeql/badge.svg
   :target: https://github.com/HydroRoll-Team/HydroRoll/actions/workflows/github-code-scanning/codeql
