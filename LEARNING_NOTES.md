# 学习笔记

## Python 项目环境

### 核心原则

一个项目
→ 一个虚拟环境
→ 一套独立依赖
→ 一个稳定运行环境

### 理解

虚拟环境用于隔离不同项目的 Python、FastAPI、Uvicorn 以及其他第三方依赖，避免版本冲突和环境互相干扰。

## API、FastAPI 与 Uvicorn

- API = 我们要创建的后端接口。
- FastAPI = 我们选择的 Python 工具，用来编写 API。
- Uvicorn = 运行 FastAPI 服务的服务器。

关系：

```text
FastAPI + Uvicorn
        ↓
运行 API
        ↓
/projects、/docs 等地址
```
