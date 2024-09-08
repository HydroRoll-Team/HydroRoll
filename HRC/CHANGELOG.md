# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.0.3] - 2024-07-18
### BREAKING CHANGES
- due to [`c6f28bd`](https://github.com/HydroRoll-Team/HydroRollCore/commit/c6f28bd75141da583bdd95e86d37ae5884276c55) - change namespace<perf, feat, doc, dev> *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*:

  change namespace<perf, feat, doc, dev>


### New Features
- [`fae8d22`](https://github.com/HydroRoll-Team/HydroRollCore/commit/fae8d2273dfad2dd0cf9709f15e24640e7ebfd8d) - **Improve the underlying business directory**: Improve the underlying business directory *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Refactors
- [`c6f28bd`](https://github.com/HydroRoll-Team/HydroRollCore/commit/c6f28bd75141da583bdd95e86d37ae5884276c55) - change namespace<perf, feat, doc, dev> *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`0f39a9d`](https://github.com/HydroRoll-Team/HydroRollCore/commit/0f39a9dfbbb98975c4cc054f98fd7cb14b7e8fb7) - Remove useless code *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`14368e5`](https://github.com/HydroRoll-Team/HydroRollCore/commit/14368e5a7bdcc4b6d3b151ecd9cb3162c30f292e) - Comment hook function while running the rules packages *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Chores
- [`9c06867`](https://github.com/HydroRoll-Team/HydroRollCore/commit/9c068671612655855368bdec569fb7be5890e9d7) - Remove unecessary folder tree *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`4e89d4a`](https://github.com/HydroRoll-Team/HydroRollCore/commit/4e89d4a1b9b5e35ff4bdc9bdafaa5e9d68d3d83a) - Bump version into 0.0.3 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*


## [v0.0.2] - 2024-07-06
### BREAKING CHANGES
- due to [`0ed1048`](https://github.com/HydroRoll-Team/HydroRollCore/commit/0ed10486f719c23ab7e0e84d2e119a7fa5f70475) - rewrite core business logic *(commit by @HsiangNianian)*:

  rewrite core business logic

- due to [`9f7019a`](https://github.com/HydroRoll-Team/HydroRollCore/commit/9f7019a860d3ff10b0f2cf885d8b9df547a6fa5e) - fix AttributeError: wrong '_run_core_reload' method *(commit by @HsiangNianian)*:

  fix AttributeError: wrong '_run_core_reload' method

- due to [`da32df8`](https://github.com/HydroRoll-Team/HydroRollCore/commit/da32df814f9949c7172290dfb4770f7c64c28a5d) - rewrite side bar structures *(commit by @HsiangNianian)*:

  rewrite side bar structures


### New Features
- [`a0ebfdc`](https://github.com/HydroRoll-Team/HydroRollCore/commit/a0ebfdc2cf5f37c40caedcd1dfdcef9660b08f69) - **BaseRule**: add Character.py *(commit by @HsiangNianian)*
- [`e8fc106`](https://github.com/HydroRoll-Team/HydroRollCore/commit/e8fc106776d066e4d8f36e6ea84e5cc98742abff) - **rules**: add decorator: aliases for class attribute property *(commit by @HsiangNianian)*
- [`87f0d8f`](https://github.com/HydroRoll-Team/HydroRollCore/commit/87f0d8fbc019b65ff942b415b107293a1024fe1d) - **exception**: enrich exceptions:: EventException, SkipException, StopException, CoreException, GetEventTimeOut, LoudModuleError *(commit by @HsiangNianian)*
- [`e44fe8d`](https://github.com/HydroRoll-Team/HydroRollCore/commit/e44fe8dfba3a56da39f444cfeb62acd0945a9462) - **core**: impl hot reload *(commit by @HsiangNianian)*

### Bug Fixes
- [`a53bc2d`](https://github.com/HydroRoll-Team/HydroRollCore/commit/a53bc2df778248a81d7d2f25bbe03223912efcdc) - repair incorrect module import path *(commit by @HsiangNianian)*
- [`1b0d676`](https://github.com/HydroRoll-Team/HydroRollCore/commit/1b0d67664557e6f0b4a421e1183cee1b0dbca2d3) - **core**: import missed  module in core.py *(commit by @HsiangNianian)*

### Refactors
- [`2827c09`](https://github.com/HydroRoll-Team/HydroRollCore/commit/2827c09958aa6778e4499d34f5949d6f5677f2c6) - hrc.rules - > hrc.rule *(commit by @HsiangNianian)*
- [`23ab264`](https://github.com/HydroRoll-Team/HydroRollCore/commit/23ab264ebe52bd050e02c5c6a009645a252a5ea0) - **rule**: change self.state with self.core.rule_state logic *(commit by @HsiangNianian)*
- [`c0518c1`](https://github.com/HydroRoll-Team/HydroRollCore/commit/c0518c138914b321d0fa2d7b0d1377f78ff85b3c) - rename as get_plugin() method *(commit by @HsiangNianian)*
- [`0ed1048`](https://github.com/HydroRoll-Team/HydroRollCore/commit/0ed10486f719c23ab7e0e84d2e119a7fa5f70475) - rewrite core business logic *(commit by @HsiangNianian)*
- [`9f7019a`](https://github.com/HydroRoll-Team/HydroRollCore/commit/9f7019a860d3ff10b0f2cf885d8b9df547a6fa5e) - **core**: fix AttributeError: wrong '_run_core_reload' method *(commit by @HsiangNianian)*
- [`7e655c9`](https://github.com/HydroRoll-Team/HydroRollCore/commit/7e655c96fa5fab04bde014b62c8db3f4b352a5dc) - **core**: fix AttributeError: wrong 'rule_disable_hook_func' method *(commit by @HsiangNianian)*

### Chores
- [`2c769a1`](https://github.com/HydroRoll-Team/HydroRollCore/commit/2c769a1958feff811424410291edd7686af40d89) - **docs**: Update README.rst *(commit by @HsiangNianian)*
- [`fce296c`](https://github.com/HydroRoll-Team/HydroRollCore/commit/fce296c7b4c92506a5ed92af83425dc80f4d1486) - add dist into .gitignore file *(commit by @HsiangNianian)*
- [`0f74df0`](https://github.com/HydroRoll-Team/HydroRollCore/commit/0f74df0e709672118f06cec1c6fdd02ccfa31e63) - **file tree**: add CustomRule class in hrc.rules.BaseRule *(commit by @HsiangNianian)*
- [`890a7a2`](https://github.com/HydroRoll-Team/HydroRollCore/commit/890a7a28f4c9075a32240725cd2b51636cab5c1e) - commented unused code *(commit by @HsiangNianian)*
- [`11f4bff`](https://github.com/HydroRoll-Team/HydroRollCore/commit/11f4bffa9934838198330be7deafb04151ea00b9) - **examples**: remove commented code *(commit by @HsiangNianian)*
- [`9558df0`](https://github.com/HydroRoll-Team/HydroRollCore/commit/9558df091151d58aa7433c79ac3b8e050674c6fc) - move COC7 folder into rules folder *(commit by @HsiangNianian)*


## [v0.0.2-alpha.2] - 2024-06-26
### BREAKING CHANGES
- due to [`f38ab2f`](https://github.com/HydroRoll-Team/HydroRollCore/commit/f38ab2f073cc6599ef4d4248a00fe07a74d0e63b) - revert for two previous commit *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*:

  revert for two previous commit


### New Features
- [`09413f0`](https://github.com/HydroRoll-Team/HydroRollCore/commit/09413f06949b421a1c5b0cc05d70d84b184d3397) - **rust**: wrap_pyfunction "process_rule_pack" in libcore module *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`fdee348`](https://github.com/HydroRoll-Team/HydroRollCore/commit/fdee34884c29216db2a6bdb7e5c714af2e780777) - **cli|project**: add Cli class && hrc entry in project.scripts section *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Bug Fixes
- [`416f5f0`](https://github.com/HydroRoll-Team/HydroRollCore/commit/416f5f04121677784b783c37dcf33b444b7c8aa2) - **ci**: fix "failed to run custom build command" *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Refactors
- [`6e555bf`](https://github.com/HydroRoll-Team/HydroRollCore/commit/6e555bf5c16815cf0982ba5891e3bbe09444091a) - **filetree**: docs -> document, features -> feature, dev -> development *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`a2477b2`](https://github.com/HydroRoll-Team/HydroRollCore/commit/a2477b28057251c4685dbf0b56359dee7b595bfa) - **filetree**: rename package's namespace as `hrc` *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Chores
- [`272310e`](https://github.com/HydroRoll-Team/HydroRollCore/commit/272310ebd50978941f9e604fa217256b8a92fdbc) - **docs**: update file *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`28a7b2e`](https://github.com/HydroRoll-Team/HydroRollCore/commit/28a7b2ecd90e7e67427682a99b8616e13042b4ab) - refresh source tree files *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ab3ea64`](https://github.com/HydroRoll-Team/HydroRollCore/commit/ab3ea641736657fd65fef673940022b8f671d83a) - Update README.rst *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`aef878f`](https://github.com/HydroRoll-Team/HydroRollCore/commit/aef878f63472bc5deadd4851b3905a4fdbdbe912) - Update README.rst *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ea840bb`](https://github.com/HydroRoll-Team/HydroRollCore/commit/ea840bbc63843bd605a00da31f80241a4f2a9746) - **deps|rust**: add clap dependencies *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`d241a9a`](https://github.com/HydroRoll-Team/HydroRollCore/commit/d241a9a0e743ff66a2961603dd44f398fb683885) - **format**: ruff lint code *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`543c06f`](https://github.com/HydroRoll-Team/HydroRollCore/commit/543c06fb61bf8c5d7bc83030d1ab45a0d5430620) - **deps**: delete features of pyo3 in Cargo.toml *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`62b9be2`](https://github.com/HydroRoll-Team/HydroRollCore/commit/62b9be2ef081517eb17cd1f32bc432ccbfda9e83) - **ci|deps**: use python3.9 && change into abi3-py37 ^^ *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`d3d289b`](https://github.com/HydroRoll-Team/HydroRollCore/commit/d3d289bcfb9252bec6fc6db3f0ce408905ac5266) - **deps**: update features of pyo3 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`eba876a`](https://github.com/HydroRoll-Team/HydroRollCore/commit/eba876aabb7335c8e3330cec924e74765c1126d7) - **deps**: delete features of pyo3 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`02dfe51`](https://github.com/HydroRoll-Team/HydroRollCore/commit/02dfe519450784f0e60e5076a9c476dda2f50827) - **deps**: update features of pyo3 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`2e5b7e8`](https://github.com/HydroRoll-Team/HydroRollCore/commit/2e5b7e8ab75e0d80066d1ef5619d10fe827fd5a8) - **deps**: remove pip deps from dev group *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`dcadac7`](https://github.com/HydroRoll-Team/HydroRollCore/commit/dcadac73813291a86a4ab3aca44706fc9b8e3b5e) - **docs**: add structures.svg and contributing guidance *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`97bf2ba`](https://github.com/HydroRoll-Team/HydroRollCore/commit/97bf2ba7a00cb594b4e17a85d0e3630f0f50a97d) - **docs**: update README.rst *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`08025ec`](https://github.com/HydroRoll-Team/HydroRollCore/commit/08025ec6b32078840e26d4584a7e79ad12cd62f2) - **project**: bump version to 0.0.2-alpha.2 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

[v0.0.2-alpha.2]: https://github.com/HydroRoll-Team/HydroRollCore/compare/v99.99.99...v0.0.2-alpha.2
[v0.0.2]: https://github.com/HydroRoll-Team/HydroRollCore/compare/v0.0.2-alpha.2...v0.0.2
[v0.0.3]: https://github.com/HydroRoll-Team/HydroRollCore/compare/v0.0.2...v0.0.3
