from shiny import *
from shiny.express import input, ui, render
from shinywidgets import render_plotly
import plotly.express as px
import pandas as pd
from faicons import icon_svg

# Load data
df = pd.read_csv('Avacado_data(1972-).csv')
df['Year'] = df['Year'].astype(str)

# Define the UI layout
ui.page_opts(title="California Avocado Insights Dashboard: Unveiling Crop Value and Volume Trends 🥑",  fillable=True)

# Define reactive function to filter data based on selected year
@reactive.calc
def filtered_df():
    selected_year = input.year_filter()
    if selected_year == "All":
        return df
    else:
        return df[df['Year'] == selected_year]

# Define UI layout with sidebar and main content
with ui.sidebar(open="closed", bg="#C0C0C0"):
    ui.input_select(
        id="year_filter",
        label="Select Year",
        choices=["All"] + sorted(df['Year'].unique().tolist()),
        selected="All"
    )

# Define UI layout with value boxes
with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("calendar"), bg="#FFCC00"):
        "Number of Years"
        @render.text
        def count_years():
            return filtered_df()['Year'].nunique()

    with ui.value_box(showcase=icon_svg("chart-bar"), bg="#66CCFF"):
        "Average Bearing Acres"
        @render.text
        def avg_bearing_acres():
            return f"{filtered_df()['Bearing Acres'].mean():.2f}"

    with ui.value_box(showcase=icon_svg("chart-line"), bg="#FF99CC"):
        "Total Volume (millions of pounds)"
        @render.text
        def total_volume():
            return f"{filtered_df()['Volume (millions of pounds)'].sum():,.2f}"

    with ui.value_box(showcase=icon_svg("coins"), bg="#99FF99"):
        "Total Crop Value ($)"
        @render.text
        def total_crop_value():
            total_value = filtered_df()['Crop Value ($)'].sum() / 1_000_000  # Dividing by 1 million
            return f"${total_value:.2f} million"

    with ui.value_box(showcase=icon_svg("dollar-sign"), bg="#FFCCFF"):
        "Average Price Per Pound (¢)"
        @render.text
        def avg_price_per_pound():
            return f"{filtered_df()['Price Per Pound (¢)'].mean():,.2f} ¢"

    with ui.value_box(showcase=icon_svg("money-bill"), bg="#FFFF99"):
        "Average Dollars Per Bearing Acre ($)"
        @render.text
        def avg_dollars_per_acre():
            return f"${filtered_df()['Average Dollars Per Bearing Acre ($)'].mean():,.2f}"

# Time series plot for Volume and Crop Value
@reactive.calc
def generate_figures():
    fig1 = px.line(filtered_df(), x='Year', y='Volume (millions of pounds)', title='Volume Over Years',
                   labels={'Volume (millions of pounds)': 'Volume (millions of pounds)', 'Year': 'Year'},
                   color_discrete_sequence=['blue'])

    fig2 = px.line(filtered_df(), x='Year', y='Crop Value ($)', title='Crop Value Over Years',
                   labels={'Crop Value ($)': 'Crop Value ($)', 'Year': 'Year'},
                   color_discrete_sequence=['green'])

    fig3 = px.scatter(filtered_df(), x='Price Per Pound (¢)', y='Crop Value ($)', color='Year',
                      title='Price Per Pound vs. Crop Value', trendline="ols",
                      labels={'Price Per Pound (¢)': 'Price Per Pound (¢)', 'Crop Value ($)': 'Crop Value ($)'},
                      color_discrete_sequence=px.colors.qualitative.Prism)

    fig4 = px.bar(filtered_df(), x='Year', y='Average Dollars Per Bearing Acre ($)', title='Average Dollars Per Bearing Acre',
                  labels={'Average Dollars Per Bearing Acre ($)': 'Average Dollars Per Bearing Acre ($)', 'Year': 'Year'},
                  color='Year',
                  color_discrete_sequence=px.colors.qualitative.Plotly)

    fig5 = px.area(filtered_df(), x='Year', y='Volume (millions of pounds)', title='Volume Trend over Years',
                   labels={'Volume (millions of pounds)': 'Volume (millions of pounds)', 'Year': 'Year'},
                   color_discrete_sequence=['purple'])

    return fig1, fig2, fig3, fig4, fig5

# Define layout for plots
with ui.layout_column_wrap(fill=False):
    with ui.card(width=6):
        ui.card_header("Volume and Crop Value Over Years")
        @render_plotly
        def plot1():
            return generate_figures()[0]

    with ui.card(width=6):
        ui.card_header("Crop Value Over Years")
        @render_plotly
        def plot2():
            return generate_figures()[1]

    with ui.card(width=6):
        ui.card_header("Price Per Pound vs. Crop Value")
        @render_plotly
        def plot3():
            return generate_figures()[2]
with ui.layout_column_wrap(fill=False):
    with ui.card(width=6):
        ui.card_header("Average Dollars Per Bearing Acre")
        @render_plotly
        def plot4():
            return generate_figures()[3]

    with ui.card(width=6):
        ui.card_header("Volume Trend over Years")
        @render_plotly
        def plot5():
            return generate_figures()[4]