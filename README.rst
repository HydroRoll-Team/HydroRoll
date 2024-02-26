.. raw:: html
  <div align="right">|logo_icon|</div>

HydroRoll'水系
============

|ruff| |python_v| |community| |docs| 

.. _getting:

快速开始
----

  仅需三步即可快速搭建一个符合水系标准的骰子机器人。你也可以在我们的 `官方文档`_ 查看更详细的部署与配置教程。

1. 安装库

推荐局部安装，使用 *pdm* 创建一个虚拟环境后在命令行输入，

.. code:: shell

   pdm add hydroroll[all]

这会在当前虚拟环境添加 *extra* 版本的 *HydroRoll*，包括 `自动热重载`_ (*hot-reload*)、`调度任务`_ (*apscheduler*) 与 `基础模型`_ (*base-model*) 等。

2. 创建机器人实例

在终端中输入执行以下指令，

.. code:: shell

  hydroroll new -b coc_example "HydroRoll"

这会在当前 *pwd* 环境的根目录下使用内置的 *coc_example* `规则包`_ 创建一个名为 "HydroRoll" 的骰子文件夹，您的所有骰子相关内容均在此文件夹中。

.. code:: shell

  tree HydroRoll

  HydroRoll
  ├─models
  ├─config
  ├─data
  ├─rules
  ├─scripts
  └─web
      ├─backend
      └─frontend

3. 使用合适的适配器, 合理修改你的 *config.toml* 配置文件, 等待连接！

.. code:: python

  hydroroll run
  # 使用 pdm run main.py 同理

.. _contributing:

Contributing
---------------

欢迎阅读 `CONTRIBUTING.md <./CONTRIBUTING.md>`__ 对水系的各个模块与标准做出贡献。

.. _community:

Community
----------

HydroRoll'水系 的论坛在 `GitHub
Discussions <https://github.com/orgs/HydroRoll-Team/discussions>`__,
你可以在这里 `提出任何问题 <https://github.com/HydroRoll-Team/HydroRoll/issues/new>`__, `分享任何想法 <https://github.com/HydroRoll-Team/HydroRoll/pulls>`__。

我们的 `行为准则(Code of Conduct) <./CODE_OF_CONDUCT.md>`__ 适用于
HydroRoll'水系 社区内的所有交流渠道。

.. _license:

License
----------

`MIT`_ © 2023-PRESENT `简律纯`_ & `HydroRoll-Team`_.

.. uri list above:
.. _自动热重载: https://docs.hydroroll.team/addons/hot-reload
.. _调度任务: https://docs.hydroroll.team/addons/apscheduler
.. _基础模型: https://docs.hydroroll.team/addons/base-model
.. _规则包: https://docs.hydroroll.team/advanced/rule-package
.. _官方文档: https://docs.hydroroll.team/
.. _MIT: https://github.com/HydroRoll-Team/HydroRoll/blob/main/LICENSE
.. _简律纯: https://github.com/HsiangNianian
.. _HydroRoll-Team: https://github.com/HydroRoll-Team

.. image list above:
.. |Structure| image:: https://images.repography.com/39938419/HydroRoll-Team/HydroRoll/structure/ZbjPFFiNYq0UR3cTqEwQHLzqWSn3SeO30n9Nk3SwmVU/-8GQ3jezs4jjRVX5ZbACiuiSwmPbkzEdEQAyP2ednF0_table.svg
   :target: https://github.com/HydroRoll-Team/HydroRoll
   :alt: Structure
.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff
   :alt: Ruff
.. |logo_icon| image:: https://cdn.jsdelivr.net/gh/HydroRoll-Team/HydroRoll@main/site/src/assets/image/logo.png
   :target: https://hydroroll.team/
   :alt: HydroRoll Logo
   :height: 128
.. |docs| image:: https://img.shields.io/badge/DOCS%20AND%20BLOGS-000000.svg?logo=Vercel&labelColor=000&style=flat-square
   :target: https://docs.hydroroll.team/
   :alt: Documentation
.. |python_v| image:: https://img.shields.io/pypi/v/hydroroll.svg?labelColor=000000&style=flat-square
   :target: https://pypi.org/project/hydroroll/
.. |community| image:: https://img.shields.io/badge/Join%20the%20community-002fa7.svg?logo=data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8CAgL/CgoK/woKCv8GBgb/BgYG/woKCv8KCgr/AgIC/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/BgYG/0ZGRv9MTEz/JiYm/ygoKP9MTEz/RkZG/wYGBv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9ycnL/Li4u/1xcXP9eXl7/Li4u/3Jycv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP88PDz/cnJy/05OTv9OTk7/UFBQ/05OTv9wcHD/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Kioq/3Jycv9cXFz/TExM/05OTv9aWlr/cHBw/yoqKv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Pj4+/zg4OP+AgID/Pj4+/2ZmZv9oaGj/PDw8/4CAgP86Ojr/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/ywsLP9iYmL/enp6/zIyMv90dHT/dHR0/zAwMP98fHz/YmJi/ywsLP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9SUlL/PDw8/3Jycv9CQkL/UlJS/1RUVP9CQkL/cnJy/zw8PP9SUlL/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/VFRU/yIiIv9aWlr/PDw8/zw8PP8+Pj7/PDw8/1hYWP8iIiL/VFRU/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/zQ0NP9CQkL/ZmZm/yIiIv9WVlb/WFhY/yIiIv9mZmb/QkJC/zY2Nv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9QUFD/BgYG/0RERP9KSkr/JCQk/yYmJv9KSkr/RERE/wgICP9QUFD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/CgoK/wICAv8KCgr/CgoK/wYGBv8GBgb/CgoK/woKCv8CAgL/CgoK/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==&labelColor=000000&logoWidth=20&logoColor=white&style=flat-square
   :target: https://github.com/orgs/HydroRoll-Team/discussions
   :alt: Join The Community
