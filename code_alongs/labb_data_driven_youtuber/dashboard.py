import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend


# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    
    st.sidebar.title("Meny")
    page = st.sidebar.radio(
        label="Välj sida",
        options=["Översikt", "Tittare"])
    
    if page == "Översikt":
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas sammanfattning för totala antal")
    
        content_kpi.display_content()
        views_graph.display_plot()

if __name__ == "__main__":
    layout()