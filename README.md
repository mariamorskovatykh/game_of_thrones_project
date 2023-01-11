# Exploring the Social Dynamics of 'A Song of Ice and Fire' Through Network Analysis

## Introduction

This project uses web scraping, data visualization, and network analysis techniques to gain insights into the complex world of George R. R. Martin's 'A Song of Ice and Fire' book series. The project focuses on the relationships between the characters of the series, and how they change and evolve throughout the books.

## Data Collection

The character data used in this project was collected by web scraping the A Song of Ice and Fire Wiki website (https://iceandfire.fandom.com/wiki/Wiki). The script collects character's name, houses, aliases, culture, and books they appeared in.

## Data Analysis

The data collected was then used to create a social network of the characters, with edges representing interactions between characters. The network was analyzed to find the important characters, communities and dynamics between them. I use various network analysis metrics such as degree centrality, betweenness centrality, and clustering coefficient to find characters' importance and their interactions with other characters.

## Visualization

The results of the data analysis are presented through interactive plots and network visualizations. These visualizations provide a deeper understanding of the interactions and power dynamics between the characters of the series.

## How to Use

The project is developed in Python 3.10.6 with Jupyter Notebook, to use the project you will need to have the following libraries installed:

* pytest
* pylint
* ipdb
* jupyterlab
* numpy
* pandas
* matplotlib
* seaborn
* selenium
* webdriver-manager

You can install them using pip:

```pip install -r requirements.txt```

To run the project, open the Jupyter notebook `exploring_social_dynamics.ipynb` and run the cells in order.

## Conclusion

This project demonstrates how network analysis and data visualization can be used to gain a deeper understanding of the relationships between the characters in George R. R. Martin's 'A Song of Ice and Fire' series. It provides an interactive way for fans of the series to explore the complex dynamics of the world and characters, and can also be used as a teaching tool for students learning about network analysis and data visualization.

## Limitations

The project is limited by the data available on A Song of Ice and Fire Wiki and the structure of the Wiki itself, the characters are represented by pages and the interactions are represented by the links between them. However, this project can be further expanded by using more sources of data, like the books and the series and extract more information about characters' traits, events and dynamics.

## Future Work

This project can be extended to look at other aspects of the series, such as the dynamics of the different houses. Additionally, it could be used as a starting point for further research on how network analysis and data visualization can be used to study fictional worlds and characters.

