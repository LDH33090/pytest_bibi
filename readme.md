## 代码结构

- testcase 主要存放测试用例
- commom 主要存放公共函数
- api_test: 接口封装层，如封装HTTP接口为Python接口
- commom: 从文件中读取数据等各种工具类
- config: 环境、数据库连接等配置
- core: requests 请求方法封装、关键字返回结果类
- testdata: 测试数据文件管理
- operation: 关键字封装层，如把多个Python接口封装为关键字
- pytest.ini: pytest 配置文件
- requirements.txt: 相关依赖包文件
- testcases: 测试用例
- api_test: 单接口测试
- scenario_test: 场景/业务流程测试
- readme.md: 框架简介