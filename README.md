# Data-Science-Introduction-Course
These are the main projects I did for my data science introduction class at university. There's a total of 4, and all of them are done using Python.

**Note**: The language for all of these tasks is in Spanish.

## Titanic Project
This project consisted on using the dataset from the Titanic in order to solve some tasks related to basic data analysis. Everything was done using Python libraries such as pandas, matplotlib and seaborn. Everything was done in [this notebook](https://github.com/DancingIguana/Data-Science-Introduction-Course-/blob/main/Titanic%20Project/Proyecto%201.ipynb)

## Beautiful Soup
The purpose of this project was to use the basic tools from the Python library known as BeautifulSoup in order to scrape data from the [Books To Scrape](https://books.toscrape.com/) website. All of the project tasks were done in [this notebook](https://github.com/DancingIguana/Data-Science-Introduction-Course-/blob/main/Beautiful%20Soup/WebScrapingBS4.ipynb)

## Scrapy Introduction
As an introduction to the library of Scrapy, this project has the objective of using its tools in order to extract data of countries from the [The World Factbook](https://www.cia.gov/the-world-factbook/countries/). The project consists of three main components:
* [Spider](https://github.com/DancingIguana/Data-Science-Introduction-Course-/tree/main/ScrapyIntro/countries): it consists of the Python scripts that handle all of the data scraping. All of it is in [this directory].
* [Data](https://github.com/DancingIguana/Data-Science-Introduction-Course-/blob/main/ScrapyIntro/countries_items.csv): It consists of a csv created directly through the scripts in the Spider containing the data of all found countries in the website. There's also a [directory](https://github.com/DancingIguana/Data-Science-Introduction-Course-/tree/main/ScrapyIntro/flags) containing all the country flags that were also extracted through the scraping process.
* [Notebook](https://github.com/DancingIguana/Data-Science-Introduction-Course-/blob/main/ScrapyIntro/Scrapy.ipynb): A Jupyter Notebook that contains an explanation of the general steps followed in order to craft the Spider. It also has some *data wrangling* from the extracted data. At the end, it has a brief data analysis of the correlation between the GDP and percentage of Internet users of a country; which was done using the tools of pandas, seaborn and matplotlib.

## Metrics and Cross Validation
The intention of doing this project is to use machine learning models to classify the type of GDP from a country given its data. The data was the same as the one extracted from the **Scrapy Introduction** project. There was a *data wrangling* process with pandas before evaluating applying the models. The efficiency of the models is compared and tested at the end using some well-knwon metrics (like precision, recall, accuracy and $F_\beta$) with cross validation. Most of this process was done with Python's library sklearn designed for machine learning. All of it is in [this notebook](https://github.com/DancingIguana/Data-Science-Introduction-Course-/blob/main/Metrics%20and%20Cross%20Validation/Proecto_MyVC.ipynb).
