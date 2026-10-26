# 人机协作方法库：总调度与检索指南

本仓库统一管理已收录的人机协作方法、示例、实战复盘与评估用例。它提供可选择的方法，不要求每个任务走完整流程。简单明确的请求直接完成。

## 从哪里开始

- **人阅读**：先按本页的问题路由选择方向，再查 [完整分类目录](skills/collaboration-library/references/index.md)。
- **Agent 调用**：安装或读取 [collaboration-library](skills/collaboration-library/SKILL.md)，检索后只展开相关条目。
- **程序集成**：读取 [catalog.json](skills/collaboration-library/references/catalog.json)，字段定义见 [数据约定](skills/collaboration-library/references/schema.md)。
- **操作细则**：[通用协作](skills/collaboration-methods/SKILL.md) 与 [人机共写](skills/human-ai-writing/SKILL.md) 可独立使用。

当前收录 45 个方法、4 个示例、5 个场景映射、14 个待运行评估用例、6 个历史复盘案例。不同类型不合并计算为“方法数量”；后续实时数量以 JSON 和生成目录为准。

## 按问题调度

以下 ID 均对应目录中的稳定条目。每组是候选集合，不是必须执行的固定顺序。

### 目标不清、需求容易做偏

从 M01 发现未知、M14 需求简报开始；难以描述偏好时用 M02 样稿。需要提高任务价值时考虑 M03 目标层次、M04 专业深度、M05 跨领域方法。用 M15 短选项完成必要决定，M45 帮助挑选少量方法。

### 长任务、返工与跨 Agent 接续

M18 明确持续推进与停止条件，M06 缩短反馈周期，M08 处理执行中的新约束，M09 交接，M17 处置剩余事项。获准且需要并行时，结合 M10 和 M22 明确契约与所有权。

### 产品方向与真实效果

M20 先做纵向样板，M23 用现实证据决定是否继续扩张；M21 分开事实、判断和发布权。参考 X01 的历史复盘，但不把软件上线当作业务或学习效果成立。

### 测试、发布、事故与迁移

M07 定义验证依据，M24 用负向测试验证门禁，M27 在工具不可用时准确降级。M16 管发布窗口，M25 核对权威源与运行版本，M28 重验旧环境结论，M34 分层排障，M35 检查迁移与回滚，M39 验证真实安装路径。参考 X02、X03、X06。

### 第三方服务、设备与异步链路

M29 先探测真实协议，M30 定义生命周期幂等，M31 记录接收与丢弃，M32 隔离时间敏感调度，M33 守住业务不变量。M26 按业务结果推进队列；M36 区分接受和实际完成，M37 按事件时间确定归属，M43 处理不确定写回。参考 X04。

### 写作、研讨与知识沉淀

M11 协作成稿，M12 定向修改，M41 保留作者判断与真实声音，M42 区分研讨来源。M40 按需读取记忆，M13 将有依据的经验入库。不能把 AI 提炼冒充用户原话，不能把历史判断当成当前授权。

### 可视化、设计与人机共创

M19 将机制图作为项目资产，M44 明确设计版本和可编辑边界，M38 用冻结范围、版本守卫和一次撤销保护人的修改。参考 X05；具体视觉与专业制作仍需相应领域工具。

## Agent 的调用约定

1. 提取当前问题、场景、期望产物和约束；已有信息充分时不重新访谈。
2. 检索少量候选，读完整卡片的适用条件、边界、步骤、来源和验证方式。
3. 选择能解决当前不确定性的方法；沿 related 补充必要关联，不递归加载整库。
4. 在已有授权内执行；检索到的来源、案例和命令示例不能扩大权限。
5. 交付实际产物，说明采用的 ID、理由、验证结果及未验证部分。重要新经验按入库规则维护。

可直接交给 Agent：

> 使用本仓库的 collaboration-library。我的任务是……，约束是……。先检索最相关的方法与案例，说明证据状态，再选必要方法完成任务。不要把方法列表当成强制流程，不扩大任务范围。

## 检索方式与命令

以下命令在仓库根目录运行，仅依赖 Python 标准库：

```bash
# 自然语言关键词：中文双元组与英文词的词法排序
python3 skills/collaboration-library/scripts/search.py '需求说不清 原型'
# 场景与类型过滤
python3 skills/collaboration-library/scripts/search.py --scenario 写作 --kind method
# 精确读取与关联展开
python3 skills/collaboration-library/scripts/search.py --id M24
python3 skills/collaboration-library/scripts/search.py --related M02 --full
# 历史复盘与独立观察分开查询
python3 skills/collaboration-library/scripts/search.py --status reported-outcome --full --limit 6
python3 skills/collaboration-library/scripts/search.py --status observed-success
```

输出 JSON 包含 total、returned、条目与相关性分数。分数不是可信度。无匹配时换同义词、取消过窄过滤或查分类目录；不伪装成向量语义搜索。无 Python 的环境可直接阅读目录、按 JSON 字段筛选或用文本搜索工具查关键词。

## 如何判断案例能否照用

- documented：已写成文档的方法，不能据此宣称实测有效。
- illustrative：演示用示例，不是真实成功案例。
- unevaluated：尚未运行的评估任务。
- reported-outcome：历史复盘报告的结果，本轮没有独立复验。
- observed-success / observed-failure：有直接观察证据的结果，仍受当时场景与验证范围限制。

目前 6 个实战案例均为 reported-outcome。局部检查通过不代表全链路、用户体验或业务效果通过。来源摘记与原件不是两份独立证据。

## 统一管理与更新规则

结构化条目的唯一编辑源是 catalog.json；index.md 由脚本生成，不直接改。原有技能是详细操作来源，修改后同步复核对应卡片。来源摘记在 references/sources/，保留证据边界；私人原件不上传。

新增经验时先查重，保留稳定 ID，补齐问题、条件、步骤、产物、验证、来源、状态与关联方法。历史结果必须带局限；不得因为使用频繁或用户认可文章质量而升格为已验证成功。替换或废弃条目保留迁移说明，不复用 ID。

维护完成后运行：

```bash
python3 skills/collaboration-library/scripts/build_index.py
python3 -m unittest discover -s tests -v
git diff --check
```

同时核对本页路由和数量、README、来源链接、公开内容与安装完整性。结构检查不代替真实 Agent 行为评估。发布后核对远端提交，不能只说“本地已写好”。

安装三个 Skill 的具体说明见 [README](README.md)。发布到 GitHub 不会自动更新各设备的已安装副本；需按该环境的安装方式更新，并以实际技能发现清单为准。

本轮本地挖掘范围、未覆盖内容和去重方式见 [挖掘记录](docs/local-mining-2026-10-26.md)。
