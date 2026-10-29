---
name: auto-empirical-research-skills
description: Route empirical research in management, organizational behavior, psychology and education to relevant AERS skills for experimental design, statistics, SEM, literature verification, academic writing and reproducibility. Select methods according to the question, design, and data. Use the catalog on demand.
license: CC-BY-SA-4.0
---
# AERS 科研技能路由

完整资料库默认位于 `${CODEX_HOME:-$HOME/.codex}/aers-library-371a40e`，可用环境变量 `AERS_LIBRARY_ROOT` 指定；资料库必须放在技能扫描目录之外。确认 `catalog/skills.json`、`scripts/find-skill.py`、`skills/` 存在。若缺失，先依据本整合包 README 的 AERS 安装步骤取得固定版本和子模块，再验证；不可用时说明并正常开展研究，不假称已加载。

按需阅读 [中文科研技能索引](references/中文科研技能索引.md) 或运行 `python <本技能目录>/scripts/research-route.py "任务描述"`；需要更广检索时运行资料库的 `scripts/find-skill.py` 或查询 `catalog/skills.json`。搜索结果仅是候选，结合研究问题、设计和数据选择 1–3 项，必要时扩展；读取各子技能的准确 SKILL.md 和需要的参考资料。避免完整输出大型目录。实验与其他实证研究同等重视，不默认某个统计模型。

按任务参考 [科研协作操作要点](references/科研协作操作要点.md)。严禁捏造或选择性报告数据和结果；原始数据只读，清洗另存并记录规则，区分探索与验证、模拟与真实。未获许可不上传未公开数据。73 p-hacking 仅用于教学、检测和审计。核查所需软件与实际运行结果，不把技能名称当作方法已经执行的证明；遵守各子合集许可。

本路由改编自 AERS，版本 371a40e，原始来源和许可见本技能 LICENSE 和整合包 SOURCES.md。
