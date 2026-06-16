import streamlit as st
from agent.react_agent import ReactAgent

st.set_page_config(page_title="清洁管家 Agent", page_icon="🤖")
st.title("清洁管家 Agent")
st.caption("扫地机器人客服 / 导购 / 使用报告助手，基于 LangChain ReAct Agent + RAG 检索增强")
st.divider()

if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})

    response_messages: list[str] = []
    with st.spinner("清洁管家正在分析问题..."):
        res_stream = st.session_state["agent"].execute_stream(prompt)

        def stream_generator(generator, cache_list):
            """逐字流式输出，同时缓存完整响应"""
            for chunk in generator:
                cache_list.append(chunk)
                for char in chunk:
                    yield char

        st.chat_message("assistant").write_stream(stream_generator(res_stream, response_messages))
        st.session_state["messages"].append({"role": "assistant", "content": "".join(response_messages)})
        st.rerun()
