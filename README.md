# basic_uia

Based on Python3

## 使用

### 配置

- 在`config.py`中添加手机id
- 在cases中添加用例，参考`sample.py`

### 运行方式

- `python run.py` 会根据`config.py`中的配置运行
- `python run.py -d 123456F` 会在id为`123456F`的机型上运行
- `python run.py -d 123456F -t abcde` 会指定任务名为abcde

### 多设备 (BETA)

`python multi_run.py -d 123456F,234567F -t abcde`

- 将会在id为123456F与234567F的机器上并行执行
- 结果会命名为`abcde_123456F`与`abcde_234567F`的形式

## 注意事项

- 在启动前需要使用`python -m uiautomator2 init`初始化设备
- 如需使用中文输入，先在手机上安装`basic_uia/tools/ADBKeyBoard.apk`并将其设置为默认输入法，之后调用api.py中的`input_chinese`

## 实用工具参考

- 一定要看的[API文档](https://blog.csdn.net/qq_38071435/article/details/80003212)
- 用来查看控件，代替uiautomatorviewer的[Weditor](https://github.com/openatx/weditor)

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
    