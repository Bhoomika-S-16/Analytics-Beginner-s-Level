# Analytics-Beginner-s-Level
Explore and Learn with me!

This project performs exploratory data analysis (EDA) and visualization on the Netflix Titles Dataset.
It uses Python libraries such as Pandas, Matplotlib, Seaborn, and Collections to uncover insights about movies, TV shows, countries, genres, and directors available on Netflix.

## Dataset

The project uses the netflix_titles.csv file, which contains information about Netflix Movies and TV Shows, including:

Title

Director

Cast

Country

Release year

Rating

Duration

Genre categories (listed_in)

Type (Movie or TV Show)

## Data Cleaning

The script includes optional steps to clean the dataset:

Filling missing values with "unknown"

Converting year fields to numeric

Handling genre categories by splitting and exploding them into individual rows

These lines are currently commented out and can be enabled as needed.

## Visualizations Included
✔️ Count of Movies vs TV Shows

A Seaborn countplot to show how many titles fall under each category.

✔️ Top Countries Producing Netflix Content

A bar chart showing the top 5 countries with the highest number of Netflix titles.

✔️ Most Common Genres

Genres are extracted from the listed_in column, split, and counted using Counter.
The top 5 are visualized with a barplot.

✔️ Most Popular Directors

A bar chart showing the top 5 directors based on the number of titles in the dataset

