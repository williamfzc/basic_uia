# basic_uia

## 使用

- Python3
- 安装requirements.txt中的依赖
    - `pip install -r requirements.txt`
- 在`config.py`中添加手机id
- 在cases中添加用例，参考`sample.py`，更具体的看[这里](https://github.com/xiaocong/uiautomator)
- 运行方式:
    - `python run.py` 会根据`config.py`中的配置运行
    - `python run.py -d 123456F` 会在id为`123456F`的机型上运行
        - 支持多设备，`python run.py -d 123456F,234567E`，逗号分隔，不能有空格
        - 串行执行，如果需要并行建议使用上层流水线
    - 支持指定任务名
        - `python run.py -d 123456F -t abcde`

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
    