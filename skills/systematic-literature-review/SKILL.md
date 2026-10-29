---
name: systematic-literature-review
description: 多来源检索、去重、筛选和证据提取，撰写可追溯的系统综述，并导出可编辑 Word 和 PDF。用于系统文献综述、范围综述及结构化文献调研。
---

# Systematic literature review — Codex

1. 从用户任务确定研究问题、检索范围、时间窗口、纳入排除标准、语言和交付格式。已有明确约束时直接开展工作。
2. 使用 Codex 原生网络检索与网页阅读工具，结合 OpenAlex、Crossref、Semantic Scholar、arXiv 和学科适用的公开数据库。记录真实查询式、检索时间、来源、结果和访问限制；不得声称检索了未访问的数据库。需要 API 密钥时使用用户已有授权，不编造访问权。
3. 去重并逐篇筛选；保存排除理由、真实筛选计数、题录、DOI、原文链接和证据卡。区分摘要推断与全文证据、预印本与同行评审论文。自动相关性评分辅助筛选，不替代明确标准。
4. 围绕问题综合方法、样本、结果、偏倚和证据局限；核验每条引用。系统综述保留必要的方法与可复现检索信息。不要捏造研究结果、统计量、筛选数量或参考文献，也不要为满足数量比例添加无关论文。
5. 输出长度和引文格式服从用户及目标期刊要求。未明确规模时采用与问题相称的范围，不自动承诺顶刊水平或固定上百篇文献。
6. 导出 Word 与 PDF 时优先使用当前可用的 documents、pdf 技能与内置运行时，并按其流程渲染核验。LaTeX、BibTeX 为需要时的附加交付；外部 Pandoc/TeX 不可用时使用 Word/PDF 路线并说明真实限制。

## Packaged pipeline

上游详细流程见 [references/upstream-SKILL.md](references/upstream-SKILL.md)，数据结构及配置见本目录的 config.yaml、references/ 与 scripts/。按需阅读，不将上游的 Claude 工具名、固定数量预算、隐藏方法信息或 Unix 路径要求应用于 Codex。

通过 load_workspace_dependencies 获取 Python 路径；如不可用，使用本机可用 Python。所需依赖在 requirements.txt 中；按任务检查后安装到本技能的 .python-deps，勿将其他机器的依赖目录直接复制过来。运行脚本使用 `python <本技能绝对路径>/scripts/codex_run.py <script.py> [arguments]`，包装器会加载本技能隔离的 .python-deps。先读取脚本或运行 --help，再传递参数。所有输出保存在当前项目的独立研究目录；必要时将 SLR_SCOPE_ROOT 设置为该目录。联网命令遵循当前工具权限。

