# -*- coding: utf-8 -*-

import scrapy
from countries.items import CountriesItem


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    item_count = 0
    allowed_domain = ['www.cia.gov']

    start_urls = ["https://www.cia.gov/the-world-factbook/"]

    def parse(self, response):
        for region in response.xpath('//*[@id="main-content"]/div[4]/section/section//a[not(text()="World")]/@href'):
            yield response.follow(region.get(), callback=self.parse_regions)

    def parse_regions(self, response):
        for country in response.xpath('//*[@id="main-content"]/section/div/div//a/@href'):
            #print(self.allowed_domain[0] + country.get())
            yield response.follow(country.get(), callback = self.parse_country)
    
    def parse_country(self, response):
        country_item = CountriesItem()

        country_item['nombre'] = response.xpath('//h1/text()').get()
        country_item['continente'] = response.xpath('//h1/../following-sibling::div/a/text()').get()
        country_item['area'] = response.xpath('//*[@id="geography"]//h3/a[text()="Area"]/ancestor::h3/following-sibling::p/text()[1]').get()
        country_item['poblacion'] = response.xpath('//*[@id="people-and-society"]//h3/a[text()="Population"]/ancestor::h3/following-sibling::p/text()[1]').get()
        country_item['gdp'] = response.xpath('//*[@id="economy"]//h3/a[text()="Real GDP per capita"]/ancestor::h3/following-sibling::p/text()[1]').get()
        country_item['desempleo'] = response.xpath('//*[@id="economy"]//h3/a[text()="Unemployment rate"]/ancestor::h3/following-sibling::p/text()[1]').get()
        country_item['impuestos'] = response.xpath('//*[@id="economy"]//h3/a[text()="Taxes and other revenues"]/ancestor::h3/following-sibling::p/text()[1]').get()
        country_item['deuda'] = response.xpath('//*[@id="economy"]//h3/a[text()="Debt - external"]/ancestor::h3/following-sibling::p/text()[1]').get()
        
        #En la tasa de cambio, casi todos los datos de tasa de cambio se encuentran en el segundo párrafo
        #de la sección 'Exhange rates'
        #Pero hay casos raros, hay un solo párrafo en esta sección que dice solamente 'the US dollar is used'
        #Entonces, vamos a asumir todas las tasas de cambio que tengan este enunciado como 1, el resto lo dejaremos
        #con lo que dice el segundo párrafo del exchange rate
        country_item['tasa_de_cambio'] = response.xpath('//*[@id="economy"]//h3/a[text()="Exchange rates"]/ancestor::h3/following-sibling::p/text()').getall()

        if(country_item['tasa_de_cambio'] == []):
            country_item['tasa_de_cambio'] == None
        else:
            if(country_item['tasa_de_cambio'][0] == 'the US dollar is used'):
                country_item['tasa_de_cambio'] = '1'
            
            elif len(country_item['tasa_de_cambio']) > 1:
                country_item['tasa_de_cambio'] = country_item['tasa_de_cambio'][1]
            else:
                country_item['tasa_de_cambio'] = None


        country_item['usuarios_internet'] = response.xpath('//*[@id="communications"]//h3/a[text()="Internet users"]/ancestor::h3/following-sibling::p/text()[1]').get()
        country_item['porcentaje_internet'] = response.xpath('//*[@id="communications"]//h3/a[text()="Internet users"]/ancestor::h3/following-sibling::p/text()[2]').get()
        country_item['aeropuertos'] = response.xpath('//*[@id="transportation"]//h3/a[text()="Airports"]/ancestor::h3/following-sibling::p/text()[1]').get()
        country_item['carreteras_km'] = response.xpath('//*[@id="transportation"]//h3/a[text()="Roadways"]/ancestor::h3/following-sibling::p/text()[1]').get()
        country_item['inversion_militar'] = response.xpath('//*[@id="military-and-security"]//h3/a[text()="Military expenditures"]/ancestor::h3/following-sibling::p/text()[1]').get()

        country_item['image_urls'] = [response.urljoin(response.xpath('//h5[text() = "Country Flag"]/../../..//picture/img/@src').get())]
        #print("IMAGE URLS:")
        #print(country_item['image_urls'])
        country_item['image_name'] = country_item['image_urls'][0].split('/')[-1] #La bandera, al menos en la página principal, no tiene valor alt con su nombre
                                                                                #Mejor vamos a sacar de su URL el nombre de la imagen

        self.item_count += 1
        print(f"Count: {self.item_count}")
        if self.item_count > 300:
            raise scrapy.exceptions.CloseSpider('item_exceeded')

        yield country_item