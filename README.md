# DBot_platform

DBot微服务的平台程序。
作为一个API网关程序和消息代理程序，负责接收和处理来自不同微服务的请求和消息，并进行路由和转发，实现微服务之间的通信和协作。
DBot_platform作为微服务架构的入口程序，用于运行其他微服务架构的[服务程序](README.md#其他服务程序)，提供了可靠、高效、灵活的服务注册、发现和调用功能，从而帮助企业快速构建和扩展微服务架构。

## 其他服务程序

- [DBot_monitor](https://github.com/dzming-git/DBot_monitor)

## 功能与权限要求

### 主程序支持的指令

| 指令               | 举例             | 功能                                   | 权限要求 |
| ------------------ | ---------------- | -------------------------------------- | -------- |

### 服务程序支持的指令

前往[服务程序](README.md#服务程序)中对应的链接中查看。

## 安装运行

### 安装

1. 从 [go-cqhttp](https://docs.go-cqhttp.org/guide/quick_start.html) 下载合适你的操作系统的安装包，并根据说明完成初始化。
   
2. 从 [Consul官网](https://www.consul.io/downloads.html) 下载适合你的操作系统的安装包，并安装。

3. 下载代码到本地的`DBot_platform`目录。

4. 安装依赖库，运行以下命令：

   ``` python
   pip install -r requirements.txt
   ```

### 运行

1. 运行`consul`：

   ``` bash
   consul agent -dev
   ```

2. 运行`go-cqhttp`：
   [go-cqhttp帮助中心](https://docs.go-cqhttp.org/guide/quick_start.html#%E4%BD%BF%E7%94%A8)
   

3. 运行DBot微服务的平台程序 `app/server.py`：
   
   **注意 项目的工作目录必须是根目录**

   ``` python
   python -m app.server
   ```
   或者
   
   配置`run.bat`文件中运行该程序的python地址后，双击打开`run.bat`

## 配置文件

- `conf/route_info/route_info.yaml` - 配置文件，包括DBot微服务的API网关和消息代理的配置信息。

## 授权许可

本项目使用 MIT 许可证，有关更多信息，请参阅 LICENSE 文件。

## 联系我们

如果您对本项目有任何问题或建议，请随时通过以下方式联系我们：

- Email: dzm_work@163.com
- QQ: 715558579
