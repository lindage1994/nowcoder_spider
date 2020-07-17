# nowcoder_spider

## 描述

对于爬虫这种东西，向来都是按需求来的

最近在整理面试相关的东西，就想着把别人的面经爬下来

参考了[利用selenium写一牛客网面经的爬虫](https://blog.csdn.net/qq_40050586/article/details/105729740) ，于是就有了这个

## 结果列表
[面经列表](./overview.md)

## chromedriver

- 下载对应 chrome 版本的 chromedriver， [chromdriver 下载地址](http://chromedriver.storage.googleapis.com/index.html)
- 将 chromedriver.exe 解压到 chrome 安装目录下(C:\Program Files (x86)\Google\Chrome\Application\)
- 配置环境变量 path 添加 C:\Program Files (x86)\Google\Chrome\Application\

## selenium
selenium 是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。
```
pip install selenium
```

## BeautifulSoup
一个解析html页面的库
```
pip install BeautifulSoup
```


## 参考
[利用selenium写一牛客网面经的爬虫](https://blog.csdn.net/qq_40050586/article/details/105729740)