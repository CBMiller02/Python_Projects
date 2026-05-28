# This is a list of the 50 largest metro areas in the United States.
# The purpose of this project is to build a simple list where I can organize the data in multiple ways and utilize different Python functions to display or quantity the data.


# States in the Northeastern United States (per the U.S. Census Bureau)
NY = "New York: "
PA = "Pennsylvania: "
NJ = "New Jersey: "
CT = "Connecticut: "
ME = "Maine: "
MA = "Massachusetts: "
NH = "New Hampshire: "
RI = "Rhode Island: "
VT = "Vermont: "

# States in the Midwest United States (per the U.S. Census Bureau)
IL = "Illinois: "
IN = "Indiana: "
MI = "Michigan: "
IND = "Indiana: "
OH = "Ohio: "
WI = "Wisconsin: "
IA = "Iowa: "
KS = "Kansas: "
MN = "Minnesota: "
MO = "Missouri: "
NE = "Nebraska: "
ND = "North Dakota: "
SD = "South Dakota: "

# States in the Southern United States (per the U.S. Census Bureau)
DE = "Delaware: "
DC = "District of Columbia (DC): "
FL = "Florida: "
GA = "Georgia: "
MD = "Maryland: "
NC = "North Carolina: "
SC = "South Carolina: "
VA = "Virginia: "
WV = "West Virginia: "
AL = "Alabama: "
KY = "Kentucky: "
MS = "Mississippi: "
TN = "Tennessee: "
AR = "Arkansas: "
LA = "Louisiana: "
OK = "Oklahoma: "
TX = "Texas: "

# States in the Western United States (per the U.S. Census Bureau)
AZ = "Arizona: "
CO = "Colorado: "
ID = "Idaho: "
MT = "Montana: "
NV = "Nevada: "
NM = "New Mexico: "
UT = "Utah: "
WY = "Wyoming: "
AK = "Alaska: "
CA = "California: "
HI = "Hawaii: "
OR = "Oregon: "
WA = "Washington: "



# The following metro area population statistics are supported by information from Statista.  We are using total metro area population for the cities listed.
#Source: https://www.statista.com/statistics/183600/population-of-metropolitan-areas-in-the-us/?srsltid=AfmBOoqEvzIJNh8psrJQOl7nHUEVtFlLDIkB0ypRvdqGV6On2B4bvuo-
from idlelib.config_key import ALPHANUM_KEYS

nyc_pop = 19498249
la_pop = 12799100
chicago_pop = 9262825
dfw_pop = 8100037
houston_pop = 7510253
atl_pop = 6307261
dc_pop = 6304975
philly_pop = 6246160
miami_pop = 6183199
phx_pop = 5070110
boston_pop = 4919179
riverside_pop = 4688053
sfo_pop = 4566961
detroit_pop = 4342304
seattle_pop = 4044837
msp_pop = 3712020
tampa_pop = 3342963
sdo_pop = 3269973
denver_pop = 3005131
baltimore_pop = 2834316
orlando_pop = 2817933
charlotte_pop = 2805115
stl_pop = 2796999
stx_pop = 2703999
pdx_pop = 2508050
atx_pop = 2473275
pittsburgh_pop = 2422725
sac_pop = 2420608
lasvegas_pop = 2336573
cincy_pop = 2271479
kansas_city_pop = 2221343
columbus_pop = 2180271
indy_pop = 2138468
nashville_pop = 2102573
cleveland_pop = 2063132
sjo_pop = 1945767
vbeach_pop = 1787169
jacksonville_pop = 1713240
providence_pop = 1677803
milwaukee_pop = 1560424
raleigh_pop = 1509231
okc_pop = 1477926
louisville_pop = 1365557
richmond_pop = 1349732
memphis_pop = 1335674
saltlake_pop = 1267864
birmingham_pop = 1184290
fresno_pop = 1180020
grandrapids_pop = 1162950
buffalo_pop = 1155604

usa_pop = 348943759


# Here is the introductory line for our project. Notice I use \n\n.
# This is to push the second sentence two lines below the first, basically just making the output more easily readable.

print("The following is a list of the 50 largest metro areas in the United States.\n\nListed are Ranking, City, State, and population in millions.")
print("_______________________________________________")
print("1. New York City,", NY, nyc_pop)
print("2. Los Angeles,", CA, la_pop)
print("3. Chicago,", IL, chicago_pop)
print("4. Dallas-Fort Worth,", TX, dfw_pop)
print("5. Houston,", TX, houston_pop)
print(" 6. Atlanta,", GA, atl_pop)
print(" 7. Washington,", DC, dc_pop)
print(" 8. Philadelphia,", PA, philly_pop)
print(" 9. Miami,", FL, miami_pop)
print("10. Phoenix,", AZ, phx_pop)
print("11.", "Boston,", MA, boston_pop)
print("12. Riverside-San Bernardino", CA, riverside_pop)
print("13. San Francisco,", CA, sfo_pop)
print("14. Detroit,", MI, detroit_pop)
print("15. Seattle,", WA, seattle_pop)
print("16. Minneapolis-St Paul", MN, msp_pop)
print("17. Tampa,", FL, tampa_pop)
print("18. San Diego,", CA, sdo_pop)
print("19. Denver,", CO, denver_pop)
print("20. Baltimore,", MD, baltimore_pop)
print("21. Orlando,", FL, orlando_pop)
print("22. Charlotte,", NC, charlotte_pop)
print("23. St. Louis,", MO, stl_pop)
print("24. Portland,", OR, pdx_pop)
print("25. Austin,", TX, atx_pop)
print("26. Pittsburgh,", PA, pittsburgh_pop)
print("27. Sacramento,", CA, sac_pop)
print("28. Las Vegas,", NV, lasvegas_pop)
print("29. Cincinnati,", OH, cincy_pop)
print("31. Kansas City,", MO, kansas_city_pop)
print("32. Columbus,", OH, columbus_pop)
print("33. Indianapolis,", IN, indy_pop)
print("34. Nashville,", TN, nashville_pop)
print("35. Cleveland,", OH, cleveland_pop)
print("36. San Jose,", CA, sjo_pop)
print("37. Virginia Beach,", CA, vbeach_pop)
print("38. Jacksonville,", FL, jacksonville_pop)
print("39. Providence,", RI, providence_pop)
print("40. Milwaukee,", WI, milwaukee_pop)
print("41. Raleigh,", NC, raleigh_pop)
print("42. Oklahoma City", OK, okc_pop)
print("43. Louisville,", KY, louisville_pop)
print("44. Richmond,", VA, richmond_pop)
print("45. Memphis,", TN, memphis_pop)
print("46. Salt Lake City,", UT, saltlake_pop)
print("47. Birmingham,", AL, birmingham_pop)
print("48. Fresno,", CA, fresno_pop)
print("49. Grand Rapids,", MI, grandrapids_pop)
print("50. Buffalo,", NY, buffalo_pop)
print("_______________________________________________")
print("US total population: ", usa_pop)

#The combined populations of the top five, top ten, top twenty, top thirty, top forty and top fifty metro areas in the United States

top_five = nyc_pop + la_pop + chicago_pop + dfw_pop + houston_pop
top_ten = nyc_pop + la_pop + chicago_pop + dfw_pop + houston_pop + atl_pop + dc_pop + philly_pop + miami_pop + phx_pop
top_twenty = nyc_pop + la_pop + chicago_pop + dfw_pop + houston_pop + atl_pop + dc_pop + philly_pop + miami_pop + phx_pop + boston_pop + riverside_pop + sfo_pop + detroit_pop + seattle_pop + msp_pop + tampa_pop + sdo_pop + denver_pop + baltimore_pop
top_thirty = nyc_pop + la_pop + chicago_pop + dfw_pop + houston_pop + atl_pop + dc_pop + philly_pop + miami_pop + phx_pop + boston_pop + riverside_pop + sfo_pop + detroit_pop + seattle_pop + msp_pop + tampa_pop + sdo_pop + denver_pop + baltimore_pop + orlando_pop + charlotte_pop + stl_pop + stx_pop + pdx_pop + atx_pop + pittsburgh_pop + sac_pop + lasvegas_pop + cincy_pop
top_forty = nyc_pop + la_pop + chicago_pop + dfw_pop + houston_pop + atl_pop + dc_pop + philly_pop + miami_pop + phx_pop + boston_pop + riverside_pop + sfo_pop + detroit_pop + seattle_pop + msp_pop + tampa_pop + sdo_pop + denver_pop + baltimore_pop + orlando_pop + charlotte_pop + stl_pop + stx_pop + pdx_pop + atx_pop + pittsburgh_pop + sac_pop + lasvegas_pop + cincy_pop + kansas_city_pop + columbus_pop + indy_pop + nashville_pop + cleveland_pop + sjo_pop + vbeach_pop + jacksonville_pop + providence_pop + milwaukee_pop
top_fifty = nyc_pop + la_pop + chicago_pop + dfw_pop + houston_pop + atl_pop + dc_pop + philly_pop + miami_pop + phx_pop + boston_pop + riverside_pop + sfo_pop + detroit_pop + seattle_pop + msp_pop + tampa_pop + sdo_pop + denver_pop + baltimore_pop + orlando_pop + charlotte_pop + stl_pop + stx_pop + pdx_pop + atx_pop + pittsburgh_pop + sac_pop + lasvegas_pop + cincy_pop + kansas_city_pop + columbus_pop + indy_pop + nashville_pop + cleveland_pop + sjo_pop + vbeach_pop + jacksonville_pop + providence_pop + milwaukee_pop + raleigh_pop + okc_pop + louisville_pop + richmond_pop + memphis_pop + saltlake_pop + birmingham_pop + fresno_pop + grandrapids_pop + buffalo_pop

print("The combined population of the top fifty metro areas in the United States is:", top_fifty, "\n")


# The output percentages of the top five, top ten, top twenty, top thirty, top forty, and top fifty metro areas in the United States

top_five_percentage = (top_five / usa_pop) * 100
print("The top five metro areas contain", f"{top_five_percentage:.2f}%", "of the total United States population.\n")

top_ten_percentage = (top_ten / usa_pop) * 100
print("The top ten metro areas contain", f"{top_ten_percentage:.2f}%", "of the total United States population.\n")

top_twenty_percentage = (top_twenty / usa_pop) * 100
print("The top twenty metro areas contain", f"{top_twenty_percentage:.2f}%", "of the total United States population.\n")

top_thirty_percentage = (top_thirty / usa_pop) * 100
print("The top thirty metro areas contain", f"{top_thirty_percentage:.2f}%", "of the total United States population.\n")

top_forty_percentage = (top_forty / usa_pop) * 100
print("The top forty metro areas contain", f"{top_forty_percentage:.2f}%", "of the total United States population.\n")

top_fifty_percentage = (top_fifty / usa_pop) * 100
print("The top fifty metro areas contain", f"{top_fifty_percentage:.2f}%", "of the total United States population.\n")

# US regions from the US census bureau.
# https://www.census.gov/programs-surveys/economic-census/guidance-geographies/levels.html