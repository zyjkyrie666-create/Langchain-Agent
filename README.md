# LangChain ReAct Agent 新能源汽车客服案例模板

这是一个基于 **LangChain + LangGraph ReAct Agent + RAG** 的智能客服示例项目，当前业务案例为「新能源汽车客服 / 用车顾问 / 车辆使用报告」。

项目架构保持原项目不变，仍然保留：

- `agent/`：ReAct Agent 主流程和工具调用
- `rag/`：知识库加载、向量检索、RAG 总结
- `model/`：模型与 Embedding 工厂
- `config/`：YAML 配置
- `prompts/`：普通问答和报告生成提示词
- `data/`：新能源汽车知识库文档
- `data/external/records.csv`：模拟车主月度车辆使用记录
- `app.py`：Streamlit 对话入口

## 当前案例能力

这个模板可以模拟新能源汽车品牌的智能助手，支持三类核心问题：

1. 用车咨询：续航、电耗、充电、低温用车、雨天充电、动能回收。
2. 故障排查：无法充电、续航突然下降、无法启动车辆、辅助驾驶异常。
3. 个性化报告：结合外部用户记录，生成某个用户某月的车辆使用报告和服务建议。

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
│   ├── new_energy_vehicle_faq.txt
│   ├── charging_and_battery_guide.txt
│   ├── nev_maintenance_and_service.txt
│   ├── nev_troubleshooting.txt
│   └── nev_buying_guide.txt
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

首次运行前，先把 `data/` 目录中的新能源汽车文档写入 Chroma 向量库：

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
新能源汽车日常充电一定要充到100%吗？
```

```text
车辆突然无法充电，我应该怎么排查？
```

```text
冬天续航下降明显，怎么降低电耗？
```

```text
帮我生成这个月的车辆使用报告
```

## 案例说明

这版模板没有改变底层 Agent 和 RAG 架构，只替换业务内容：

- `prompts/main_prompt.txt`：定义新能源汽车客服的工具使用规则。
- `prompts/report_prompt.txt`：定义车辆使用报告生成格式。
- `prompts/rag_summarize.txt`：定义新能源汽车知识库总结规则。
- `data/`：提供新能源汽车 FAQ、充电、电池、保养、故障排查、选购等知识库文档。
- `data/external/records.csv`：模拟车主月度车辆使用记录。

## 注意事项

1. 运行前必须配置 `DASHSCOPE_API_KEY`。
2. 第一次运行问答前需要先初始化知识库。
3. 如果修改了 `data/` 中的知识库文档，建议删除旧向量库后重新初始化，避免旧知识残留。
4. 本项目是学习模板，真实商用前需要接入真实车主、车辆、工单和售后系统。

## License

MIT
