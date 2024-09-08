Core' 水系核心 |Structure|
=======================================

|HydroRollCoreIcon| |Documentation Status| |release_status| |community| |ruff|

去中心化应用程序。

  📕 水系核心是骰系去中心化的一种解决方案，提供了强大的 TRPG 规则书处理功能。
  支持在 CLI 中单独使用，同时也提供 REST API 和 WebSocket 通信接口以便其他语言接入。
  此外，它能够读取一种约定式的规则包，并行处理规则包，生成 PDF 文件和本地在线文档站点。

- 🦀 *Rust* 底层实现，“性能优异、速度惊人”。
- 🐍 *Python* 编写的顶层业务逻辑，方便使用、更快入门。
- 📦 兼容的规则包继承解决方案，完善的社区与规则包市场。
- 🛠️ *CLI* 呼出，通过脚手架可以直接使用全部功能。
- 📃 多语言支持：提供 *REST API* 和 *WebSocket* 接口，支持多语言接入和交互。
- 🏗️ 高并发处理 ，使用 *Rust* 实现的规则包加载模块支持并行处理，极大提高性能。
- 📚 *PDF* 生成，结合自定义 *PDF* 模板，能够生成符合需求的 *PDF* 文件与 *LaTeX* 源码。
- 🌏 离线文档与在线协作站点，使用 *Sphinx* 框架与 *Vue* 技术栈生成的本地文档与在线站点。
- 🥰 不止这些...

..
  架构设计
  -------
  
  .. code-block:: mermaid
  
    graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
  
  
  .. code-block:: stl
  
    solid cube_corner
      facet normal 0.0 -1.0 0.0
        outer loop
          vertex 0.0 0.0 0.0
          vertex 1.0 0.0 0.0
          vertex 0.0 0.0 1.0
        endloop
      endfacet
      facet normal 0.0 0.0 -1.0
        outer loop
          vertex 0.0 0.0 0.0
          vertex 0.0 1.0 0.0
          vertex 1.0 0.0 0.0
        endloop
      endfacet
      facet normal -1.0 0.0 0.0
        outer loop
          vertex 0.0 0.0 0.0
          vertex 0.0 0.0 1.0
          vertex 0.0 1.0 0.0
        endloop
      endfacet
      facet normal 0.577 0.577 0.577
        outer loop
          vertex 1.0 0.0 0.0
          vertex 0.0 1.0 0.0
          vertex 0.0 0.0 1.0
        endloop
      endfacet
    endsolid


----

`AGPL3.0`_ © 2023-PRESENT `简律纯`_ & `HydroRoll-Team`_.

|license icon|

|FOSSA Status|



.. uri list above:
.. _AGPL3.0: https://github.com/HydroRoll-Team/HydroRollCore/blob/main/LICENSE
.. _简律纯: https://github.com/HsiangNianian
.. _HydroRoll-Team: https://github.com/HydroRoll-Team

.. image list above:
.. |Structure| image:: https://images.repography.com/39938419/HydroRoll-Team/HydroRollCore/structure/tMt9z2RexIQ8rnXCIMFWe7YTZtx9reheQCtxqgPqZ1Q/XERnotqf4h5EPFL215lPSb7Dk3fQ5EUniRD-gEckW3M_table.svg
   :alt: Structure
   :target: https://github.com/HydroRoll-Team/HydroRollCore
   :width: 60
.. |license icon| image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2FHydroRoll-Team%2FHydroRollCore.svg?type=shield&issueType=license
   :target: https://app.fossa.com/projects/git%2Bgithub.com%2FHydroRoll-Team%2FHydroRollCore?ref=badge_shield&issueType=license
.. |FOSSA Status| image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2FHydroRoll-Team%2FHydroRollCore.svg?type=large&issueType=license
   :target: https://app.fossa.com/projects/git%2Bgithub.com%2FHydroRoll-Team%2FHydroRollCore?ref=badge_large&issueType=license
.. |HydroRollCoreIcon| image:: https://img.shields.io/pypi/v/hydro_roll_core?style=flat&label=HydroRollCore&color=green
   :target: https://pypi.org/project/hydro_roll_core
.. |Documentation Status| image:: https://readthedocs.org/projects/hydrorollcore/badge/?version=latest
   :target: https://core.hydroroll.team/zh-cn/latest/?badge=latest
.. |crates_v| image:: https://img.shields.io/crates/v/hydro_roll_core?logo=rust&color=red
   :target: https://crates.io/crates/hydro_roll_core
.. |release_status| image:: https://github.com/HydroRoll-Team/HydroRollCore/actions/workflows/release.yml/badge.svg
   :target: https://github.com/HydroRoll-Team/HydroRollCore/actions/workflows/release.yml
.. |community| image:: https://img.shields.io/badge/论坛-002fa7.svg?logo=github&labelColor=gray&logoWidth=20&logoColor=white&style=flat-square
   :target: https://github.com/orgs/HydroRoll-Team/discussions
   :alt: Join The Community
.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff
   :alt: Ruff
