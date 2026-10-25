# 人机协作分类目录

此页由 catalog.json 生成；完整字段可按 ID 用 scripts/search.py --id 读取。

当前：method 45 条、example 4 条、scenario 5 条、evaluation 14 条、experience 6 条。真实成功经验 0 条。

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

### M14 · 需求简报与范围锁定

- 场景：通用；状态：documented
- 用途：新功能可能长出结构时，把自然语言压缩成可执行边界。
- 检索词：简报、范围膨胀、需求
- 关联：无

### M15 · 短选项决策

- 场景：通用；状态：documented
- 用途：用户需要在重要取舍上快速决定。
- 检索词：拍板、A/B、选项、推荐
- 关联：无

### M16 · 发布窗口与批次验收

- 场景：编程、运维；状态：documented
- 用途：用户正在使用或验收时，避免改动破坏现场。
- 检索词：发布、冻结、部署、用户在测
- 关联：无

### M17 · 遗留项明确处置

- 场景：通用；状态：documented
- 用途：任务收尾发现真正影响目标的剩余工作。
- 检索词：尾巴、剩余、择期
- 关联：无

### M18 · 规格驱动的持续推进

- 场景：通用；状态：documented
- 用途：已授权任务需要多阶段持续执行。
- 检索词：长任务、继续、停止条件
- 关联：无

### M19 · 机制图作为项目资产

- 场景：通用、产品设计；状态：documented
- 用途：文字难以表达关系、路径或方案差异。
- 检索词：画图、可视化、机制、HTML
- 关联：无

### M20 · 先做纵向样板再扩容

- 场景：产品设计、编程；状态：documented
- 用途：大量内容或多模块尚未形成完整交付链。
- 检索词：样板、端到端、扩容、vertical slice
- 关联：无

### M21 · 事实、判断与发布权分离

- 场景：通用、知识管理；状态：documented
- 用途：自动化会生成评价或公开内容。
- 检索词：审核、事实、发布权
- 关联：无

### M22 · 契约先行与目录所有权

- 场景：编程；状态：documented
- 用途：获准并行时多执行者可能修改同一接口。
- 检索词：并行、schema、所有权
- 关联：无

### M23 · 现实证据决定下一阶段

- 场景：产品设计、研究；状态：documented
- 用途：工程已完成但核心价值还未验证。
- 检索词：停止扩张、真实用户、效果
- 关联：无

### M24 · 事故驱动门禁与负向测试

- 场景：编程；状态：documented
- 用途：同类缺陷反复出现或静默失效。
- 检索词：验证闸门、负向测试、mutation、历史缺陷
- 关联：无

### M25 · 单一真源与线上版本一致

- 场景：编程、运维；状态：documented
- 用途：多个副本或手工上线导致实际版本不清。
- 检索词：配置漂移、唯一真源、线上仓库
- 关联：无

### M26 · 业务结果控制队列推进

- 场景：编程；状态：documented
- 用途：外部接口可能 HTTP 成功但业务全部失败。
- 检索词：success、队列、静默丢失、error
- 关联：无

### M27 · 验证降级不降结论标准

- 场景：通用、编程；状态：documented
- 用途：首选验证工具不可用。
- 检索词：工具不可用、DOM、截图、降级
- 关联：无

### M28 · 环境变化后重验旧结论

- 场景：通用、运维；状态：documented
- 用途：迁移、改路由或版本更新后将使用旧判断。
- 检索词：旧记忆、迁移、过期
- 关联：无

### M29 · 真实协议探针先于实现

- 场景：编程、设备接入；状态：documented
- 用途：第三方文档与现场行为可能不一致。
- 检索词：探针、真实返回、协议
- 关联：无

### M30 · 生命周期幂等与状态演进

- 场景：编程、设备接入；状态：documented
- 用途：同一业务 ID 会经历开始、完成和分片等状态。
- 检索词：幂等、eventId、重复、ready
- 关联：无

### M31 · 接收台账与可解释丢弃

- 场景：设备接入、编程；状态：documented
- 用途：对方未发和本方丢弃表现相同。
- 检索词：丢弃、台账、没收到、可观测
- 关联：无

### M32 · 时间敏感任务独立节拍

- 场景：设备接入、编程；状态：documented
- 用途：慢任务会阻塞有过期窗口的数据获取。
- 检索词：调度、队列、过期、节拍
- 关联：无

### M33 · 不变量与路径细节分开

- 场景：编程；状态：documented
- 用途：新增处理路径与旧数据库条件冲突。
- 检索词：约束、不变量、状态成功
- 关联：无

### M34 · 分层取证与错误聚类

- 场景：运维；状态：documented
- 用途：用户报告不可用、慢或大量失败。
- 检索词：事故、502、SSH、公网
- 关联：无

### M35 · 迁移预检与真实回滚条件

- 场景：运维；状态：documented
- 用途：数据或服务迁到另一环境。
- 检索词：迁移、回滚、备份、存储
- 关联：无

### M36 · 指令接受不等于设备完成

- 场景：设备接入；状态：documented
- 用途：外部指令成功返回但实际设备状态未确认。
- 检索词：accepted、回读、reportedAt、在线
- 关联：无

### M37 · 按事件时间确定归属

- 场景：设备接入、知识管理；状态：documented
- 用途：事件延迟到达且实体持有人可能变化。
- 检索词：归属、时间区间、改派
- 关联：无

### M38 · 冻结范围、版本守卫与一次撤销

- 场景：产品设计、编程；状态：documented
- 用途：AI 提案和人的编辑可能同时发生。
- 检索词：共创、提案、撤销、冻结范围
- 关联：无

### M39 · 真实安装路径与资源清理验收

- 场景：编程；状态：documented
- 用途：库内测试通过但用户安装或组合可能失败。
- 检索词：安装、插件、dispose、HMR
- 关联：无

### M40 · 记忆分层与渐进读取

- 场景：知识管理；状态：documented
- 用途：多个 Agent 复用背景但容易读太多或误用候选。
- 检索词：索引、按需读取、候选、记忆
- 关联：无

### M41 · 真实声音样本与作者判断边界

- 场景：写作；状态：documented
- 用途：生成内容容易冒充作者经验或污染声音样本。
- 检索词：声音、署名、样本、原话
- 关联：无

### M42 · 研讨五类来源分开

- 场景：写作、知识管理；状态：documented
- 用途：一次研讨与后续讨论要整理成可复用文章。
- 检索词：研讨、说话人、转写、沉淀
- 关联：无

### M43 · 幂等写回与不确定结果恢复

- 场景：知识管理、编程；状态：documented
- 用途：外部写入超时可能已经成功。
- 检索词：回执、重试、request_id、发布
- 关联：无

### M44 · 设计版本与可编辑性显式交付

- 场景：产品设计；状态：documented
- 用途：生成设计需要人继续编辑或转换格式。
- 检索词：设计包、可编辑、栅格化、保真
- 关联：无

### M45 · 按未知编排方法而非堆框架

- 场景：通用、研究；状态：documented
- 用途：大量方法可选但用户只需要关键判断。
- 检索词：方法编排、InnoLab、索引、不适用
- 关联：无

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

## 实战经验（区分来源报告与独立观察）

### X01 · 先小样板后扩量与入口纠偏

- 场景：实战复盘；状态：reported-outcome
- 用途：产品复盘记载先以少量项目贯通处理链，再扩大内容；用户指出入门难后重做新手入口。
- 检索词：先小样板后扩量与入口纠偏、经验、复盘、先做纵向样板再扩容、现实证据决定下一阶段
- 关联：M20, M23

### X02 · 故障注入检查验证器

- 场景：实战复盘；状态：reported-outcome
- 用途：复盘记载注入历史格式与版本缺陷，验证脚本能够拒绝，并在恢复后通过。
- 检索词：故障注入检查验证器、经验、复盘、事故驱动门禁与负向测试
- 关联：M24

### X03 · 接口没有 error 仍然整批失败

- 场景：实战复盘；状态：reported-outcome
- 用途：复盘记录外部接口返回零成功却没有 error 字段，旧脚本错误推进队列。
- 检索词：接口没有 error 仍然整批失败、经验、复盘、业务结果控制队列推进
- 关联：M26

### X04 · 设备 accepted 与可用状态混淆

- 场景：实战复盘；状态：reported-outcome
- 用途：复盘撤回把授权标记和指令接受当成设备可用的判断，改用设备回读并附新鲜度。
- 检索词：设备 accepted 与可用状态混淆、经验、复盘、指令接受不等于设备完成、按事件时间确定归属
- 关联：M36, M37

### X05 · 共创交接保留原稿并支持撤销

- 场景：实战复盘；状态：reported-outcome
- 用途：来源记录合成画布经转换、提案应用与撤销验证；本次读取完整性摘要，其 sceneUnchanged 为 true。
- 检索词：共创交接保留原稿并支持撤销、经验、复盘、冻结范围、版本守卫与一次撤销
- 关联：M38

### X06 · 浏览器不可用时补实际脚本验证

- 场景：实战复盘；状态：reported-outcome
- 用途：复盘记录截图能力不可用，随后用最小 DOM 环境实际执行导航脚本，并做缺失项负向检查。
- 检索词：浏览器不可用时补实际脚本验证、经验、复盘、验证降级不降结论标准
- 关联：M27
