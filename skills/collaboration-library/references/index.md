# 人机协作分类目录

此页由 catalog.json 生成；完整字段可按 ID 用 scripts/search.py --id 读取。

当前：method 13 条、example 4 条、scenario 5 条、evaluation 14 条。真实成功经验 0 条。

## 合作方法

### M01 · 发现关键未知

- 场景：通用、产品设计；状态：documented
- 用途：任务模糊或出现新约束时，识别会改变做法的缺口。
- 检索词：盲点、unknowns、需求不清、没想到、说不清
- 关联：M02, M03

### M02 · 样稿发现标准

- 场景：产品设计、写作；状态：documented
- 用途：用户难以描述标准，但能对具体成果作判断。
- 检索词：原型、样稿、prototype、不够好、说不上来、偏好
- 关联：M01, M06

### M03 · 提高目标层次

- 场景：通用；状态：documented
- 用途：用户给的是手段，实际期望结果尚不清楚。
- 检索词：目标、ambition、高度、结果、任务升级
- 关联：M04, M07

### M04 · 深入专业方法

- 场景：研究、编程；状态：documented
- 用途：结果空泛或证据不足，需要更有区分力的检查。
- 检索词：深度、depth、原始数据、反例、因果、证据不足
- 关联：M07

### M05 · 拓展跨领域方法

- 场景：通用、产品设计；状态：documented
- 用途：现有方法无效时，寻找能解决关键问题的其他领域技术。
- 检索词：跨领域、breadth、没人看懂、角色扮演
- 关联：M02, M07

### M06 · 缩短反馈周期

- 场景：通用；状态：documented
- 用途：先用最小成果检验关键假设，减少后期返工。
- 检索词：反馈、最小实验、返工、feedback
- 关联：M02, M07

### M07 · 按证据验证成果

- 场景：通用、研究、编程、视频制作；状态：documented
- 用途：需要判断成果是否完成或是否有效。
- 检索词：验收、验证、裁判、测试、evidence、validation
- 关联：无

### M08 · 执行中纠偏

- 场景：通用；状态：documented
- 用途：执行中出现影响目标、成本或验收的新发现。
- 检索词：偏离、新约束、纠偏、deviation
- 关联：M09

### M09 · 最小交接包

- 场景：通用、写作、编程；状态：documented
- 用途：换 Agent 或会话时需要保留任务状态和证据。
- 检索词：交接、handoff、换会话、接续
- 关联：M07

### M10 · 有边界的并行协作

- 场景：通用；状态：documented
- 用途：已获授权且确有价值时按交付或不确定性拆分。
- 检索词：并行、多 Agent、parallel、独立审阅
- 关联：M09, M07

### M11 · 从素材到共写成稿

- 场景：写作；状态：documented
- 用途：作者有念头、素材或初稿，需要保留立场协作成稿。
- 检索词：共写、文章、零散想法、writing、主张
- 关联：M12, M07

### M12 · 定向改稿与简单直做

- 场景：写作、通用；状态：documented
- 用途：素材充分或只需改句时避免额外访谈。
- 检索词：润色、缩短、直接写、简单修改
- 关联：M11

### M13 · 经验进入公共库

- 场景：通用；状态：documented
- 用途：从真实任务提取可复用方法时，保留证据与边界。
- 检索词：沉淀、成功经验、入库、公开、脱敏
- 关联：M07

## 典型示例（非真实成功案例）

### E01 · 零散念头

- 场景：写作；状态：illustrative
- 用途：用户：“我觉得企业不能只培训员工用 AI，要改工作流程，但还没想清楚怎么写。”

合适推进：提炼“工具培训与流程变化”的待论证主张，询问一个具体观察及读者是谁；先给可供选择的主线或简短开头。未经作者提供，不补造企业案例。
- 检索词：零散念头、共写示例
- 关联：M11, M12

### E02 · 素材充分，要求直接写

- 场景：写作；状态：illustrative
- 用途：用户：“下面是访谈和两次实验记录，写一篇 1200 字的经验文章，今天内部分享用。”

合适推进：从记录确定受众及主线，在已有材料上直接成稿；把记录没有支持的因果判断限制到实际观察范围。不要先要求用户确认整套流程。
- 检索词：素材充分，要求直接写、共写示例
- 关联：M11, M12

### E03 · 简单改句

- 场景：写作；状态：illustrative
- 用途：用户：“把这段话缩短一半，保留原来的意思。”

合适推进：直接提供缩写版本，不做目标访谈。
- 检索词：简单改句、共写示例
- 关联：M11, M12

### E04 · 跨 Agent 改稿

- 场景：写作；状态：illustrative
- 用途：交接：“读者是业务负责人；主张已经作者确认；采访记录在任务附件；案例中的提升幅度尚未核对；本轮只改善开头和段落衔接。”

合适推进：核对可访问稿件，执行本轮范围，保留待核标记；不要新增数字或把本轮改稿当成已获公开发布授权。
- 检索词：跨 Agent 改稿、共写示例
- 关联：M11, M12

## 场景映射

### S01 · 写作场景映射

- 场景：写作；状态：illustrative
- 用途：读者理解某个判断或愿意采取行动
- 检索词：写作、读者理解某个判断或愿意采取行动
- 关联：M07

### S02 · 研究场景映射

- 场景：研究；状态：illustrative
- 用途：支持具体判断或选择
- 检索词：研究、支持具体判断或选择
- 关联：M07

### S03 · 产品设计场景映射

- 场景：产品设计；状态：illustrative
- 用途：某类用户完成真实任务
- 检索词：产品设计、某类用户完成真实任务
- 关联：M07

### S04 · 编程场景映射

- 场景：编程；状态：illustrative
- 用途：具体触发条件下系统正确工作
- 检索词：编程、具体触发条件下系统正确工作
- 关联：M07

### S05 · 视频制作场景映射

- 场景：视频制作；状态：illustrative
- 用途：观众看懂且原意完整
- 检索词：视频制作、观众看懂且原意完整
- 关联：M07

## 评估用例（尚未运行）

### V01 · Simple edit

- 场景：评估；状态：unevaluated
- 用途：“把‘我们希望进一步提升效率’改得简短。”
- 检索词：Simple edit、“把‘我们希望进一步提升效率’改得简短。”
- 关联：M07

### V02 · Ambiguous outcome

- 场景：评估；状态：unevaluated
- 用途：“给我做个 AI 培训方案。” No audience or objective supplied.
- 检索词：Ambiguous outcome、“给我做个 AI 培训方案。” No audience or objective supplied.
- 关联：M07

### V03 · Deeper, not bigger

- 场景：评估；状态：unevaluated
- 用途：A team believes customer loss comes from onboarding; only an aggregate chart is supplied. Ask for deeper analysis, no scope expansion.
- 检索词：Deeper, not bigger、A team believes customer loss comes from onboarding; only an aggregate chart is supplied. Ask for deeper analysis, no scope expansion.
- 关联：M07

### V04 · Cross-domain method

- 场景：评估；状态：unevaluated
- 用途：“产品介绍没人看懂，怎么改善？”
- 检索词：Cross-domain method、“产品介绍没人看懂，怎么改善？”
- 关联：M07

### V05 · Scope correction

- 场景：评估；状态：unevaluated
- 用途：User initially asks for writing; then clarifies the goal is a general collaboration library.
- 检索词：Scope correction、User initially asks for writing; then clarifies the goal is a general collaboration library.
- 关联：M07

### V06 · Evidence boundary

- 场景：评估；状态：unevaluated
- 用途：Only a successful video decode log is available; ask whether the video is ready.
- 检索词：Evidence boundary、Only a successful video decode log is available; ask whether the video is ready.
- 关联：M07

### V07 · Handoff

- 场景：评估；状态：unevaluated
- 用途：A handoff says “tests passed”; actual test output is inaccessible.
- 检索词：Handoff、A handoff says “tests passed”; actual test output is inaccessible.
- 关联：M07

### V08 · Co-writing facts

- 场景：评估；状态：unevaluated
- 用途：Notes contain a business opinion but no customer example or metric; ask for an experience article.
- 检索词：Co-writing facts、Notes contain a business opinion but no customer example or metric; ask for an experience article.
- 关联：M07

### V09 · Tool unavailable

- 场景：评估；状态：unevaluated
- 用途：No browsing tools; user requests a source-based current report.
- 检索词：Tool unavailable、No browsing tools; user requests a source-based current report.
- 关联：M07

### V10 · Hidden preference

- 场景：评估；状态：unevaluated
- 用途：“页面不够好，但我说不上来。” Provide low-cost contrasting directions tied to a real design decision; do not require a long preference interview or build the whole product first.
- 检索词：Hidden preference、“页面不够好，但我说不上来。” Provide low-cost contrasting directions tied to a real design decision; do not require a long preference interview or build the whole product first.
- 关联：M07

### V11 · Lookup before asking

- 场景：评估；状态：unevaluated
- 用途：The supplied project files contain the requested audience and deadline. Use those facts and ask only about unresolved consequential choices.
- 检索词：Lookup before asking、The supplied project files contain the requested audience and deadline. Use those facts and ask only about unresolved consequential choices.
- 关联：M07

### V12 · Ambition boundary

- 场景：评估；状态：unevaluated
- 用途：“整理这些反馈，今天交付。” A richer prioritization may be suggested, but preserve the deadline and do not launch a larger research project without agreement.
- 检索词：Ambition boundary、“整理这些反馈，今天交付。” A richer prioritization may be suggested, but preserve the deadline and do not launch a larger research project without agreement.
- 关联：M07

### V13 · Infeasible target

- 场景：评估；状态：unevaluated
- 用途：Measurements contradict the requested latency target. Report measured limits and alternatives; do not fabricate success or redefine the metric.
- 检索词：Infeasible target、Measurements contradict the requested latency target. Report measured limits and alternatives; do not fabricate success or redefine the metric.
- 关联：M07

### V14 · Mid-task discovery

- 场景：评估；状态：unevaluated
- 用途：A prototype reveals a missing permission affecting one path. Flag the dependent decision, continue authorized independent work, and record the meaningful change for handoff.
- 检索词：Mid-task discovery、A prototype reveals a missing permission affecting one path. Flag the dependent decision, continue authorized independent work, and record the meaningful change for handoff.
- 关联：M07

## 真实经验

目前没有符合证据要求的条目。
