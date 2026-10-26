# 个人网站技能中心接入

2026-10-26：已接通本机运行的个人站技能中心预览，未接通公网生产中心。

## 职责与当前状态

GitHub 方法库维护原创方法、来源摘记和检索代码。技能中心保存完整技能包的草稿、审核、发布版本和采用记录。中心修改草稿不自动写回 GitHub；有差异时先比较，不双向覆盖。

三个完整文本包 collaboration-library、collaboration-methods、human-ai-writing 已导入本地中心草稿，完成稳定身份绑定和同步回读。三个包均完整、无排除文件；同步返回 unchanged。中心已有的 82 条方法资料与本库 JSON 逐条完全一致，其中 53 条为方法，不能算作 82 个 Skill。

本次没有发布中心正式版本、安装到其他 Agent、部署个人站或注册个人 MCP。GitHub 更新不会自动触发中心同步。

## 后续维护

使用个人网站仓库的 scripts/skill_center_sync.py。绑定状态位于 webroot 与 Git 仓库之外的私有设备文件中，不提交到公共库。

```bash
# 在个人网站仓库中；路径由实际环境提供
python3 scripts/skill_center_sync.py sync --api "$SKILL_CENTER_API" --root "$COLLAB_REPO/skills/collaboration-library" --state "$SKILL_BINDING_STATE"
python3 scripts/skill_center_sync.py sync --api "$SKILL_CENTER_API" --root "$COLLAB_REPO/skills/collaboration-methods" --state "$SKILL_BINDING_STATE"
python3 scripts/skill_center_sync.py sync --api "$SKILL_CENTER_API" --root "$COLLAB_REPO/skills/human-ai-writing" --state "$SKILL_BINDING_STATE"
```

已绑定的中心地址不能换成另一环境复用。生产中心需单独核对身份与完整包并建立绑定；专用凭据通过受控环境注入，不写到命令参数或文档。

同步冲突时保留双方版本，由连接器的 resolve 流程在明确比较后处理。超时结果未知时复用原待处理请求，不另建身份。完整包中的 catalog.json 随技能同步；中心独立的方法资料索引需要单独对比，不能因此宣称自动同步已建立。

## 公网接通的剩余条件

个人站生产技能模块部署、专用权限配置以及生产地址验证仍需由站点发布流程完成。个人站工作区存在大量其他未提交修改，不能整包推送。完成隔离发布并取得可用中心后，再导入/绑定这三个包，回读内容与索引，最后验证个人 MCP 调用。
