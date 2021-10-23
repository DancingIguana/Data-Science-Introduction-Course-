# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountriesItem(scrapy.Item):
    # Información de los países del mundo
    nombre = scrapy.Field()
    continente = scrapy.Field() # Map references
    area = scrapy.Field()
    poblacion = scrapy.Field()
    gdp = scrapy.Field() # Real GDP per capita (2019)
        # Outliers < 50
        # Low income >= 50 and <= 5,000
        # Median income > 5,000 and <= 25,000
        # High income > 25,000

    desempleo = scrapy.Field() # Unemployment rate (2017)
    impuestos = scrapy.Field() # Taxes and other revenues (2017)
    deuda = scrapy.Field() # Debt - external
    tasa_de_cambio = scrapy.Field() # Exchange rates in US Dollars (2017)
    usuarios_internet = scrapy.Field() # Internet users - total
    porcentaje_internet = scrapy.Field() # Internet users - percent of population
    aeropuertos = scrapy.Field() # Airports
    carreteras_km = scrapy.Field() # Roadways
    inversion_militar = scrapy.Field() # Militar expenditures: % of GDP (2019)

    # Imágenes de las banderas
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()