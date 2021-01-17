Dashboard Proposal <br> *Criminality in Canada: Fighting Anecdotes with
Data*
================

  - [1 Motivation and purpose](#motivation-and-purpose)
  - [2 Description of data](#description-of-data)
  - [3 Research questions and usage
    scenarios](#research-questions-and-usage-scenarios)

# 1 Motivation and purpose

**Our Role:** Data scientists at a consultancy firm.

**Target Audience:** General public.

The public’s understanding of the distribution and prevalence of crime
in Canada is often not based on the robust data collected by police
departments around the country. Instead, people’s knowledge of crime is
often derived from stories circulating through communities and stories
presented in the media. Both these sources of information have
significant limitations. For example, a given person will only hear
about a small percentage of total crimes committed across the nation
through the media or through community connections. Additionally, crimes
that are violent or otherwise sensational are often overrepresented.

In order to foster an understanding of crime that is more comprehensive
and less biased, our team will create a dashboard which allows the
public to easily view and explore Canadian crime data. These data will
be derived from Statistics Canada. The dashboard should be easy to
navigate for someone from the general population and provide summary
information in a way that is easy to interpret. The dashboard should be
interactive and allow users to explore types, locations, and frequency
of crimes committed as well as the time period in which they occurred.

# 2 Description of data


We will be visualizing a dataset which consists of approximately 49732 observations of reported occurrences of the rate of crime per 100,000 population in different provinces and CMAs in Canada. Each row describes the rate of crime per 100,000 population for a given province/CMA for a given year. There are some missing values in this dataset. The `GEO` column illustrates the province or CMA being observed, the `Violations` column describes the types of crime/violations that occurred in that province or CMA. The `Value` column represents the number of crime rate per 100,000 population. This dataset was created by the Canadian Centre for Justice and Community Safety Statistics (CCJCSS), in co-operation with the policing community, collects police-reported crime statistics through the Uniform Crime Reporting Survey (UCR), it was sourced from  Statistics Canada website (Statistics Canada) and it can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/cv.action?pid=3510017701).



# 3 Research questions and usage scenarios

**Sample usage scenario:** 
Sarah and her family, who currently live in the United States, have been considering moving to Canada on the premise of better job prospects. She is interested in purchasing a house that is in an area with a relatively low crime rate and she wants to understand how the crime rate has varied over time for different types of crime. Sarah has heard stories in the news about crime in various parts of Canada but wants to make sure she is making her decision based on reliable information. She wants to explore a dataset with the purpose of comparing the types, frequency, and the time period of crimes committed in various provinces and Census Metropolitan Areas (CMA), to be able to identify a relatively low crime environment for her move. When Sarah accesses the "Criminality in Canada: Fighting Anecdotes with Data" dashboard to \[learn\] more about violent crime rates in Canada. She will see an overview of the available variables in her dataset, which is based on the police-reported crime statistics collected through the Uniform Crime Reporting Survey. Sarah would like to live near the mountains so she \[limits\] the crime rate data she is viewing to areas in Alberta, British Columbia, Quebec, Northwest Territories, Yukon, and Nunavut. Sarah is primarily concerned with violent crimes so she \[excludes\] all other types of crime from her search. Sarah is now able to \[explore\] a map on the 'Geographic Crime Trends' tab of the dashboard which shows the relative violent crime rates in her areas of interest. Sarah chooses the 10 regions having the lowest violent crime rates and does some more research on these areas. Based on factors other than violent crime rates, she narrows her list down to 5. Sarah understands that crime rates are not static so she wants to understand whether violent crimes have been increasing or decreasing recently. Sarah opens the 'Crime Time Trends' tab of the dashboard and views a plot showing the violent crime rates over the past 5 years. Identifying the region in which the violent crime rate is decreasing the fastest, Sarah is able to decide where in Canada she and her family will settle.



# References 

Statistics Canada. Table 35-10-0177-01  Incident-based crime statistics, by detailed violations, Canada, provinces, territories and Census Metropolitan Areas