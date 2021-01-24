# Canadian Crime Dashboard Reflection

There are two tabs in our dashboard, so we have decided to reflect on them individually. 

## Tab 1

### Widgets

We have four widgets that are in a partial state of completion.

- The first widget (Select Metric) is fully implemented.

- For the second widget (Select Violation), a user can select from a complete list of violation types. This is not our final implementation, as we actually want this widget to only display high-level crime types (e.g., all property crimes, all violent crimes). We intend that by selecting a value, a user would then have the option in the 3rd widget to select from lower-level crime types (e.g., homicides, assaults) that belong to the higher-level crime category picked in the 2nd widget.

- As explained above, our 3rd widget has not been implemented yet.

- The fourth widget - not implemented yet - will have a user select year of interest (~1990 to 2019).

- One other comment is that for our first three dropdown widgets, the values inside are in a random order. We should order them alphabetically.

### Visualizations

We have two visualizations to display in this tab.

- First is a Choropleth map - not implemented. Our challenge is finding an appropriate Canadian province shape file. We don't require a shape file with granular precision; we only need a Canadian map that has provincial boundaries that would be recognizable to a user (i.e., mostly straight lines).

- The second visualization is a bar chart that displays what the widgets have selected, broken down by Census Metropolitan Area (CMA). We need to have the graph sort the values from top to bottom.

There are some visual layout improvements to make for future milestones. Our 2nd graph has white dead space to the right that could be removed. Our widgets are quite long and take up valuable dashboard real-estate. Additional dashboard narrative text, and formatting, would be helpful.


## Tab 2

### Widgets 

- The radio button, that is used to select either a Census Metropolitian Area or a province has been fully implemented.

- The second widget (dropdown component) that lets a user select one or multiple CMAs or provinces has been fully implemented.  

- The last widget that lets a user select a crime metric (e.g., incidents per 100k, % of incidents unfounded) has not been implemented yet. 


### Visualizations 

There are four plots on display in this tab. Each plot displays a metric (currently Criminal Incidents per 100,000 population) for different types of crimes in different geographical locations. 

Improvements here can include improving the asthetic layout of the page; allowing tooltips on the graphs. 


## Other Components

Our dataset is composed of text descriptions that are either excessively wordy, or have a mix of text and associated codes (e.g., "Winnipeg, Manitoba [466062]", "Total other Controlled Drugs and Substances Act drugs, trafficking, or production or distribution [440]"). This distracts from the user experience. We would look to the TA whether cleaning up these strings with hard-coding is necessary (e.g., "Winnipeg, MB").

