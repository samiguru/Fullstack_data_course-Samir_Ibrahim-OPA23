from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st
import pycountry

class ViewsTrend:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.views_per_date").df
        self._gender = QueryDatabase("SELECT * FROM marts.views_per_gender").df
        self._age = QueryDatabase("SELECT * FROM marts.views_per_age").df
        self._top_10 = QueryDatabase("SELECT * FROM marts.views_top_10").df
        self._latest_10 = QueryDatabase("SELECT * FROM marts.views_latest_10").df
        self._geografy = QueryDatabase("SELECT * FROM marts.viewer_content_geografy").df
        self._op_system = QueryDatabase("SELECT * FROM marts.views_per_op_system").df


        print(self._content)

    def display_plot(self):
        fig = px.line(self._content, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)
    
    def top_10_plot(self):
        fig = px.bar(self._top_10, x="Videotitel", 
        y="totala_visningar", title="De 10 Mest Visade Videorna med Totala Visningar", 
        height=600)
        fig.update_yaxes(range=[0, 120])
        st.plotly_chart(fig)

    def latest_10_plot(self):
        fig = px.scatter(self._latest_10, x="Videotitel", 
        y="Publiceringstid för video", 
        title="Releasedatum och Videotitel till de senaste videon", 
        height=600)
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig)

    def op_system_plot(self):
        op_system_df = self._op_system[:-1].sort_values(
            by='Totala_visningar', ascending=True).reset_index(drop=True)

        fig = px.bar(
            op_system_df,
            x='Totala_visningar',
            y='Operativsystem',
            orientation='h',
            color='Totala_visningar',
            title='Vanligaste operativsystemet baserat på totala visningar',
            labels={'Totala_visningar': 'Antal visningar',
                    'Operativsystem': 'Operativsystem'},
            height=600
        )

        fig.update_layout(
            xaxis_title="",
            yaxis_title="",
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
        )

        st.plotly_chart(fig, use_container_width=True)

    def geografy_map_plot(self):
        top_10_plot_df = self._geografy

        def convert_to_iso3(iso2):
            try:
                return pycountry.countries.get(alpha_2=iso2).alpha_3
            except AttributeError:
                return None

        top_10_plot_df['Geografi_ISO3'] = self._geografy['Geografi'].apply(convert_to_iso3)

        top_10_plot_df = self._geografy.dropna(subset=['Geografi_ISO3'])

        fig = px.choropleth(
            self._geografy,
            locations="Geografi_ISO3",
            locationmode="ISO-3",
            color="Visningar",
            hover_name="Geografi",
            color_continuous_scale=px.colors.sequential.Plasma,
            title="Visningar per land",
            labels={'Visningar': 'Totala Visningar'}
        )

        fig.update_layout(
            title={
                'text': "Visningar per land",
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },

            geo=dict(
                showframe=False,
                showcountries=True,
                projection_type="equirectangular",
                resolution=50,
                showcoastlines=True,
                coastlinecolor="gray",
                countrycolor="black",
                center=dict(lat=45, lon=25),
                lataxis_range=[20, 60],
                lonaxis_range=[-20, 40]
            ),
            margin={"r": 0, "t": 40, "l": 0, "b": 0},
            height=500,
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
            coloraxis_colorbar=dict(
                title="Totala Visningar",
                x=0.85,
                xanchor='left')

        )

        st.plotly_chart(fig, use_container_width=True)