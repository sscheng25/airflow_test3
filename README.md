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

 -   **[Crime data one year prior to present](https://data.cityofchicago.org/api/views/dfnk-7re6/rows.json?accessType=DOWNLOAD)** -- Chicago data portal
       
       Size: 202882 rows, 30 columns
       
       Update regularly.

 - 	 **[Public transit stations](https://data.cityofchicago.org/Transportation/CTA-Bus-Stops/hvnx-qtky)** -- Chicago data portal
        
       Size: 10833 rows, 14 columns)

 - 	 **[Grocery data](https://data.cityofchicago.org/Community-Economic-Development/Grocery-Stores-2013/53t8-wyrc)** -- Chicago data portal

       Size: 265 rows, 6 columns.

 - 	**[Restaurants data](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections-Dashboard/2bnm-jnvb)** -- Chicago data portal
       
       Size: 228176 rows, 17 columns

 - 	**[Chicago neighborhood data](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Neighborhoods/bbvz-uum9)** -- Chicago data portal

       Size: 99 rows, 5 columns

## Metric in evaluating neighborhoods

 - **Normalization**

Normalization is process to convert values with different ranges to range (0, 1). Since our indicators have different units, we apply normalization to all of them, including crime cases, number of bus stops, number of groceries, and number of restaurants in each neighborhood.  

 - **Index Calculation**


