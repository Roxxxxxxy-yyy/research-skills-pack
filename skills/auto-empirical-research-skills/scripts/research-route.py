import pathlib,json,sys,importlib.util,os
ROOT=pathlib.Path(os.environ.get('AERS_LIBRARY_ROOT', str(pathlib.Path(os.environ.get('CODEX_HOME', pathlib.Path.home() / '.codex')) / 'aers-library-371a40e'))).expanduser()
q=' '.join(sys.argv[1:]).lower()
paths=[]
if any(k in q for k in ['2×2','2x2','ancova','因子实验','重复测量','前后测','randomized experiment','实验设计','随机实验','factorial']):
 paths += ['skills/25-HosungYou-Diverga/skills/c1/SKILL.md','skills/25-HosungYou-Diverga/skills/e1/SKILL.md']
if any(k in q for k in ['multilevel','mixed effects','混合效应','多层模型','班级聚类']):
 paths += ['skills/25-HosungYou-Diverga/skills/e1/SKILL.md','skills/17-DAAF-Contribution-Community-daaf/dot-claude/skills/statsmodels/SKILL.md']
if any(k in q for k in ['三重交互','johnson','简单斜率','调节中介']):
 paths += ['skills/61-phdemotions-research-methods/skills/process-model/SKILL.md']
if any(k in q for k in ['spss','量表','sem','信效度','测量等值']):
 paths += ['skills/74-brycewang-spss-amos-sem/spss-amos-sem/SKILL.md']
if any(k in q for k in ['文献综述','prisma','系统综述']):
 paths += ['skills/52-keemanxp-slr-prisma/SKILL.md','skills/36-taoyunudt-literature-review-skill/SKILL.md']
if any(k in q for k in ['doi','核验','参考文献']):
 paths += ['skills/62-PHY041-claude-skill-citation-checker/SKILL.md']
spec=importlib.util.spec_from_file_location('finder',ROOT/'scripts/find-skill.py'); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
# Hand-written matches are only suggestions; always include broad catalog results,
# even when a common keyword matched, so mixed tasks do not lose coverage.
paths += [s['path'] for _,s in mod.load_index().search(q,5)]
result=[]
for rel in dict.fromkeys(paths):
 p=ROOT/rel
 if not p.is_file(): raise FileNotFoundError(p)
 t=p.read_text(encoding='utf-8'); name=next((l[5:].strip() for l in t.splitlines() if l.startswith('name:')),p.parent.name)
 result.append(dict(name=name,path=str(p),exists=True))
print(json.dumps(result,ensure_ascii=False,indent=2))

