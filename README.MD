# web_dic
  web高精度字典生成

# 简要介绍
  - 1、使用python，依据常见的字典规则来创造新的高精度字典；
  - 2、用到了python第三方库，exrex(其实是对re库的分析和扩展)；
  - 3、程序完成后，考虑以插件的形式加入BurpSuite。

# 使用方法：
  ```
  	shell
  	python web_dic.py www.demo.com.cn
  ```

# 配置说明
  web_dic.ini 存放的是配置文件，关键配置只有一行，写入你认为适合的正则代码即可