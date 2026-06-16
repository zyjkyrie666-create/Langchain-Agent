# LangChain ReAct Agent 扫地机器人案例模板

这是一个基于 **LangChain + LangGraph ReAct Agent + RAG** 的智能客服示例项目，当前案例已经替换为「扫地机器人 / 扫拖一体机器人」场景。

项目架构保持原项目不变，仍然保留：

- `agent/`：ReAct Agent 主流程和工具调用
- `rag/`：知识库加载、向量检索、RAG 总结
- `model/`：模型与 Embedding 工厂
- `config/`：YAML 配置
- `prompts/`：普通问答和报告生成提示词
- `data/`：扫地机器人知识库文档
- `app.py`：Streamlit 对话入口

## 当前案例能力

这个模板可以模拟一个扫地机器人品牌的智能助手，支持三类核心问题：

1. 使用咨询：例如清扫模式、拖地水量、地毯增压、地图管理、禁区设置。
2. 故障排查：例如无法回充、吸力下降、漏扫、边刷缠绕、拖布不出水。
3. 个性化报告：结合外部用户记录，生成某个用户某月的清洁效率、耗材状态和维护建议。

## 技术栈

| 模块 | 技术 |
|---|---|
| Agent | LangChain + LangGraph ReAct |
| LLM | 通义千问 DashScope / ChatTongyi |
| RAG | Chroma + DashScope Embedding |
| 文档处理 | TXT / PDF + RecursiveCharacterTextSplitter |
| 前端 | Streamlit |
| 配置 | YAML |

## 项目结构

```text
Langchain-Agent/
├── agent/
│   ├── react_agent.py
│   └── tools/
│       ├── agent_tools.py
│       └── middleware.py
├── config/
│   ├── agent.yml
│   ├── chroma.yml
│   ├── prompts.yml
│   └── rag.yml
├── data/
│   ├── external/records.csv
│   ├── robot_vacuum_service_template.txt
│   └── 其他扫地机器人知识库文档
├── model/
├── prompts/
├── rag/
├── utils/
├── app.py
└── requirements.txt
```

## 环境准备

建议使用 Python 3.10 或更高版本。

```powershell
pip install -r requirements.txt
```

配置 DashScope API Key：

```powershell
$env:DASHSCOPE_API_KEY="your-api-key"
```

如果使用 CMD：

```cmd
set DASHSCOPE_API_KEY=your-api-key
```

## 初始化知识库

首次运行前，先把 `data/` 目录中的扫地机器人文档写入 Chroma 向量库：

```powershell
python -c "from rag.vector_store import VectorStoreService; VectorStoreService().load_document()"
```

默认配置在 `config/chroma.yml`：

- 知识库目录：`data`
- 向量库目录：`chroma_db`
- 支持文件类型：`txt`、`pdf`
- 检索数量：`k=3`

## 启动应用

```powershell
streamlit run app.py
```

启动后访问：

```text
http://localhost:8501
```

## 测试问题

可以在聊天框输入：

```text
我家有猫，扫地机器人应该怎么设置清扫计划？
```

```text
机器人找不到充电座，应该怎么排查？
```

```text
木地板拖地时水量应该怎么设置？
```

```text
帮我生成这个月的扫地机器人使用报告
```

## 案例说明

这版模板没有改变底层 Agent 和 RAG 架构，只把业务场景换成了扫地机器人：

- `prompts/main_prompt.txt`：定义扫地机器人客服的工具使用规则。
- `prompts/report_prompt.txt`：定义使用报告生成格式。
- `data/`：提供扫地机器人 FAQ、选购、维护、故障排查等知识库文档。
- `data/external/records.csv`：模拟用户每月设备使用记录。

## 注意事项

1. 运行前必须配置 `DASHSCOPE_API_KEY`。
2. 第一次运行问答前需要先初始化知识库。
3. 如果修改了 `data/` 中的知识库文档，建议重新初始化向量库。
4. 本项目是学习模板，真实商用前需要补充鉴权、日志持久化、异常处理和真实业务接口。

## License

MIT
