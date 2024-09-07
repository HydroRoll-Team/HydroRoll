# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.1.9-alpha.2] - 2024-09-07
### Chores
- [`11970c0`](https://github.com/HydroRoll-Team/HydroRoll/commit/11970c0e42e5db0ceff1dae64672e484baae5535) - **docs**: update build-api workflow to remove API docs *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`d6c2085`](https://github.com/HydroRoll-Team/HydroRoll/commit/d6c208583ef98fec27c51e9e32ccfe601078c360) - **workflow**: downgrade actions/download-artifact to v3 *(PR [#107](https://github.com/HydroRoll-Team/HydroRoll/pull/107) by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`8540cb8`](https://github.com/HydroRoll-Team/HydroRoll/commit/8540cb842c22aa431b8f6ae017b4c69c717e5410) - **deps**: update cargo dependencies *(PR [#108](https://github.com/HydroRoll-Team/HydroRoll/pull/108) by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`7103a54`](https://github.com/HydroRoll-Team/HydroRoll/commit/7103a54bc899bcf1725ee844310123c19bb52637) - **workflow**: update inputs for version in workflows *(PR [#110](https://github.com/HydroRoll-Team/HydroRoll/pull/110) by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`3e8c3d7`](https://github.com/HydroRoll-Team/HydroRoll/commit/3e8c3d78b17ad9efde8aea62077ec4308fb0c9d3) - **deps**: update cargo dependencies *(PR [#108](https://github.com/HydroRoll-Team/HydroRoll/pull/108) by [@HsiangNianian](https://github.com/HsiangNianian))*


## [v0.1.9-alpha.1] - 2024-09-07
### BREAKING CHANGES
- due to [`e2c9fe7`](https://github.com/HydroRoll-Team/HydroRoll/commit/e2c9fe71fd6133f9c97943cd6c7d664a73e94ab0) - setup docs toc tree *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*:

  setup docs toc tree

- due to [`4e4c53e`](https://github.com/HydroRoll-Team/HydroRoll/commit/4e4c53ed9377f573a59b930407b903f8918959b6) - add cc 1.0 and mit license *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*:

  add cc 1.0 and mit license

- due to [`b5aba5f`](https://github.com/HydroRoll-Team/HydroRoll/commit/b5aba5f4bd40d88f10ce0ccd298f6eec61bc98e5) - bump time and num_threads crates ([#104](https://github.com/HydroRoll-Team/HydroRoll/pull/104)) *(PR [#105](https://github.com/HydroRoll-Team/HydroRoll/pull/105) by [@HsiangNianian](https://github.com/HsiangNianian))*:

  bump time and num_threads crates (#104) (#105)


### New Features
- [`357db22`](https://github.com/HydroRoll-Team/HydroRoll/commit/357db22d9cac9e40d7364f0a9b6606b130382210) - **bones**: add submodule hydro_roll_core *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`67a4e90`](https://github.com/HydroRoll-Team/HydroRoll/commit/67a4e90568903200102ca369e3522d9093877277) - **docs**: enable docs preview *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`b07b7ec`](https://github.com/HydroRoll-Team/HydroRoll/commit/b07b7ec21285536d7f6f21a9752ca11bcf330d44) - **bones**: add nivis-python submodule *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`2bc0635`](https://github.com/HydroRoll-Team/HydroRoll/commit/2bc0635742cfbad16e16388a42e3a6c97e5153d5) - **project**: add scripts interface named "atien" *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`a5f1a55`](https://github.com/HydroRoll-Team/HydroRoll/commit/a5f1a55920ad7ddaaac0104dc10b3bc985bb0ae2) - **workflows**: build api triggered *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`e30752e`](https://github.com/HydroRoll-Team/HydroRoll/commit/e30752e59013997351399420412785973e56fd2f) - **docs**: add script for run dev server with Makefile *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`1605bd6`](https://github.com/HydroRoll-Team/HydroRoll/commit/1605bd66ab97a206e4698954d47b10d87b09ec2d) - add router-guards for site *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`d77828d`](https://github.com/HydroRoll-Team/HydroRoll/commit/d77828d97ee98792e50a034f905cd3894807d5ff) - add Vue code snippets for faster development *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`731d318`](https://github.com/HydroRoll-Team/HydroRoll/commit/731d318b4d5f279ea58f0688353a011a41532f42) - add video background to index page *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`e3ddb39`](https://github.com/HydroRoll-Team/HydroRoll/commit/e3ddb391b9a6b047af37eb1633e114edb598e91b) - update favicon path in index.html *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`65c8f78`](https://github.com/HydroRoll-Team/HydroRoll/commit/65c8f781eff477f65183a480a9f63255a2f8f77f) - force play bg video *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`5656f85`](https://github.com/HydroRoll-Team/HydroRoll/commit/5656f85eab324e13a5c66a49b0994a96f1acffec) - adjust UI components for better portrait view *(commit by [@NtskwK](https://github.com/NtskwK))*

### Bug Fixes
- [`9a8beed`](https://github.com/HydroRoll-Team/HydroRoll/commit/9a8beed071512f013a3c0afe50ab7e84a37e6024) - **docs**: remove infini import *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`a0c9308`](https://github.com/HydroRoll-Team/HydroRoll/commit/a0c93083eba37761b266a0bfefd1d76ea2120dab) - **readme**: correct pronounce *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`93d2670`](https://github.com/HydroRoll-Team/HydroRoll/commit/93d2670039f7d68546a68eb0a917209b393b6527) - **gitmodules**: add branch for sub modules *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`4e4c53e`](https://github.com/HydroRoll-Team/HydroRoll/commit/4e4c53ed9377f573a59b930407b903f8918959b6) - **license**: add cc 1.0 and mit license *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`d39faa0`](https://github.com/HydroRoll-Team/HydroRoll/commit/d39faa0fba9cdedbcfdddb6728ea6f9dd72ecdc8) - **docs**: depth limit for chapter I *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ac0a560`](https://github.com/HydroRoll-Team/HydroRoll/commit/ac0a56074bfe3b87b762b17ee7b7f1ee89eac502) - **docs**: toc tree repair *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`990236b`](https://github.com/HydroRoll-Team/HydroRoll/commit/990236b37073f6858a16b2e2056d3ed9bf6ae3aa) - **docs**: toc tree repair *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`31de219`](https://github.com/HydroRoll-Team/HydroRoll/commit/31de219af4430121ebc0d26e8dd0b7c57e3ec399) - **docs**: toc tree repair *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`a4c6355`](https://github.com/HydroRoll-Team/HydroRoll/commit/a4c6355d994d26a5413bc350f3e7a57f344296f2) - **docs**: changelog.rst -> changelog.md *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`455ca3e`](https://github.com/HydroRoll-Team/HydroRoll/commit/455ca3e3db84f36ae9464468de54f7aa693a3dd2) - **docs**: toc tree repair *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`1257f4b`](https://github.com/HydroRoll-Team/HydroRoll/commit/1257f4b85f15872b6f73facaccddea9094751063) - **docs**: toc tree repair *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`99a2823`](https://github.com/HydroRoll-Team/HydroRoll/commit/99a2823e6477f52cb2f16366a3a37f3cb05b289f) - **docs**: toc tree repair *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`5597a8a`](https://github.com/HydroRoll-Team/HydroRoll/commit/5597a8af382e256951d3813aad1cedf41fcde9ac) - **docs**: toc tree repair *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`571611a`](https://github.com/HydroRoll-Team/HydroRoll/commit/571611a0958382b0d8c69e283879b52856a47090) - **readme**: fix **webui** render shape *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`b5aba5f`](https://github.com/HydroRoll-Team/HydroRoll/commit/b5aba5f4bd40d88f10ce0ccd298f6eec61bc98e5) - **deps**: bump time and num_threads crates ([#104](https://github.com/HydroRoll-Team/HydroRoll/pull/104)) *(PR [#105](https://github.com/HydroRoll-Team/HydroRoll/pull/105) by [@HsiangNianian](https://github.com/HsiangNianian))*
  - :arrow_lower_right: *fixes issue [#104](https://github.com/HydroRoll-Team/HydroRoll/issues/104) opened by [@HsiangNianian](https://github.com/HsiangNianian)*

### Refactors
- [`679ca51`](https://github.com/HydroRoll-Team/HydroRoll/commit/679ca51b78cda9044dc8d8eb3fa246fd76cb227e) - **cli**: rename class Cli as "Atien" *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ac0dbc5`](https://github.com/HydroRoll-Team/HydroRoll/commit/ac0dbc5b1c9b48079e3a450794030b3e0bc6096a) - **site**: rewrite with vuejs *(PR [#93](https://github.com/HydroRoll-Team/HydroRoll/pull/93) by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`e2c9fe7`](https://github.com/HydroRoll-Team/HydroRoll/commit/e2c9fe71fd6133f9c97943cd6c7d664a73e94ab0) - **docs**: setup docs toc tree *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`525de52`](https://github.com/HydroRoll-Team/HydroRoll/commit/525de52d687b44fb14be7da2c46c548eb8a32fbd) - **examples**: update file tree *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`a1a20e5`](https://github.com/HydroRoll-Team/HydroRoll/commit/a1a20e51d6c9efea406cf18facf707ea50e3d18c) - Optimize the structure of the code *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`b336845`](https://github.com/HydroRoll-Team/HydroRoll/commit/b336845dac0567bfce09dc0d4ffd6e27b1bc3d66) - Optimize the cache of changelog *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`72a79bd`](https://github.com/HydroRoll-Team/HydroRoll/commit/72a79bd525e72f80c6b46b4514f0e6bb4c3cc07a) - **site**: move site to HydroRoll-site repo *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Chores
- [`93f23ba`](https://github.com/HydroRoll-Team/HydroRoll/commit/93f23ba52b24d352891d3b39dac1e97612b732cf) - **readme**: update profile *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ac876a4`](https://github.com/HydroRoll-Team/HydroRoll/commit/ac876a4519a6987df95d5cac9ce7f4968e5f4809) - **readme**: update profile *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`0415601`](https://github.com/HydroRoll-Team/HydroRoll/commit/04156018dcf7e7813d18083eaa2b88c006629fa7) - **readme**: update profile *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`6fd080e`](https://github.com/HydroRoll-Team/HydroRoll/commit/6fd080e9a7130682a5e53c8c81b199eac1726029) - **docs**: uncomment code *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`c6bd76e`](https://github.com/HydroRoll-Team/HydroRoll/commit/c6bd76ebec81e22898bfb9054b1eda2b1c24342c) - **readme**: add docs status *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ca49233`](https://github.com/HydroRoll-Team/HydroRoll/commit/ca492339aaf149231b3106dd9109d244aa142875) - **readme**: update profile *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`9e568c4`](https://github.com/HydroRoll-Team/HydroRoll/commit/9e568c4b886f361e97c2f03a28880b06398c7d2c) - **readme**: update profile *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ec57636`](https://github.com/HydroRoll-Team/HydroRoll/commit/ec576369137a3b22b5eb7178777cf4f54976e2d7) - **project**: fix authors *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`13aecc2`](https://github.com/HydroRoll-Team/HydroRoll/commit/13aecc2ac55d703145a95779719710ca0b3ef4bf) - **submodule**: sync nivis_python *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`1ac8738`](https://github.com/HydroRoll-Team/HydroRoll/commit/1ac87386f9295f9e57ac7055f3ddc5a7d2458736) - **readme**: update readme *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`2c400c2`](https://github.com/HydroRoll-Team/HydroRoll/commit/2c400c23db91b4fe33f38fb988991a5c4a259c55) - **deps**: bump follow-redirects from 1.15.3 to 1.15.5 in /site *(PR [#94](https://github.com/HydroRoll-Team/HydroRoll/pull/94) by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`ce65463`](https://github.com/HydroRoll-Team/HydroRoll/commit/ce65463177512c8fb385e8ab2c3c31a6596ce9bd) - **gitmodules**: fmt pages *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`38ca529`](https://github.com/HydroRoll-Team/HydroRoll/commit/38ca529bd3e937416a2b3ffd5814aaef5911f26c) - **gitmodule**: delete modules *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`ab670c2`](https://github.com/HydroRoll-Team/HydroRoll/commit/ab670c2993bd3943b0fa743afc4a89622181fc2e) - **submodule**: add core and nivis *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`c4d13f3`](https://github.com/HydroRoll-Team/HydroRoll/commit/c4d13f375a4f8ac8942f24cbfe63ded420f1e04e) - delete .husky *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`861ec02`](https://github.com/HydroRoll-Team/HydroRoll/commit/861ec02a05c1bcd22d878d2f29b615dc553c3a69) - **project**: add printpdf deps for rust *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`1dec684`](https://github.com/HydroRoll-Team/HydroRoll/commit/1dec684f34ee7d52737cd33fa0a37a0de011894e) - **project**: sync cargo and pyproject *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`2a43b45`](https://github.com/HydroRoll-Team/HydroRoll/commit/2a43b4540ffd94667b4cf1aaac04654497f7f692) - **docs**: complete page *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`5555113`](https://github.com/HydroRoll-Team/HydroRoll/commit/5555113f058304edc77ad72b412f6318c313c1e5) - **docs**: complete pages for about chapter *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`c0abf6b`](https://github.com/HydroRoll-Team/HydroRoll/commit/c0abf6bffbf1ec4e4b992b10ab3f548fd719affe) - **docs**: complete pages content for about chapter *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`e5f3bc6`](https://github.com/HydroRoll-Team/HydroRoll/commit/e5f3bc6f0f832a9617432fe488c7a89e8b5f444d) - **deps**: bump the npm_and_yarn group across 1 directory with 2 updates *(PR [#96](https://github.com/HydroRoll-Team/HydroRoll/pull/96) by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`8f9b49e`](https://github.com/HydroRoll-Team/HydroRoll/commit/8f9b49eb2151607e546ead7f34ede1762b3e1e4b) - **readme**: add badge for CodeQL *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`6ea6359`](https://github.com/HydroRoll-Team/HydroRoll/commit/6ea635975a770cb8f95d544534a10a370663c63c) - **readme**: sync with banner fix *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`1a8296d`](https://github.com/HydroRoll-Team/HydroRoll/commit/1a8296d9a698185406fe4e72678dc430fff0760a) - Update README.rst *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`5a3d0c9`](https://github.com/HydroRoll-Team/HydroRoll/commit/5a3d0c96a7b62e82a43eff9e5a7fd7dd15985b95) - Update .gitmodules *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`9e5f95a`](https://github.com/HydroRoll-Team/HydroRoll/commit/9e5f95a735c6e7884feeeaeb95557499c1f39240) - **deps**: rename package && add more docs deps *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`a9f6964`](https://github.com/HydroRoll-Team/HydroRoll/commit/a9f696460e0e3a2b5b2509c08f7841996a643e56) - **deps**: add dev deps maturin ^^ *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`e914584`](https://github.com/HydroRoll-Team/HydroRoll/commit/e914584e3e441a5b875e68d9443d99a745164e34) - **deps**: add ruff dev deps for lint code *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`dfec9f9`](https://github.com/HydroRoll-Team/HydroRoll/commit/dfec9f99d1726b3c3a4e9426f50c955fcaddb623) - **format**: ruff lint code *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`e960ff1`](https://github.com/HydroRoll-Team/HydroRoll/commit/e960ff10b9e9a0d8c9842d23aa278d524b7de124) - **deps**: remove IDE-related files from .gitignore *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`7b6a0d4`](https://github.com/HydroRoll-Team/HydroRoll/commit/7b6a0d472c88f55e6f31aa633099f96cd28be8b5) - solve the anomalies of  appearance *(commit by [@NtskwK](https://github.com/NtskwK))*
- [`09f5a26`](https://github.com/HydroRoll-Team/HydroRoll/commit/09f5a2634c1817780a068a224d1d0f21f8e18009) - **deps**: bump axios *(PR [#99](https://github.com/HydroRoll-Team/HydroRoll/pull/99) by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`8a32052`](https://github.com/HydroRoll-Team/HydroRoll/commit/8a32052835e155b5577fe15cd2b09b7aa56a8d65) - **readme**: update intro content *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`30b6798`](https://github.com/HydroRoll-Team/HydroRoll/commit/30b679877d1360d932d6a45f963c12f011fca89a) - **deps**: bump actions/download-artifact *(PR [#103](https://github.com/HydroRoll-Team/HydroRoll/pull/103) by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`93a01aa`](https://github.com/HydroRoll-Team/HydroRoll/commit/93a01aafb3a58bf08be48ae3b7bfb5d44a25b87e) - **deps**: bump cargo dependencies *(PR [#106](https://github.com/HydroRoll-Team/HydroRoll/pull/106) by [@HsiangNianian](https://github.com/HsiangNianian))*


## [v0.1.8-alpha.2] - 2024-02-27
### Bug Fixes
- [`0013c4f`](https://github.com/HydroRoll-Team/HydroRoll/commit/0013c4ffe35ecd1c65fdf0d77bb741696a2ae1a2) - **workflow**: update release step, add pypi_api_token *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`48bea2a`](https://github.com/HydroRoll-Team/HydroRoll/commit/48bea2a9641ad49f3425b16a14fd1451de1e0203) - **project**: change version to 0.1.8-alpha.2 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*


## [v0.1.8-alpha.1] - 2024-02-27
### Bug Fixes
- [`e4612c2`](https://github.com/HydroRoll-Team/HydroRoll/commit/e4612c2bdf0e501bc51f99d51eb73a0ee47a6ce0) - **project**: change version to 0.1.8-alpha.1 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*

### Chores
- [`17dc291`](https://github.com/HydroRoll-Team/HydroRoll/commit/17dc2911204fa9e3d247f97c67666e2cf3e27061) - **readme**: update uri *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`f106d69`](https://github.com/HydroRoll-Team/HydroRoll/commit/f106d69a8a04a13dd20635039089758a24045186) - **readme**: add logo for python_v *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`48ad461`](https://github.com/HydroRoll-Team/HydroRoll/commit/48ad461ca568212f7972f7de3195803aa01da28a) - **project**: bump version from 0.1.7 to 0.1.8a1 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*


## [v0.1.8a1] - 2024-02-27
### Chores
- [`17dc291`](https://github.com/HydroRoll-Team/HydroRoll/commit/17dc2911204fa9e3d247f97c67666e2cf3e27061) - **readme**: update uri *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`f106d69`](https://github.com/HydroRoll-Team/HydroRoll/commit/f106d69a8a04a13dd20635039089758a24045186) - **readme**: add logo for python_v *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*
- [`48ad461`](https://github.com/HydroRoll-Team/HydroRoll/commit/48ad461ca568212f7972f7de3195803aa01da28a) - **project**: bump version from 0.1.7 to 0.1.8a1 *(commit by [@HsiangNianian](https://github.com/HsiangNianian))*


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
[v0.1.8a1]: https://github.com/HydroRoll-Team/HydroRoll/compare/v0.1.7...v0.1.8a1
[v0.1.8-alpha.1]: https://github.com/HydroRoll-Team/HydroRoll/compare/v0.1.7...v0.1.8-alpha.1
[v0.1.8-alpha.2]: https://github.com/HydroRoll-Team/HydroRoll/compare/v0.1.8-alpha.1...v0.1.8-alpha.2
[v0.1.9-alpha.1]: https://github.com/HydroRoll-Team/HydroRoll/compare/v0.1.8-alpha.2...v0.1.9-alpha.1
[v0.1.9-alpha.2]: https://github.com/HydroRoll-Team/HydroRoll/compare/v0.1.9-alpha.1...v0.1.9-alpha.2
