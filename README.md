# 科研 Skills 整合包

面向管理学、组织行为、心理学和教育学研究，供 Codex 按任务调用：多来源调研、论文精读、文献综述、写作优化、实证研究协作。每个目录是独立技能，可以单独安装。技能提供工作方法，不替代研究判断、实际文献查证或统计软件。

## 让 Codex 自动安装

将仓库链接发给 Codex，并告诉它“请安装这个仓库里的全部科研 skills”。Codex 可以读取本 README 并完成安装。

给 Codex 的安装指引：使用可用的 skill-installer，从 `Roxxxxxxy-yyy/research-skills-pack` 的 `main` 分支安装以下五个独立技能目录到当前用户的 Codex skills 目录：

- `skills/active-research`
- `skills/paper-deep-reading`
- `skills/systematic-literature-review`
- `skills/anti-defensive-writing`
- `skills/auto-empirical-research-skills`

将每个目录完整安装，保留其 references 和 LICENSE；不要只复制 SKILL.md。遵守当前网络和文件权限；如果已有同名技能，不覆盖，列出冲突并安装其余技能。安装完成后告知结果，建议新建会话后尝试调用。联网失败时报告具体问题。此包是五个独立技能，不需要安装整套上游 AERS 或运行仓库中的安装脚本。

## 手动安装

下载本仓库，将 `skills` 下想用的技能文件夹复制到 Codex 用户技能目录 `~/.codex/skills/`（Windows 通常为 `C:\Users\你的用户名\.codex\skills\`）；文件夹内应直接包含 `SKILL.md`。重启 Codex 或新建会话后使用。已有同名技能时先备份并检查，避免覆盖自己的版本。

## 使用示例

- “用 active-research 梳理组织认同的近期研究，列出来源和证据边界。”
- “用 paper-deep-reading 精读这篇论文，区分作者结论和你的评价。”
- “用 systematic-literature-review 制定检索策略并记录筛选过程。”
- “用 anti-defensive-writing 润色这段讨论，保留结果和必要限定。”
- “用 auto-empirical-research-skills 帮我检查这项问卷研究的设计和分析计划。”

联网能力、全文访问和软件是否可用取决于实际环境；请核查 AI 生成的引用和结果。实证技能是轻量指导，不包含完整 AERS 库，也不自带 SPSS、R 或统计依赖。

各组件来源、修改和许可见 [SOURCES.md](SOURCES.md)。
