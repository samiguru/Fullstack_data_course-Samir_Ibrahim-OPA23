import streamlit as st
from frontend.kpi import ContentKPI, GenderAgeKPI, ViewerGeografy, OpSystemViews, Subscribers, Top10
from frontend.graphs import ViewsTrend



content_kpi = ContentKPI()
views_graph = ViewsTrend()
age_kpi = GenderAgeKPI()
viewer_geografy = ViewerGeografy()
viewer_geografy_plot = ViewsTrend()
op_system = OpSystemViews()
op_system_plot = ViewsTrend()
subscribers = Subscribers()
top_10 = Top10()
top_10_plot = ViewsTrend()
latest_10_plot = ViewsTrend()


def layout():

    st.sidebar.title("Meny")
    page = st.sidebar.radio(
        label="Välj sida",
        options=["Översikt", "Tittare", "Trender och nya releaser", "Enhetstyp"])

    if page == "Översikt": # Första sidan
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas sammanfattning för totala antal")
        content_kpi.display_content()
        views_graph.display_plot()
    

    elif page == "Tittare": # Andra sidan
        st.markdown("## Tittarstatistik")
        age_kpi.display_gender_age()
        viewer_geografy.display_viewer_geografy()
        viewer_geografy_plot.geografy_map_plot()
        subscribers.display_subscribers()


    elif page == "Trender och nya releaser": # Tredje sidan
        st.header("Videostatistik och trender")
        top_10_plot.top_10_plot()
        top_10.display_top_10()
        latest_10_plot.latest_10_plot()


    elif page == "Enhetstyp": # Fjärde sidan
        st.header("Statistik")
        op_system_plot.op_system_plot()
        op_system.display_op_system()


if __name__ == "__main__":
    layout()