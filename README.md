# FinalProject
This project was designed to model a new, lower cost way to collect weather and atmospheric data from diverse locations. A drone equipped
with sensors and a camera can replace a team of scientists who would have to travel to these places with expensive equipment to collect 
this data. To portray the viability of this idea, we used a hobby drone equipped with sensors, a camera, an arduino, a raspberry pi, 
and a cell phone. We then took the data collected from the sensors in the drone, interpreted it using arduino libraries, turned the data
into database insert statements via a Python script on the Raspberry Pi, and used a heroku postgres cloud database with phone internet 
connection to store this data. 
This rather robust backend work culminates in a frontend site with live data updates from the drone. This includes atmospheric data, 
temperature, pressure, and altitude. 
