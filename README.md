# DSCI 532 - Group 22

The project housed in this repository has been created in partial fulfillment of the requirements of DSCI 532 of the University of British Columbia's Master of Data Science program (2020/2021).  The purpose of this project is to create an interactive dashboard that allows users to explore and interact with a data set.  The [proposal document](https://github.com/UBC-MDS/532_Group_22/proposal.md) provides information on the hypothetical scenario for which this dashboard is being created.

#### Project Details
The purpose of this project is to create an interactive dashboard for DSCI 532: Visualization II. Please click the following link to view our proposal for [*Criminality in Canada: Fighting Anecdotes with Data*](https://github.com/UBC-MDS/532_Group_22/blob/main/proposal.md). 

The data source is [Incident-based crime statistics, by detailed violations, Canada, provinces, territories and Census Metropolitan Areas](https://www150.statcan.gc.ca/t1/tbl1/en/cv.action?pid=3510017701) released by Statistics Canada. 

#### App Design
A pdf copy of the sketch of our proposed app can be found [here](https://github.com/sbabicki/532_Group_22/blob/main/design_mockup.pdf).  

The app contains two tabs which can be selected which have different customization options. Widgets with writing in <span style="color:red">red</span> are additional features that we would like to have, but we do not deem them essential to implement if we do not have the time or resources to complete them. 

The first tab, **Geographic Crime Comparisons**, explores differences in crime between different provinces and between different census metropolitan areas (CMA). 
![Tab 1](design_mockup_tab_1.png "Tab 1 - Geographic Crime Comparisons")

A choropleth map shows the colour coded difference in the crime rate metric for provinces and a bar chart shows the deference for CMAs for a given year. The user can select one of 5 violation types from a dropdown menu (e.g. Total drug violations). The user can also filter for results for a specific year using a slider. 

Additional Features (Optional): 
- Select Metric - the user can select a different metric to display instead of the default Rate per 100,000 (e.g. Actual incidents).
- Select Subcategory - the user can specify a violation subcategory rather than its parent category (e.g. Possession, Cocaine instead of Total drug violations)

The second tab, **Crime Time Trends**, explores trends in crime over time for selected areas.
![Tab 2](design_mockup_tab_2.png "Tab 2 - Crime Time Trends")


#### Members
- Cal Schafer
- Ifeanyi Anene
- Sasha Babicki
- Steffen Pentelow

#### Teamwork Contract
Our Teamwork Contract is available [here](https://docs.google.com/document/d/1f04WVT0w_p6jisDtVyJdbquXe1HNhaqbPbXEgrY51Ng/edit)

#### License
The *Incident-based crime statistics, by detailed violations, Canada, provinces, territories and Census Metropolitan Areas* data contains information licensed under the Open Government Licence – Canada (version 2.0).
