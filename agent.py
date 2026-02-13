import asyncio
import streamlit as st
from dotenv import load_dotenv
from agents import Agent, Runner, trace

load_dotenv(override=True)

st.set_page_config(page_title="AI Chat", page_icon="🏆")

st.title("🏆 AI Chat")
st.write("Ask the AI about anything in this website")
agent = Agent(
    name="chatapp",
    instructions="You are an AI agent for my real-time chat application",
    model="gpt-4.1-mini"
)
async def run_agent(prompt: str):
    with trace("Application Conversation"):
        result = await Runner.run(agent, prompt)
        return result.final_output

def run_agent_sync(prompt: str):
    return asyncio.run(run_agent(prompt))

prompt = st.text_input(
    "Your question:",
    placeholder="ask me about chatty"
)

if st.button("Ask AI"):
    if prompt.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            try:
                response = run_agent_sync(prompt)
                st.success("AI Response")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")