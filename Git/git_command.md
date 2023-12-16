# Git command tutorial
## 远程操作
### remote
`git remote` 命令用于用于管理 Git 仓库中的远程仓库。
```git      
//列出当前仓库中已配置的远程仓库
$ git remote
//列出当前仓库中已配置的远程仓库，并显示它们的 URL。
$ git remote -v
//添加一个新的远程仓库。指定一个远程仓库的名称和 URL，将其添加到当前仓库中。
$ git remote add <remote_name> <remote_url>
//将已配置的远程仓库重命名
$ git remote rename <old_name> <new_name>
//从当前仓库中删除指定的远程仓库
$ git remote remove <remote_name>
//修改指定远程仓库的 URL
$ git remote set-url <remote_name> <new_url>
//显示指定远程仓库的详细信息，包括 URL 和跟踪分支
$ git remote show <remote_name>
```
### fetch & pull
`git fetch`将远程仓库的最新内容拉取到本地，可以在检查后决定是否合并。
`git pull`将远程仓库的最新内容拉取到本地并直接合并。可能产生冲突，需要手动解决
#### git fetch
```git
$ git fetch <远程主机名> //将远程主机的更新全部取回本地
$ git fetch <远程主机名> <分支名> //仅将该分支取回
```
如取回Learning主机的main分支：
```git
$ git fetch Learning main
From github.com:mostimaaa/Learning
 * branch            main       -> FETCH_HEAD
```
如果之后要进行merge操作最好指明分支名
取回更新后会返回`FETCH_HEAD`，指向某个分支在服务器上的最新状态，可以通过以下指令查看：
```git
$ git log -p FETCH_HEAD
commit cccb391c24e8bacdb0eb5d88730f8a6278a0d68d (Learning/main)
Author: mostimaaa <112405530+mostimaaa@users.noreply.github.com>
Date:   Sat Dec 16 19:27:59 2023 +0800

    Initial commit

diff --git a/README.md b/README.md
new file mode 100644
index 0000000..f986672
--- /dev/null
+++ b/README.md
@@ -0,0 +1,2 @@
+# Learning
+a simple repo for some learning resources
```
#### git pull
`git pull = git fetch + git merge`，即：
```git
$ git fetch Learning main   //获取最新分支，返回FETCH_HEAD
$ git merge FETCH_HEAD  //将该远程分支合并到本地当前分支
```
用`git pull`可表示为：
```git
$ git pull <远程主机名> <远程分支名>:<本地分支名>
```
如果是与本地当前分支合并则可不写本地分支名：
```git
$ git pull Learning main
```
### conflict
要进行合并的分支有互相冲突的文件或行为，如两个分支中相同名称的文件有不同内容
```git
$ git pull Learning main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 665 bytes | 55.00 KiB/s, done.
From github.com:mostimaaa/Learning
 * branch            main       -> FETCH_HEAD
   cccb391..5a0f9f5  main       -> Learning/main
CONFLICT (modify/delete): README.md deleted in HEAD and modified in 5a0f9f57ec2556de6729f76549832fd2e16c337a.  Version 5a0f9f57ec2556de6729f76549832fd2e16c337a of README.md left in tree.
Automatic merge failed; fix conflicts and then commit the result.
```
操作步骤：
* 将两个分支的代码拉取到本地
* 手动整合
* 提交

拉取到本地后，在本地打开冲突的文件，修改为想要保留的内容后提交即可。
如，修改README后如下：
```git
86156@lzp MINGW64 ~/desktop/Learning (master|MERGING)
$ git add README.md

86156@lzp MINGW64 ~/desktop/Learning (master|MERGING)
$ git commit
[master c410de8] Merge branch 'main' of github.com:mostimaaa/Learning
```
### push
`git push`将本地分支上传到远程并合并
```git
$ git push <远程主机名> <本地分支名>:<远程分支名>
$ git push <远程主机名> <本地分支名>    //如远程分支名与本地分支名相同则可省略
```
如将本地master分支推送到Learning主机的main分支：
```git
$ git push Learning master:main
```
如果本地版本与远程版本有差异，但又要强制推送可以使用`--force`参数
```git
$ git push --force Learning master:main
```
删除主机的分支可以使用 --delete 参数，以下命令表示删除 Learning 主机的 main 分支：
```git
$ git push Learning --delete main
```