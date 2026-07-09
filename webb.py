import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)

st.title("Todo app")
st.subheader("check your todos here")

for index, todo in enumerate(todos):
    chck = st.checkbox(todo, key=todo)
    if chck:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="enter new todos here..",
              on_change=add_todo, key="new_todo")


