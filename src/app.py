import streamlit as st
import plotly.express as px
import pandas as pd

def main():
    st.title('Gantt Chart Example')
    st.write('This is a basic Gantt chart using Plotly in Streamlit.')

    # Example data for Gantt chart
    df = pd.DataFrame([
        dict(Task="Task A", Start='2025-06-01', Finish='2025-06-05'),
        dict(Task="Task B", Start='2025-06-03', Finish='2025-06-08'),
        dict(Task="Task C", Start='2025-06-06', Finish='2025-06-10'),
    ])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")
    fig.update_yaxes(autorange="reversed")  # Tasks from top to bottom
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
