# Pull Request 提交指南

## 一、什么是 Pull Request

Pull Request（简称 PR）是向开源项目贡献代码的标准方式。它允许你将自己的修改提交给项目管理员审核，并将你的代码合并到主项目中。

**PR 的作用**：

- 代码审查 - 让他人检查你的代码质量
- 早期发现潜在问题 - 在合并前修复 bug
- 知识共享 - 让团队成员了解代码变更
- 追踪变更 - 保留完整的修改记录

## 二、提交 PR 的完整流程

### 步骤 1：Fork 原始仓库

进入原始仓库页面（[本仓库](https://github.com/SUEP-RM-Lab-107/git-playground)），点击右上角的 **Fork** 按钮，将仓库复制到你的 GitHub 账户。

```
原仓库：https://github.com/SUEP-RM-Lab-107/git-playground
你的仓库：https://github.com/你的用户名/git-playground
```

### 步骤 2：克隆你的仓库到本地

```bash
# 克隆你 Fork 的仓库
git clone https://github.com/你的用户名/git-playground.git

# 进入项目目录
cd git-playground
```

### 步骤 3：创建特性分支

不要在 main 分支上直接修改，创建一个新的分支来进行修改：

```bash
# 确保在 main 分支上
git checkout main

# 拉取最新代码
git pull origin main

# 创建并切换到新分支
git checkout -b feature/你的功能名称
```

分支命名规范：

- `feature/` - 新功能
- `fix/` - 修复 bug
- `docs/` - 文档修改
- `refactor/` - 代码重构

### 步骤 4：进行修改并提交

```bash
# 查看修改状态
git status

# 添加修改的文件
git add 你的修改文件

# 提交修改
git commit -m "feat: 添加新功能描述"

# 推送分支到你的远程仓库
git push origin feature/你的功能名称
```

### 步骤 5：创建 Pull Request

1. 打开你的 GitHub 仓库页面
2. 你会看到一个 **Compare & pull request** 的绿色按钮，点击它
3. 填写 PR 标题和描述
4. 点击 **Create pull request** 按钮

## 三、PR 描述撰写指南

一份好的 PR 描述能帮助审核者更快理解你的修改。

### 推荐模板

```markdown
## 做了什么修改

简要说明本次 PR 的内容和目的。

## 为什么需要这个修改

解释修改的背景和原因。

## 如何测试

说明如何验证这个修改是否正确工作。

## 相关截图（如有 UI 变更）

[添加截图]

## 检查清单

- [ ] 代码已通过 lint 检查
- [ ] 已添加必要的测试
- [ ] 文档已更新
```

### 示例

```markdown
## 新增用户个人简介功能

在 profiles 目录下添加用户个人简介的模板文件，方便团队成员介绍自己。

## 为什么需要这个修改

为了增强团队凝聚力，让大家更好地互相了解。

## 如何测试

1. 在 profiles 目录下创建以你用户名命名的 .md 文件
2. 参考模板填写内容
3. 提交 PR

## 检查清单

- [x] 遵循模板格式
- [x] 添加了个人简介
```

## 四、PR 提交后的跟进

### 响应审核意见

审核者可能会提出修改建议，你需要：

1. **及时查看反馈** - 在 PR 页面查看评论
2. **在原分支上修改** - 不要创建新的 PR
3. **推送更新** - 修改后自动更新 PR

```bash
# 在原分支上继续修改
git checkout feature/你的分支名

# 进行修改...

# 提交并推送
git add .
git commit -m "fix: 根据审核意见修改"
git push origin feature/你的分支名
```

### 保持 PR 更新

如果原仓库有新的更新，需要同步到你的分支：

```bash
# 添加原仓库为上游仓库（只需一次）
git remote add upstream https://github.com/SUEP-RM-Lab-107/git-playground.git

# 拉取上游更新
git fetch upstream

# 合并到你的分支
git merge upstream/main

# 解决可能的冲突，然后推送
git push origin feature/你的分支名
```

### 合并 PR

当审核通过后，管理员会合并你的 PR。你可以在 PR 页面看到合并状态。

## 五、常见问题

### Q1: PR 提交后发现有错误怎么办？

直接在原分支上修改并提交，PR 会自动更新。

### Q2: 如何修改 PR 的标题和描述？

在 PR 页面点击标题或描述即可编辑。

### Q3: PR 被拒绝了怎么办？

不要气馁！仔细阅读审核意见，根据反馈进行修改。审核者通常会给出具体的建议。

### Q4: 可以同时提交多个 PR 吗？

可以，每个 PR 对应一个分支。确保不同 PR 在不同分支上。

## 六、PR 审核标准

为了提高 PR 通过率，请确保：

- [ ] 代码风格一致
- [ ] 有清晰的提交信息
- [ ] 只包含相关的修改
- [ ] 已有充分的测试
- [ ] 文档已同步更新
- [ ] 没有不必要的文件

---

**文档版本**：1.0 **最后更新**：2026年1月
