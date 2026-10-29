# 科研 Skills 整合包

适用于 Codex，面向管理学、组织行为学、心理学、教育学科研：深度调研、论文精读、系统文献综述、学术表达及实证研究。保留原技能的配套资料和脚本；AERS 通过单独安装的完整上游资料库按需路由，不预装统计软件。详细来源和许可见 [SOURCES.md](SOURCES.md)。

## 让 Codex 安装

把本仓库链接发给 Codex，并说：“请安装这个仓库的全部科研 skills 和完整 AERS 资料库，按 README 执行并验证。”支持 Mac 和 Windows 的 Codex；遵守当前网络和文件权限。安装需要联网，AERS 资料库需要 Git 与 Python。

给 Codex 的步骤：

1. 使用现有 skill-installer 将 `skills/active-research`、`skills/paper-deep-reading`、`skills/systematic-literature-review`、`skills/anti-defensive-writing`、`skills/auto-empirical-research-skills` 五个目录完整安装到当前用户 Codex skills 目录（默认 Mac 为 `~/.codex/skills`，Windows 为当前用户的 `%USERPROFILE%\.codex\skills`；若设置 `CODEX_HOME`，则使用该目录下的 `skills`）。保留 scripts、references、模板、示例和各自的 LICENSE。已有同名技能不得静默覆盖：先检查并说明冲突，询问是否替换，其他未冲突技能可继续安装。
2. 将 [完整 AERS 上游仓库](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) 安装到当前用户 Codex 数据目录下的 `aers-library-371a40e`：Mac 默认 `~/.codex/aers-library-371a40e`；Windows 默认 `%USERPROFILE%\.codex\aers-library-371a40e`；设置 `CODEX_HOME` 时使用该目录下的 `aers-library-371a40e`。上述是目录说明，不要把 Mac 的 shell 变量语法直接复制到 Windows。克隆后检出 `371a40e488c5d9e8e75ca2af5dd9667f8349c199`，再运行 `git submodule update --init --recursive`，并核对子模块状态及 `catalog/skills.json`、`scripts/find-skill.py` 和 `skills/`。该目录必须在 Codex skills 扫描目录之外。若目标已存在，检查来源和版本，勿覆盖或重置用户已有修改；也可用 `AERS_LIBRARY_ROOT` 指向已有兼容副本。克隆或子模块失败要如实报告，不得声称 AERS 安装完成。
3. 使用可用 Python 运行已安装路由技能的 `scripts/research-route.py "实验设计 randomized experiment"`，确认返回的路径存在且属于安装的资料库；再用一个问卷或文献任务检查。网络、Git、Python 不可用或路径验证失败时报告具体限制。新建 Codex 会话后，请用户用 `$auto-empirical-research-skills` 测试一次；文件安装和路由脚本验证不代表各子技能的统计模型已运行。
4. 文献综述的 Python 脚本依赖见其 `requirements.txt`。根据具体任务检查 Python 和依赖；需要时安装到该技能的 `.python-deps`（例如 `python -m pip install --target <该技能目录>/.python-deps -r <该技能目录>/requirements.txt`），不得从别的电脑复制平台相关依赖。先检查脚本再运行，不自动安装统计软件。仅阅读或指导任务不必预装全部依赖。

## 使用

Windows 上注意使用可用的 `py -3`、`python` 或 Codex 自带 Python；Mac 上使用可用的 `python3` 或 Codex 自带 Python。使用各系统正确的命令与路径，不假设软件已安装。需要 LaTeX、Pandoc 或其他程序的特定脚本，应按任务检查这些工具；一般调研、阅读与写作不需要事先安装它们。

新建会话，直接说“用论文精读技能分析这篇论文”，或“使用 AERS 选择适合这个问卷研究的方法”。Codex 可依据任务选择技能；也可以显式指定 `$paper-deep-reading`、`$systematic-literature-review` 或 `$auto-empirical-research-skills`。

文献检索、全文获取与统计软件取决于实际网络、授权和本机环境。核验 AI 引用与研究结论；不上传未经允许的未公开数据。上游资料库各子合集的许可和依赖可能不同，应按实际使用的技能核查。
