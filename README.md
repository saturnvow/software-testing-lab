# software-testing-lab

软件测试与质量保证课程实验项目：一个简易计算器模块（Python + pytest）。

## 功能

- 四则运算：加、减、乘、除
- 幂运算（power）
- 统计运算：平均值（mean）
- 异常处理：除数为 0、非法参数抛出明确异常

## 运行测试

```bash
pip install pytest
pytest -v
```

## 目录结构

```
calculator.py        # 被测模块
tests/               # 单元测试
```
