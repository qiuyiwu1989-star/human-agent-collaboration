# 条目数据约定

`catalog.json` 是结构化条目的唯一编辑源，`index.md` 由脚本生成。原有技能文档仍是详细操作的来源；修改原文后应复核对应卡片，不自动认为二者同步。

## 字段

- `id`：稳定唯一 ID；M 方法、E 示例、S 场景、V 评估，新增实际经验可用 X 前缀。删除或合并时保留迁移说明，不复用旧 ID。
- `title / kind / summary`：名称、类型、简述。kind 为 method、example、scenario、evaluation、experience。
- `scenarios / keywords`：场景与中英文检索词，检索标签不表示已具备对应领域的完整能力。
- `when_to_use / avoid_when`：适用与不适用条件。
- `steps / output / verification`：操作、预期产物与验收依据。
- `sources`：原始仓库相对路径与章节；不得使用私人绝对路径或将未核查出处当作权威背书。
- `related`：相关条目 ID，表达可选关联而非强制流程。
- `evidence_status`：documented（已有方法文档）、illustrative（示例）、unevaluated（尚未运行的评估）、reported-outcome（历史复盘报告的结果，本次未独立复验）、observed-success / observed-failure（有直接观察证据的经验）。这些状态不是质量等级。
- `outcome`：未观察结果时为 null。来源报告或直接观察的经验需包含 `context`、`action`、`result`、`limitations`、`evidence`，其中 evidence 为非空公开仓库证据路径列表。记录日期、观察者与方法版本可写在 context。单次成功不能证明普遍有效。

## 入库与维护

先找重复条目，再新增或更新；保留来源与适用边界。只有可公开且有明确维护授权的内容才进入仓库，不从私有聊天自动抽取对外发布。没有真实证据就保持方法或示例状态，不能因点赞、检索频率或模型自评升级为成功。

修改 catalog.json 后，在本技能目录运行 `python3 scripts/build_index.py`。仓库维护者再运行根目录的检索测试及字段、来源检查。文档同步和结构校验不代表行为评估或真实业务验证。

来源摘记位于 sources/，独立改写、保留原件摘要指纹及证据局限。摘记不是独立来源，不因公开了摘记就将 reported-outcome 升为 observed-success。公开原件不可得时，不声称读者能独立复现其历史结论。
