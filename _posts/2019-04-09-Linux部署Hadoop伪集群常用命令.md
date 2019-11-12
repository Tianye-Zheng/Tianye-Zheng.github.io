---
layout: post
title:  "Linux部署Hadoop伪集群常用命令"
date:   2019-04-09
desc: ""
keywords: ""
categories: [Linux]
tags: []
icon: icon-html
---

实验总结的小备忘录
<br />
首先切换到目录下，在我的虚拟机是 `/home/hadoop/hadoop_installs/hadoop-2.7.1/`

启动
`sbin/start-all.sh`
<br />

列出运行进程
`jps`
<br />

停止
`sbin/stop-all.sh`
<br />

集群启动正常启动后，用浏览器打开查看 HDFS 文件系统

`localhost:50070`
<br />

查看集群运行状态

`http://localhost:8088/cluster`
<br />

切换到 hadoop2.7.1 目录下，列出集群中所有文件

`bin/hdfs dfs -ls /`
<br />

删除 HDFS 文件系统中名为 test-out 的文件夹

`bin/hdfs dfs -rm -R /test-out`
<br />

运行 jar 包，test-in/lab3Data 作为输入 test-out/lab3-out 作为输出

`hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.1.jar wordcount /test-in /test-out`
`hadoop jar /home/hadoop/Desktop/IdeaProjects/HadoopLab3/target/HadoopLab3-1.0-SNAPSHOT.jar /lab3Data /lab3-out`
<br />

从本地文件系统复制文件到集群中

`bin/hdfs dfs -copyFromLocal /home/hadoop/Desktop/test/ /lab3Data`
<br />


