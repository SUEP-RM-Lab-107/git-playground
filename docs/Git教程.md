# Git 入门教程

## 一、Git 基础

### 什么是 Git

Git 是由 Linus Torvalds 于 2005
年开发的分布式版本控制系统，简单来说就是一个帮助我们管理代码版本历史的工具。

**为什么要使用 Git？**

在日常开发中，我们经常遇到以下情况：

- 写了一段代码后发现 bug，想回到之前的版本却发现已经覆盖
- 多人协作时，大家各自修改代码，不知道谁改了什么
- 不小心删除了重要文件，却无法恢复

这些问题都可以通过 Git 来解决。Git 的核心优势包括：

- **分布式架构**：每个开发者都有完整的代码仓库副本，不依赖中央服务器
- **速度快**：大多数操作都在本地执行，无需网络连接
- **非线性开发**：通过分支机制可以同时进行多个功能的开发
- **数据完整性**：使用 SHA-1 哈希算法确保数据的完整性

### Git 工作原理

理解 Git 的工作原理是掌握 Git 的基础。Git
有三个核心区域：工作目录、暂存区和版本库。

工作目录是你正在编辑文件的地方，也就是你的项目文件夹。当你修改文件时，修改首先发生在工作目录中。暂存区是一个特殊的区域，用于存放准备提交的文件。你可以把它理解为一个「准备区」，只有被添加到暂存区的修改才会被提交。版本库是
Git 存储所有提交历史的地方，每次提交都会在版本库中创建一个快照。

文件在这三个区域之间流转的过程是：首先在工作目录中修改文件，然后使用 `git add`
命令将修改添加到暂存区，最后使用 `git commit` 命令将暂存区的修改提交到版本库。

每个文件在 Git
中都有三种状态：已修改（Modified）表示文件已被修改但尚未添加到暂存区；已暂存（Staged）表示文件已被添加到暂存区，等待提交；已提交（Committed）表示修改已经被提交到版本库中。

> **注意**：Git 在处理图片、音频、视频、PDF 等二进制文件时存在一定局限性。由于
> Git
> 会对每次提交的文件进行完整的快照存储，大量或频繁修改的二进制文件会导致仓库体积快速增长。此外，Git
> 无法对二进制文件进行有效的差异对比和合并处理，这意味着两个人同时修改同一张图片时，Git
> 难以自动合并他们的修改。对于大型二进制文件的管理，建议考虑使用 Git LFS（Large
> File Storage）扩展，或将二进制素材与代码仓库分离存储。

## 二、安装与配置

### 安装 Git

执行 `git --version` 来检查是否已安装

- **Windows 系统**

  在 Windows 上安装 Git 最简单的方法是访问 Git
  [官方网站](https://git-scm.cn/)，下载 Windows
  版本的安装包。下载完成后，双击安装包进行安装，安装过程中保持默认选项即可。安装完成后，在开始菜单中找到「Git」文件夹，选择「Git
  Bash」打开命令行终端。

  使用 winget 工具

  ```powershell
  winget install --id Git.Git -e --source winget
  ```

- **macOS 系统**

  macOS 用户可以通过多种方式安装 Git。最简单的方法是使用 Homebrew
  包管理器，在终端中执行以下命令：

  ```bash
  brew install git
  ```

  如果系统中已经安装了 Xcode Command Line Tools，Git
  可能已经预装在系统中。可以通过执行 `git --version` 来检查是否已安装。

- **Linux 系统**

  Linux 用户可以使用包管理器来安装 Git。 Debian/Ubuntu 系统执行：

```bash
sudo apt update
sudo aot upgrade
sudo apt install git
```

CentOS/Fedora 系统执行：

```bash
sudo dnf update
sudo dnf install git
```

### 首次配置

安装完成后，需要进行一些基本的配置。这些配置信息会随着每次提交而保存，所以需要设置正确的用户名和邮箱地址。

执行以下命令配置用户信息：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

这里的 `--global`
参数表示这是全局配置，会对当前用户的所有仓库生效。如果需要在特定仓库中使用不同的配置，可以进入该仓库目录后去掉
`--global` 参数重新执行。

其他常用的配置项包括：配置默认文本编辑器，例如
`git config --global core.editor vim`；配置命令别名，例如
`git config --global alias.co checkout` 可以将 `co` 设置为 `checkout`
的别名；查看所有配置可以使用 `git config --list` 命令。

## 三、基础操作

### 初始化新仓库

如果你有一个尚未被 Git 管理的新项目，需要先将其初始化为 Git
仓库。进入项目目录后执行：

```bash
git init
```

> **主分支命名**：Git 旧版本默认主分支名为 `master`，新版本（Git 2.28+）默认
> `main`。如需指定主分支名，可执行
> `git init -b main`。后续如需修改主分支名，可执行 `git branch -m main`。

执行这个命令后，Git 会在当前目录下创建一个 `.git` 隐藏文件夹，这就是 Git
版本库的核心目录。不要手动修改这个目录中的内容，否则可能会破坏仓库结构。

### 克隆远程仓库

如果你想参与一个已经存在的项目，或者想获取别人的项目代码，可以使用克隆命令：

```bash
# HTTPS 方式（需要输入用户名和 Personal Access Token）
git clone https://github.com/SUEP-RM-Lab-107/git-playground.git

# SSH 方式（需要配置 SSH 密钥，克隆后无需输入密码）
git clone git@github.com:SUEP-RM-Lab-107/git-playground.git
```

> **HTTPS vs SSH**：HTTPS
> 方式无需配置，在公司网络环境下也能正常工作，但每次操作需输入凭据；SSH
> 方式需要先配置密钥，之后无需输入密码，更安全高效。个人开发推荐使用 SSH。

执行克隆命令后，Git
会在当前目录下创建一个与远程仓库同名的文件夹，并将远程仓库的所有内容下载到本地。克隆操作会自动设置远程仓库的别名
origin，并下载所有分支的历史。

### 提交代码

提交是 Git
中最基本的操作，也是版本控制的核心。每次提交都会创建一个保存点，记录当前时刻的代码状态。

#### 添加到暂存区

在提交之前，需要先将修改的文件添加到暂存区。添加单个文件使用
`git add 文件名`，添加所有修改的文件使用
`git add .`，添加所有修改的文件（包括删除）使用 `git add -A`。

```bash
# 添加单个文件
git add README.md

# 添加所有修改的文件
git add .

# 查看文件状态，确认哪些文件会被提交
git status
```

#### 执行提交

将文件添加到暂存区后，就可以执行提交了。提交时需要附带一条说明信息，描述这次提交的内容。

```bash
git commit -m "修改README"
```

**提交规范**

良好的提交规范对于团队协作非常重要。推荐使用 **约定式提交（Conventional
Commits）** 标准：

```
<类型>[可选范围]: <描述>

[空行]

[正文]

[空行]

[尾部]
```

**标题**（必填）

格式：`type(scope): description`

示例：`feat(login): 新增用户登录功能`

- **type**类型(必选)

| 类型       | 说明                       |
| ---------- | -------------------------- |
| `feat`     | 新功能                     |
| `fix`      | 修复问题                   |
| `docs`     | 文档变更                   |
| `style`    | 代码样式调整（不影响功能） |
| `refactor` | 代码重构                   |
| `test`     | 测试相关                   |
| `chore`    | 构建工具或辅助脚本变更     |

- **description**描述用动词开头，不超过 50 字符
- **scope**范围**可选**，如模块名 `user` 或文件名 `api.js`

**正文**（可选）

详细说明变更的背景、原因和结果，每行不超过 72 字符。

**尾部**（可选）

- 关联问题：`Closes #123`、`Fixes #456`
- 破坏性变更：`BREAKING CHANGE: 不兼容说明`

**示例**：

```
feat(user): 新增用户头像上传功能

- 支持 PNG/JPG 格式
- 最大支持 5MB
- 上传前进行图片压缩

Closes #88
```

### 查看历史

**查看提交历史**

查看项目的提交历史是了解项目发展过程的重要方式。最基本的历史查看命令是
`git log`，它会显示当前分支的提交历史。

```bash
# 查看完整提交历史
git log

# 简化显示，每行只显示提交哈希和说明
git log --oneline

# 查看最近的3条提交
git log -3

# 查看提交历史并显示文件变更统计
git log --stat

# 查看提交历史的图形化展示（分支合并情况）
git log --graph --oneline
```

**查看文件差异**

diff 命令用于查看文件之间的差异。在提交前查看修改内容是一个好习惯。

```bash
# 查看工作区与暂存区的差异
git diff

# 查看工作区与最新提交的差异
git diff HEAD

# 查看暂存区与最新提交的差异
git diff --cached

# 查看两个提交之间的差异
git diff commit1_hash commit2_hash
```

### 查看状态

`git status`
是最常用的命令之一，它显示当前仓库的状态，包括：已修改但未暂存的文件、已暂存但未提交的文件、当前所在分支等信息。

```bash
git status

# 简化显示
git status -s
```

输出中常见的符号含义：`A` 表示已添加到暂存区的新文件；`M` 表示已修改的文件，`M`
在左边表示已暂存，在右边表示未暂存；`??`
表示未跟踪的文件，既未添加到暂存区也不在版本库中。

## 四、分支管理

### 理解分支

分支是 Git
最强大的功能之一。简单来说，分支就是指向提交对象的可变指针。默认情况下，每次提交都会沿着一条主线（通常叫
main 或 master 分支）向前移动。

分支的主要用途包括：开发新功能时不影响主代码、多个功能可以并行开发、便于代码审查和合并、实验性开发可以随时丢弃。

### 分支操作

**查看分支**

```bash
# 查看所有分支，当前分支前面有星号标记
git branch

# 查看所有分支，包括远程分支
git branch -a

# 查看每个分支的最新提交
git branch -v
```

**创建分支**

```bash
# 创建新分支
git branch develop

# 创建并切换到新分支
git checkout -b feature/user-login
# 或者使用新语法
git switch -c feature/user-login
```

**切换分支**

```bash
# 切换到指定分支
git checkout develop
# 或者
git switch develop

# 切换回主分支
git checkout main
# 或者
git switch main
```

**合并分支**

当一个分支上的开发完成后，需要将其合并回主分支。

```bash
# 首先切换到目标分支（通常是主分支）
git checkout main

# 合并指定分支到当前分支
git merge develop
```

**删除分支**

分支合并后，如果不再需要可以删除。

```bash
# 删除已合并的分支
git branch -d develop

# 强制删除分支（即使未合并）
git branch -D develop
```

### 冲突解决

当两个分支修改了同一个文件的同一部分时，合并时就会产生冲突。Git
无法自动合并这些冲突，需要手动解决。

**冲突的产生**

假设在 feature 分支和 main 分支上都修改了 index.html
文件的同一行，合并时就会产生冲突。

**识别冲突**

执行 `git merge` 后，如果存在冲突，Git 会提示哪些文件有冲突：

```
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

**解决冲突**

打开有冲突的文件，会看到类似这样的内容：

```html
<<<<<<< HEAD
<div class="header">主分支的代码</div>
=======
<div class="header">特性分支的代码</div>
>>>>>>> feature-branch
```

`<<<<<<<` 和 `=======` 之间的内容是当前分支（HEAD）的代码，`=======` 和
`>>>>>>>`
之间的内容是要合并的分支的代码。根据实际需求，保留一方的代码或者合并两方的代码，然后删除冲突标记符号。

解决完所有冲突后，执行以下命令完成合并：

```bash
git add .
git commit -m "解决合并冲突"
```

**避免冲突的技巧**

为了减少冲突的发生，建议：团队成员之间及时沟通，避免多人同时修改同一文件；合理划分模块，让每个成员负责不同的文件或功能；频繁合并主分支的更新到自己的分支。

## 五、远程仓库

### 认识远程仓库

远程仓库是指托管在网络上的仓库，常见的平台包括 GitHub、GitLab、Gitee
等。通过远程仓库，团队成员可以共享代码、协作开发。

每个本地仓库可以关联多个远程仓库，最常见的远程仓库名是 origin。origin
只是一个约定俗成的命名惯例，你也可以将其命名为其他名字。

### 关联远程仓库

**添加远程仓库**

如果你的本地仓库还没有关联远程仓库，可以使用以下命令添加：

```bash
git remote add origin https://github.com/用户名/仓库名.git
```

**查看远程仓库**

```bash
# 查看已关联的远程仓库
git remote -v

# 查看远程仓库的详细信息
git remote show origin
```

### 推送与拉取

**推送到远程**

将本地分支的提交推送到远程仓库：

```bash
# 首次推送并关联分支
git push -u origin main

# 后续推送
git push

# 推送本地分支到远程仓库（如果远程不存在）
git push origin feature-branch
```

**拉取远程更新**

从远程仓库获取最新的更新并合并到本地：

```bash
# 拉取并合并远程更新
git pull

# 只获取远程更新，不合并
git fetch

# 拉取特定分支
git pull origin feature-branch
```

**fetch 与 pull 的区别**

`git fetch`
只获取远程仓库的更新到本地，但不会自动合并或修改你的工作目录。`git pull` 相当于
`git fetch` 加 `git merge`，会自动将远程更新合并到当前分支。推荐在合并前先使用
`git fetch` 查看有哪些更新，然后再决定是否合并。

### SSH 密钥配置

使用 SSH 协议连接远程仓库可以避免每次操作都输入密码。

**生成 SSH 密钥**

```bash
# 生成 SSH 密钥（邮箱使用你的邮箱地址）
ssh-keygen -t ed25519 -C "你的邮箱@example.com"
# Ed25519 比ssh-keygen -t rsa更安全
```

敲击三次回车键接受默认保存位置，可以选择设置密码（passphrase）来保护密钥。
执行`ls ~/.ssh/` 应该会有`id_ed25519.pub`(公钥)和`id_ed25519`(私钥)两个文件。

**配置远程仓库使用 SSH**

复制公钥内容（`~/.ssh/id_ed25519.pub`）到 GitHub/GitLab 的 SSH Keys
设置中。之后克隆或添加远程仓库时使用 SSH 地址：

```bash
git clone git@github.com:用户名/仓库名.git
```

## 六、撤销操作

### 撤销工作区修改

如果修改了文件但还没有添加到暂存区，可以使用以下命令撤销：

```bash
# 撤销单个文件的修改
git checkout -- 文件名

# 撤销所有文件的修改
git checkout -- .
```

注意：这条命令会丢失所有未提交的修改，请谨慎使用。

### 撤销暂存区操作

如果错误地将文件添加到了暂存区，可以使用以下命令撤销：

```bash
# 将文件从暂存区移回工作区
git reset HEAD 文件名

# 将所有文件从暂存区移回工作区
git reset HEAD .
```

### 回退版本

如果需要回退到之前的某个提交，可以使用 reset 命令：

```bash
# 回退一个版本（保留修改在工作区）
git reset --soft HEAD~1

# 回退一个版本（保留修改在工作区，文件状态为已修改）
git reset HEAD~1

# 回退一个版本（丢弃所有修改）
git reset --hard HEAD~1

# 回退到指定提交
git reset --hard 提交哈希值
```

使用 `--hard`
参数时要特别小心，它会丢失所有未提交的修改且无法恢复。如果只是想查看历史提交但不想修改，可以使用
`git checkout` 创建一个「分离头指针」状态。

### 反转提交

如果想撤销某次提交但保留历史记录（推荐用于已推送到远程的提交），可以使用
`git revert`：

```bash
# 反转最近一次提交
git revert HEAD

# 反转指定提交
git revert 提交哈希值
```

revert
会创建一个新的提交来撤销指定提交的修改，这样在团队协作中更安全，不会影响其他人的工作。

## 七、常用命令速查表

### 基础操作命令

`git init` 用于初始化一个新的 Git 仓库。`git clone 仓库地址`
用于克隆一个已存在的远程仓库。`git add 文件名`
用于将文件添加到暂存区。`git commit -m "说明"`
用于提交暂存区的修改。`git status` 用于查看仓库当前状态。`git log`
用于查看提交历史。

### 分支管理命令

`git branch` 用于查看所有分支。`git branch 分支名`
用于创建一个新分支。`git checkout 分支名`
用于切换到指定分支。`git switch 分支名`
是切换分支的新语法。`git checkout -b 分支名`
用于创建并切换到新分支。`git merge 分支名`
用于合并指定分支到当前分支。`git branch -d 分支名` 用于删除指定分支。

### 远程操作命令

`git remote add origin 地址` 用于添加远程仓库。`git remote -v`
用于查看远程仓库信息。`git push -u origin 分支名` 用于推送到远程仓库。`git pull`
用于拉取并合并远程更新。`git fetch` 用于获取远程更新（不合并）。

### 查看与撤销命令

`git diff` 用于查看工作区与暂存区的差异。`git diff HEAD`
用于查看工作区与最新提交的差异。`git checkout -- 文件名`
用于撤销工作区的修改。`git reset HEAD 文件名`
用于撤销暂存区的操作。`git reset --hard 提交哈希`
用于回退到指定提交。`git revert 提交哈希` 用于反转指定提交。

## 八、学习建议

### 持续练习

学习 Git 最有效的方法是不断练习。
建议在日常开发中尽量使用Git，遇到问题时查阅文档或搜索引擎。
尝试在个人项目中创建不同的分支，体验分支管理的便利性。

### 善用资源

[Git 官方文档](https://git-scm.cn/docs) 是最权威的学习资源，提供了详细的命令说明和教程。
Pro Git 书籍是一本免费的在线书籍，深入讲解了 Git 的原理和高级用法。
GitHub Learning Lab 提供了互动式的 Git 学习课程。
Learn Git Branching 是一个可视化的 Git 学习网站，非常适合初学者。

### 进阶方向

掌握基础操作后，可以学习以下进阶内容：Git 工作流了解不同团队采用的开发流程，如
Git Flow、GitHub Flow；Rebase 学习如何使用 rebase 整理提交历史；Git
内部原理深入理解 Git 的对象模型和存储方式；Git 钩子使用 hooks 自动化开发流程。

## 结语

Git 是一个强大的工具，熟练使用 Git可以大大提高开发效率和代码管理能力。
本教程覆盖了 Git最常用的功能和操作，希望能够帮助你快速入门。
随着使用的深入，你会发现 Git 还有更多强大的功能等待探索。

记住：遇到问题时不要害怕，多尝试、多搜索、多实践。

---

**文档版本**：1.0 **最后更新**：2026年1月
？