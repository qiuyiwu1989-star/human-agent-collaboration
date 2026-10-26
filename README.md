# Human–Agent Collaboration · 人机协作方法库

可跨 Agent 复用的人机协作 Skills：理解目标、深入专业方法、引入跨领域技巧、验证成果、交接工作，并把真实协作经验逐步沉淀为可维护的方法。

这是一套持续扩展的方法库。目前包含统一检索入口、通用协作基础和人机共写；研究、产品设计、编程、内容制作等目前提供方法映射，尚未发布各自的专项技能。库不绑定个人资料、特定模型或付费服务。

## 统一入口

**[总调度与检索指南](GUIDE.md)**：按问题选方法、按证据选案例、按需组合调用，以及统一维护规则。完整条目仍由 JSON 目录管理。

## 技能目录

| Skill | 用途 |
| --- | --- |
| [collaboration-library](skills/collaboration-library/SKILL.md) | 统一入口：按问题、场景、关键词、ID、证据状态和关联条目检索 |
| [collaboration-methods](skills/collaboration-methods/SKILL.md) | 通用方法：目标、深度、跨领域、反馈、验证及 Agent 交接 |
| [human-ai-writing](skills/human-ai-writing/SKILL.md) | 场景方法：从经验提炼主张、补足证据、协作成稿 |

通用方法与专业领域技能配合使用。各技能可独立安装；参考文件按需读取，不需要每次加载整个库。多 Agent 复用不等于每项任务必须多 Agent 执行。

## 安装

先把仓库克隆到自己维护的位置：

```bash
git clone https://github.com/qiuyiwu1989-star/human-agent-collaboration.git
cd human-agent-collaboration
```

Codex：将选定的技能目录复制到技能目录中（默认路径如下）。若目标已存在，先比较修改，避免覆盖自己的版本。

```bash
mkdir -p ~/.codex/skills
cp -R skills/collaboration-library ~/.codex/skills/
cp -R skills/collaboration-methods ~/.codex/skills/
cp -R skills/human-ai-writing ~/.codex/skills/
```

其他 Agent：把选定的完整技能目录放到该 Agent 实际支持的技能目录；如不支持 Skill 发现，显式提供 SKILL.md 和本次所需参考文件。agents/openai.yaml 为可选 UI 元数据，核心方法不依赖它。请勿假设安装到一个 Agent 后会自动同步给所有 Agent。

长期在同一台机器维护时，也可以把各 Agent 的技能入口软链接到同一份本地仓库；在该环境允许链接时使用，并避免与已有安装同名。新会话是否能发现技能，以该 Agent 的实际技能清单为准。

## 结构化目录与检索

当前共有 **3 个可安装 Skill**，其中 collaboration-library 是检索入口，不是新增的一套协作理论。结构化目录包含 **53 个方法条目、4 个典型示例、5 个场景映射、14 个待运行评估用例、6 个实战复盘案例**。这些是不同粒度，不能相加称作 82 种方法。6 个实战案例标记为 reported-outcome（来源复盘报告），本轮独立复验的历史成功案例为 **0 条**。示例、历史报告和直接观察分开，不把上线或测试通过当成真实业务效果。

- 人阅读：[分类目录](skills/collaboration-library/references/index.md)。
- AI 调用：[统一检索 Skill](skills/collaboration-library/SKILL.md)。
- 程序集成：[JSON 目录](skills/collaboration-library/references/catalog.json) 与 [字段、证据及维护约定](skills/collaboration-library/references/schema.md)。

```text
使用 $collaboration-library，找适合“需求说不清、反复返工”的方法。
先给最相关的条目及证据状态，再按需应用，不扩大任务范围。
```

```bash
python3 skills/collaboration-library/scripts/search.py '需求说不清 原型'
python3 skills/collaboration-library/scripts/search.py --scenario 写作 --kind method
python3 skills/collaboration-library/scripts/search.py --id M02
python3 skills/collaboration-library/scripts/search.py --related M02 --full
python3 skills/collaboration-library/scripts/search.py --status observed-success
```

脚本仅依赖 Python 标准库，离线可用，输出 JSON。中文双元组与英文词匹配用于词法排序，不声称具备向量语义检索。无 Python 的 Agent 可直接浏览目录或过滤 JSON。单独复制 collaboration-library 目录即可检索完整卡片；sources 路径用于追溯完整仓库中的原文。

## 使用

```text
使用 $collaboration-methods。我的目标是……，必须保留……。
先判断最有用的路径，能推进的直接做，给我实际成果及验证依据。
```

```text
再深一层，先不扩大范围：从哪些原始材料开始？
采用什么实际方法？什么证据能推翻当前判断？
```

```text
使用 $human-ai-writing。以下是我的零散想法，帮我提炼主张，
补足关键缺口，再协作成稿。保留我的立场，不虚构经历。
```

遇到说不清标准、反复返工或需要提高任务价值时，可用 [发现未知与提升目标](skills/collaboration-methods/references/unknowns-and-ambition.md)：扫盲点、看样稿、提目标、设验证，按需要选用。

```text
先扫盲点：能查的自己查，说不清的给样稿，只问会改变做法的问题。
再给一个值得升级的版本，说明成本与验收，先别扩大执行范围。
```

跨会话或多人协同时使用 [最小交接包](skills/collaboration-methods/references/handoff.md)，传递当前目标、约束、版本、证据、待核事项和下一步。任务状态放在任务自己的空间，公共库仅保存可公开的方法与脱敏示例。

## 扩展与验证

新增技能应源于真实问题：写清适用场景、方法、产物、验证方式及边界。只为确有独立流程的场景新增技能；通用的小技巧优先补充参考文档。避免提前建一套没有实践内容的目录。

[评估用例](evaluations/scenarios.md) 用于检查行为是否符合方法；结构检查通过不能证明协作效果。请在实际使用中记录有效变化、失败条件和用户反馈，提交不含私有资料的改进。

## 本地经验挖掘

本轮补充来自协作契约、需求简报、设备接入、事故诊断、写作引擎、研讨沉淀、设计与记忆规范，以及项目复盘。详见 [检索范围与处理记录](docs/local-mining-2026-10-26.md)。公开库保存独立改写的方法和脱敏来源摘记，私人原件留在本地。

```bash
python3 skills/collaboration-library/scripts/search.py '负向测试 历史缺陷' --kind method
python3 skills/collaboration-library/scripts/search.py 'accepted 回读' --kind method
python3 skills/collaboration-library/scripts/search.py --status reported-outcome --full --limit 6
```

## 维护结构化条目

编辑 catalog.json 后运行：

```bash
python3 skills/collaboration-library/scripts/build_index.py
python3 -m unittest discover -s tests -v
```

每条记录保留稳定 ID、适用条件、步骤、产物、验证、来源及证据状态。原始技能修改后同步复核卡片；不要直接编辑自动生成的目录。真实经验必须有可公开的结果证据和适用边界才能入库，具体规则见数据约定。检索测试通过不等于 Agent 行为或业务效果已验证。

## 来源与许可

本库受 Felix Rieseberg 的 [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) 启发，围绕速度、目标层次、专业深度和跨领域方法，结合人机协作实践进行了独立编写。原文不属于本库许可范围，不代表原作者认可本项目。

本库原创内容采用 [MIT License](LICENSE)。

## English

A portable library of human–agent collaboration skills. The initial release includes a general collaboration skill and a co-writing skill. Skills are written in Chinese, are model-independent, and include task handoff guidance. Install only the skill folders you need; other agent environments may require their own discovery configuration. Core instructions do not depend on a specific connector or paid service.
