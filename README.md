# basic_uia

Based on Python3

## 使用

### 配置

- 在`config.py`中添加手机id
- 在cases中添加用例，参考`sample.py`
- API参考[这里](https://blog.csdn.net/qq_38071435/article/details/80003212)

### 运行方式

- `python run.py` 会根据`config.py`中的配置运行
- `python run.py -d 123456F` 会在id为`123456F`的机型上运行
- `python run.py -d 123456F -t abcde` 会指定任务名为abcde

## 工程主要结构

- basic_uia
    - 工程核心
    - 开发人员维护
    - 测试人员不必关心这个部分
- cases
    - 用例脚本文件都放置在这里
- extend_api.py
    - 自定义的API放置在这里
    - 用于简化一些重复性比较高的动作
- run.py
    - 入口
    