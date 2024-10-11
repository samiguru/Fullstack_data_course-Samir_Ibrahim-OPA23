import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        #st.dataframe(df)

class GenderAgeKPI:
    def __init__(self) -> None:
        self._gender = QueryDatabase("SELECT * FROM marts.views_per_gender").df
        self._age = QueryDatabase("SELECT * FROM marts.views_per_age").df

    def display_gender_age(self):
        gender_df = self._gender
        age_df = self._age


        st.markdown("KPIer för kön och ålder")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Statistik per kön")
            selected_gender = st.selectbox("Välj en kön:", gender_df["Kön"].unique(), key='gender_selectbox')

            filtered_gender_df = gender_df[gender_df["Kön"] == selected_gender]

            if not filtered_gender_df.empty:
                st.markdown(f"#### Data för könkategori: {selected_gender}")
                st.write(f"- Genomsnittlig visningslängd: {filtered_gender_df['Genomsnittlig visningslängd'].values[0]}")
                st.write(f"- Genomsnittlig procent som har visats: {filtered_gender_df['Genomsnittlig_%_visat'].values[0]}")


        with col2:
            st.markdown("### Statistik per åldersgrupp")
            selected_age = st.selectbox("Välj en åldersgrupp:", age_df["Ålder"].unique(), key='age_selectbox')

            filtered_age_df = age_df[age_df["Ålder"] == selected_age]

            if not filtered_age_df.empty:
                st.markdown(f"#### Data för åldergrupp: {selected_age}")
                st.write(f"- Genomsnittlig visningslängd: {filtered_age_df['Genomsnittlig visningslängd'].values[0]}")
                st.write(f"- Genomsnittlig procent som har visats: {filtered_age_df['Genomsnittlig_%_visat'].values[0]}")


class ViewerGeografy:
    def __init__(self) -> None:
        self._geografy = QueryDatabase("SELECT * FROM marts.viewer_content_geografy").df

    def display_viewer_geografy(self):
        geografy_df = self._geografy
        st.markdown("## Geografisk placering")


        kpis = {
            "Geografi": geografy_df["Geografi"],
            "Visningar": geografy_df["Visningar"],
            "Genomsnittlig visningslängd": geografy_df["Genomsnittlig visningslängd"]
        }

        cols = st.columns(4)

        for index, row in geografy_df.iterrows():
            col_index = index % 4
            with cols[col_index]:
                    self.display_kpi(index, row)

    def display_kpi(self, index, row):
        st.markdown(f"""
        **{index + 1}. {row['Geografi']}**  
        - Visningar: {int(row['Visningar'])}
        - Genomsnittling visningstid: {row['Genomsnittlig visningslängd']}
        """)
        st.markdown("-"*10)
        

class OpSystemViews:
    def __init__(self) -> None:
        self._op_system = QueryDatabase("SELECT * FROM marts.views_per_op_system").df

    def display_op_system(self):
        op_system_df = self._op_system[:-1]
        st.markdown("### Vilka operativsystem är vanligast")

        op_system_df = op_system_df.sort_values(by="Totala_visningar", ascending=False).reset_index(drop=True)

        cols = st.columns(4)

        for index, row in op_system_df.iterrows():
            col_index = index % 4
            with cols[col_index]:
                    self.display_kpi(index, row)

    def display_kpi(self, index, row):
        st.markdown(f"""
        **{index + 1}. {row['Operativsystem']}**  
        - Totala visningar: {int(row['Totala_visningar'])}
        """)
        st.markdown("-"*10)
              


class Subscribers:
    def __init__(self) -> None:
        self._subscribers = QueryDatabase("SELECT * FROM marts.subscribers").df

    def display_subscribers(self):
        subscribers_df = self._subscribers
        st.markdown("## Prenumeranter")

        for index, row in subscribers_df.iterrows():
            st.markdown(f"### {row['Prenumerationskälla']}")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Totala prenumeranter", row["Totala_prenumeranter"])
            with col2:
                st.metric("Nya prenumeranter", row["Totala_nya_prenumeranter"])
            with col3:
                st.metric("Förlorade prenumeranter", row["Totala_förlorade_prenumeranter"])



class Top10:
    def __init__(self) -> None:
        self._top_10 = QueryDatabase("SELECT * FROM marts.views_top_10").df


    def display_top_10(self):

        top_10_df = self._top_10[['Videotitel', 'Publiceringstid för video', 'totala_visningar', 'Visningstid (timmar)', 'Prenumeranter']]
        
        top_10_df.columns = ['Videotitel', 'Publiceringstid', 'Totala visningar', 'Visningstid (timmar)', 'Prenumeranter']

        st.markdown("### Mer detaljerat om de 10 senaste videorna")

        for index, row in top_10_df.iterrows():
            st.markdown(f"#### {index + 1}. {row['Videotitel']}")
            kpis = {
                "Publiceringstid": row['Publiceringstid'],
                "Totala visningar": row['Totala visningar'],
                "Visningstid (timmar)": round(row['Visningstid (timmar)'], 2),
                "Prenumeranter": row['Prenumeranter']
            }

            columns = st.columns([2, 1, 1, 1])
            for col, (label, value) in zip(columns, kpis.items()):
                with col:
                    st.metric(label=label, value=value, label_visibility="visible")
                    st.markdown("")
