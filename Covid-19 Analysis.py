import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_and_clean_data(filepath):
    """
    Load the COVID-19 dataset and clean the column names.
    """
    df = pd.read_csv(filepath)
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df
def plot_top_confirmed(df):
    #Top values by confirmed
    top_confirmed=df.sort_values(by="confirmed",ascending=False).head(10)

    # Bar chart: Top 10 countries by confirmed cases
    plt.figure(figsize=(10, 6))
    plt.bar(top_confirmed['country/region'], top_confirmed['confirmed'])
    plt.title('Top 10 Countries by Confirmed COVID-19 Cases')
    plt.xlabel('Country')
    plt.ylabel('Confirmed Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_top_deaths(df):
    #top countries by death
    top_deaths_country=df.sort_values(by="deaths",ascending=False).head(10)

    # Bar chart: Top contries By Death
    plt.figure(figsize=(10,6))
    plt.bar(top_deaths_country["country/region"],top_deaths_country["deaths"])
    plt.title("Top contries By Death Covid-19 cases")
    plt.xlabel("Country")
    plt.ylabel("Deaths")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_weekly_increases(df):
    #Highest weekly increase in cases
    top_weekly_increase = df.sort_values(by='1_week_%_increase', ascending=False).head(10)

    # Line plot: Highest weekly increase in cases
    plt.figure(figsize=(10,6))
    plt.plot(top_weekly_increase["country/region"],top_weekly_increase["1_week_%_increase"])
    plt.title("Highest weekly increase in cases")
    plt.xlabel("Country")
    plt.ylabel("Weekly increase")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_death_rate(df):
    # Calculate Death Rate (%)
    df['death_rate_percent'] = (df['deaths'] / df['confirmed']) * 100
    top_death_rates = df.sort_values(by='death_rate_percent', ascending=False).head(10)

    # Barchart: Death rate calculation
    plt.figure(figsize=(10,6))
    plt.bar(top_death_rates ["country/region"],top_death_rates ["death_rate_percent"])
    plt.title("Death rate calculation")
    plt.xlabel("Country")
    plt.ylabel("Death Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def plot_Total_Cases_by_WHO_Region(df):
    #Total Cases by WHO Region
    cases_by_region = df.groupby('who_region')['confirmed'].sum().sort_values(ascending=False)
    
    # Bar Chart:Total Cases by WHO Region
    plt.figure(figsize=(10,6))
    plt.bar(df["who_region"],df["confirmed"],color="teal")
    plt.title("Total Cases by WHO Region")
    plt.xlabel("WHO Region")
    plt.ylabel("Confirmed")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def plot_Active_Cases_vs_Recovered(df):
    #Active Cases vs Recovered
    top_active = df.sort_values(by='active', ascending=False).head(10)
    countries = top_active['country/region']
    active_cases = top_active['active']
    recovered_cases = top_active['recovered']

    # Set up the bar positions
    x = np.arange(len(countries))
    width = 0.35
    #Bar chart: Active Cases vs Recovered
    plt.figure(figsize=(12, 6))
    plt.bar(x - width/2, active_cases, width, label='Active Cases', color='orange')
    plt.bar(x + width/2, recovered_cases, width, label='Recovered Cases', color='green')
    plt.xlabel('Country')
    plt.ylabel('Number of Cases')
    plt.title('Top 10 Countries: Active vs Recovered COVID-19 Cases')
    plt.xticks(x, countries, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
def main():
    filepath = r"C:\Users\K7\Desktop\country_wise_latest.csv"
    df = load_and_clean_data(filepath)

    plot_top_confirmed(df)
    plot_top_deaths(df)
    plot_weekly_increases(df)
    plot_death_rate(df)
    plot_Total_Cases_by_WHO_Region(df)
    plot_Active_Cases_vs_Recovered(df)
   
    # Summary stats
    print("Total confirmed:", df["confirmed"].sum())
    print("Total deaths:", df["deaths"].sum())
    print("Total recovered:", df["recovered"].sum())

if __name__ == "__main__":
    main()




