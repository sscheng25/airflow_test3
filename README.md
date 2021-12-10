# Seek Your Home in Chicago

Final Project for MUSA 509, fall 2021.

## People
**Authors**:
* Sisun Cheng, sisunc@upenn.edu
* Shimin Tu, tushimin@upenn.edu

**Instructor**:
* Mjumbe Poe

## Introduction

A Chinese student Dennis who just graduated from University of Chicago, was shot dead near the campus On Nov 9th.  Chicago has appealed a large amount of people from all over the world because of its outstanding education resources and prosperity, but it is also recognized as one of the most dangerous cities in the United States. Shocked by Dennis’s misfortune, we wonder how people can find a suitable place in Chicago to live. Thus, we’d like to design an application which aims to provide recommendations for people who plan to buy or rent houses in Chicago. 

We choose indicators from three dimensions, respectively safety, transportation, and commercial places. Users can enter an address in the search bar, or click the neighborhood they are interested in on the list or on the map. After that, users will come to a webpage which contains the neighborhood’s information in the format of charts and maps. Maps are mainly used to show the spatial distribution of public transit stations, crimes, restaurants, and groceries.  And Charts are used to convey quantitative information such as the frequency of crimes. Our application will also highlight the safest and the most convenient community targeted for different people. 

## Data sources

 -   **[Crime data 30 days prior to present](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)** 
       
       Crime data is of an important part in evaluating the neighborhoods in Chicago. As a city of high crime rate, residents and visitors never spare efforts in seeking a safer place to live. In this project, we fetch crime data 30 days prior to present to make our analysis. We dive into crime spatial distribution and crime type composition. On average, there are about 36,000 crime cases of all types every month in Chicago. 
      
      We get the crime data via **Socrata Open Data API** frome **[Chicago Data Portal](https://data.cityofchicago.org/)**, and the crime data is updated regularly, approximately every one or two days. So we can easily catch the latest crime trend in Chicago.

 - 	 **[Public transit stations](https://data.cityofchicago.org/Transportation/CTA-Bus-Stops/hvnx-qtky)**
        
       Size: 10833 rows, 14 columns

 - 	 **[Grocery data](https://data.cityofchicago.org/Community-Economic-Development/Grocery-Stores-2013/53t8-wyrc)**

       Size: 265 rows, 6 columns

 - 	**[Restaurants data](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections-Dashboard/2bnm-jnvb)**
       
       Size: 228176 rows, 17 columns

 - 	**[Chicago neighborhood data](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Neighborhoods/bbvz-uum9)**

       Size: 99 rows, 5 columns

## Metric in evaluating neighborhoods

 - **Normalization**

Normalization is process to convert values with different ranges to range (0, 1). Since our indicators have different units, we apply normalization to all of them, including crime cases, number of bus stops, number of groceries, and number of restaurants in each neighborhood.  

 - **Index Calculation**
We calculate the index for evaluation neighborhoods with the following formula,

** index = 0.5*(1-crime_norm) + 0.3*bus_stop_norm + 0.1*restaurant_norm + 0.1*grocery_norm**

We give the coefficient according to our own experiences and users may define their weights. In our formula, the higher the index is, the more livable the neighborhood is.

## Data Pipeline

