# git学习

## git 安装()
$ sudo apt-get install git

## 创建git仓库 初始化
$ mkdir [name]

$ cd [name]

$ git init
  
## Git clone 拷贝一个 Git 仓库到本地，让自己能够查看该项目，或者进行修改。
git clone [url]

## 基本快照 （Git 的工作就是创建和保存你的项目的快照及与之后的快照进行对比）
 ###git add

 git add 命令可将该文件添加到缓存，如我们添加以下文件：

  $ touch README

  $ touch hello.php

  $ ls  

  README        hello.php

  $ git status -s      ##git status 命令用于查看项目的当前状态。

  ?? README

  ?? hello.php

接下来我们执行 git add 命令来添加文件：

  git add README hello.php (通常新建仓库我们使用git add . & git add * 添加全部)
  
  再执行 git status，就可以看到这两个文件已经加上去了。
  
##git commit
使用 git add 命令将想要快照的内容写入缓存区， 而执行 git commit 将缓存区内容添加到仓库中。

Git 为你的每一个提交都记录你的名字与电子邮箱地址，所以第一步需要配置用户名和邮箱地址。


 

## github 

## mysql 关系型数据库 
    _mysql_
