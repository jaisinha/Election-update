import pandas #Ro read wikipedia
#pip install lxml(To handle XML and HTML files)
wiki=pandas.read_html('https://en.wikipedia.org/wiki/2019_Indian_general_election')

candidates_info=wiki[2] #saari candidates ki info mil gayi!!
candidate_info_first=candidates_info[1] #1st candidate info
candidate1_seats_won=candidate_info_first[7]
candidate_info_second=candidates_info[2]
candidate2_seats_won=candidate_info_second[7]


#print(candidate1_seats_won)
#print(candidate2_seats_won)

if(candidate1_seats_won>candidate2_seats_won):
    print("Modi ji winner")
else:
    print("Rahul ji winner")
