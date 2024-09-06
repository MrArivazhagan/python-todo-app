import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    # session_state is dict
    # it contains widgets values, if it has key
    new_todo = st.session_state["new todo"]
    todos.append(new_todo + '\n')
    functions.write_todos(todos)

st.title("Todo App")
st.subheader("This is web-based Todo App")
st.write("Store all your <b>works</b> to do here", unsafe_allow_html=True)
print(todos)
for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.rerun()

# label is not optional parameter
# after calling add_todo the whole script will run
st.text_input(label="Enter a todo",
              label_visibility="hidden",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new todo")

# st.session_state