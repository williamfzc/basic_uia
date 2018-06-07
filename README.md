# basic_uia

** 项目初期，如果遇到各种问题请马上反馈 **

## 使用

- Python3
- 安装requirements.txt中的依赖
    - `pip install -r requirements.txt`
- 在`config.py`中添加手机id
- 在cases中添加用例，参考`sample.py`，更具体的看[这里](https://blog.csdn.net/Temanm/article/details/49366485)
- 运行方式:
    - `python run.py` 会根据`config.py`中的配置运行
    - `python run.py -d 123456F` 会在id为`123456F`的机型上运行
        - 支持多设备，`python run.py -d 123456F,234567E`，逗号分隔，不能有空格
        - 串行执行，如果需要并行建议使用上层流水线
    - 支持指定任务名
        - `python run.py -d 123456F -t abcde`

## 扩展

### API

参见`basic_uia/api.py`，可以在其中自定义API供用例调用。