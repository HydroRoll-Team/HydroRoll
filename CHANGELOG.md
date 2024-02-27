# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.1.7] - 2024-02-27
### BREAKING CHANGES
- due to [`cac060a`](https://github.com/HydroRoll-Team/HydroRoll/commit/cac060a6e8b70e4e4e1b34555d3d4fee8bc6d007) - rename HydroRoll dir as hydro_roll *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*:

  rename HydroRoll dir as hydro_roll


### New Features
- [`21d7c37`](https://github.com/HydroRoll-Team/HydroRoll/commit/21d7c371f20dc1cb1f429f98bc0642cf8c9ca62e) - 将 HydroRoll.Dice 类修改为一个泛型类，更好的IDE支持 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`35caa7c`](https://github.com/HydroRoll-Team/HydroRoll/commit/35caa7c2f51878bcef3edea304c20e87040d767a) - **deps**: 添加 `lupa` 依赖 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`4c08ec9`](https://github.com/HydroRoll-Team/HydroRoll/commit/4c08ec908bfaba35c6055ee273a0768ba6749089) - **tests**: 实现对 `Lua5.4` 的封装 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`7894ed7`](https://github.com/HydroRoll-Team/HydroRoll/commit/7894ed73f929c6676242da3a1c3bd11d78d8e711) - 实现在 lua 脚本中调用被注册的 Python 同步函数与类 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`f5926cd`](https://github.com/HydroRoll-Team/HydroRoll/commit/f5926cd9277a76e3779958d2b387ce0229697d51) - 支持lua内调用lua库 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`8353aa8`](https://github.com/HydroRoll-Team/HydroRoll/commit/8353aa8e757716cd7144baee56992bf23f89c5e8) - develop with pdm and maturin *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Bug Fixes
- [`f4ae5b6`](https://github.com/HydroRoll-Team/HydroRoll/commit/f4ae5b6be02973f823024095aa07e3e3acf2b5d2) - **dir**: 补齐 `scripts` 文件夹内的预生成文件夹 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`58fda5c`](https://github.com/HydroRoll-Team/HydroRoll/commit/58fda5c68c3c6d5e2c7a9e7a1118f65f7a919323) - **readme**: delete repeated lines *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`255c259`](https://github.com/HydroRoll-Team/HydroRoll/commit/255c259cbf5ea143927dd988049c4d9ed14ac4f7) - **cargo**: fix lib name *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Refactors
- [`e6e9453`](https://github.com/HydroRoll-Team/HydroRoll/commit/e6e9453a024dff943ea52b4fb588f2cf7fec509b) - **command**: 命令词法解析器 *(PR [#82](https://github.com/HydroRoll-Team/HydroRoll/pull/82) by [@HsiangNianian](https://github.com/HsiangNianian))*
  - :arrow_lower_right: *addresses issue [#81](https://github.com/HydroRoll-Team/HydroRoll/issues/81) opened by [@HsiangNianian](https://github.com/HsiangNianian)*
- [`4426854`](https://github.com/HydroRoll-Team/HydroRoll/commit/4426854b2788804bc4dfe3826a63959f973df416) - **core**: rewrite HydroRoll in rust *(PR [#91](https://github.com/HydroRoll-Team/HydroRoll/pull/91) by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`cac060a`](https://github.com/HydroRoll-Team/HydroRoll/commit/cac060a6e8b70e4e4e1b34555d3d4fee8bc6d007) - rename HydroRoll dir as hydro_roll *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Chores
- [`a904949`](https://github.com/HydroRoll-Team/HydroRoll/commit/a904949c07a621c471ce326732a1fb496407a3c2) - 修复主页介绍的大标题链接 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`c97d5fe`](https://github.com/HydroRoll-Team/HydroRoll/commit/c97d5fe720ad25d110304c8980555dcb4460ca0e) - 同步协议至 MIT *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`42e10b3`](https://github.com/HydroRoll-Team/HydroRoll/commit/42e10b33ef3bec8057fdbadc68df2bfe7e4db1f9) - Update LICENSE *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`773f435`](https://github.com/HydroRoll-Team/HydroRoll/commit/773f435335948237fae4fb4f7cbd208955df6713) - update readme *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ee71cdc`](https://github.com/HydroRoll-Team/HydroRoll/commit/ee71cdc800449b9322fd928c46410876b6f996f7) - update readme *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`de6afb8`](https://github.com/HydroRoll-Team/HydroRoll/commit/de6afb89c1386924e37c5bd869eba6732baa1fec) - ?uh?? *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`b7f99a0`](https://github.com/HydroRoll-Team/HydroRoll/commit/b7f99a0466834d5b9c45052d94ac57918efc584a) - 我想睡觉，但我失眠了。 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`e0671b6`](https://github.com/HydroRoll-Team/HydroRoll/commit/e0671b682be5e5a949185e0baf737d4f08b62cbe) - **@todo**: 兼容 shiki 的大部分 lua 脚本内建指令 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`f485b69`](https://github.com/HydroRoll-Team/HydroRoll/commit/f485b697d8e981e5b17fd37fce2941e82f11c14a) - **deps-dev**: bump vite from 4.5.0 to 4.5.1 in /site *(PR [#86](https://github.com/HydroRoll-Team/HydroRoll/pull/86) by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`22b9300`](https://github.com/HydroRoll-Team/HydroRoll/commit/22b9300e6be4f821da9d83b948e20d039434c89c) - **deps-dev**: bump vite from 4.5.1 to 4.5.2 in /site *(PR [#89](https://github.com/HydroRoll-Team/HydroRoll/pull/89) by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`3eb819d`](https://github.com/HydroRoll-Team/HydroRoll/commit/3eb819d7c48020df35336e141c38ab4d9926c21e) - **readme**: update *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`1618bc3`](https://github.com/HydroRoll-Team/HydroRoll/commit/1618bc380d2f14b31b225e8decd3530f2944949c) - **project**: sync pyproject.toml with dev branch *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ac47c7d`](https://github.com/HydroRoll-Team/HydroRoll/commit/ac47c7d083619c3f45b02e018a766a28f7667ef9) - **readme**: delete README.md to sync dev branch *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`f5b87bb`](https://github.com/HydroRoll-Team/HydroRoll/commit/f5b87bb917a1cbad5ba81d3860b358129831bcae) - **bones**: mv HydroRoll src dir *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`7f6bf69`](https://github.com/HydroRoll-Team/HydroRoll/commit/7f6bf6928f5dc62b706b2ffe154f811f54d722d8) - **project**: add pip deps and bump version from 0.1.4 to 0.1.5 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`55bdd19`](https://github.com/HydroRoll-Team/HydroRoll/commit/55bdd192566df10f927de9f902270ba3789cb3e8) - **workflow**: delete .github/workflows/docs.yml *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`679880c`](https://github.com/HydroRoll-Team/HydroRoll/commit/679880c0bd8e6ad1d8c6e4f9ee92cf89ddbd3cdd) - remove pdm *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`63ae3d6`](https://github.com/HydroRoll-Team/HydroRoll/commit/63ae3d6beae1094b313109379b8e6298bbad84fe) - **project**: update cargo.toml *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`c1be571`](https://github.com/HydroRoll-Team/HydroRoll/commit/c1be571e61320aad3233d20b830e7476fa5453a8) - **project**: update pyproject.toml *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`60902c7`](https://github.com/HydroRoll-Team/HydroRoll/commit/60902c77d53c73027650be66f8ed11aec3ca8238) - **project**: update pyproject.toml *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`af61638`](https://github.com/HydroRoll-Team/HydroRoll/commit/af6163870e647a5f1c46f238e5675cd18b2de2ae) - **project**: update pyproject.toml *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ae75d22`](https://github.com/HydroRoll-Team/HydroRoll/commit/ae75d221d185b8b53e1e151ee354ecd81fc0e061) - **readme**: update profile *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`dfff6a0`](https://github.com/HydroRoll-Team/HydroRoll/commit/dfff6a0c2f4347287406b687f89b880611597994) - **readme**: update profile *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`506265d`](https://github.com/HydroRoll-Team/HydroRoll/commit/506265dc202696477390f453456a891905bdb744) - **readme**: update profile *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`bdcc5c9`](https://github.com/HydroRoll-Team/HydroRoll/commit/bdcc5c94bc9fca1cc4cf86b3c8bb0687e675b823) - **project**: update pyproject.toml *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ab2c402`](https://github.com/HydroRoll-Team/HydroRoll/commit/ab2c4024160330f3465686ffa3870d2316e797ae) - **project**: update pyproject.toml and cargo.toml *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*


[v0.1.7]: https://github.com/HydroRoll-Team/HydroRoll/compare/v0.1.4...v0.1.7