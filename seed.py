from app import app
from models import db, User, Representative, Bill, User_Rep, User_Bill

#Delete and create all tables
db.drop_all()
db.create_all()

#Empty the table
User.query.delete()
Representative.query.delete()
Bill.query.delete()
User_Bill.query.delete()
User_Rep.query.delete()

##sign up 10 people
##2 from senate
##2 from house
##8 bills 

# ADD to database 2 Senators and 2 House Representatives

cSchumer = Representative(
    id = "S000148",
    first_name = "Charles",
    last_name = "Schumer",
    chamber = "Senate",
    state = "NY",
    party = "D",
    twitter = "SenSchumer",
    facebook = "senschumer",
    next_election = "2022"
)

mRomney = Representative(
    id = "R000615",
    first_name = "Mitt",
    last_name = "Romney",
    chamber = "Senate",
    state = "UT",
    party = "R",
    twitter = "SenatorRomney",
    facebook = "null",
    next_election = "2024"
)

aOcasioCortez = Representative(
    id = "O000172",
    first_name = "Alexandria",
    last_name = "Ocasio-Cortez",
    chamber = "House",
    state = "NY",
    party = "D",
    twitter = "RepAOC",
    facebook = "null",
    next_election = "2020"
)

wHurd = Representative(
    id = "H001073",
    first_name = "Will",
    last_name = "Hurd",
    chamber = "House",
    state = "TX",
    party = "R",
    twitter = "hurdonthehill",
    facebook = "HurdOnTheHill",
    next_election = "2020"
)

db.session.add(cSchumer)
db.session.add(mRomney)
db.session.add(aOcasioCortez)
db.session.add(wHurd)
db.session.commit()

# ADD 8 bills added

cSchumer_Bill_1 = Bill(
    id = "s908-116",
    sponsor_id = "S000148",
    introduce_date = "2019-03-27",
    title =  "A bill to provide for an equitable management of summer flounder based on geographic, scientific, and economic data and for other purposes.",
    short_title = "Fluke Fairness Act of 2019",
    govtrack_url = "https://www.govtrack.us/congress/bills/116/s908",
    committees = "Senate Commerce, Science, and Transportation Committee",
    latest_major_action = "Placed on Senate Legislative Calendar under General Orders. Calendar No. 317.",
    primary_subject = "Public Lands and Natural Resources",
)

cSchumer_Bill_2 = Bill(
    id = "s1044-116",
    sponsor_id = "S000148",
    introduce_date = "2019-04-04",
    title = "A bill to impose sanctions with respect to foreign traffickers of illicit opioids, and for other purposes.",
    short_title = "Fentanyl Sanctions Act",
    govtrack_url = "https://www.govtrack.us/congress/bills/116/s1044",
    committees = "Senate Banking, Housing, and Urban Affairs Committee",
    latest_major_action = "Committee on Banking, Housing, and Urban Affairs. Hearings held.",
    primary_subject = "International Affairs",
)

mRomney_Bill_1 = Bill(
    id = "s3556-116",
    sponsor_id = "R000615",
    introduce_date = "2020-03-20",
    title = "A bill to amend the Higher Education Act of 1965 to provide for deferral of loan repayment for graduates during the period of the coronavirus.",
    short_title = "COVID-19 Graduate Relief Act",
    govtrack_url = "https://www.govtrack.us/congress/bills/116/s3556",
    committees = "Senate Health, Education, Labor, and Pensions Committee",
    latest_major_action = "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
    primary_subject = "Education",
)

mRomney_Bill_2 = Bill(
    id = "s3214-116",
    sponsor_id = "R000615",
    introduce_date = "2020-01-16",
    title = "A bill to amend the Agricultural Credit Act of 1978 with respect to preagreement costs of emergency watershed protection measures, and for other purpose.",
    short_title = "MATCH Act of 2020",
    govtrack_url = "https://www.govtrack.us/congress/bills/116/s3214",
    committees = "Senate Agriculture, Nutrition, and Forestry Committee",
    latest_major_action = "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
    primary_subject = "Agriculture and Food",
)

aOcasioCortez_Bill_1 = Bill(
    id = "hr6827-116",
    sponsor_id = "O000172",
    introduce_date = "2020-05-12",
    title = "To amend the Coronavirus Economic Stabilization Act of 2020 to place certain requirements on corporations receiving Federal aid related to COVID-19.",
    short_title = "Corporate Accountability Act",
    govtrack_url = "https://www.govtrack.us/congress/bills/116/hr6827",
    committees = "House Financial Services Committee",
    latest_major_action = "Referred to the House Committee on Financial Services.",
    primary_subject = "Commerce",
)

aOcasioCortez_Bill_2 = Bill(
    id = "hr5185-116",
    sponsor_id = "O000172",
    introduce_date = "2019-11-19",
    title = "To provide economic empowerment opportunities in the United States through the modernization of public housing, and for other purposes.",
    short_title = "Green New Deal for Public Housing Act",
    govtrack_url = "https://www.govtrack.us/congress/bills/116/hr5185",
    committees = "House Financial Services Committee",
    latest_major_action = "House Financial Services Committee",
    primary_subject = "Housing and Community Development",
)

wHurd_Bill_1 = Bill(
    id = "hr7101-116",
    sponsor_id = "H001073",
    introduce_date = "2020-06-04",
    title = "To provide for the continuation of paid parental leave for members of the Armed Services in the event of the death of the child.",
    short_title = "Elaine M. Checketts Military Families Act of 2020",
    govtrack_url = "https://www.govtrack.us/congress/bills/116/hr7101",
    committees = "House Armed Services Committee",
    latest_major_action = "Referred to the House Committee on Armed Services.",
    primary_subject = "Armed Forces and National Security",
)

wHurd_Bill_2 = Bill(
    id = "hr6901-115",
    sponsor_id = "H001073",
    introduce_date = "2018-09-26",
    title =  "To amend chapter 36 of title 44, United States Code, to make certain changes relating to electronic Government services, and for other purposes.",
    short_title ="Federal CIO Authorization Act of 2018",
    govtrack_url = "https://www.govtrack.us/congress/bills/115/hr6901",
    committees = "Senate Homeland Security and Governmental Affairs Committee",
    latest_major_action = "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
    primary_subject = "Government Operations and Politics",
) 

db.session.add(cSchumer_Bill_1)
db.session.add(cSchumer_Bill_2)
db.session.add(mRomney_Bill_1)
db.session.add(mRomney_Bill_2)
db.session.add(aOcasioCortez_Bill_1)
db.session.add(aOcasioCortez_Bill_2)
db.session.add(wHurd_Bill_1)
db.session.add(wHurd_Bill_2)
db.session.commit()

