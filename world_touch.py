import streamlit as st
import webbrowser
import smtplib



st.title("...................✈Welcome To World Touch✈.................")
st.write("### 😉😉😉😉😉😉------*Know about the best tourist places in any country with us!*------😉😉😉😉😉😉")


home = st.sidebar.radio("" , ("Home" , "About us","Get info"))

if home=='Get info':

    countryselect=st.sidebar.selectbox("Country",("Select country","Malaysia", "India","Switzerland","Spain","France","Norway"))

    if countryselect=='India':

        emailr = st.text_input("Enter email address")

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("traveld496@gmail.com", "travel@18")

        # message to be sent
        message = """
                           India takes pride in flaunting its unsurpassed heritage; eras over eras have influenced, moulded and face 
                           lifted the rich heritage of which we all are part of. Distinctive edifices, perennial culture and the determination
                           to keep this incredibility have preserved for us an era no short of marvels. With a startling number of 
                           places and monuments enlisted in the list of UNESCO World Heritage Sites, India has made an indelible mark in world histor
                           # Beaches:-\n
                           1. Radhanagar Beach, Havelock Island\n
                           2. Tarkarli beach, Maharashtra\n
                           3. Gokarna, Karnataka\n
                           4. Mandrem, North Goa
                           5. Yarada Beach, Andhra Pradesh\n
                           6. Light House Beach, Kovalam\n
                           7. Puri Beach, Orissa\n
                           
                           ## Cities :-\n
                           1. Varanasi
                           2. Kolkata
                           3. Banglore
                           4. Agra
                           5. Mumbai
                           6. Jaipur
                           7. Delhi
                           
                           ## Hill station\n
                           1. Manali
                           2. Gulmarg
                           3. Shimla
                           4. Nainita
                           5. Munnar

                           ##National Park:
                           1. Corbett National Park, Uttarakhand
                           2. Ranthambore National Park, Rajasthan
                           3. Kanha National Park, Madhya Pradesh
                           4. Kaziranga National Park, Assam
                           5. Sundarbans National Park, West Bengal
                           
                           ## Resorts
                           1.Radisson Blu Udaipur Palace Resort & Spa
                           2. The Ananta Udaipur
                           3. Taj Lake Palace
                           4. Club Mahindra Assonora
                           5. Anantya Resorts
                           
                           ##For Booking:
                           Link="https://www.yatra.com/india-tour-packages"       

                """

        # sending the mail
        if st.button("Send info"):
            s.sendmail("traveld496@gmail.com", emailr, message)

        # terminating the session
        s.quit()


    if countryselect=='Malaysia':

        emailr = st.text_input("Enter email address")

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("traveld496@gmail.com", "travel@18")

        # message to be sent
        message = """
            Welcome To World Touch
            

             Cities in malaysia:

             1. Kuala Lumpur
             2. George Town
             3. Malacca
             4. Ipoh
             5. Kota Kinabalu

             Beaches in Malaysia:

             1. Pasir Panjang, Redang
             2. Pantai Cenang, Langkawi
             3. Rawa Island, Mersing
             4. Kapas Island, Terengganu
             5. Manukan Island, Sabah

             National Parks in Malaysia:

             1. Gunung Mulu National Park
             2. Taman Negara National Park
             3. Kinabalu National Park
             4. Bako National Park
             5. Gunung Gading National Park

             Malaysia Beach Resorts:

             1. Casa del Mar Langkawi
             2. The Danna Langkawi Malaysia
             3. The Datai Langkawi
             4. Four Seasons Resort Langkawi Malaysia
             5. Pangkor Laut Resort

             Malaysia tour packages:

             https://www.makemytrip.com/holidays-international/malaysia-vacation-tour-packages.html 



              """

        # sending the mail
        if st.button("Send info"):
            s.sendmail("traveld496@gmail.com", emailr, message)

        # terminating the session
        s.quit()

    if countryselect=='Switzerland':

        emailr = st.text_input("Enter email address")

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("traveld496@gmail.com", "travel@18")

        # message to be sent
        message = """
                        ****About us:

1.List of Most Beautiful Lakes in Switzerland:
1.Lake Lucerne
2.Lake Geneva
3.Lake Thun
4. Lake Lugano
5. Lake Brienz

2.List of Cities in Switzerland:

1. Zurich
2. Lucerne
3. Bern
4. Basel
5. Geneva

3.List of Best Switzerland Resorts:

1. Hotel Villa Honegg
2. The Omnia, Zermatt
3.Grand Hotel Kronenhof, Pontresina
4. Ascher Guesthouse
5.Hotel The Cambrian, Adelboden


4.List for Scenic Small Towns:

1. Zermatt
2. Lauterbrunnen
3. Guarda
4.Grindelwald
5. Murren


5.Links of website for booking:

1.Tripadvisor:
https://www.tripadvisor.in/Search?q=Switerland&searchSessionId=F9349ACB65E16CA15E54A885761B3D251626153506586ssid&searchNearby=false&sid=61E7AE3C141949F2BFE8AA81325C3B451626153527039&blockRedirect=true

2.Trivago:
https://www.trivago.in/?aDateRange%5Barr%5D=2021-07-23&aDateRange%5Bdep%5D=2021-07-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=174%2F200&hasList=1&hasMap=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode=

Location for Switzerland:
https://www.google.com/maps/place/Switzerland/@46.7912769,5.9814056,7z/data=!3m1!4b1!4m5!3m4!1s0x478c64ef6f596d61:0x5c56b5110fcb7b15!8m2!3d46.818188!4d8.227512



                """

        # sending the mail
        if st.button("Send info"):
            s.sendmail("traveld496@gmail.com", emailr, message)

        # terminating the session
        s.quit()


    if countryselect=='Spain':

        emailr = st.text_input("Enter email address")

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("traveld496@gmail.com", "travel@18")

        # message to be sent
        message =               """
                           ****About us:

                              1.List of Most Beautiful beaches in spain:
                                        1. Burriana Beach, Nerja
                                        2.Tossa De Mar
                                        3.Cala D’en Serra, Ibiza
                                        4. Playa de Bolonia, Tarifa
                                        5. Platja de Ses Illetes, Formentera


                              2.List of Best spanish Resorts:

                                        1. Praia da Rodas, Galici
                                        2. W Barcelona
                                        3.Maspalomas, Gran Canaria
                                        4.Parador de Cuenca
                                        5.Hotel Hacienda Na Xamena, Ibiza

                                          """

        # sending the mail
        if st.button("Send info"):
            s.sendmail("traveld496@gmail.com", emailr, message)

        # terminating the session
        s.quit()


    if countryselect=='France':

        emailr = st.text_input("Enter email address")

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("traveld496@gmail.com", "travel@18")

        # message to be sent
        message = """
                        About us:
I.	List of Beautiful Lakes
1.	Lake Annecy
2.	Lac de Serre-Poncon
3.	Lake Geneva
4.	Lac de Sainte Croix
5.	Lac du Bourget

II.	List of Best Cities
1.	Paris
2.	Avignon
3.	Nice
4.	Annecy
5.	Bordeaux

III.	List of Beautiful Churches
1.	Chartres Cathedral
2.	Notre Dame de la Garde
3.	Notre Dame de Paris
4.	Saint Michel d'Aiguilhe
5.	Amiens Cathedral

IV.	List of Best National Parks
1.	Reunion National Park
2.	Vanoise National Park
3.	Guadeloupe National Park
4.	Guiana Amazonian National Park
5.	Mercantour National Park

V.	List of Best Resorts
1.	Terre Blanche Hotel Spa Golf Resort
2.	Le Cristal de Jade
3.	Mineral Lodge & Spa
4.	Chalets de la Colagne
5.	Maranatha Porto Vecchio

VI.	Links of Website for booking:
1.Trivago:
https://www.trivago.in/?aDateRange%5Barr%5D=2021-07-25&aDateRange%5Bdep%5D=2021-07-26&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=56%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode=
2.Tripadvisor:
https://www.tripadvisor.in/Search?q=France&searchSessionId=99C35B0757C07F9D954E6847EDC76AA71626155311978ssid&searchNearby=false&sid=43DFBF75D2514B63A8FDA6483633A22E1626155327919&blockRedirect=true
VII.	Location for France:
https://www.google.com/maps/place/%E0%A4%AB%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A8%E0%A5%8D%E0%A4%B8/@46.1313542,-2.4365078,6z/data=!3m1!4b1!4m5!3m4!1s0xd54a02933785731:0x6bfd3f96c747d9f7!8m2!3d46.227638!4d2.213749


                """

        # sending the mail
        if st.button("Send info"):
            s.sendmail("traveld496@gmail.com", emailr, message)

        # terminating the session
        s.quit()


    if countryselect=='Norway':

        emailr = st.text_input("Enter email address")

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("traveld496@gmail.com", "travel@18")

        # message to be sent
        message = """
                        
•	Best Beaches:
1.	Paradisbukta, Oslo
2.	Huk Beach, Oslo
3.	Godalen Beach, Stavanger
4.	Mjelle Beach, Bodo
5.	Seljesanden, Nordfjord



•	Resorts:
1.	Gudvangen Fjordtell
2.	Snowhotel Kirkenes
3.	The Arctic Hideaway
4.	Hotel Brosundet
5.	Det Hanseatiske Hotel

Booking Options:
•	Trivago:
https://www.trivago.in/?aDateRange%5Barr%5D=2021-07-20&aDateRange%5Bdep%5D=2021-07-21&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=145%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode=
                """

        # sending the mail
        if st.button("Send info"):
            s.sendmail("traveld496@gmail.com", emailr, message)

        # terminating the session
        s.quit()



# ----------------------------------------------------------------------------------------------------------------------


if home=='About us':
    st.write("""We intend to provide our travelers with the most genuine and authenticate information. Numerous and 
    soothing destinations, with scenic views have been listed.""")
    st.write("""Different adventure activities, resorts, national parks, beaches and cities available in a country have 
    been complied for all our adventure seekers on this platform.   """)
    st.write("""Feel free to contact us at : \n
    Email - traveld496@gmail.com \n
    Call @ - 9975940901""")

if home == 'Home':

    countryselect = st.sidebar.selectbox("Country", ("Select country","Malaysia", "India","Switzerland","Spain","France","Norway"))

    if countryselect == 'Select country':
        st.title("")
        st.warning("Please select country")

    if countryselect == 'Malaysia':

        st.sidebar.title("...Malaysia...")
        st.sidebar.image("images/pr/flag.jfif", width=150)
        sidbar = st.sidebar.radio("", ("About", "Best beaches", "Best cities", "Best resorts",
                                       "Best national Parks"))

        if sidbar == 'About':
            st.title("Welcome to Malaysia")

            col11, col22 = st.beta_columns(2)

            with col11:
                st.balloons()
                st.image("images/pr/about.jpg", width=500)
                st.write(
                    "If countries were awarded for diversity, Malaysia would top first place. Not only is Malaysia a "
                    "melting pot of ethnic cultures, but it is also a blend of many different customs, cuisines and "
                    "religions all coexisting peacefully together. From large island groups to mountains, fertile "
                    "highlands, tropical rainforest and mangrove estuaries, the country’s geography is every bit as "
                    "diverse. What’s more, Malaysia is a unique country in that is divided into two main landmasses. "
                    "West Malaysia occupies the southern half of a peninsula shared with Thailand, while across the "
                    "South China Sea is East Malaysia, situated on the Borneo island.")
                st.write(
                    "West Malaysia is home to the capital city, Kuala Lumpur, a large metropolis of impressive "
                    "skyscrapers, fabulous shopping districts, museums, theaters, hotels, international restaurants "
                    "and buzzing nightlife. Melaka is a city rich in history, architecture and traditions. Penang "
                    "Island is famous for its exquisite cuisine and beautiful colonial George Town. A visit to the "
                    "Cameron Highlands offers cool weather and spectacular scenery of flower farms and tea plantations."
                    " Tioman, Langkawi and the Perhentian Islands are some of the world’s most breathtaking islands,"
                    "and Redang is a scuba diving paradise.")
                st.write(
                    "On the Borneo side, East Malaysia is known for its wild jungle, rainforests, extraordinary cave"
                    " systems, orangutans, granite peaks and remote tribes. Major cities like Kuching and Kota Kinabalu"
                    " serve as gateways to exploring these natural attractions.")

            with col22:
                st.image("images/pr/about2.jfif", width=500)
                st.title("")
                st.image("images/pr/flag.jfif")
                st.write("")
                st.image("images/pr/map.jpg")

                if st.button("View location"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Malaysia/@4.1279224,105.1196274,1837433m/'
                            'data=!3m2!1e3!4b1!4m5!3m4!1s0x3034d3975f6730af:0x745969328211cd8!8m2!3d4.21'
                            '0484!4d101.975766!5m1!1e2')

            st.video("https://www.youtube.com/watch?v=mtIeLsMbfzg")
            st.video("https://www.youtube.com/watch?v=sKDQFvw-wrM")



        if sidbar == 'Best beaches':

            st.title("Best Beaches in Malaysia......")
            st.write("Malaysia isn’t necessarily known for its beaches, often falling by the wayside due to the "
                     "beautiful beaches of nearby Thailand and Indonesia, so it’s not a traditional go-to beach "
                     "destination. But since it boasts the same beautiful seas as Thailand on both its east and west "
                     "coasts, Malaysia definitely has a number of star coastlines that are easily on-par with "
                     "neighboring countries.")
            st.write("From stunning tropical islands complete with coral and white sands, to the long, languorous "
                     "beaches of the mainland – as well as incredible locations in far-flung Malaysian Borneo, this "
                     "Southeast Asian country sure packs a punch when it comes to the confluence of sand and sea. So "
                     "let’s take a look at some of the best beaches in Malaysia, shall we?")

            col1, col2 = st.beta_columns(2)

            with col1:

                # Beach1
                st.write("## 1. Pasir Panjang, Redang")
                st.image("images/beaches/1.jpg", width=500, caption="Pasir Panjang, Redang")
                st.write(
                    "One of the largest islands off mainland Malaysia, Redang Island is located in the seas off the "
                    "northeastern state of Terrenganu, and is famous for its incredibly white sand and shimmering, "
                    "crystal-clear water.")
                st.write(
                    "It is well known as a tropical island getaway thanks to this reputation for coastal beauty, which"
                    " of course includes a fair few beaches – but none of these are quite as beautiful as Pasir Panjang.")
                st.write(
                    "This sloping stretch of soft sand that sweeps around a circular bay in a sharp curve is a popular "
                    "place that sees many local and international tourists – on day trips or staying at one of the now "
                    "numerous beachside hotels. There is a bonus here; part of the sand spills over a spit to form a "
                    "smaller section of beach away from the main bay area.")

                if st.button("Location","id(1)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Pasir+Panjang,+Redang/@5.7'
                                                '750622,103.0340365,2989m/data=!3m1!1e3')



                # Beach3
                st.write("## 3. Rawa Island, Mersing")
                st.image("images/beaches/3.jpg", width=500, caption="Rawa Island, Mersing")
                st.write(
                    "Set off the northeast coast of mainland Malaysia’s most southerly state of Johor, and easily reached"
                    " from the coastal town of Mersing, the island of Rawa is truly a gem of a beach destination. Named "
                    "for the white doves (known locally as rawa) that populate the island in great numbers, this tiny "
                    "little island is a haven for wildlife – both marine and land dwelling.")
                st.write(
                    "Since there are no proper roads on the island, only footpaths can take you from one destination to "
                    "the other. With tall, craggy cliffs on one side of the island, the other side is almost entirely"
                    " comprised of white-sand beaches that meet the beautiful azure sea in a perfect harmony of what "
                    "paradise ought to look like.")

                if st.button("Location","id(3)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Rawa+Island,+Mersing,+Johor,'
                                                '+Malaysia/@2.520846,103.9740785,1797m/data=!3m1!1e3!4m5!3m4!1s0x31c'
                                                '53713051ed20f:0x42285157fe04015a!8m2!3d2.520353!4d103.9758811')

                # Beach5
                st.write("## 5. Manukan Island, Sabah")
                st.image("images/beaches/5.jpg", width=500, caption="Manukan Island, Sabah")
                st.write(
                    "Yet another island located in Sabah – this time off the state’s west coast – Manukan Island is very "
                    "popular with residents from the nearby state capital of Kota Kinabalu. It lies within the boundaries "
                    "of Tunku Abdul Rahman National Park, the first marine national park in Malaysia – dating back to 1974.")
                st.write(
                    "Because of this, the tiny island is famous for the amazing scuba diving and snorkeling opportunities "
                    "just off its coast. Of course, it is just as well known for stunning beaches; the perfect meeting-"
                    "point between azure sea and pure white sand in a slice of coral paradise.")
                st.write(
                    "Away from the coastline, however, there are ample opportunities to explore the island’s dense "
                    "vegetation, thanks to a number of hiking trails that crisscross through it.")

                if st.button("Location","id(5)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Manukan+Island/@5.9744109,116.000'
                                                '5786,1789m/data=!3m1!1e3!4m5!3m4!1s0x323b4249434ae36f:0x4661be55566'
                                                '22a5c!8m2!3d5.9758774!4d116.0007493')

                # Beach7
                st.write("## 7. Long Beach, Perhentian Kecil")
                st.image("images/beaches/7.jpg", width=500, caption="Long Beach, Perhentian Kecil")
                st.write(
                    "The Perhentian islands off the northeastern coast of mainland Malaysia are already renowned for their"
                    " beauty, and are probably the country’s most famous destination for a tropical island getaway.")
                st.write(
                    "The smaller of the two main islands, Perhentian Kecil caters more towards backpackers, whilst "
                    "neighboring Perhentian Besar is full of expensive resorts. Perhantian Kecil features a number of "
                    "beautiful beaches, but none quite as good as the huge and aptly named Long Beach. The sand at Long "
                    "Beach is fine, white sand, and, since the tide stays out here for quite a while, the water stays very"
                    " shallow for a period, making for ideal swimming conditions in the warm waters.")
                st.write(
                    "Snorkeling, splashing around in the water and catching some rays are the order of the day at"
                    " this exquisite beach.")

                if st.button("Location","id(7)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Long+Beach,+Perhentian+Kecil/@5'
                                                '.9183039,102.7211612,895m/data=!3m1!1e3')

                # Beach9
                st.write("## 9. Coral Beach, Pangkor")
                st.image("images/beaches/9.jpg", width=500, caption="Coral Beach, Pangkor")
                st.write(
                    "One of the main attractions of Perak – a state on Malaysia’s west coast – is the beautiful Pangkor"
                    " Island. Littered with historical sites that run the gamut from a centuries-old Dutch fort to "
                    "evidence of previous Chinese settlers in the Fu Lin Kong Taoist temple, it’s a well-trodden tourist"
                    " destination in the area.")
                st.write(
                    "However it’s not just the cultural heritage of this storied little island – which saw one of the "
                    "first treaties that led to British rule of Malaysia – that brings visitors to its shores. Pangkor"
                    " is known for its beautiful beaches, the best of these is the stunning Coral Beach.")
                st.write(
                    "With a very much deserted island feeling, the white sand sweeps against the turquoise-blue sea "
                    "in a picturesque curve, whilst tall palms lean over the bright sand in what is practically a"
                    " postcard of paradise.")

                if st.button("Location","id(9)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Coral+Beach/@4.2393462,100.5421'
                                                '666,1542m/data=!3m1!1e3!4m5!3m4!1s0x3034d3f7a6fd8517:0x744b19fb7e6e3'
                                                '897!8m2!3d4.2413085!4d100.5422836')

            with col2:


                # Beach2
                st.write("## 2. Pantai Cenang, Langkawi")
                st.image("images/beaches/2.jpg", width=512, caption="Pantai Cenang, Langkawi")
                st.write(
                    "Malaysia’s premier island destination, Langkawi has it all when it comes to the elements that make "
                    "up the best beaches – facilities, nearby accommodation, restaurants. So it’s no wonder that its best"
                    " beach is a composite of all these things.")
                st.write(
                    "Pantai Cenang, whilst popular with domestic and international tourists, will practically be yours as"
                    " a private beach ‘out of season’ since, if you’re backpacking, there is no ‘out of season’!")
                st.write(
                    "Smaller islets jut out of the turquoise sea that laps the huge white-sand beach at Pantai Cenang, "
                    "whilst there are plenty of options for food and drink literally steps away from the beach. The nearby"
                    " amenities plus the relatively calm waters make it a very family-friendly beach, too.")

                if st.button("Location","id(2)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Pantai+Cenang/@6.2891044,99.72084'
                                                '35,5131m/data=!3m1!1e3!4m5!3m4!1s0x304b880ba2f7821b:0xc3f05608f58761'
                                                '03!8m2!3d6.2955916!4d99.7228132')

                # Beach4
                st.write("## 4. Kapas Island, Terengganu")
                st.image("images/beaches/4.jpg", width=500, caption="Kapas Island, Terengganu")
                st.write(
                    "Kapas Island is another one of Malaysia’s picture-perfect paradise islands, with beaches here that"
                    " look exactly like those you’d see on a postcard of yesteryear. Nowadays, it more resembles the "
                    "beaches on your Instagram feed; palms nod over fine, white sand, lapped by clear seas which lead "
                    "out into a beautiful turquoise-blue vista.")
                st.write(
                    "Just off the coast from the town of Marang in Terengganu, Kapas really is one of Malaysia’s most "
                    "beautiful islands. It’s a paradise for snorkeling and diving, with a wide array of marine life – the "
                    "coral here is bright and vivid – always an incredible sight.")

                if st.button("Location","id(4)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Kapas+Island/@5.2216497,103.2582'
                                                '232,4292m/data=!3m1!1e3!4m5!3m4!1s0x31b7eb62ae4ed317:0xeae0e00cf35268'
                                                '64!8m2!3d5.2190041!4d103.2649049')

                # Beach6
                st.write("## 6. Juara Beach, Tioman")
                st.image("images/beaches/6.jpg", width=500, caption="Juara Beach, Tioman")
                st.write(
                    "This relatively large tropical island is located off the east coast of the Malaysian state of Pahang."
                    " Whilst this densely forested, sparsely populated island also comes complete with several lovely "
                    "beaches – helping it to earn the title of one of the world’s most beautiful islands according to TIME"
                    " Magazine in the 1970’s – one beach stands out amongst the rest – Juara.")
                st.write(
                    "Yes, the incredible Juara Beach is a true jewel in the crown of Malaysia’s best beaches, helped by "
                    "its relatively remote location – ferries do not land at the beach, it is only reachable via 4WD on a"
                    " paved road that cuts through Tioman’s central mountain range.")
                st.write(
                    "Whilst the beach is unreal, it’s also known for the conservation of sea turtles, with the Juara "
                    "Turtle Project managing a hatchery here.")

                if st.button("Location","id(6)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Juara+Beach,+Tioman/@2.7911406,'
                                                '104.1801505,15230m/data=!3m1!1e3')

                # Beach8
                st.write("## 8. Mataking Island, Sabah")
                st.image("images/beaches/8.jpg", width=500, caption="Mataking Island, Sabah")
                st.write(
                    "Another fantastic tropical island located just off the east coast of Sabah in Malaysian Borneo, "
                    "Mataking Island is something of a bonus when it comes to a beach destination. It’s connected to "
                    "another, much smaller island called Pulau Mataking Kecil via a sandbar, meaning that most of this "
                    "beautiful island is basically a collection of beach, beach and more beach.")
                st.write(
                    "The whole island is ringed by white sand, meaning there’s never going to be any lack of space for"
                    " you. In fact, you probably won’t know where to sit – there’s so much opportunity to simply take a "
                    "while to stare out at the perfect coral sea surrounding Mataking.")
                st.write(
                    "This eastern island is also known for its amazing diving opportunities – aside from being the "
                    "location of Malaysia’s first ‘underwater post box’, the marine life here is wonderfully diverse "
                    "and beautifully vibrant.")

                if st.button("Location","id(8)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Mataking+Island/@4.5767424,118.'
                                                '9467051,2148m/data=!3m1!1e3!4m5!3m4!1s0x32401a0011cd7e39:0xab52ac777'
                                                '2465465!8m2!3d4.5762588!4d118.9489446')

                # Beach10
                st.write("## 10. Sipadan Island")
                st.image("images/beaches/10.jpg", width=500, caption="Sipadan Island")
                st.write(
                    "A stunning, turquoise jewel in the deep Celebes Sea off eastern Sabah on Malaysian Borneo, "
                    "Sipadan Island is a beautiful destinations, both above sea level and underwater.")
                st.write(
                    "Boasting an impossibly picturesque tropical reef lagoon, the island is a well-known dive spot that "
                    "sees visitors flocking to it for its flourishing marine life. In fact, it has been voted ‘Top Dive "
                    "Destination In The World’ on Scuba Diving Magazine’s Gold List, and for good reason: loggerhead "
                    "turtles, manta rays, hammerhead and whale sharks are frequent visitors of this almost fabled "
                    "location.")
                st.write(
                    "Even renowned undersea explorer Jacques Cousteau called it ‘an untouched piece of art’ back in 1989,"
                    " and thankfully – for both marine conservationists and amateur divers – not much has changed since "
                    "then. Though there are beautiful beaches here, to not dive in Sipadan’s waters would be verging on "
                    "foolish.")

                if st.button("Location","id(10)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Sipadan+Island+beach/@4.11'
                                                '78093,118.6287784,4722m/data=!3m1!1e3')






        if sidbar == 'Best cities':
            st.title("Best Cities to Visit in Malaysia......")
            st.write("With a long and fascinating history, Malaysia is home to an intoxicating mix of different "
                     "cultures and people – this is what makes its cities so fascinating to explore. Buddhist temples,"
                     " skyscrapers and bustling markets can be found alongside colonial architecture and Malay "
                     "buildings, while a mesmerizing array of beautiful landscapes border the cities themselves.")
            st.write("With its rich cultural heritage, delicious cuisine and welcoming, friendly people, the best "
                     "cities in Malaysia are unlike any place you´ve been before.")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1. Kuala Lumpur")
                st.image("images/cities/1.jpg", width=500, caption="Kuala Lumpur")
                st.write(
                    "With so much to see and do, Malaysia´s massive multicultural metropolitan capital really does have "
                    "something for everyone. Appearing to be almost endless, the city stretches away to the horizon, with"
                    " domineering skyscrapers and the Petronas Towers reaching towards the heavens. With its infectious "
                    "energy and plethora of attractions, wandering around its temples, mosques, shopping malls and busy "
                    "markets is intoxicating.")
                st.write(
                    "Because it is home to a diverse population, Kuala Lumpur´s unique cultural heritage really does "
                    "shine through. Colonial architecture is on show around Merdeka Square, while fantastic restaurants"
                    " and cafes are spread throughout other neighborhoods such as Little India and Chinatown.")

                if st.button("Location","id(1)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Kuala+Lumpur,+Federal+Territory+o'
                                                'f+Kuala+Lumpur,+Malaysia/@3.1372718,101.6440879,11.22z/data=!4m5!3m4!'
                                                '1s0x31cc49c701efeae7:0xf4d98e5b2f1c287d!8m2!3d3.139003!4d101.686855')


                st.write("## 3. Malacca")
                st.image("images/cities/3.jpg", width=500, caption="Malacca")
                st.write(
                    "Lying on the west coast of the Malaysian peninsula, Malacca (Melaka in Malay) is a unique place to"
                    " visit due to the British, Dutch and Portuguese all having ruled here at one point. As such, there"
                    " is a wealth of lovely colonial architecture to explore, with each nation having left its mark in "
                    "terms of the buildings left behind and the cultural impact that they had.")
                st.write(
                    "With a lively night market and a wide range of different cuisines on offer, this charming city is"
                    " understandably a popular tourist destination in Malaysia.")

                if st.button("Location","id(3)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Malacca,+Malaysia/@2.2448351,102'
                                                '.1807167,11z/data=!4m5!3m4!1s0x31d1ee278e8c65dd:0x32a7281769e016a!8m'
                                                '2!3d2.189594!4d102.2500868')

                st.write("## 5. Kota Kinabalu")
                st.image("images/cities/5.jpg", width=500, caption="Kota Kinabalu")
                st.write(
                    "Although Kota Kinabalu may not initially appear very enticing due to its sprawling concrete "
                    "buildings, once you get to know it, you´ll soon become enamored with all that it has to offer."
                    " Located in Borneo, the city looks out over the South China Sea and has a vibrant waterfront "
                    "and some incredible sunsets.")
                st.write(
                    "With malls, markets, fantastic cuisine, and a vibrant arts and music scene, Kota Kinabalu has "
                    "everything that you could want in a city. With so many sights lying nearby, it´s definitely worth"
                    " checking out. From here you can hike Mount Kinabalu, go scuba diving off the coast, or visit "
                    "the spectacular islands of the Tunku Abdul Rahman National Park.")

                if st.button("Location","id(5)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Kota+Kinabalu,+Sabah,+Malaysia/@6'
                                                '.022289,116.0271464,11.52z/data=!4m5!3m4!1s0x323b6995e6a6aba7:0xf1823'
                                                '36a16947a7e!8m2!3d5.980408!4d116.0734568')

                st.write("## 7. Miri")
                st.image("images/cities/7.jpg", width=500, caption="Miri")
                st.write(
                    "Fueled by oil money from the petroleum industry, Miri has modernized and expanded into the large "
                    "city we know today. A modern place full of life, the city has numerous fine restaurants, hotels and"
                    " bars for visitors to choose from, as well as some shopping malls and bustling markets.")
                st.write(
                    "Due to its diverse population, it is possible to try dishes from all around Malaysia and further"
                    " afield. As it is a major transport hub, many people stop by Miri on their way to other cities"
                    " in Malaysia.")

                if st.button("Location","id(7)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Miri,+Sarawak,+Malaysia/@4.44254'
                                                '18,113.9732766,10.82z/data=!4m5!3m4!1s0x321941fc74729dcf:0x2e911b344'
                                                'f6c4816!8m2!3d4.399493!4d113.9913832')


                st.write("## 9. Kuala Terengganu")
                st.image("images/cities/9.jpg", width=500, caption="Kuala Terengganu")
                st.write(
                    "Formerly a tiny fishing village, the discovery of oil transformed the face of the city – skyscrapers"
                    " now rub shoulders with quaint old buildings. Despite the proliferation of modern developments, "
                    "Kuala Terengganu is still a charming place, with a particularly lovely Chinatown and some delightful"
                    " beaches along the coast.")
                st.write(
                    "Mostly used as a base to explore the surrounding region’s mesmerizing jungles and beautiful islands,"
                    " the city has enough to keep visitors entertained for a couple of days.")

                if st.button("Location","id(9)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Kuala+Terengganu,+Terengganu,+Ma'
                                                'laysia/@5.4100269,102.8659023,10z/data=!4m5!3m4!1s0x31b7099e976e862f:'
                                                '0x1bc0ee85cb232492!8m2!3d5.329624!4d103.1370142')


                st.write("## 11. Kuantan")
                st.image("images/cities/11.jpg", width=500, caption="Kuantan")
                st.write(
                    "The capital of Pahang state, Kuantan´s unattractive sprawl of concrete buildings and lack of cultural"
                    " or historic attractions means that it often gets overlooked by tourists. However, the second largest"
                    " port in the country does have a couple of nice points that make it worth exploring, with the oldest"
                    " part of Kuantan, the Padang, being the highlight.")
                st.write(
                    "There are some nice beaches nearby, and people often use Kuantan as a base from which to explore the"
                    " nearby Gua Charas cave temple, or the royal town at Pekan with its fantastic palace.")

                if st.button("Location","id(11)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Kuantan,+Pahang,+Malaysia/@3.80'
                                                '85656,103.124215,11z/data=!3m1!4b1!4m5!3m4!1s0x31c8b9f8e826e005:0xa'
                                                '44c16aafb214f62!8m2!3d3.7633859!4d103.2201828')


                st.write("## 13. Putrajaya")
                st.image("images/cities/13.jpg", width=500, caption="Putrajaya")
                st.write(
                    "Lying around thirty kilometers from Kuala Lumpur, Putrajaya is a planned city that hosts the "
                    "government´s administrative body. Impressive to behold, there are some great monuments and "
                    "architecture on show here, as well as some fantastic green spaces and parks.")
                st.write(
                    "Beautifully illuminated at night, the city is well below its intended population, which makes it "
                    "a bizarre and slightly unsettling place to visit. Well worth a visit, Putrajaya testifies to "
                    "Malaysia´s ambition and vision for the future.")

                if st.button("Location","id(13)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Putrajaya,+Malaysia/@2.9339569,1'
                                                '01.6644429,12.74z/data=!4m5!3m4!1s0x31cdb625448e0b23:0x85165e8fa98'
                                                '1af6c!8m2!3d2.926361!4d101.696445')


                st.write("## 15. Alor Setar")
                st.image("images/cities/15.jpg", width=500, caption="Alor Setar")
                st.write(
                    "Known as ‘the rice bowl of Malaysia,’ Alor Setar is the capital of Kedah State, which is full of "
                    "padi fields and delightful curving hills. The city itself is a bastion of Malay culture and has some"
                    " interesting galleries to visit, as well as some lovely architecture on show.")
                st.write(
                    "Nearby is the stunning Pulau Langkawi, a tropical island with idyllic beaches. This is where most"
                    " visitors stop by when exploring the state. Part of an archipelago with around hundred islands, it "
                    "is this contrast of padi fields and beautiful beaches that makes Kedah such a delight to discover.")

                if st.button("Location","id(15)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Alor+Setar,+Kedah,+Malaysia/@6.1'
                                                '293116,100.2834061,12z/data=!3m1!4b1!4m5!3m4!1s0x304b44974ac2ef47:0x'
                                                '570491a0e03b1b7b!8m2!3d6.1263074!4d100.3671695')



            with col2:



                st.write("## 2. George Town")
                st.image("images/cities/2.jpg", width=500, caption="George Town")
                st.write(
                    "An eclectic mix of cultures greet you as you wander around George Town´s chaotic streets – this is"
                    " what makes it so captivating to visit. An attractive place, beautiful mosques and temples can be"
                    " found scattered about, while skyscrapers and shopping malls compete for space alongside the old "
                    "colonial architecture and local Malay buildings.")
                st.write(
                    "Its narrow streets that take you past little old shrines, bustling cafes and lively bars are fun"
                    " to get lost in, and there are plenty of great street art murals. With delicious cuisine that is "
                    "a blend of the various cultural influences readily available, the second largest city in the "
                    "country is well worth a visit.")

                if st.button("Location","id(2)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/George+Town,+Penang,+Malaysia/@'
                                                '5.4040213,100.2858927,12.74z/data=!4m5!3m4!1s0x304ac397ad2b7bd5:0x'
                                                '239ae45978a9b934!8m2!3d5.4141307!4d100.3287506')

                st.write("## 4. Ipoh")
                st.image("images/cities/4.jpg", width=500, caption="Ipoh")
                st.write(
                    "The capital of Perak state, Ipoh lies between Kuala Lumpur and the Thai border, and is a lovely "
                    "place to stop by. Its old town is pleasant to stroll around, with lots of little shops and cafes"
                    " dotting its tiny streets. The new part of town has many great restaurants serving up traditional"
                    " local dishes.")
                st.write(
                    "A plethora of impressive temples catering to all religions lie within the city, with the Perak "
                    "Tong cave temple being the highlight. A nice place to get away from the bustle of larger cities, "
                    "Ipoh is also a gateway to the nearby Cameron Highlands.")

                if st.button("Location","id(4)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Ipoh,+Perak,+Malaysia/@4.613315'
                                                '2,101.0648601,12z/data=!4m5!3m4!1s0x31caec79f34033e3:0x8fdc9f46695'
                                                '2e859!8m2!3d4.597479!4d101.090106')

                st.write("## 6. Kuching")
                st.image("images/cities/6.jpg", width=500, caption="Kuching")
                st.write(
                    "Despite being the the largest city in Borneo, Kuching is a laid-back, relaxing place to visit, with "
                    "a lot to see and do. Lying on the banks of the Sarawak River, the city has a charming waterfront "
                    "promenade and many interesting museums. There are also numerous restaurants, bars and cafes that "
                    "highlight the multicultural side of Kuching.")
                st.write(
                    "Skyscrapers rise as if from amidst the jungle, and it is this, along with its colonial architecture,"
                    " that makes for such a picturesque setting. A great base for exploring the rest of the island and"
                    " the nearby national parks, in Kuching you can organize treks into the jungle as well as trips "
                    "along the coast.")

                if st.button("Location","id(6)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Kuching,+Sarawak,+Malaysia/@1.63'
                                                '25898,110.2539592,11z/data=!4m5!3m4!1s0x31fb0784258cbf11:0xd3725759'
                                                '1ab17e72!8m2!3d1.553504!4d110.3592927')

                st.write("## 8. Kota Bharu")
                st.image("images/cities/8.jpg", width=500, caption="Kota Bharu")
                st.write(
                    "Located in the far northeast of the Malaysian peninsula, Kota Bharu is mainly visited by people "
                    "looking to head on to nearby Thailand or the Perhentian Islands. The city itself, however, is the"
                    " perfect place to gain an insight into Malay culture, with the interesting and educational Culture "
                    "Centre being particularly captivating.")
                st.write(
                    "With some lovely old architecture on offer, as well as some fantastic Buddhist temples and lively "
                    "markets, Kota Bharu is a good location from which to explore the delights of Kelantan state.")

                if st.button("Location","id(8)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/15200+Kota+Bharu,+Kelantan,+Malay'
                                                'sia/@6.1310996,102.2413289,15z/data=!4m5!3m4!1s0x31b6afd8841d6f33:0'
                                                'xbf251986c16f7589!8m2!3d6.124785!4d102.2543825')

                st.write("## 10. Johor Bahru")
                st.image("images/cities/10.jpg", width=500, caption="10. Johor Bahru")
                st.write(
                    "The most southern city in Malaysia lies on the border with Singapore. As such, most people only "
                    "stop by on their way to the neighboring country. A chaotic, traffic-filled place with poor air "
                    "quality, in recent years, Johor Bahru has tried to reinvent itself – things are slowly getting "
                    "better, with more large developments still to come.")
                st.write(
                    "A bustling city, it has more than enough museums and cultural attractions to make it worth "
                    "visiting. It also has some great shopping malls and lively nightlife.")

                if st.button("Location","id(10)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Johor+Bahru,+Johor,+Malaysia/@1'
                                                '.5448538,103.6395866,12z/data=!3m1!4b1!4m5!3m4!1s0x31da12c6d36b3a27'
                                                ':0xd5f4b21db593d4f5!8m2!3d1.492659!4d103.7413591')

                st.write("## 12. Sandakan")
                st.image("images/cities/12.jpg", width=500, caption="Sandakan")
                st.write(
                    "Looking out over the bay of the same name, Sandakan´s strategic location meant that it was heavily "
                    "bombed during the Second World War. Despite this, there is a nice waterfront and some quaint "
                    "colonial buildings and war memorials on offer – though in truth, Sandakan is seldom frequented by "
                    "tourists. From here you can take a scenic boat ride down the Kinabatangan River, where there is a "
                    "plethora of wildlife on show, or visit the orangutan sanctuary at Sepilok.")


                if st.button("Location","id(12)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Sandakan,+Sabah,+Malaysia/@5.78'
                                                '54993,117.7674936,10z/data=!3m1!4b1!4m5!3m4!1s0x3238c52b5714e379:0x'
                                                '8f0a9f314370d353!8m2!3d5.839444!4d118.1171729')

                st.write("")
                st.write("")

                st.write("## 14. Semporna")
                st.image("images/cities/14.jpg", width=500, caption="Semporna")
                st.write(
                    "A hectic place without any historic or cultural attractions of note, tourists stop by Semporna for"
                    " one reason only – to get to the nearby Semporna Archipelago. Full of traffic, if visitors do stay"
                    " in the city for any period of time, they invariably head to a check out the mosque and the "
                    "distinctive hotels on stilts lining the waterfront.")
                st.write(
                    "Although some people do stay in the city´s cheap hotels to save money for a couple more dives, "
                    "in general, you are much better off simply using Semporna to reach the nearby islands with "
                    "their divine diving sites.")

                if st.button("Location","id(14)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Semporna,+Sabah,+Malaysia/@4.50'
                                                '12741,118.272578,11z/data=!3m1!4b1!4m5!3m4!1s0x321557ccdef4f6e5:0x'
                                                '1ef5312593771503!8m2!3d4.479391!4d118.611545')

            st.write("# ---Map of cities in Malaysia---")
            st.image("images/cities/map.jpg", width=800)

        if sidbar == 'Best resorts':
            st.title("Best Malaysia Beach Resorts......")
            st.write("Thailand is definitely not the only country in southeast Asia with stunning beaches and islands."
                     " Malaysia has dozens of islands on both the east and west coasts that easily rival the beauty "
                     "of those in Thailand. In addition, Malaysia’s beach resorts rank as some of the best in the "
                     "region. This list presents the best beach resorts in Malaysia, as rated by visitors.")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1. Casa del Mar Langkawi")
                st.image("images/resorts/1.jpg")
                st.write("Rated as one of the best Malaysia beach resorts, the Casa del Mar in Langkawi, sits on Pantai "
                    "Cenang Beach. This is one of the most popular entertainment areas in Langkawi with a wide selection"
                    " of restaurants and pubs nearby. All hotel rooms face the sea and are cooled by air-conditioning "
                    "and ceiling fans. Floor to ceiling sliding picture windows provide great views of Cenang Beach. "
                    "Deluxe rooms are located on the ground floor and suites are on the first floor.")


                if st.button("Location","id(1)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@6.296507,99.722435,13z')

                if st.button("Book now","id(1)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g1096282-d307707-Reviews-Casa_del_'
                            'Mar_Langkawi-Pantai_Cenang_Langkawi_Langkawi_District_Kedah.html')

                st.write("## 3. The Datai Langkawi")
                st.image("images/resorts/3.jpg")
                st.write(
                    "The Datai Langkawi Hotel features a variety of villas and suites set against a tropical rainforest"
                    " atmosphere in close proximity to the beach. Facilities are plentiful and include a gym, health "
                    "club, sauna and not one but two pools. The larger of the two pools is elevated among the forest "
                    "canopy, with stunning views through the tree tops to the sea below. The other pool is located down"
                    " near the beach for those who wish to enjoy refreshing sea breeze. The resort contains five "
                    "specialty restaurants serving a range of global cuisine. Situated high up in the rainforest canopy,"
                    " The Pavilion restaurant for example serves authentic Thai cuisine in an open-air setting.")

                if st.button("Location","id(3)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/The+Datai+Langkawi/@6.4223438,'
                                                '99.6682566,17z/data=!3m1!4b1!4m8!3m7!1s0x304c71227e467659:0x82eef857'
                                                '296681f3!5m2!4m1!1i2!8m2!3d6.4223438!4d99.6704453')

                if st.button("Book now","id(3)"):
                    webbrowser.open_new_tab(url='https://www.touropia.com/tripadvisor/Hotel_Review-g298283-d302014-Re'
                                                'views-The_Datai_Langkawi-Langkawi_Langkawi_District_Kedah.html/u_malaysia-br')


                st.write("## 5. Pangkor Laut Resort")
                st.image("images/resorts/5.jpg")
                st.write(
                    "Pangkor Laut is a privately owned island located three miles off the West Coast of Malaysia along"
                    " the Straits of Malacca. There is no other resorts on the island, just secluded bays curled around"
                    " pristine beaches and a deep sense of serenity reserved exclusively for the guests. The villas are"
                    " carefully positioned along the island. Some are on the hillside amongst tropical rain forest, others"
                    " in lush tropical gardens, and others overlook the beach with beautiful views of the sea.")

                if st.button("Location","id(5)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Pangkor+Laut+Resort/@4.1953039'
                                                ',100.5353432,15z/data=!3m1!4b1')

                if st.button("Book now","id(5)"):
                    webbrowser.open_new_tab(url='https://www.touropia.com/bookingcom/my/pangkor-laut-resort/u_malaysia-br')

                st.write("## 7. Shangri-La's Tanjung Aru Resort & Spa")
                st.image("images/resorts/7.jpg")
                st.write(
                    "The Shangri-La’s Tanjung Aru Resort & Spa is nestled in beautiful natural surroundings in Kota "
                    "Kinabalu. Shopping and entertainment venues are close by. There are private balconies attached to "
                    "all of the rooms at the Tanjung Aru Resort. Guests can choose between six different restaurants "
                    "and bars. The hotel also offers extensive spa services to its guests.")

                if st.button("Location","id(7)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Shangri-La+Tanjung+Aru,+Kota+Kina'
                                                'balu/@5.9557196,116.0398227,17z/data=!3m1!4b1!4m8!3m7!1s0x323b69d565d'
                                                'ad5ab:0x362eaab09340cabd!5m2!4m1!1i2!8m2!3d5.9557196!4d116.0420114')

                if st.button("Book now","id(7)"):
                    webbrowser.open_new_tab(url='https://www.touropia.com/bookingcom/my/shangrilatar/u_malaysia-br')

                st.write("## 9. The Westin Langkawi Resort & Spa")
                st.image("images/resorts/9.jpg")
                st.write(
                    "Set in an idyllic natural retreat on the island of Langkawi, the Westin Langkawi Resort & Spa "
                    "boasts its own private beach. Tastefully designed with contemporary decor, all 202 rooms and suites"
                    " offer modern amenities such as a 42″ plasma TV with satellite channels and internet access. Guests"
                    " can cool down in the infinity pool, relaxation ocean pool or on the white sandy beach while "
                    "enjoying the magnificent view of neighboring islands.")

                if st.button("Location","id(9)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Shangri-La+Tanjung+Aru,+Kota+Kin'
                                                'abalu/@5.9557196,116.0398227,17z/data=!3m1!4b1!4m8!3m7!1s0x323b69d565'
                                                'dad5ab:0x362eaab09340cabd!5m2!4m1!1i2!8m2!3d5.9557196!4d116.0420114')

                if st.button("Book now","id(9)"):
                    webbrowser.open_new_tab(url='https://www.touropia.com/bookingcom/my/the-westin-langkawi-resort-spa/u_malaysia-br')

            with col2:


                st.write("## 2. The Danna Langkawi Malaysia")
                st.image("images/resorts/2.jpg")
                st.write(
                    "The Danna Langkawi is located on Pantai Kok in the northwest of Pulau Langkawi. Set in a five-storey"
                    " building, the beach resort offers spectacular views of the sea, marina and mountains. It comes with"
                    " facilities such as a fitness center, spa, and games room. The luxury hotel comes with a mix of local"
                    " architectural design and British colonial style, with a vibrant greenery of the landscaped courtyard"
                    " overlooks the pool. The 125 rooms and suites are equipped with a host of modern amenities and are "
                    "designed with timber flooring and handcrafted woodwork.")

                if st.button("Location","id(2)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/The+Danna+Langkawi/@6.3669674,99.'
                                                '6788114,17z/data=!3m1!4b1!4m8!3m7!1s0x304c7702fcfbd8af:0x4dfec21834ef'
                                                'e3c2!5m2!4m1!1i2!8m2!3d6.3669674!4d99.6810001')

                if st.button("Book now","id(2)"):
                    webbrowser.open_new_tab(url='https://www.touropia.com/bookingcom/my/the-danna/u_malaysia-br')

                st.write("## 4. Four Seasons Resort Langkawi Malaysia")
                st.image("images/resorts/4.jpg")
                st.write(
                    "The Four Seasons Resort Langkawi is located on the Tanjung Rhu Beach. All guest pavilions and "
                    "villas offer the soothing sounds of the Andaman Sea and sensational views of sunsets beyond the"
                    " beach. The guest accommodations are a fusion of traditional Malaysian design elements and "
                    "contemporary resort features, with timber floors, soaring ceilings and large open verandas. "
                    "The standalone villas offer complete privacy overlooking the azure sea. The spacious patio outside"
                    " the room is furnished with a dining table for four and an oversized daybed. The living area "
                    "includes a 42 inch plasma screen television and high speed internet.")
                st.write("")

                if st.button("Location","id(4)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Four+Seasons+Resort+Langkawi,+Ma'
                                                'laysia/@6.44642,99.8057773,17z/data=!3m1!4b1!4m8!3m7!1s0x304c7b7ddca'
                                                '70c81:0x916a996ac009c91a!5m2!4m1!1i2!8m2!3d6.44642!4d99.807966')

                if st.button("Book now","id(4)"):
                    webbrowser.open_new_tab(url='https://www.touropia.com/bookingcom/my/four-seasons-resort-langkawi'
                                                '/u_malaysia-br')

                st.write("## 6. Shangri-La's Rasa Ria Resort")
                st.image("images/resorts/6.jpg")
                st.write(
                    "The Shangri-La’s Rasa Ria Resort is situated just over a half an hour from the center of Kota "
                    "Kinabalu. The hotel is close to crystal clear waters and pristine beaches. The facilities at the "
                    "hotel itself include a restaurant that serves California dishes, a gym, a steam room and a massage"
                    " service. There is also a swimming pool and the hotel even has its own golf course.")

                if st.button("Location","id(6)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Shangri-La+Rasa+Ria,+Kota+Kinabal'
                                                'u/@6.1538356,116.1467603,17z/data=!4m12!1m2!2m1!1sShangri-Las+Rasa+'
                                                'Ria+Resort!3m8!1s0x0:0x3555d598ee59d186!5m2!4m1!1i2!8m2!3d6.1533961!'
                                                '4d116.1487348!15sChxTaGFuZ3JpLUxhJ3MgUmFzYSBSaWEgUmVzb3J0Wh4iHHNoYW5nc'
                                                'mkgbGEncyByYXNhIHJpYSByZXNvcnSSAQVob3RlbJoBJENoZERTVWhOTUc5blMwVkpRM'
                                                'EZuU1VSVGVIQmxNREJSUlJBQg')

                if st.button("Book now","id(6)"):
                    webbrowser.open_new_tab(url='https://www.touropia.com/bookingcom/my/shangri-la-s-rasa-ria-resor'
                                                't/u_malaysia-br')

                st.write("## 8. Tanjung Rhu Resort")
                st.image("images/resorts/8.jpg")
                st.write(
                    "Tanjung Rhu sits on the northern tip of Langkawi at on one of the most peaceful and beautiful "
                    "beaches on the island. It is the only resort on this part of the island ensuring its exclusivity"
                    " and the privacy of its guests. The resort is flanked by a landscape of centuries-old limestone "
                    "caves and uninhabited islands. Every room is spacious, with timber floors and large windows, to "
                    "take advantage of the tropical breeze and a choice of enchanting garden, pool or sea view.")

                if st.button("Location","id(8)"):
                    webbrowser.open_new_tab(url='')

                if st.button("Book now","id(8)"):
                    webbrowser.open_new_tab(url='https://www.touropia.com/bookingcom/my/tanjung-rhu-resort/u_malaysia-br')

                st.write("## 10. Bunga Raya Island Resort & Spa")
                st.image("images/resorts/10.jpg")
                st.write(
                    "The Bunga Raya Island Resort & Spa is located in a secluded spot close to the city of Kota "
                    "Kinabalu. Cable television service, air conditioning, high speed Internet and minibars are available"
                    " in every room. The villas at the Bunga Raya Island Resort & Spa also feature balconies. The beach"
                    " resort has modern amenities but features a design that incorporates many of the characteristic "
                    "elements of Borneo architecture such as timbered construction. The villas are located on the beach "
                    "swhere they enjoy sweeping views of the South China Sea.")

                if st.button("Location","id(10)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Bungaraya+Island+Resort/@6.027663'
                                                ',116.0169073,17z/data=!3m1!4b1!4m8!3m7!1s0x323b41ca8f699e79:0x11575ae'
                                                '05ff0c391!5m2!4m1!1i2!8m2!3d6.0275822!4d116.0190848')

                if st.button("Book now","id(10)"):
                    webbrowser.open_new_tab(url='https://www.touropia.com/bookingcom/my/bunga-raya-island-resort-spa'
                                                '/u_malaysia-br')




        if sidbar == 'Best national Parks':

            st.title("Most Beautiful National Parks in Malaysia")

            st.write("Multicultural Malaysia is home to a stunning array of sights and sounds that will entice and awe"
                     " any lucky visitor to this beautiful tropical country. Divided into two, its territories are "
                     "split between West Malaysia, which is located on a peninsula connected to the mainland of Asia,"
                     " and East Malaysia which lies on the island of Borneo. Consequently, it is home to a wide "
                     "variety of diverse ecosystems just waiting to be explored.")
            st.write("Whether it is pristine beaches you are after, the pumping nightlife of Malaysia’s bustling "
                     "cities or even the delicious Malay cuisine that entices you; this gem of a country has "
                     "something for everyone to delight in.")
            st.write("With such a wealth of incredible things to see and do, it can be hard to choose the perfect "
                     "itinerary. To help you decide, here are the most beautiful national parks in Malaysia; all "
                     "of which are well worth a visit!")

            col1, col2 = st.beta_columns(2)

            with col1:


                st.write("## 1. Gunung Mulu National Park")
                st.image("images/nationalparks/1.jpg")
                st.write("Named after the impressive Mount Mulu, this national park is phenomenal for the wealth of"
                         " amazing scenery and stunning landscapes on show. Remote and relatively inaccessible, the "
                         "only ways to reach it are by plane or by riverboat; it doesn’t matter how you get here "
                         "just as long as you do!")
                st.write("The ancient karst formations are what Gunung Mulu National Park is primarily known as over"
                         " the millennia they have thrown up an incredible array of astounding rock formations. With "
                         "caverns, cliffs and canyons spectacularly cutting their way through the undergrowth of the"
                         " park, the scenery simply needs to be seen to be believed.")
                st.write("Huge caves dot the area and in actual fact Sarawak Chamber is the largest known chamber in "
                         "the world. Stretching forever, the mind boggles at its colossal size. Mesmerizing and unique,"
                         " this national park in Malaysia is definitely worth the effort!")

                if st.button("Location","id(1)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Gunung+Mulu+National+Park/@4.'
                                                '0935479,114.8899537,8598m/data=!3m1!1e3')

                st.write("## 3. Kinabalu National Park")
                st.image("images/nationalparks/3.jpg")
                st.write("One of the most important biodiversity hotspots in the world, Kinabalu has an awe-inspiring "
                         "range of fauna and flora for visitors to revel in. With over 4500 different types on show, "
                         "the abundance of life springs out at you from every side and in the dense undergrowth the "
                         "rustles and movements of its concealed birds and animals can be heard.")
                st.write("Named after the mountain that gave it its name, Kinabalu is actually the tallest mountain "
                         "on the island standing at over 4000 meters in height. Despite being one of the most popular"
                         " parks in Malaysia, the national park is delightfully pristine and untouched.")

                if st.button("Location","id(3)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Kinabalu+National+Park/@6.028'
                                                '2995,116.5336964,16656m/data=!3m1!1e3')

                st.write("## 5. Gunung Gading National Park")
                st.image("images/nationalparks/5.jpg")
                st.write("Magical to behold, the dense and oppressive foliage of the jungle hems in on either side of"
                         " you before giving way to breathtaking views of the surrounding area as you reach one of "
                         "the park’s lofty peaks.")
                st.write("The mountainous area has numerous waterfalls and streams hidden among its forests and these"
                         " offer visitors a refreshing break after the arduous treks. While the scenic park is well "
                         "worth visiting in itself, the main draw for visitors are the incredible rafflesia; the "
                         "world’s largest flower. These huge and unique flowers are special to see and are the "
                         "undoubted highlight of Gunung Gading National Park.")

                if st.button("Location","id(5)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Gunung+Gading+National+Park/@1'
                                                '.7175208,109.8158237,7193m/data=!3m2!1e3!4b1')


                st.write("## 7. Similajau National Park")
                st.image("images/nationalparks/7.jpg")
                st.write("Located on the coast of the island of Borneo, this national park is a delightful combination"
                         " of a number of diverse ecosystems and has a huge catalogue of different activities for "
                         "visitors to choose from.")
                st.write("Whether you are an avid birdwatcher, a hiking aficionado or passionate about snorkeling; the"
                         " facilities on offer are astounding and as such each visitor is free to pursue their "
                         "preferred pastime as they please. Stunning beaches line the shore and thick impenetrable "
                         "jungle rears up until the sand prevents it from encroaching further.")
                st.write("Take to the water and enjoy a memorable boat trip; looking back at the coast will offer you"
                         " an unbelievable panorama of this beautiful stretch of coastline. At night, adventurous "
                         "visitors can charter a boat to partake in some crocodile sighting!")

                if st.button("Location","id(7)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Similajau+National+Park/@3.3482'
                                                '887,113.1542052,898m/data=!3m2!1e3!4b1!4m5!3m4!1s0x321e7dd6b3882d21'
                                                ':0xd1b357fda2b54d43!8m2!3d3.3482887!4d113.1563939')
                st.write("")
                st.write("")
                st.write("")

                st.write("## 9. Tunku Abdul Rahman National Park")
                st.image("images/nationalparks/9.jpg")
                st.write("An idyllic paradise, the five islands that make up Tunku Abdul Rahman National Park are "
                         "simply divine. Speeding through the beautiful blues waters to the islands, you can be "
                         "forgiven for imagining that you are daydreaming such is its splendor.")
                st.write("Varying in size, all of the islands have lovely beaches to relax on and the surrounding "
                         "coral reefs make for some fantastic snorkeling and scuba diving. Although the park can get"
                         " crowded, this only demonstrates its popularity and testifies to the incredible "
                         "attractions on show.")
                st.write("The lush verdant forests that slowly give way to dazzling white beaches that slip into the"
                         " waters around them make these islands a must-see in Malaysia.")

                if st.button("Location","id(9)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Tunku+Abdul+Rahman+Park/@5.975'
                                                '1613,115.9982501,1284m/data=!3m1!1e3!4m5!3m4!1s0x323b4236310d3b6d:'
                                                '0x6a4250d1adf6edee!8m2!3d5.9750449!4d115.9997596')

                st.write("## 11. Penang National Park")
                st.image("images/nationalparks/11.jpg")
                st.write("Located in the far northwest of the country, Penang National Park has a huge range of "
                         "activities on offer for tourists to enjoy. A biodiversity hotspot, the park is home to an "
                         "astounding array of fauna and flora that coat and cover every available surface. With "
                         "beautiful beaches galore and fun and wild treks through the dense forest; there truly is "
                         "something for everyone in this amazing national park.")
                st.write("Whether it is lounging on the deserted beaches, taking a boat trip to marvel at the fish "
                         "below or setting up camp to stay the night, Penang is a haven of peace and calm which will"
                         " certainly soothe your soul.")
                st.write("Within the boundaries of the park lies a Canopy Walk which offers you the chance to see the"
                         " forest from a different perspective as you walk along the flimsy walkways fifteen meters "
                         "above the ground.")

                if st.button("Location","id(11)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Penang+National+Park/@5.460354'
                                                '7,100.1891128,2208m/data=!3m1!1e3!4m5!3m4!1s0x304aebcd109625ed:0xe4'
                                                '8f33317fbd27c1!8m2!3d5.4620008!4d100.189996')

            with col2:



                st.write("## 2. Taman Negara National Park")
                st.image("images/nationalparks/2.jpg")
                st.write("Taman Negara has it all. Whether you are after unforgettable climbing, relaxing fishing or "
                         "learning about the local culture; this national park really does have something for everyone."
                         " With one of the oldest tropical rainforests in the world, its fauna and flora give off a "
                         "feeling of timelessness that seeps into everything, slowing down time and giving you more "
                         "memorable moments to enjoy the park.")
                st.write("For a beautiful view of the forest below, walk precariously along the narrow canopy walk "
                         "that stretches between the trees and hides itself among the surrounding foliage. Roaming its"
                         " forests down below are ferocious Malayan Tigers, secretive Asian elephants and the furtive"
                         " Malayan gaur; all of which are protected within the confines of the park.")
                st.write("A dreamy way to spend an afternoon is to take to the Tembeling River and drift your way "
                         "through the rainforest, gazing upon all of the natural wonder before you. Serene and "
                         "relaxing, Taman Negara needs to be experienced to be understood.")

                if st.button("Location","id(2)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Taman+Negara+National+Park/@5.'
                                                '4603547,100.1891128,2208m/data=!3m2!1e3!4b1')

                st.write("## 4. Bako National Park")
                st.image("images/nationalparks/4.jpg")
                st.write("With beautiful and distinctive rock formations and sea arches twisting their way up out of"
                         " the water, Bako National Park is home to some absolutely delightful sights that belie "
                         "its small size.")
                st.write("The snaking paths of the park make their way through a number of lovely landscapes that are"
                         " just waiting to be explored as dense rainforest, pristine beaches and stunning waterfalls"
                         " make up just some of its scenic views. Only accessible by boat, the journey and arrival at"
                         " the incredible and secluded beach of Bako make this national park well worth a visit.")

                if st.button("Location","id(4)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Bako+National+Park/@1.7160764,11'
                                                '0.4643287,1851m/data=!3m1!1e3!4m5!3m4!1s0x31fa532cb6e56807:0x5abbf3'
                                                '14c5effda6!8m2!3d1.7166667!4d110.4666667')


                st.write("## 6. Niah National Park")
                st.image("images/nationalparks/6.jpg")
                st.write("Wow! This impressive national park is well worth visiting for the spectacular caves contained"
                         " within its boundaries. The complex of caves has signs of human habitation dating back over"
                         " 40,000 years and as such it is a very important archaeological site in Malaysia.")
                st.write("Pottery, axes, jewellery and other various tools from across the millennia have been found "
                         "within the caves testifying to their long-lasting appeal to humans as a place for shelter "
                         "and protection. The caves themselves are stunning to explore and the distinctive geological"
                         " formations are marvelous to behold.")
                st.write("Outside, the thriving fauna and flora stops suddenly before the shade of the caves unable "
                         "to continue their advance. The juxtaposition of the warm and welcoming life-filled forests "
                         "with the bleak and cold caves makes Niah National Park a special place to visit.")

                if st.button("Location","id(6)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Niah+National+Park/@3.803598'
                                                '1,113.7753413,5151m/data=!3m1!1e3')

                st.write("## 8. Lambir Hills National Park")
                st.image("images/nationalparks/8.jpg")
                st.write("Although it is small in stature, Lambir Hills National Park definitely punches above its "
                         "weight when it comes to all that is has on offer. A biodiversity hotspot that is home to a "
                         "veritable menagerie of animals and birds both large and small, this park is perfect for "
                         "nature lovers who will adore all that there is to see and do.")
                st.write("Trails and paths delightfully weave their way through the undergrowth of the forest and, in"
                         " the shade of the canopy above, birds and monkeys play amidst the foliage. With the trees "
                         "reaching up to eighty meters in height, you sometimes feel dwarfed by the oppressive forest"
                         " that hems in all around you.")
                st.write("To feel a breeze on your skin and escape from towering trees, make for the highest point in"
                         " the park, Bukit Lambir, which also offers up some amazing views. With waterfalls and "
                         "secluded pools scattered around the park, there are a wealth of beautiful sights to discovery"
                         " in the lovely and peaceful Lambir Hills.")

                if st.button("Location","id(8)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Lambir+Hills+National+Park/@4.196'
                                                '8069,114.0420544,1075m/data=!3m1!1e3!4m5!3m4!1s0x321f318678a19e09:0xc'
                                                '7d372467b2b6306!8m2!3d4.198371!4d114.042873')

                st.write("## 10. Endau-Rompin National Park")
                st.image("images/nationalparks/8.jpg")
                st.write("Named after two rivers that flow through it, Endau-Rompin National Park is coated in "
                         "pristine tropical rainforest that makes for some delightful trekking. This ancient landscape"
                         " that dates back some 240 million years is well worth exploring on your visit to Malaysia "
                         "due its beautiful scenery that look like something out of Jurassic Park.")
                st.write("Rivers, pools and waterfalls dot the park’s premises and stumbling upon them after a tiring"
                         " trek through the rainforest is an unforgettable feeling. With the second highest peak in "
                         "Malaysia, this national park has an abundance of natural wonders that will astound and awe "
                         "you with their magnificence.")
                st.write("Slowly wandering along the paths that are dwarfed by the enormous trees on either side is a "
                         "liberating experience as you feel free and unfettered, alone in the wild.")

                if st.button("Location","id(10)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/place/Endau+Rompin+National+Park/@2.471'
                                                '4197,103.2596437,6545m/data=!3m1!1e3!4m5!3m4!1s0x31cfe189383916af:0xe'
                                                '724e311a3c49573!8m2!3d2.471916!4d103.2663479')

                st.write("## 12. Gunung Ledang National Park")
                st.image("images/nationalparks/10.jpg")
                st.write("This charming national park surrounds the imposing Mount Ophir which looms dramatically at "
                         "the heart of the jungle that coats its slopes. Myths and legends abound about the origins "
                         "of the mount’s name and fine mist cloaks the higher realms of its slopes, hiding its "
                         "mysterious past alongside it.")
                st.write("Paths snake their way through the lush undergrowth ever upwards and the view from the top "
                         "is breathtaking as you are greeted with panoramic views of the forest below. A wide variety "
                         "of birdlife resides in the rich and verdant canopies that cover Gunung Ledang National Park."
                         " Waterfalls also dot Mount Ophir and one of the most popular are the Puteri Waterfalls which"
                         " offers visitors the chance to cool off after an arduous trek in its refreshing and "
                         "welcoming pool.")

                if st.button("Location","id(12)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/search/Gunung+Ledang+National+Park/@2'
                                                '.3471656,102.6106042,7190m/data=!3m1!1e3')










    if countryselect == 'Switzerland':

        st.sidebar.title("...switzerland...")
        st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5kKRWjvy-lw0GFpuO03r_TqXm98kkRhhwcQ&usqp=CAU")
        sidbar = st.sidebar.radio("", ("About", "Best Lakes", "Best cities", "Best resorts",
                                       "Best Scenic Small Towns"))

        if sidbar == 'About':
            st.title("Welcome to Switzerland")

            col11, col22 = st.beta_columns(2)

            with col11:
                st.balloons()
                st.image("https://www.nationsonline.org/gallery/Switzerland/Toblerone-mountain.jpg")
                st.write(
                    "To begin, you should know some interesting facts about Switzerland. The capital of Switzerland "
                    "is Berne. The Swiss Confederation (conventional name of Switzerland) is a federal republic "
                    "divided into Executive, Legislative and Judicial branch. The country is split into 26 administrative "
                    "divisions (cantons). The Swiss Confederation was found on August 1, 1291 and the Swiss celebrate "
                    "this 1 of August as their National holiday.")
                st.write(
                    "With the help of an experienced travel guide planning your Swiss vacation, Switzerland is an exhilarating place."
                    " The diversity of the landlocked, mountainous country is the essence of Switzerland and gives the country its unique"
                    " identity. Along with its attractiveness as one of Europe's main tourist destinations, it is best known for its "
                    "financial institutions, fine cheeses, and chocolate, the watchmaking industry, for its scenery and an "
                    "excellent network of public transportation.")


            with col22:

                st.write("The renowned Swiss obsessiveness with cleanliness, punctuality and hard work, coupled with the "
                         "highest standard of living in Europe, make Switzerland one of the most desirable and least problematic of countries"
                         " in which to travel. The tourist infrastructure is highly developed, and the Swiss themselves are unfailingly courteous "
                         "and proud of the beauty of Switzerland. You will leave with lasting memories of a great Switzerland vacation. Most Swiss "
                         "speak English, and at least one of the other Swiss languages - French, German, Italian, or, in the extreme southeast, Romansch.")

                st.write(
                    "One of the best things about Switzerland is its untouched nature and in general, people are careful with it with many efforts "
                    "being undertaken to protecting the environment. As a result, Switzerland is far advanced in recycling waste material. Chemicals, "
                    "paper, carton, glass, plastic, cans, textile, oil and cooking fat are all collected separately. For most tourists, our recycling "
                    "measures are relatively drastic. However, you will get used to it quickly and the advantages are clear: Switzerland is a very clean "
                    "country. You will not find a lot of street litter along your way. Read on for more information about Switzerland and our Swiss travel guide.")

            st.image("https://www.worldatlas.com/r/w1200/upload/8b/0d/df/cantons-of-switzerland-map.png")
            if st.button("View location"):
                webbrowser.open_new_tab(
                    url='https://www.google.com/maps/place/Switzerland/@46.7912769,5.9814056,7z/data=!3m1!4b1!4m5!3m4!1s0x478c64ef6f596d61:0x5c56b5110fcb7b15!8m2!3d46.818188!4d8.227512')

            st.video("https://www.youtube.com/watch?v=linlz7-Pnvw&ab_channel=8KWorld")
            st.video("https://www.youtube.com/watch?v=Ww4Wc34s-fA&ab_channel=PJski")

        if sidbar == 'Best Lakes':
            st.title("Most Beautiful Lakes in Switzerland......")

            col1, col2 = st.beta_columns(2)

            with col1:


                st.subheader("1. Lake Lucerne")
                st.image("https://www.touropia.com/gfx/b/2017/06/lake_lucerne.jpg","Lake Lucerne")
                st.write(
                    "Switzerland’s fourth largest lake, Lake Lucerne is a study in contrasts. Though the winding body"
                    " of water is surrounded by the Alps, the climate is generally mild. When wreathed in fog, the lake "
                    "can take on a forbidding atmosphere, yet its one of the most popular travel destinations in"
                    " Switzerland. Numerous hotels and resorts dot the shores. Breathtaking landscapes explain the "
                    "appeal of lovely Lake Lucerne. In addition to boating, hiking and cycling, popular activities include"
                    " visits to the meadow of the Rutli, the legendary site of the founding of Swiss independence.")

                if st.button("View location","1(id)"):
                    webbrowser.open_new_tab(url='https://www.google.co.in/maps/@5.7736202,'
                                                '103.0350471,1790m/data=!3m1!1e3!5m1!1e2')

                # Beach3
                st.subheader(" 3.Lake Thun")
                st.image("https://www.touropia.com/gfx/d/lakes-in-switzerland/lake_thun.jpg?v=1","Lake Thun")
                st.write(
                    "Separated from neighboring Lake Brienz by a small sliver of land, Lake Thun offers numerous sightseeing "
                    "activities, from medieval churches and castles to natural wonders. Oberhofen on the northeast shore"
                    " is dominated by a 13th-century castle overhanging the lake. On the opposite side lies pretty Spiez"
                    " with its own castle and Romanesque church. Near the Beatushohlen-Sundlauenen ferry terminal at the "
                    "south end of the lake are the St. Beatus Caves where you can view with stalagmites, stalactites and waterfalls.")
                if st.button("View location","3(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Lake+Thun/@46.7003716,7.658179,12z/data=!3m1!4b1!4m5!3m4!1s0x478fae3554ddf6eb:0xc692ca79d2500aea!8m2!3d46.6958354!4d7.7212158')

                # Beach5
                st.subheader(" 5. Lake Brienz")
                st.image("https://www.touropia.com/gfx/d/lakes-in-switzerland/lake_brienz.jpg?v=9ea1c00d1c1a68460cbff58e3d2b30f3","Lake Brienz")
                st.write(
                    "One of Switzerland’s most beautiful lakes, Lake Brienz is known for its setting and spectacular turquoise-blue water."
                    " Surrounded by soaring mountains, the lake is best experienced by boat. Passenger ships have operated on Lake Brienz"
                    " since 1839, providing regular service to shoreline locations, including the resort town of Interlaken. Hiking from the "
                    "lake to the Geissbach Falls is another popular activity. A funicular railway takes you up the final stretch,"
                    " landing you on the grounds of the historic Grand Hotel Geissbach.")
                if st.button("View location","5(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Lake+Brienz/@46.7229753,7.932183,13z/data=!3m1!4b1!4m5!3m4!1s0x478fbd607bfad2fb:0x19281ec105cab0c7!8m2!3d46.7267426!4d7.9674729')

                #Beach7
                st.subheader("7. Walensee")
                st.image("https://www.touropia.com/gfx/d/lakes-in-switzerland/walensee.jpg?v=704b2476729883e17d5cf3dd4367ca0a")
                st.write(
                    "One of the larger lakes in Switzerland, Walensee is located within the area known as “Heidiland,” the region that "
                    "inspired Swiss writer Johanna Spyri’s famous Heidi stories. Scattered across the steep vertical cliffs framing lake"
                    " are a series of quaint villages, spa towns and ski resorts. Each offers breathtaking views of the lake below. "
                    "Lake Walen is a great spot for a variety of outdoor activities, from boating and hiking to downhill skiing. For"
                    " fans of the Heidi books, a visit to the tourist attraction Heididorf in nearby Maienfeld is sure to delight")
                if st.button("View location","7(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Walensee/@47.1255477,9.130186,12z/data=!3m1!4b1!4m5!3m4!1s0x479ad5ac5164db07:0xbbac9756d0fa37c9!8m2!3d47.1233017!4d9.2021972')

                # Beach9
                st.subheader("9. Blausee")
                st.image(
                    "https://www.touropia.com/gfx/d/lakes-in-switzerland/blausee.jpg?v=ffa067a6ee6f5cce3002445cf2ab6cd3",
                    "9. Blausee")
                st.write(
                    "Located in the Kander River valley, Blausee is a small lake that’s big on charm. Fed by subterranean springs, the "
                    "lake is named after its deep blue water. Legend has it that the lake got its color from a blue-eyed maiden who died "
                    "of a broken heart. The picturesque lake is situated in a lush green forest in the middle of the Blausee Nature Park. "
                    "While the Blue Lake has been a popular destination for centuries, it retains a feeling of peace and solitude. Fishing, "
                    "hiking and picnicking are favorite pastimes. If you simply want to unwind, a hotel on the shore of the lake"
                    " features a full-service spa.")
                if st.button("View location","9(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Blausee/@46.532439,7.6626503,17z/data=!3m1!4b1!4m5!3m4!1s0x478f071e871fc6b1:0x59fed3fa3889da49!8m2!3d46.5324482!4d7.6647629')

            with col2:


                # Beach2
                st.subheader("2. Lake Geneva")
                st.image("https://www.touropia.com/gfx/d/best-places-to-visit-in-switzerland/lake_geneva.jpg?v=1"," Lake Geneva")
                st.write(
                    "The largest lake in Switzerland, Lake Geneva shares its many attractions with neighboring France."
                    " Situated at the northern side of the Alps, the crescent-shaped lake is a favorite holiday spot "
                    "for the rich and famous. Luxury shops line the cobblestone streets of Geneva, and yachts float"
                    " serenely on the lake’s waters. A scenic cruise around the lake takes you past lakeshore castles "
                    "and hillside vineyards. Opportunities for outdoor activities draw visitors to Lake Geneva too. Ski "
                    "resorts and mountainous hiking trails are less than an hour’s drive away from the shoreline.")
                if st.button("View location","2(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Lake+Geneva/@46.361019,6.2586029,10z/data=!3m1!4b1!4m5!3m4!1s0x478c3d06fcbe3e07:0x3282c0cb7f4bf243!8m2!3d46.4414195!4d6.5295235')

                st.subheader("4. Lake Lugano")
                st.image("https://www.touropia.com/gfx/d/lakes-in-switzerland/lake_lugano.jpg?v=fc02ce537679cb3d207404477c7bc92c","Lake Lugano")
                st.write(
                    "Straddling the border between Switzerland and Italy, Lake Lugano offers visitors a multicultural holiday "
                    "experience. This large, branching lake boasts spectacular views from every angle. A great way to take it "
                    "all in is with a ride up the rack railway from the village of Capolago to the top of Monte Generoso. From "
                    "the Renaissance church in Morcote to the Hermann Hesse Museum in Montagnola, lakeside towns offer "
                    "unique insights into the region’s rich history.")
                if st.button("View location","4(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@45.983334,8.966667,13z')

                # Beach6
                st.subheader(" 6.Oeschinensee")
                st.image("https://www.touropia.com/gfx/d/lakes-in-switzerland/oeschinensee.jpg?v=1","Oeschinensee")
                st.write(
                    "Situated above the resort village of Kandersteg, Oeschinensee is a high-altitude lake that "
                    "attracts visitors in every season. A gondola ride from Kandersteg provides easy access to the "
                    "large alpine lake. Summer and winter, Lake Oeschinen boasts an array of unique experiences."
                    " In warm weather, a ride on a long slide winding through the mountainous landscape offers an "
                    "adrenaline-fueled thrill. Rowboat rentals are readily available for on-the-water fun. Ice fishing, "
                    "tobogganing and skating are popular pastimes when the lake freezes over, which generally occurs from December to May.")
                if st.button("View location","6(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Oeschinen+Lake/@46.4985177,7.7210951,16z/data=!3m1!4b1!4m5!3m4!1s0x478f08a670704edd:0x30815e0b3a5ce4ee!8m2!3d46.4989089!4d7.7291063')


                # Beach8
                st.subheader(" 8. Lake Zurich")
                st.image("https://www.touropia.com/gfx/d/lakes-in-switzerland/lake_zurich.jpg?v=1a3ae66f351c3961cc9a509106324249","Lake Zurich")
                st.write(
                    "With its northern section jutting into the Switzerland’s largest city, Lake Zurich is one of the "
                    "easiest lakes in the country to access. Adventures on the water begin with a boat cruise that "
                    "takes you past Zurich’s architectural wonders into the countryside. Glide past storybook villages"
                    " to the town of Rapperswil where you can stroll along a lakeside promenade, ramble through a medieval"
                    " castle and explore more than 600 varieties of roses in the public gardens. With a chapel that dates "
                    "to the 7th century, the nearby island Ufenau is worth visiting too.")
                if st.button("View location","8(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Lake+Zurich/@47.2836166,8.6008455,11z/data=!3m1!4b1!4m5!3m4!1s0x479aba90b8887a5f:0x6ac6428c5e8536ef!8m2!3d47.2225216!4d8.7527114')


                # Beach10
                st.subheader(" 10. Bachalpsee")
                st.image("https://www.touropia.com/gfx/d/lakes-in-switzerland/bachalpsee.jpg?v=1","Bachalpsee")
                st.write(
                    "Also known as Bachse, Bachalpsee is located above the resort town of Grindelwald in the canton of "
                    "Berne. The hike up to the small-sized lake from the popular ski resort takes around 1.5 hours. Views "
                    "of the surrounding glaciers, mountains and meadows make the trek well worth the effort. Don’t be"
                    " surprised if the scenery looks a bit familiar. The region around Grindelwald has provided a backdrop")
                if st.button("View location","10(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Bachalpsee/@46.6694431,8.0145568,15z/data=!3m1!4b1!4m5!3m4!1s0x478f99a2dab57f55:0x2fe44c469bb38461!8m2!3d46.669444!4d8.023333')


        if sidbar == 'Best cities':
            st.title("15 Best Cities to Visit in Switzerland......")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.subheader(" 1. Zurich")
                st.image("https://www.touropia.com/gfx/b/2018/06/zurich.jpg","Zurich")
                st.write(
                    "The largest city in Switzerland lies on the shores of Lake Zurich. It has the River Limmat twisting "
                    "through it and snow-capped mountains lying on the horizon. Along with its enchanting setting, the city"
                    " is a vibrant and lively place that is great to live in as well as explore as a visitor.")
                st.write(
                    "Zurich is the perfect mix of old and new, as its hip cultural and arts scene perfectly blends with the"
                    " delightful historic center. The trendy city has some great shopping, as well as fashionable cafes and a happening nightlife.")
                if st.button("View location","1(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@47.366669,8.55,13z')



                st.subheader(" 3. Bern")
                st.image("https://www.touropia.com/gfx/b/2018/06/bern.jpg","Bern")
                st.write(
                    "The picturesque capital of Switzerland is a dream of a place. Walking around the winding cobbled "
                    "streets of the Old Town, you´ll pass fountains and bell towers interspersed among the plentiful "
                    "old buildings. Many edifices date back over five hundred years, to when Bern was reconstructed "
                    "following a fire – the coherent design and architecture is in part what makes the city so impressive.")
                st.write(
                    "There are over six kilometers of covered arcades in Bern, giving it a distinctive feel, and these house"
                    " a number of great bars, restaurants and shops. Dripping with history, the city also has a lot of"
                    " good museums which are worth checking out. Bern´s beautiful location, on a peninsula surrounded by "
                    "the tree-lined Aare River, only adds to its charm and laid-back vibe.")
                if st.button("View location","3(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@46.946999,7.447,13z')

                st.subheader("5. Geneva")
                st.image("https://www.touropia.com/gfx/b/2018/06/geneva.jpg","Geneva")
                st.write(
                    "The second largest city in the country is a wealthy, cosmopolitan place that certainly has a luxurious feel."
                    " Home to numerous international organizations, such as the UN and World Bank, there is an opulence and glitter about its streets.")
                st.write(
                    "Lying on the shores of Lake Geneva, the city has a plethora of expensive hotels, boutiques, and"
                    " restaurants for visitors to choose from, although there is, of course, another side to Geneva. Head"
                    " to neighborhoods such as Les Grottes and Quartier des Paquis and you´ll soon find bars with bucket "
                    "loads of ambiance and energy – a world away from the stuffy corridors of the UN.")
                if st.button("View location","5(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@46.200001,6.15,13z')

                st.subheader("7. Lugano")
                st.image("https://www.touropia.com/gfx/b/2018/06/lugano.jpg","Lugano")
                st.write(
                    "Set in the Italian-speaking part of Switzerland, Lugano lies on the shores of Lake Lugano and has "
                    "mountains throughout the landscape surrounding it. Along with its scenic setting, Lugano is a chic"
                    " and glitzy place to visit, thanks to its up-market boutiques, restaurants and bars.")
                st.write(
                    "Its delightful cobbled streets snake away from the heart of the city at Piazza della Riforma, and there "
                    "are some great promenades along the waterfront which offer fantastic views over the lake. With a fine cathedral,"
                    " a great modern art museum, and hiking on offer in the nearby mountains, Lugano has more than enough to make it worth stopping by.")
                if st.button("View location","7(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.000000,8.950000&z=13')

                st.subheader("## 9. Bellinzona")
                st.image("https://www.touropia.com/gfx/d/best-cities-to-visit-in-switzerland/bellinzona.jpg?v=50d2cf7f6dac769c2be2d51c6f1ddf19","Bellinzona")
                st.write(
                    "With three medieval fortresses lying around this city and its beautiful location at the point where "
                    "several valleys join, it is somewhat surprising that Bellinzona´s wealth of attractions receive relatively few visitors.")
                st.write(
                    "The Old Town is a pleasure to wander around, and its twisting alleys are home to renaissance churches, "
                    "homely cafes and chiming bell-towers – all of which gives Bellinzona a charming feel. Once ruled "
                    "by the Italians, Swiss and Italian culture mix together in this delightful hidden gem.")
                if st.button("View location","9(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.200001,9.016667&z=13')

                st.subheader("11.Chur")
                st.image("https://www.touropia.com/gfx/d/best-cities-to-visit-in-switzerland/chur.jpg?v=74bd4a2bd912d9977acd2138c3b507e4","Chur")
                st.write(
                    "The oldest city in Switzerland, Chur is delightfully surrounded by the Alps. As such, there is "
                    "some grand hiking and trekking to be had in the nearby mountains. The city itself is small and "
                    "easily walkable in a day, with the Old Town being the undoubted highlight.")
                st.write(
                    "Here you´ll find a laidback center with some nice bars and restaurants dotted amongst the old buildings. "
                    "In the winter months there’s great skiing in the mountains, with St Moritz and Davos not too far away.")
                if st.button("View location","11(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.849998,9.533333&z=13')

                st.subheader(" 13.Fribourg")
                st.image("https://www.touropia.com/gfx/d/best-cities-to-visit-in-switzerland/fribourg.jpg?v=985e8e383161755a4090782999f1ab7a","Fribourg")
                st.write(
                    "With a stunning location straddling the gorge that splits the city in two parts, Fribourg is "
                    "certainly dramatic to behold and there are a number of great views to be had from the city itself.")
                st.write(
                    "Rising above the Samara River, a couple of picturesque bridges join the western, French-speaking "
                    "part of the city with the eastern part which speaks German. It has a magnificent medieval old town "
                    "with an impressive cathedral that towers above everything, as well as some interesting museums, "
                    "impressive fortifications and beautiful architecture. Thanks to its large student body there "
                    "is also lively nightlife for visitors to enjoy.")
                if st.button("View location","13(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.799999,7.150000&z=13')


            with col2:

                st.subheader(" 2. Lucerne")
                st.image("https://www.touropia.com/gfx/b/2018/06/lucerne.jpg","Lucerne")
                st.write(
                    "This beautiful city is absolutely stunning to visit, thanks to the surrounding mountains and the "
                    "glistening lake that borders it. There are a number of great views to be had, and, in addition to"
                    " the picture-perfect scenery, Lucerne has a delightful medieval quarter which only adds to the charming feel.")
                st.write(
                    "The winding alleys of the old town weave their way along the banks of the river that runs through "
                    "the center, and strolling along the waterfront in the sun is simply heavenly. The 14th century Chapel "
                    "Bridge is a popular sight to visit and there is a lively music scene too.")
                if st.button("View location","2(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=47.049000,8.308000&z=13')

                st.subheader(" 4. Basel")
                st.image("https://www.touropia.com/gfx/d/best-cities-to-visit-in-switzerland/basel.jpg?v=3b76595dd127b54475e60055c6494e74","Basel")
                st.write(
                    "Located on the banks of the Rhine, Basel´s strategic location right on the borders of France and "
                    "Germany has seen wealth accumulate in the city as trade and commerce flowed through its streets. "
                    "Consequently, it has a host of fine old buildings and there is a wealthy vibe about the place. "
                    "There are also some fantastic museums and galleries on offer.")
                st.write(
                    "Although it is not as picturesque as Bern, Basel still has a lovely old town which is worth "
                    "visiting, and some great architecture both old and new located around its confines. To get a feel "
                    "for the everyday life of its residents, head to Kleinbasel to enjoy some fine dining down on the riverbanks.")
                if st.button("View location","4(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@47.566666,7.6,13z')

                st.subheader(" 6. Lausanne")
                st.image("https://www.touropia.com/gfx/b/2018/06/lausanne.jpg","Lausanne")
                st.write(
                    "Buzzing with life, Lausanne´s large student body makes it a fun city in which to spend some time. "
                    "There´s an upbeat and youthful feel about the city, and it´s a great place to hit the town due to its"
                    " bustling nightlife scene. More than just a university town, Lausanne is beautifully located on the hillsides "
                    "overlooking Lake Geneva. The city drips down the gentle slopes, with the beautiful gothic old town located at the top.")
                st.write(
                    "There are some great museums scattered around, or take some time to relax in the many cafes and bars "
                    "that line the warehouses along the waterfront at the bottom of the city – Lausanne has something for everyone.")
                if st.button("View location","6(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.519833,6.633500&z=13')

                st.subheader(" 8. St. Gallen")
                st.image("https://www.touropia.com/gfx/d/best-cities-to-visit-in-switzerland/st_gallen.jpg?v=1583146aad94b9fe752bae105e31f36b"," St. Gallen")
                st.write(
                    "Steeped in history, St. Gallen´s ancient streets are perfect for history buffs to revel in. Its "
                    "picturesque squares and tiny cobbled alleyways weave their way about the old part of town, until "
                    "you suddenly stumble across the impressive cathedral towering above you.")
                st.write(
                    "The main attraction is the beautiful baroque library located in the abbey, containing a large number"
                    " of books dating back to medieval times. A cultured seat of learning, St. Gallen is set amongst roving "
                    "green hills, while mountains can be seen far off in the distance.")
                if st.button("View location","8(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=47.424168,9.370833&z=13')

                st.subheader("10. Thun")
                st.image("https://www.touropia.com/gfx/d/best-cities-to-visit-in-switzerland/thun.jpg?v=78e1ace30401763312cce4985ad741b1","Thun")
                st.write(
                    "Lying alongside the banks of the Aare River, Thun is ringed by mountains and looks like the archetypal"
                    " Swiss town. With a domineering castle overlooking the city, old buildings lining the riverside,"
                    " and cafes along the waterfront, Thun is a charming place to wander around. There´s a certain energy "
                    "about the city and unique artisanal shops dotted about its streets.")
                if st.button("View location","10(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.766666,7.633333&z=13')

                st.subheader(" 12. Interlaken")
                st.image("https://www.touropia.com/gfx/b/2018/06/interlaken.jpg","Interlaken")
                st.write(
                    "Interlaken´s incredible setting between two alpine lakes with snow-capped mountains dotted around "
                    "makes it a splendid city to visit in Switzerland. Although the city itself is small and touristy"
                    " due to its plethora of souvenir shops, it is the beautiful scenery surrounding it which draws people to the area.")
                st.write("It is the gateway to the famed Jungfrau region of the country, and from here you can go "
                         "white-water rafting, abseil down waterfalls, and hike around the lovely lakes and mountaintops.")
                if st.button("View location","12(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@46.683334,7.85,13z')

                st.subheader(" 14. Sion")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/sion_switzerland.jpg?v=1"," Sion")
                st.write(
                    "Lying on the banks of the Rhone, Sion is a small city that is beautifully located in the Rhone Valley. "
                    "While it does have a modern side to it, the highlight is undoubtedly the old town, which has two dramatic"
                    " hilltops overlooking it. Atop of these lie a ruined castle and a 13th Century church; they certainly make "
                    "for impressive viewing with the Alps peering out from behind them.")
                st.write(
                    "With vineyards surrounding the city, wine plays an important part in Sion´s social life, so there are"
                    " lots of great restaurants and atmospheric cafes from which to sample some of the local wines. From here "
                    "there are some fantastic hiking trails around the valley.")
                if st.button("View location","14(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@46.233334,7.366667,13z')


        if sidbar == 'Best resorts':
            st.title(" Best Switzerland Resorts......")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.subheader("1. Hotel Villa Honegg")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-switzerland/Hotel_Villa_Honegg.jpg?v=1","Hotel Villa Honegg")
                st.write("The Hotel Villa Honegg says its heated infinity pool has the most beautiful views in the world."
                         " It’s hard to argue with that statement since the pool overlooks Lake Lucerne and the mountains "
                         "beyond. Located on Mount Burgenstock, the hotel was built in 1905 as a private mansion, "
                         "undergoing renovations into a luxury boutique hotel in 2011.If you’re not in the mood to swim,"
                         " you can enjoy the same views from the terrace of this five-story stone chalet.")


                if st.button("View location","1(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Hotel+Villa+Honegg/@46.9948149,8.4008155,17z/data=!3m1!4b1!4m8!3m7!1s0x478ff83d3cb6dd83:0xb199aa43bcaa777d!5m2!4m1!1i2!8m2!3d46.9947972!4d8.4029095')

                if st.button("Book now","11(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g1973980-d2060431-Reviews-Hotel_Villa_Honegg-Ennetbuergen_Canton_of_Nidwalden.html')


                st.subheader("3.Grand Hotel Kronenhof, Pontresina")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-switzerland/Grand_Hotel_Kronenhof.jpg?v=1","Grand Hotel Kronenhof, Pontresina")
                st.write(
                    "The Grand Hotel Kronenhof has been serving guests since 1848. Located in the heart of the Swiss"
                    " Alps, this historic Neo-Baroque building is one of the most architecturally significant hotels "
                    "in the Alps. Renovated in 2007, it still retains its old-world charm. Its spa offers stunning views"
                    " of the Bernina glaciers and is considered one of the best in the world; it’s hard to beat the mountain"
                    " views, too. If you’re traveling with children, the hotel has restaurant just for them.")
                if st.button("View location","3(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Grand+Hotel+Kronenhof/@46.493499,9.898856,17z/data=!3m1!4b1!4m8!3m7!1s0x47837c729730c365:0x515ef3d9d9c74227!5m2!4m1!1i2!8m2!3d46.4935075!4d9.9010757')

                if st.button("Book now","33(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g198832-d236315-Reviews-Grand_Hotel_Kronenhof-Pontresina_Engadin_St_Moritz_Canton_of_Graubunden_Swiss_Alps.html')


                st.subheader(" 5.Hotel The Cambrian, Adelboden")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-switzerland/Hotel_The_Cambrian.jpg?v=1","Hotel The Cambrian, Adelboden")
                st.write(
                    "Hotel The Cambrian is located just 15 minutes from Bern, but it seems worlds away from a big city."
                    " Originally built in the early 1900s, it remains one of the region’s top hotels. Today it is a 21st "
                    "century ultra-modern chateau, its stone and slate sleekness interspersed with panoramic windows"
                    " displaying the mountains and greenery of the Adelboden Valley. You’ll enjoy world-class skiing "
                    "in the winter, while hiking and biking allow you to explore the environs in the summer.")
                if st.button("View location", "5(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/The+Cambrian+Adelboden/@46.4936111,7.5589171,17z/data=!3m1!4b1!4m8!3m7!1s0x478f022150a2631f:0xc6a08028cc31ade3!5m2!4m1!1i2!8m2!3d46.4936542!4d7.5610744')

                if st.button("Book now", "55(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g198862-d231843-Reviews-The_Cambrian-Adelboden_Bernese_Oberland_Canton_of_Bern.html')

                st.subheader(" 7.Hotel d'Angleterre, Geneva")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-switzerland/Hotel_dAngleterre.jpg?v=1","Hotel d'Angleterre, Geneva")
                st.write(
                    "The Hotel d’Angleterre oozes stately charm and elegance on the banks of Lake Geneva. Built in 1872,"
                    " It also oozes accolades from Forbes, Conde Nast and TripAdvisor, among others, for being one of"
                    " the world’s top hotels. The hotel is filled with antiques, with some modern décor in the rooms. "
                    "It offers great views not only of the lake and Mount Blanc but also of Switzerland’s largest water"
                    " fountain, which stands between the hotel and the lake.")
                if st.button("View location", "7(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/@46.20948,6.150365,13z')

                if st.button("Book now", "77(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g188057-d195979-Reviews-Hotel_d_Angleterre-Geneva.html')


            with col2:


                st.subheader("2. The Omnia, Zermatt")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-switzerland/The_Omnia_Zermatt.jpg?v=1","The Omnia, Zermatt")
                st.write(
                    "The Omnia Mountain Lodge, built against a mountain overlooking the village of Zermatt, is one of "
                    "the top hotels in the world. TripAdvisor named it the best hotel in Switzerland in 2016, ranked it "
                    "sixth in Europe and 19th in the world. There’s a reason for this, starting an elevator ride to the "
                    "rock the lodge sits on, then entering the hotel through a James Bond-style cave and stunning views"
                    " of the Matterhorn. Its Caverne bar is carved into the mountain.")
                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/THE+OMNIA/@46.0203252,7.7433079,17z/data=!3m1!4b1!4m8!3m7!1s0x478f35df2141df13:0x10f4370d5ae3ad96!5m2!4m1!1i2!8m2!3d46.0203164!4d7.7454958')

                if st.button("Book now", "22(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g188098-d619925-Reviews-THE_OMNIA-Zermatt_Canton_of_Valais_Swiss_Alps.html')


                st.subheader(" 4. Ascher Guesthouse")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-switzerland/Ascher_Guesthouse.jpg?v=1","Ascher Guesthouse")
                st.write(
                    "If heights challenge you, better skip the Ascher Guesthouse (Berggasthaus Aescher), but if they "
                    "don’t, you’ll love it here. It’s built into the side of a mountain just below the summit of the "
                    "Appenzell Alps. The dormitory lodge appears to sit precariously on the vertical cliff, but looks "
                    "can be deceiving; it’s been there for 170 years. Access is via a challenging hike and cable car. "
                    "The guesthouse-restaurant, with awesome views, is next to Wildkirchli caves.")
                if st.button("View location", "4(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Aescher+-+Gasthaus+am+Berg/@47.2834461,9.4123794,17z/data=!3m1!4b1!4m5!3m4!1s0x479b24115605fa13:0xd55fdbc28cf47289!8m2!3d47.2834461!4d9.4145734')

                if st.button("Book now", "44(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotels-g198851-Weissbad_Canton_of_Appenzell-Hotels.html')


                st.subheader(" 6. Palace Luzern, Lucerne")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-switzerland/Palace_Luzern.jpg?v=1","Palace Luzern, Lucerne")
                st.write(
                    "Palace Luzern marked a new level of luxury when it opened in Lucerne in 1906: It had en-suite "
                    "bathrooms. Built on the banks of Lake Lucerne, it was stately and elegant. It still is today, "
                    "adding a new distinction in 2015: home to Lucerne’s only fish restaurant. If it’s extravagance "
                    "you’re after, book the Suite of Arts, inspired by such artists as Chagall and Miro, with furnishings"
                    " reminiscent of the ‘60s and ‘70s. Rooms have lake or mountain views.")
                if st.button("View location", "6(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Hotel+Palace+Luzern/@47.05526,8.317013,17z/data=!3m2!4b1!5s0x478ffb916b9cb4d3:0x59fecbe458762cf0!4m8!3m7!1s0x478ffb916d973cfb:0xcd38b97b38c0382f!5m2!4m1!1i2!8m2!3d47.05526!4d8.319207')

                if st.button("Book now", "66(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g188064-d234238-Reviews-Palace_Luzern-Lucerne.html')


                st.subheader("8. Whitepod Hotel")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-switzerland/Whitepod_Hotel.jpg?v=1","Whitepod Hotel")
                st.write(
                    "When you’re a guest at the eco-friendly Whitepod Hotel, you won’t stay in bungalows."
                    " You’ll stay in one of 15 high-tech pods, a snug geometric-shaped stand-alone building "
                    "that is self-contained. It’s like staying in an igloo, only warmer since it has its own"
                    " wood stove. You’ll breathe in crisp mountain air as you make the 20-minute walk from the"
                    " canvas-covered pod to t he dining facilities. In the winter, you’ll have use of a private"
                    " ski run as well as runs elsewhere on the mountain.")

                if st.button("View location", "8(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Whitepod+Eco-Luxury+Hotel/@46.2229734,6.9561554,17z/data=!3m1!4b1!4m8!3m7!1s0x478ebb796f3391c3:0xd67703746ac4de46!5m2!4m1!1i2!8m2!3d46.222972!4d6.9583477')

                if st.button("Book now", "88(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g1113403-d522000-Reviews-Whitepod_Eco_Luxury_Hotel-Monthey_Canton_of_Valais_Swiss_Alps.html')




        if sidbar == 'Best Scenic Small Towns':

            st.title("Most Scenic Small Towns in Switzerland")

            st.write("Switzerland is one great big picture postcard. From border to border, you’ll find gorgeous rugged"
                     " mountain views punctuated with picturesque villages hugging valley floors. It’s a paradise for"
                     " hikers in the summer and skiers in the winter.")
            st.write("The best places to go Swiss are its small towns, which are gateways to this alpine paradise."
                     " But do spend time in these charming villages in Switzerland before taking off for parts unknown.")

            col1, col2 = st.beta_columns(2)

            with col1:


                st.subheader(" 1. Zermatt")
                st.image("https://www.touropia.com/gfx/d/best-places-to-visit-in-switzerland/zermatt.jpg?v=12b04c54013134a6f8e32b5542c24b45","Zermatt")
                st.write("Named after the impressive Mount Mulu, this national park is phenomenal for the wealth of"
                         " amazing scenery and stunning landscapes on show. Remote and relatively inaccessible, the "
                         "only ways to reach it are by plane or by riverboat; it doesn’t matter how you get here "
                         "just as long as you do!")
                st.write("The ancient karst formations are what Gunung Mulu National Park is primarily known as over"
                         " the millennia they have thrown up an incredible array of astounding rock formations. With "
                         "caverns, cliffs and canyons spectacularly cutting their way through the undergrowth of the"
                         " park, the scenery simply needs to be seen to be believed.")
                st.write("Huge caves dot the area and in actual fact Sarawak Chamber is the largest known chamber in "
                         "the world. Stretching forever, the mind boggles at its colossal size. Mesmerizing and unique,"
                         " this national park in Malaysia is definitely worth the effort!")
                if st.button("View location","1(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@46.016666,7.75,13z')

                st.subheader("3. Guarda")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/guarda_switzerland.jpg?v=1"," Guarda")
                st.write("Guarda is another small Swiss town that is noted for its historic architecture, including "
                         "17th homes that have colorfully painted exteriors. It’s called a Schellenursli village"
                         " after a character by that name in a children’s book.")
                st.write("There’s even a path named Schellenursli that is suitable for families to hike together."
                         " If winter blahs get you down here, you can indulge in Guarda’s ancient tradition of "
                         "using cow bells to chase winter away. You can find your way around Guarda with a "
                         "special app that explains what the village is about..")
                if st.button("View location","3(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.775398,10.152542&z=13')


                st.subheader(" 5. Murren")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/murren.jpg?v=ab5d4312646fe2e23a8a160ebaa6e395","Murren")
                st.write("If you’re a fan of James Bond, chances are good you’re familiar with the cable car and "
                         "revolving restaurant on Schilthorn. They were featured in On Her Majesty’s Secret Service "
                         "that was filmed at Murren.")
                st.write("TOr if you loved Heidi books as a child, this traditional Alpine village will remind you"
                         " of her home. Wherever you look in Murren, you’ll see stunning views, from mighty "
                         "mountains like Eiger and Jungfrau to flower-filled meadows.")
                if st.button("View location","5(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.559444,7.892222&z=13')



                st.subheader("7.Wengen")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/wengen.jpg?v=1","Wengen")
                st.write("Wengen, in central Switzerland, may have only 1,300 permanent residents but you"
                         " wouldn’t guess that from the crowds. The popular soars to 5,000 souls in the summer"
                         " who come to hike 310 miles of trails and 10,000 people in the winter who come for the skiing.")
                st.write("Wengen is a popular venue for ski races. This holiday resort has historic homes dating "
                         "to the Belle Epoque era. As you travel by train to Wengen, be on the lookout for"
                         " climbers attempting to go up the north face of Eiger mountain.")
                if st.button("View location","7(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.599998,7.916667&z=13')



                st.subheader(" 9. Morcote")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/morcote.jpg?v=1","Morcote")
                st.write("Morcote is like other small towns in Switzerland: picturesque. But this tiny town of 771"
                         " takes it one step further. Located on the shores of Lake Lugano, Morcote was named "
                         "the most beautiful town in Switzerland in 2016.")
                st.write("The village is famous for its architecture, with an arcade dating back to the Middle Ages."
                         " You’ll also find houses from the 16th century and the 13th century church, Santa Maria del"
                         " Sasso. Also worth visiting is the Botanical and Art Park with its displays of plants and artworks.")
                if st.button("View location","9(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=45.916668,8.916667&z=13')


                st.subheader(" 11. Spiez")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/spiez.jpg?v=1","Spiez")
                st.write("Standing on the shores of Lake Thun, surrounded by vineyards and forests, is the town "
                         "of Spiez. With a 12,000 population, Spiez is best known for its medieval castle with"
                         " its 1,000-year-old Early Romanesque church.")
                st.write("Except for the tall stone tower, the castle, which houses a museum today, might be mistaken"
                         " for a huge white chalet. Many people combine a visit to the castle with a cruise on Lake Thun."
                         " After a day of hiking or fishing, end your day with a glass of Spiezer, the locally made wine")
                if st.button("View location","11(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.683334,7.666667&z=13')



            with col2:

                st.subheader(" 2. Lauterbrunnen")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/lauterbrunnen.jpg?v=d292d9ed8de14ac89a395e4aa2a63ae4","Lauterbrunnen")
                st.write("Waterfalls abound in Lauterbrunnen: This picturesque valley is home to 72 falls that cascade"
                         " down the mountains. The most famous of these is Staubbach Falls, which drops nearly a thousand"
                         " feet, making it one of Europe’s highest waterfalls.")
                st.write("The town itself is a jumping off place for excursions into the Jungfrau region, including "
                         "across the valley to Murren. This tiny picturesque village nestled among the mountains"
                         " provided inspiration to many writers, including Goethe. Walking the valley is a must,"
                         " though more adventurous souls may enjoy sky diving or paragliding.")
                if st.button("View location","2(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.599998,7.900000&z=13')



                st.subheader(" 4.Grindelwald")
                st.image("https://www.touropia.com/gfx/d/tourist-attractions-in-switzerland/grindelwald.jpg?v=31200f8a8a74438751da02807bd77e97","Grindelwald")
                st.write("Grindelwald and Gilbert Grindelwald may bear the same name, but there the resemblance ends."
                         " Gilbert Grindelwald is a dark character in the Harry Potter series, while Grindelwald is"
                         " a picturesque town in the Bernese Alps.")
                st.write("The scenery from here is fantastic and includes north face views of Eiger. Home to the"
                         " largest ski resort in the Jungfrau region, Grindelwald has been a top tourist destination "
                         "since the 18th century. There’s plenty of good hiking in the summer, including the Eiger Trail.")
                if st.button("View location","4(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.616669,8.033333&z=13')



                st.subheader(" 6. Stein am Rhein")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/stein_am_rhein.jpg?v=a5b613cc6e31af08c4c37ecec1fefe62","Stein am Rhein")
                st.write("While visitors may come to Stein am Rhein to view the scenery – it’s on Lake Constance – many "
                         "will come to view the village’s unique architecture. Half-timbered buildings in its well-preserved"
                         " Old Town are enhanced with ornately decorated and colorful facades.")
                st.write("Stein am Rhein was once a Roman fortress, but the village is filled with remarkable buildings"
                         " that came afterward. There’s an early church dedicated to St. John the Baptist, the monastery "
                         "of St. Georgen and a museum that showcases Stein am Rhein life in the 19th century.")
                if st.button("View location","6(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@47.666668,8.85,13z')



                st.subheader(" 8.Interlaken")
                st.image("https://www.touropia.com/gfx/d/best-places-to-visit-in-switzerland/interlaken.jpg?v=24a571daf1ae4594d7145a71e475c14f","Interlaken")
                st.write("Interlaken is the gateway to mountain villages in the Bernase Alps, but it’s worth a visit "
                         "on its own merit. It’s been a tourist destination since the early 1800s when landscape artists,"
                         " including Franz Konig, provided inspiration through their paintings.")
                st.write("Back in those days, visitors came for the spa treatments and to breathe in the crisp mountain"
                         " air. Interlaken is famous for its music festivals. Since it’s located on Lakes Thun and Brienz,"
                         " you’ll want to take a relaxing paddleboat cruise on one (or both) of them.")
                if st.button("View location","8(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.683334,7.850000&z=13')


                st.subheader(" 10. Soglio")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/soglio.jpg?v=c43241a9235ae3aeb0abc776d4e35528","Soglio")
                st.write("Soglio is another small Swiss village with awesome scenery. Wildflowers blossom on hills in "
                         "the summer while snow-capped mountains fill the horizon. Overlooking this stunning scenery is "
                         "Soglio’s chief landmark, the Church of San Lorenzo with its bell tower that stands above the village.")
                st.write("Wander the narrow cobblestone streets to the Palazzo Solis, now a hotel, with its Mediterranean"
                         " ambiance and giant sequoia trees. Bask in the solitude this tiny village begets, especially"
                         " if you are hiking the Bergell trail or through the chestnut forest.")
                if st.button("View location","10(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.333332,9.533333&z=13')



                st.subheader("12. Sion")
                st.image("https://www.touropia.com/gfx/d/small-towns-in-switzerland/sion_switzerland.jpg?v=1","Sion")
                st.write("With 34,000 people, Sion may not be exactly a small town unless, of course, you consider the "
                         "small-town charm it oozes. The capital of Valais, it is a gateway to smaller villages in the "
                         "canton. Sion is known for its sun, mountains and castles.")
                st.write("Two castles – the Castle of Valeria and Castle Tourbillon – sit on mountains overlooking one "
                         "of Switzerland’s oldest cities. Sion has a quaint Old Town where you can sit at a café "
                         "sipping Fendant, a white wine grown here.")
                if st.button("View location","12(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=46.233334,7.366667&z=13')









    if countryselect == 'France':

        st.sidebar.title("...France...")
        st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1280px-"
                         "Flag_of_France.svg.png")
        sidbar = st.sidebar.radio("", ("About", "Beautiful Lakes", "Best Cities", "Beautiful Churches",
                                       "Best National Parks", "Best Resorts"))

        if sidbar == 'About':
            st.title("Welcome to France")

            col11, col22 = st.beta_columns(2)

            with col11:
                st.balloons()
                st.image("https://cdn.travelpulse.com/images/99999999-9999-9999-9999-999999999999/fdd16e7f-0167-"
                         "6524-b1f9-933d7482e71e/630x355.jpg")
                st.write(
                    "For more than two decades, France has reigned as the world’s most popular tourist destination, "
                    "receiving 82 million foreign tourists annual. People from all over the world are drawn "
                    "to France’s "
                    "sophisticated culture, dazzling landmarks, exquisite cuisine, fine wines, romantic chateaux "
                    "and picturesque countryside.")
                st.write(
                    "Located in the central region of Ile-de-France is the capital city, Paris, known for its world "
                    "famous landmarks like the Eiffel Tower, the Louvre Museum and Notre Dame Cathedral. Paris is a "
                    "compact city overflowing with museums, art galleries, boutiques and attractive cafes and bars.")
                st.write(
                    "Exploring the outer regions of France is a must-do to experience the country’s best treasures. "
                    "For example, a trip to Carcassonne offers strolls through a walled medieval city while an "
                    "excursion to the Verdon Gorge offers outdoor adventures like rock climbing, kayaking and rafting. "
                    "The Chamonix Valley presents breathtaking views of the Alps.")

            with col22:
                st.title("")
                st.image("https://images.news18.com/ibnlive/uploads/2021/05/1620749252_untitled-design-4.jpg?"
                         "impolicy=website&width=1200&height=800")
                st.write("")
                st.image("https://cdn.britannica.com/s:300x169,c:crop/42/183642-050-C7D21FE8/World-Data-Loca"
                         "tor-Map-France.jpg")


                if st.button("View location"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/%E0%A4%AB%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A8%E0%A5%8D%'
                            'E0%A4%B8/@45.9205217,-0.6642238,6.26z/data=!4m5!3m4!1s0xd54a02933785731:0x6bfd3f96c747d9'
                            'f7!8m2!3d46.227638!4d2.213749')

            st.video("https://www.youtube.com/watch?v=WeqH6Rt_dGM")
            st.video("https://www.youtube.com/watch?v=AQ6GmpMu5L8")

        if sidbar == 'Beautiful Lakes':
            st.title("10 Beautiful lakes in France......")

            col1, col2 = st.beta_columns(2)

            with col1:

                # Lake1
                st.write("## 1. Lake Annecy")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/lake_annecy.jpg?v=1", caption= "Lake Annecy")
                st.write(
                    "With an atmosphere of gaiety, Lake Annecy in the Savoie region is just made for holiday makers. "
                    "You can stroll or bicycle a paved path along the lake, enjoy a meal at a lakeside café or venture "
                    "out into the water on a rental boat. You can also swim in the lake without fear of "
                    "contaminated water. "
                    "Thanks to strict environmental regulations, Lake Annecy is known as Europe’s cleanest lake; "
                    "visitors give it high marks for water purity. Lake Annecy, one of the largest lakes in France, "
                    "is quite scenic. It’s surrounded by mountains and villages including beautiful Annecy, "
                    "also known as the “Venice of the Alps”.")

                if st.button("View location", "1(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@45.849998,6.166667,13z')

                # Lake3
                st.write("## 3. Lake Geneva")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/lake_geneva_france.jpg?v=1", caption= "Lake Geneva")
                st.write(
                    "Lake Geneva, which separates France and Switzerland, is stunner. Its deep blue water ripples in "
                    "some places, while at others it is as smooth as glass. And, always, it is surrounded by the Alps. "
                    "The largest lake on the Rhone River and one of the largest in western Europe, Lake Geneva is "
                    "popular with rowers and yacht racers. Cruise the lake to see the medieval castle of Chateau "
                    "de Challon, quaint towns, vineyards and French villas on its shores. Be on the lookout for "
                    "celebrities since many have holiday hideouts here.")

                if st.button("View location", "3(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@46.4316361,6.5481983,12.22z')

                # Lake5
                st.write("## 5. Lac du Bourget")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/lac_du_bourget.jpg?v=1", caption= "Lac du Bourget")
                st.write(
                    "Lac du Bourget is an elongated lake that is considered the deepest lake within French borders. "
                    "Formed by glacial action 19,000 years ago, Lac du Bourget is surrounded by mountains "
                    "(it’s in the Savoie Mont Blanc region) on one side and towns on the other. "
                    "A good place to view the lake is from Dent du Chat, reached by driving up to Relais and the "
                    "walking to the viewpoint. Biking and hiking around the lake are popular activities. Or, "
                    "you and your kids can roller-skate along the east coast. Lac du Bourget has a nice "
                    "beach with views of the Alps.")

                if st.button("View location", "5(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=45.733334,5.866667&z=13')

                # Lake7
                st.write("## 7.  Lac du Mont Cenis")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/lac_du_mont_cenis.jpg?v=06d59fd0737347a"
                         "302cac935784242dc", caption= "Lac du Mont Cenis")
                st.write("Lac du Mont Cenis is an alpine lake located in the shadow of Mont Cenis. It lies entirely "
                         "within France, but is near the border with Italy. Though it wasn’t a lake then, Lac du Mont "
                         "Cenis lies on a route that was a major way between Western Europe and Italy during the "
                         "Middle Ages. The lake, with its pretty blue waters, is artificial, created when a "
                         "hydroelectric dam was constructed at Mont Cenis. It is one of the largest reservoirs in "
                         "France. The lake is noted for its vegetation, with some plant species found only here.")

                if st.button("View location", "7(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@45.260277,6.900833,13z')

                # Lake9
                st.write("## 9. Gaube Lake")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/gaube_lake.jpg?v=1", caption= "Gaube Lake")
                st.write(
                    "Gaube Lake is the lake so nice, they named it twice. Gaube translates as “lake” in Gascon, "
                    "so this pretty lake is actually named Lake Lake. Located in the French Pyrenees, Gaube Lake is "
                    "surrounded by the chain’s highest mountains, which hover over its glacial blue water. Most people "
                    "come here for the panoramic views, especially of Vignemale, the highest peak in the French "
                    "Pyrenees. It takes about an hour to hike into this small alpine lake, but you can do it quicker "
                    "if you take a cable car from the Bridge of Spain.")

                if st.button("View location", "9(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=42.831139,-0.139732&z=13')

            with col2:

                # Lake2
                st.write("## 2. Lac de Serre-Poncon")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/lac_de_serre_poncon.jpg?v=7a"
                         "2a04959889154c20d3e77e5ed2b7d5", caption= "Lac de Serre-Poncon")
                st.write(
                    "When you drive along Lac de Serre-Ponçon in southeastern France you’ll see craggy mountains "
                    "dropping steeply into the water. In other places, you’ll see gentle hills rolling into this "
                    "man-made lake. One of Europe’s largest artificial lakes, Lac de Serre-Ponçon was created in the "
                    "1960s as part of a flood control project. Alas, some villages were flooded to make way for the "
                    "lake. Camping is allowed along the lake, which is popular with swimmers, windsurfers and sailing "
                    "enthusiasts. Past visitors recommend avoiding this lovely lake in September because the "
                    "weather is so unpredictable.")

                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@44.516666,6.35,13z')



                # Lake4
                st.write("## 4. Lac de Sainte Croix")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/lac_de_sainte_croix.jpg?v=37243e4"
                         "cafdd3728607bfdd3e52928a6", caption= "Lac de Sainte Croix")
                st.write(
                    "France’s third largest lake hasn’t been around for eons like many other French lakes. Indeed, "
                    "it dates back only to 1973 when the Sainte Croix dam was built across the Verdun River. "
                    "There’s nothing artificial about this lake, however. It’s just as pretty as its little sisters. "
                    "Lac de Sainte Croix, surrounded by hills and forests, has sandy beaches with swimming area; "
                    "lifeguards are on duty, too. The lake is a popular place to kayak, sail or windsurf. Unless "
                    "they’re sail or human-powered water craft, only boats with electric motors are "
                    "allowed on the lake.")

                if st.button("View location", "4(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@43.7666915,6.1788952,13.52z')

                # Lake6
                st.write("## 6. Lac d'Aiguebelette")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/lac_daiguebelette.jpg?v=1", caption= "Lac d'Aiguebelette")
                st.write(
                    "Lac d’Aiguebelette has been described as an “emerald pearl,” which is fitting since the name "
                    "translates as “beautiful little waters.” The blue-green lake oozes tranquility, but don’t let "
                    "appearances fool you. Rowing competitions have been held here. Lac d’Aiguebelette is one of "
                    "France’s largest natural lakes, boasting two islands and several hot springs. Like many lakes, "
                    "this one has a legend attached to it. One day Jesus Christ, disguised as a beggar, showed up "
                    "asking for help. No one would help him but one woman. The next day, Jesus flooded "
                    "the village with "
                    "lake water, leaving only the woman and her daughter’s houses unscathed.")

                if st.button("View location", "6(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@45.552776,5.797222,13z')

                # Lake8
                st.write("## 8. Lac de Capitello")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/lac_de_capitello.jpg?v=f60"
                         "2496ad4683c27145f9790bf038dde", caption= "Lac de Capitello")
                st.write(
                    "Lac de Capitello is Corsica’s contribution to France’s list of pretty lakes. "
                    "It’s a small circular "
                    "alpine lake surrounded by craggy mountains in the Restonica Valley. It is Corsica’s deepest lake "
                    "and a good place to savor the scenic deep blue water. A visit to Lac de Capitello is usually "
                    "combined with a visit to Lac de Melo. Lac de Capitello is about an hour’s hike beyond Melo; "
                    "this route is more challenging than the trek to Melo. Once at Capitello, you’ll pretty much "
                    "have the lake to yourself since only about 1,200 people make the trip during the summer.")

                if st.button("View location", "8(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=42.212502,9.011944&z=13')

                # Lake10
                st.write("## 10. Lac du Salagou")
                st.image("https://www.touropia.com/gfx/d/lakes-in-france/lac_du_salagou.jpg?v=1", caption= "Lac du Salagou")
                st.write(
                    "Mother Nature didn’t decide when, where or how Lac du Salagou would be created in southern "
                    "France’s Languedoc region. Man did. The lake is a reservoir created when the Salagou River was "
                    "dammed in the 1960s. The lake presents a pretty picture for visitors since the blue water "
                    "contrasts nicely with the reddish orange soil that surrounds it. You can drive around the lake, "
                    "but if you have time, you gain a better appreciation of its beauty by walking or "
                    "biking around it. "
                    "The lake is surrounded by hills, with tidy fields behind it. The lake is popular "
                    "with visitors who "
                    "like to sunbathe au naturel.")

                if st.button("View location", "10(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=43.641701,3.420200&z=13')

        if sidbar == 'Best Cities':

            st.title("15 Best Cities to Visit in France......")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1. Paris")
                st.image("https://www.touropia.com/gfx/b/2018/06/paris.jpg", caption= "Paris")
                st.write(
                    "With some of the most recognizable buildings and monuments in the world, Paris is a must-see city "
                    "to visit, with a never-ending array of things to see and do. Situated on the banks of La Seine, "
                    "the elegant and stylish capital of France is a romantic place, with lovely boulevards, beautiful "
                    "buildings, and sights like the Eiffel Tower and gleaming Sacre-Coeur rising towards the heavens. "
                    "Renowned for its cuisine, Paris has a plethora of restaurants to choose from – watch out though, "
                    "it is very easy to spend a lot of money in a short amount of time.")
                st.write(
                    "From the stunning art collections at the Louvre to the eerie catacombs beneath "
                    "the streets and the "
                    "breath taking Notre-Dame Cathedral, you could spend a lifetime getting to know "
                    "all of Paris´ wonderful sights.")

                if st.button("View location", "1(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@48.856701,2.3508,13z')

                st.write("## 3. Nice")
                st.image("https://www.touropia.com/gfx/d/things-to-do-in-the-french-riviera/nice.jpg?v=1", caption= "Nice")
                st.write(
                    "Located on the French Riviera, or Cote d´Azur, as it is known in French, Nice is "
                    "constantly bathed "
                    "in sunshine. As the fifth largest city in France, it has a vibrant mix of cultures. Because it is "
                    "a port city, Nice has a gritty side to it, which contrasts with its Italian inspired "
                    "architecture and the medieval streets of the old town.")
                st.write(
                    "Walking along the famous Promenade des Anglais and gazing out over the turquoise waters is simply "
                    "heavenly. For a great view of the city and the shimmering Mediterranean Sea below, head to the "
                    "Colline du Chateau. A charming place to spend some time, Nice has something for everyone, as it "
                    "combines city life with a beautiful setting.")

                if st.button("View location", "3(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@43.7034,7.2663,13z')

                st.write("## 5. Bordeaux")
                st.image("https://www.touropia.com/gfx/b/2018/06/bordeaux.jpg", caption= "Bordeaux")
                st.write(
                    "Straddling the banks of the Garonne River, Bordeaux is a large city with a lot to offer. "
                    "Its impressive old town is delightful to walk around, and the architecture on show is ravishing. "
                    "Surrounding Place de la Bourse, you can find 18th century mansions rubbing "
                    "shoulders with decadent "
                    "palaces, as well as a number of great art museums.")
                st.write(
                    "With a modern feel to it, Bordeaux has a thriving university community. In recent years, a number "
                    "of vintage shops have sprung up. For a great walk, head to Les Quais and gaze out over the waters "
                    "of the river – at night, the view of the city lights from the Napoleonic-era Pont de Pierre is "
                    "magical. Home to some of the best wines in the world, make sure to give them a "
                    "taste before you head off.")

                if st.button("View location", "5(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@44.8386,-0.5783,13z')

                st.write("## 7. Lyon")
                st.image("https://www.touropia.com/gfx/b/2018/06/lyon.jpg", caption= "Lyon")
                st.write(
                    "Lyon, the third largest city in the country, is located where the Rhone and Saone Rivers join. "
                    "Its strategic location has enabled it to attract merchants and industries to the city ever since "
                    "it was founded by the Romans in 43 BC.")
                st.write(
                    "An orderly and sophisticated place, renaissance buildings dot its streets. Lyon seamlessly mixes "
                    "the new with the old, with a rich cultural heritage that encompasses gastronomic delights and "
                    "fine architecture. Lyon Cathedral is one of the most impressive sights, and the old town is "
                    "lovely to walk around. Make sure to try some of the sumptuous cuisine before "
                    "you continue on your way.")

                if st.button("View location", "7(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@45.759701,4.8422,13z')

                st.write("## 9. Marseille")
                st.image("https://www.touropia.com/gfx/b/2018/06/marseille.jpg", caption= "Marseille")
                st.write(
                    "France´s second city is a diverse melting pot of people and cultures that all "
                    "call Marseille their "
                    "home. Traditionally thought of as grimy and a bit run-down, this bustling port city has undergone "
                    "something of a renaissance in recent years, though its primary attractions remain the same.")
                st.write(
                    "The old harbor, for instance, is a magical setting from which to watch fishermen returning to "
                    "shore with their catch. It is the heart of Marseille, and you´ll really get a feel for the city "
                    "here. The oldest neighborhood, Le Panier, is definitely worth checking out, as is the stunning "
                    "Notre Dame de Major cathedral that overlooks the sea.")

                if st.button("View location", "9(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@43.296398,5.37,13z')

                st.write("## 11. Nantes")
                st.image("https://www.touropia.com/gfx/d/best-cities-to-visit-in-france/nantes.jpg?v=1", caption= "Nantes")
                st.write(
                    "Situated on the banks of the Loire, Nantes´ long and tumultuous history has seen the city "
                    "constantly reinvent itself. As such, it has numerous sites from different "
                    "epochs that entice visitors to its shores.")
                st.write(
                    "As the historic capital of Brittany, Nantes´ old medieval center, with its cathedral and castle, "
                    "is enchanting to explore. In recent years, it has developed a thriving student body that gives "
                    "the city its energetic vibe. An incredible and unique attraction to visit is the Machines "
                    "de l´Ile – a fantastical and futuristic exhibition of giant mechanical animals.")

                if st.button("View location", "11(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=47.218102,-1.552800&z=13')

                st.write("## 13. Strasbourg")
                st.image("https://www.touropia.com/gfx/b/2018/06/strasbourg.jpg", caption= "Strasbourg")
                st.write(
                    "Capital of Alsace, Strasbourg has a stunning historical center and occupies "
                    "a strategic setting on "
                    "the west bank of the Rhone. Consequently, it has been fought over by France "
                    "and Germany throughout its long history.")
                st.write(
                    "Now, however, the glassy European Union buildings glitter in the sun and, along with the teeming "
                    "student body, help to give a modern air to this ancient city. The gothic cathedral is simply "
                    "stunning to behold, as is the delightful La Petite France that is home to the old part of town.")

                if st.button("View location", "13(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@48.5844,7.7486,13z')

                st.write("## 15. Biarritz")
                st.image("https://www.touropia.com/gfx/b/2018/06/biarritz.jpg", caption= "Biarritz")
                st.write(
                    "Formerly a playground for the rich and famous, this seaside resort now attracts families, "
                    "surfers and sun-worshippers alike. Situated in the Pyrenees-Atlantiques, Biarritz´s town center "
                    "lies on the Bay of Biscay, and is famed for its beautiful coast and excellent beaches, which are "
                    "its main attraction. While the town is not the most picturesque to look at, its great location "
                    "right next to the water more than makes up for that slight downfall.")

                if st.button("View location", "15(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@43.481701,-1.5561,13z')

            with col2:


                st.write("## 2. Avignon")
                st.image("https://www.touropia.com/gfx/d/best-places-to-visit-in-the-provence/avignon.jpg?v=1", caption= "Avignon")
                st.write(
                    "Famous for the popes that set up shop in the city after fleeing Rome in the 14th century, "
                    "Avignon was the capital of the Catholic Church for a period during the Middle Ages. "
                    "The colossal palace that the popes built is impressive for its size and Gothic architecture, "
                    "while the ramparts, towers and gates that line the old town are also fantastic to view.")
                st.write(
                    "The old part of the city is beautifully enclosed by the River Rhone that "
                    "snakes its way around it. "
                    "A great time to visit is during the art festival in July, though you will have to battle your "
                    "way through the crowds at this popular destination.")

                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@43.950001,4.81,13z')

                st.write("## 4. Annecy")
                st.image("https://www.touropia.com/gfx/d/tourist-attractions-in-france/annecy.jpg?v=1", caption= "Annecy")
                st.write(
                    "Located in the north of the Alps, Annecy´s proximity to Geneva, along with its historic city "
                    "center, make it a popular day-trip among tourists. Also known as the ´Venice of Savoie´, quaint "
                    "canals crisscross Annecy and weave their way between its ancient buildings.")
                st.write(
                    "Lying on the shores of Lake Annecy, the city´s surroundings are stunning, and visitors can hike, "
                    "bike or swim in the nearby natural attractions. With a 14th century castle located in the center, "
                    "it´s a picturesque and memorable place to visit, though it can get a bit too crowded in summer.")

                if st.button("View location", "4(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@45.916,6.133,13z')

                st.write("## 6. Colmar")
                st.image("https://www.touropia.com/gfx/d/underrated-destinations-in-france/colmar."
                         "jpg?v=cdba7df5f553632e3c3bb9b33b2b21ea", caption= "Colmar")
                st.write(
                    "Situated in the Alsace region, Colmar´s proximity to Germany has meant that it has changed hands "
                    "numerous times between the two nations over the course of its history. Tourists flock to the city "
                    "for its stunning old town that so perfectly combines weaving cobblestone alleys with delightful "
                    "canals, and the distinctive houses that line its streets.")
                st.write(
                    "Churches and museums are dotted around the place, and the Isenheim Altarpiece is particularly "
                    "impressive to behold. As it is in the wine region, take the time to sample some of the best wines "
                    "that Colmar has to offer.")

                if st.button("View location", "6(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@48.081699,7.3556,13z')

                st.write("## 8. La Rochelle")
                st.image("https://www.touropia.com/gfx/d/best-cities-to-visit-in-france/la_rochelle.jpg?v=1", caption= "La Rochelle")
                st.write(
                    "Nicknamed the ´White City,´ due to its limestone edifices that are so beautifully illuminated at "
                    "night, La Rochelle is a charming place to visit. Once an important seaport in centuries gone by, "
                    "the old port, historic center and picturesque waterfront are reason enough to visit La Rochelle. "
                    "With a huge marina at Port des Minimes, and sandy beaches in the vicinity, it´s a nice laidback "
                    "place to spend some time.")

                if st.button("View location", "8(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@46.1591,-1.1517,13z')

                st.write("## 10. Ajaccio")
                st.image("https://www.touropia.com/gfx/d/best-cities-to-visit-in-france/ajaccio.jpg?v=1", caption= "Ajaccio")
                st.write(
                    "Located on the lovely Mediterranean island of Corsica, Ajaccio – its capital city – is worth "
                    "stopping by, even if only to use it as a base from which to explore the beautiful landscapes "
                    "surrounding it.")
                st.write(
                    "The old town itself has some nice streets to wander around, while the harbor surrounding it "
                    "conjures up images of the Cote d´Azur. Famed as the birthplace of Napoleon, Ajaccio is "
                    "pleasant enough to visit without setting the world alight.")

                if st.button("View location", "10(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@41.926701,8.7369,13z')

                st.write("## 12. Rouen")
                st.image("https://www.touropia.com/gfx/d/best-places-to-visit-in-normandy/rouen.jpg?v=1", caption= "Rouen")
                st.write(
                    "The city where Joan of Arc was burned at the stake is a pleasant contrast to this violent event, "
                    "and a picturesque place to wander around. The old town is full of restored medieval "
                    "buildings constructed from wattle and daub. Situated on the banks of the Seine, one sight stands "
                    "alone when it comes to visiting Rouen: that of the majestic cathedral that dominates the center. "
                    "Dating all the way back to the 4th century it encompasses an eclectic mix of architectural "
                    "styles – inspiring Monet to create over thirty paintings of it.")

                if st.button("View location", "12(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@49.439999,1.1,13z')

                st.write("## 14. Toulouse")
                st.image("https://www.touropia.com/gfx/d/underrated-destinations-in-france/toulouse."
                         "jpg?v=1583146aad94b9fe752bae105e31f36b", caption= "Toulouse")
                st.write(
                    "The fourth largest city in the country, Toulouse is a lively place, in part thanks to its huge "
                    "university community. With bustling markets, a vibrant music scene and a penchant for the "
                    "alternative, there are different sides to Toulouse – the old town remains a peaceful and "
                    "picturesque place to wander around.")
                st.write(
                    "Nicknamed ´the Pink City´ due to its rose-colored buildings, a lovely way to see Toulouse is to "
                    "go on a boat trip along the Canal du Midi or Garonne River that frame the center.")

                if st.button("View location", "14(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps?ll=43.604500,1.444000&z=13')

            st.write("# ---Map of cities in France---")
            st.image("https://www.vhv.rs/dpng/d/590-5904798_france-cities-map-giverny-on-map-of-france.png")

        if sidbar == 'Beautiful Churches':
            st.title("10 Beautiful Churches in France......")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1. Chartres Cathedral")
                st.image("https://www.touropia.com/gfx/d/gothic-cathedrals/chartres_cathedral."
                         "jpg?v=bda90b7402cb42f3ed2d7ce51ae1d18a", caption= "Chartres Cathedral")
                st.write("In 1194, construction began on the Chartres Cathedral. This incredible building, constructed "
                         "in the Gothic style, is considered to be one of the most important pieces of architecture "
                         "in France. The colorful stained glass windows are preserved well, and two different spires "
                         "compete for attention on the roof of the cathedral. Although the exterior is phenomenal, "
                         "don’t miss the artworks and relics found inside, such as the dress that was allegedly "
                         "worn by Mary when she gave birth to Jesus.")

                if st.button("View location", "1(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@48.447224,1.487778,18z')

                st.write("## 3. Notre Dame de Paris")
                st.image("https://www.touropia.com/gfx/d/gothic-cathedrals/notre_dame_de_paris."
                         "jpg?v=2ec548b2f101bb860a486158294f4055", caption= "Notre Dame de Paris")
                st.write(
                    "France’s most famous cathedral is the Notre Dame de Paris, which was constructed starting in the "
                    "middle of the 12th century. The jewel of Parisian architecture, Notre Dame de Paris is undeniably "
                    "Gothic in style, and it boasts an incredibly large size. Its flying buttresses were among the "
                    "first in the world, and many gargoyles were used not just for design but for column supports and "
                    "even water spouts. You’ll absolutely want to tour the cathedral, but make time to also see the "
                    "extensive crypts underneath the church that are open to the public.")

                if st.button("View location", "3(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@48.853001,2.3498,18z')

                st.write("## 5. Amiens Cathedral")
                st.image("https://www.touropia.com/gfx/d/churches-in-france/amiens_cathedral.jpg?v=1", caption= "Amiens Cathedral")
                st.write(
                    "Just two hours outside of Reims is Amiens, home to the Cathedral of Amiens. When the Reims "
                    "Cathedral was unveiled, the population of Amiens wanted something similar. So, in the 13th "
                    "century, the French Gothic Cathedral of Amiens was constructed. It is just slightly taller "
                    "than the one in Reims, an intentional part of the planning process. Impressive cantilevers "
                    "create a high ceiling for the nave, making it an incredible structure to behold from the "
                    "interior. Detailed carvings of saints, many of which have been intricately painted, are "
                    "just one more reason to explore this beautiful cathedral in France.")

                if st.button("View location", "5(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@49.895,2.302222,18z')

                st.write("## 7. Reims Cathedral")
                st.image("https://www.touropia.com/gfx/d/gothic-cathedrals/reims_cathedral.jpg?v=1", caption= "Reims Cathedral")
                st.write(
                    "Over 800 years ago, construction began on Reims Cathedral. Today, the cathedral is a stunning "
                    "example of Gothic architecture and serves as the biggest attraction in the city of Reims. "
                    "It was in this very cathedral that many French kings had their coronations, and records show "
                    "that even Joan of Arc was in attendance at one of these ceremonies in the 15th century. "
                    "With multiple chapels and the first ever use of bar tracery in France, it took nearly a "
                    "century to complete the Reims Cathedral.")

                if st.button("View location", "7(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@49.253613,4.034167,18z')

                st.write("## 9. Mont Saint Michel Abbey")
                st.image("https://www.touropia.com/gfx/d/churches-in-france/mont_saint_michel_abbey.jpg?v=1", caption= "Mont Saint Michel Abbey")
                st.write(
                    "Part of the appeal and beauty of the Mont Saint Michel Abbey owes to its location. "
                    "The island of Mont Saint Michel is just half a mile off the coast near Normandy, making access "
                    "limited. Approaching the island, you’ll see the abbey rise from the water, occupying a large "
                    "portion of the island itself. Built in the 15th century, and still home to Benedictine monks, "
                    "the abbey is surrounded by quaint streets, shops, cafes and museums devoted to the island and "
                    "its history.")

                if st.button("View location", "9(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@48.635834,-1.511389,18z')

            with col2:


                st.write("## 2. Notre Dame de la Garde")
                st.image("https://www.touropia.com/gfx/d/things-to-do-in-marseille/notre_dame_de_la_garde.jpg?v=1", caption= "Notre Dame de la Garde")
                st.write(
                    "The port city of Marseille is home to the incredible Notre-Dame de la Garde, a cathedral honoring "
                    "the patron saint of sailors. The Roman Catholic Cathedral was built on the ruins of an ancient "
                    "fort in the 19th century, and it was created in the Byzantine Revival style. Inside, don’t miss "
                    "the chance to see the iconic Madonna and Child statue sculpted from copper and covered in "
                    "brilliant gold leaf as well as the impressive belfry and the stone arches.")

                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@43.284027,5.371111,18z')

                st.write("## 4. Saint Michel d'Aiguilhe")
                st.image("https://www.touropia.com/gfx/d/churches-in-france/saint_michel_daiguilhe.jpg?v=1", caption= "Saint Michel d'Aiguilhe")
                st.write(
                    "Getting to the Saint Michel d’Aiguilhe is a challenge in and of itself. This amazing church is "
                    "perched on a rocky point, and to reach it you’ll have to climb 268 steep steps carved right into "
                    "the rock face. The climb is well worth the effort, however, because you’ll get the chance to "
                    "see the sacred brick and rock building constructed in the middle of the 10th century. "
                    "The church looks incredible from below, but getting to the top also provides stunning vistas "
                    "over the French landscape and the city of Aiguilhe.")

                if st.button("View location", "4(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@45.049999,3.8825,18z')

                st.write("## 6. Sacre-Coeur")
                st.image("https://www.touropia.com/gfx/d/tourist-attractions-in-paris/sacre_coeur.jpg?v=1", caption= "Sacre-Coeur")
                st.write(
                    "The Basilica of Sacré-Coeur in Paris is one of the most well-known churches in France. To start, "
                    "it has an imposing presence, thanks to its location on a hill perched about the trendy, "
                    "artsy Montmartre district. It was designed in the Romano-Byzantine style, and it is remarkably "
                    "similar to the famed Hagia Sophia Cathedral in Istanbul. One of the top features of the "
                    "Sacré-Coeur is the enormous mosaic of Jesus, and the inclusion of his golden heart.")

                if st.button("View location", "6(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@48.886696,2.343,18z')

                st.write("## 8. Rouen Cathedral")
                st.image("https://www.touropia.com/gfx/d/churches-in-france/rouen_cathedral.jpg?v=1", caption= "Rouen Cathedral")
                st.write(
                    "The city of Rouen is sometimes called the City of a Thousand Spires because it is home to so "
                    "many churches. However, one stands out among the rest: Rouen Cathedral. This enormous, towering "
                    "cathedral is the tallest in all of France. Listen for the hourly bells on the giant 56-bell "
                    "carillon, admire the incredible Bookseller’s Stairway and spot the statues of saints "
                    "filling the interior walls of the Rouen Cathedral.")

                if st.button("View location", "8(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@49.440201,1.095,18z')

                st.write("## 10. Monolithic Church of Saint-Jean")
                st.image("https://www.touropia.com/gfx/d/churches-in-france/monolithic_church_of_saint_"
                         "jean.jpg?v=04b4a24f0711cf04aa8e8dedb622f3c6", caption= "Monolithic Church of Saint-Jean")
                st.write(
                    "The town of Aubeterre-sur-Dronne is small and picturesque, with traditional architecture and "
                    "quaint homes. The most incredible attraction in Aubeterre-sur-Dronne, however, is actually "
                    "underground. The Monolithic Church of Saint-Jean is carved almost entirely from limestone. "
                    "Built in the 7th century and greatly enlarged in the 12th century, the church has a vaulted "
                    "nave, a baptismal pool and dozens of ancient coffins. It is far from the traditional picture "
                    "of a French church, but this unique religious structure is truly one of a kind.")

                if st.button("View location", "10(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@45.27216,0.171102,18z')

        if sidbar == 'Best National Parks':

            st.title("10 Most Beautiful National Parks in France")

            st.write("From its beautiful beaches in the south to the indomitable Alps and rustic roving countryside; "
                     "France has an incredible array of natural sights that are sure to astound and entice visitors to "
                     "this marvelous country and that’s without even mentioning its stunning overseas territories!")
            st.write("With fantastic cities such as Paris, Lyon and Bordeaux to explore, there are a plethora of "
                     "things to see and do in France and one could spend months taking in all the sights on offer. "
                     "One of the most popular countries in the world for tourists, France will continually delight "
                     "and enamour visitors who are sure to revel in its historical sites, world-renowned cuisine and "
                     "vibrant cultural heritage. To help you out on your trip, here are all ten national parks in "
                     "France for you enjoy.")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1. Reunion National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/reunion_national_"
                         "park.jpg?v=64068a78618ed06b10d0f63378f3a898", caption= "Reunion National Park")
                st.write("Phwoar. This idyllic island is an absolute dream to visit and lucky tourists will never "
                         "want to leave such is the natural beauty on offer. Located in the Indian Ocean, this "
                         "national park in the French overseas territory of La Reunion has a volcanic "
                         "landscape that is home to a variety of ecosystems.")
                st.write("Consequently, it is a biodiversity hotspot and is popular with hikers and mountaineers due "
                         "to the extensive paths and routes that weave their way through the mountainous region. "
                         "With rainforests, dazzling waterfalls and an abundant range of fauna and flora also on "
                         "offer, nature lovers will adore this special place.")

                if st.button("View location", "1(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@-21.15,55.5,13z')

                st.write("## 3. Guadeloupe National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/guadeloupe_national_"
                         "park.jpg?v=f481247b628ac1672af001659aea4b6f", caption= "Guadeloupe National Park")
                st.write("This biodiversity hotspot is fascinating to visit for all of the amazing things there are to "
                         "see and do although it certainly is quite the trip from mainland France! "
                         "Situated in the Caribbean, this national park is well worth visiting if you have the "
                         "chance as the tropical rainforest and impressive massif of the mountains are home "
                         "to a wide array of mammals, birds and insects.")
                st.write("Beautiful to behold, amidst the dense and steamy undergrowth are a number of mesmerizing "
                         "waterfalls for you to discover. On the slopes of La Soufriere volcano for instance, there "
                         "are the Carbet Falls – a series of waterfalls that plunge great depths with pristine "
                         "tropical foliage surrounding them on either side. Hiking here is spectacular and the "
                         "sounds of the rainforest will echo in your ears long after you have left this "
                         "earthly paradise.")

                if st.button("View location", "3(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@16.083332,-61.683334,13z')

                st.write("## 5. Mercantour National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/mercantour_national_park.jpg?v=1",
                         caption= "Mercantour National Park")
                st.write("With seven rolling valleys to explore, rustic villages, mountain peaks and more; Mercantour "
                         "National Park certainly has a lot going for it. Fauna and flora abounds and amidst all of "
                         "the nature on show, marmots, ibex and chamois can be found when walking along the park´s "
                         "many trails and paths.")
                st.write("Adventurous visitors may dare to hang-glide and throw themselves off of one of the steep "
                         "cliff faces to dazzle at the world below. History lovers on the other hand will want to "
                         "head to the Vallee des Merveilles where there are over 36,000 rock engravings to delight in.")

                if st.button("View location", "5(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@44.142776,7.1275,13z')

                st.write("## 7. Ecrins National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/ecrins_national_"
                         "park.jpg?v=7a2a04959889154c20d3e77e5ed2b7d5", caption= "Ecrins National Park")
                st.write("This massive national park is so large that it has over a hundred mountain peaks contained "
                         "within it as well as sixty lakes that so beautifully reflect the mountains above them. "
                         "The landscapes on offer are to die for such is their splendor and magnificence.")
                st.write("Centered around the Massif des Ecrins, it is these lofty realms which are part of the "
                         "Dauphine Alps that form the main body of the incredible scenery and mountaineers and "
                         "hikers will adore all that there is to see and do. The forested valleys and green slopes "
                         "of the mountains eventually give way to rocky mountainside and snow amidst the higher "
                         "realms of the peaks.")

                if st.button("View location", "7(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@44.855831,6.263611,13z')


                st.write("## 9. Calanques National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/calanques_national_"
                         "park.jpg?v=8ab905b4b8f1202e8b84a4dfc9d5b0c1", caption= "Calanques National Park")
                st.write("Lying between Marseille and Cassis, this coastal park has a picturesque albeit slightly "
                         "daunting clifftop walk which hikers will adore. Following the at times treacherous path, "
                         "you weave your way amidst the rock-strewn terrain as the cliff face plunges away to the "
                         "side of you. Below, the glistening turquoise waters only add to the stunning scenery "
                         "on show.")
                st.write("The rugged white cliffs and craggy rock faces have delightful tufts of green growing from "
                         "them and the vivid colors make this a delightful part of the world to explore. Sailing "
                         "along the Calanques Massif which gives the national park its name is awe-inspiring and "
                         "in the protected waters, dolphins and turtles can be found swimming about.")

                if st.button("View location", "9(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@43.216667,5.466667,13z')

            with col2:

                st.write("## 2. Vanoise National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/vanoise_national_"
                         "park.jpg?v=d312439a111096b638ac60b397ef1dff", caption= "Vanoise National Park")
                st.write("The largest national park in mainland France is a marvel to visit due to the incredible "
                         "scenery on offer. Located in the French Alps, it is the heart achingly beautiful mountains "
                         "that are the main attraction and hikers, mountaineers and skiers will never want to leave "
                         "its astounding premises.")
                st.write("La Vanoise offers up the quintessential image of the French Alps with the domineering "
                         "mountains, sweeping valleys and gorgeous lakes all contributing to the picture-perfect "
                         "scenes. The panoramas and views are endless and up amidst the clouds, the world below "
                         "appears to be in miniature. The Grand Casse is the highest peak in the park and with the "
                         "massif surrounding it, it is awe-inspiring to behold.")

                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@45.333332,6.833333,13z')

                st.write("## 4. Guiana Amazonian National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/guiana_amazonian"
                         "_national_park.jpg?v=1", caption= "Guiana Amazonian National Park")
                st.write("Established to protect the Amazon rainforest located in French Guiana, this expansive "
                         "national park is one of the largest in the world and as such there is an unfathomable number "
                         "of things to see and do. Undeveloped, untouched and consequently pristine, wild and free, "
                         "this remote part of the world is only accessible by plane or pirogue.")
                st.write("The dense rainforest is home to a wide array of animals and birds, not to mention the fauna "
                         "and flora that proliferates absolutely everywhere. From the overgrowth, Mount Galbao "
                         "rears up dramatically towards the heavens while rivers course between the endless trees.")

                if st.button("View location", "4(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@2.838333,-53.772221,13z')

                st.write("## 6. Pyrenees National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/pyrenees_national_"
                         "park.jpg?v=e474eb59a24fda7bc63b44ff13c5e495", caption= "Pyrenees National Park")
                st.write("Simply spectacular. This incredible national park has a plethora of beautiful views and "
                         "panoramas just waiting for you to discover. Located on the border between France and Spain, "
                         "the park is named after the mountain range that dominates its area and there are "
                         "certainly an amazing array of landscapes for you to enjoy.")
                st.write("Your spirit will soar, free and unencumbered by the worries of the world you can let go and "
                         "revel in the unforgettable scenery all around you. Picturesque and perfect in their beauty "
                         "the mountains rear dramatically about you and their snow-capped peaks dominate the skyline. "
                         "As such, there are a myriad of lovely trails and climbing routes for you to explore and it "
                         "is also possible to go skiing in the higher echelons of the mountains.")
                st.write("Pyrenees National Park is definitely well worth a visit as the greens of the valleys give "
                         "way to the grey rocks of the mountainside which in turn changes to dazzling white snow "
                         "and beautiful blue skies.")

                if st.button("View location", "6(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@42.827499,-0.175833,13z')

                st.write("## 8. Port-Cros National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/port_cros_national_park.jpg?v=1", caption= "Port-Cros National Park")
                st.write("Located in the Mediterranean, this delightful national park is situated on the island of "
                         "Port-Cros that gives it its name. Three neighboring small islands are also included within "
                         "its boundaries and their serene turquoise waters welcome you into their warm embrace.")
                st.write("The beige rocks and sandy beaches that line the islands´ shores stand out beautifully "
                         "between the green fauna of their interiors and the blues waters that surround them. "
                         "The maritime waters around the national park are protected as are the fragile ecosystems of "
                         "the islands themselves and tourism is strictly managed to ensure the environments remain "
                         "in pristine condition.")
                st.write("Arriving by boat is a memorable affair as the idyllic islands appear in the distance before "
                         "you, slowly growing in size until finally they are right there in front of you in all "
                         "of their glory.")

                if st.button("View location", "8(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@43.004166,6.395278,13z')

                st.write("## 10. Cevennes National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-france/cevennes_national_"
                         "park.jpg?v=7bcd79e863547e9833b79aace39471b8", caption= "Cevennes National Park")
                st.write("With a wide variety of different landscapes on offer, Cevennes National Park makes for some "
                         "delightful hiking as the scenes slowly merge into each other and change before your very "
                         "eyes. The array of mountains and plateaus located within the park have rolling valleys and "
                         "hills that fall away from their peaks and these are beautiful to behold from up high.")

                if st.button("View location", "10(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/@44.19389,3.581389,13z')

        if sidbar == 'Best Resorts':
            st.title("6 Best Resorts in France......")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1. Terre Blanche Hotel Spa Golf Resort")
                st.image("https://cf.bstatic.com/xdata/images/hotel/max500/14509677.webp?k=0d96bf38def43788b657"
                         "afdf9f83ebf55a27cec3dc9f1c81d86532404bf61130&o=", caption= "Terre Blanche Hotel Spa Golf Resort")
                st.write(
                    "Set on a 300 hectare property, Terre Blanche Hotel Spa Golf Resort is located in Tourrettes and "
                    "offers luxury suites and villas. Guests can enjoy a variety of outdoor activities on site and "
                    "can relax in the outdoor and indoor pools.")

                if st.button("Book Now", "1(id)"):
                    webbrowser.open_new_tab(url='https://www.booking.com/hotel/fr/terre-blanche-spa-golf-resort.en-gb.'
                                                'html?aid=376614;label=country-fr-Lrixzo0kGWPaIvKfqB5R1gS37790047040%'
                                                '3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-297480555031%3Alp100'
                                                '7783%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YdK51rZczkDIdTwCMK'
                                                'OeDj8;sid=a776e9a5aa98deb6766a63d6cfecf461')

                st.write("## 3. Mineral Lodge & Spa")
                st.image("https://cf.bstatic.com/xdata/images/hotel/max500/11894811.webp?k=5cf1"
                         "b13181481af2bc24c1c358c20b202f65fc90c7994996940a6fea23fb7b1c&o=",
                         caption="Mineral Lodge & Spa")
                st.write(
                    "Guests can begin summer hiking trails from the property and La Val d’Aoste is only 24 km away. "
                    "Tignes, Val d'Isère and Saint Foy ski resorts are all within 20 km. Bourg-Saint-Maurice is a "
                    "20-minute drive from the property. Free parking is possible on site.")

                if st.button("Book Now", "3(id)"):
                    webbrowser.open_new_tab(url='https://www.booking.com/hotel/fr/mineral-lodge.en-gb.html?aid=376'
                                                '614;label=country-fr-Lrixzo0kGWPaIvKfqB5R1gS37790047040%3Apl%3Ata%'
                                                '3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-297480555031%3Alp1007783%3A'
                                                'li%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YdK51rZczkDIdTwCMKOeDj'
                                                '8;sid=a776e9a5aa98deb6766a63d6cfecf461')

                st.write("## 5. Maranatha Porto Vecchio")
                st.image("https://cf.bstatic.com/xdata/images/hotel/max500/256092057.webp?k=68eb6a8b80"
                         "0c8ff47f14e823ce37dbfb74b9b88892dda321f6d8bf214c50809c&o=",
                         caption="Maranatha Porto Vecchio")
                st.write(
                    "Set directly on the water and featuring a private beach, Maranatha proposes self-catering studios "
                    "and villas and has views of the Gulf of Porto-Vecchio. Guests are free to relax on the furnished "
                    "terrace by the pool or on the beach, 10 metres away. There is also a spa on site.")

                if st.button("Book Now", "5(id)"):
                    webbrowser.open_new_tab(url='https://www.booking.com/hotel/fr/maranatha-mini-villa-porto-vecc'
                                                'hio.en-gb.html?aid=376614;label=country-fr-Lrixzo0kGWPaIvKfqB5R1g'
                                                'S37790047040%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-2974'
                                                '80555031%3Alp1007783%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9'
                                                'YdK51rZczkDIdTwCMKOeDj8;sid=a776e9a5aa98deb6766a63d6cfecf461')

            with col2:

                st.write("## 2. Le Cristal de Jade")
                st.image("https://cf.bstatic.com/xdata/images/hotel/max500/283285686.webp?k=8a9f3849847d7d"
                         "ddfa7fa524785e266957310a9e70be22269e116e9c9b81107e&o=",
                         caption="Le Cristal de Jade")
                st.write(
                    "Located in Chamonix-Mont-Blanc, Le Cristal de Jade features a 1000 m² wellness centre including a "
                    "swimming pool, a hot tub, a sauna, a steam room and a fitness room. Free WiFi is featured "
                    "throughout the property and free private parking is available on site.")

                if st.button("Book Now", "2(id)"):
                    webbrowser.open_new_tab(url='https://www.booking.com/hotel/fr/le-cristal-de-jade.en-gb.html?aid=3'
                                                '76614;label=country-fr-Lrixzo0kGWPaIvKfqB5R1gS37790047040%3Apl%3Ata'
                                                '%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-297480555031%3Alp1007783%3A'
                                                'li%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YdK51rZczkDIdTwCMKOeDj8;'
                                                'sid=a776e9a5aa98deb6766a63d6cfecf461')

                st.write("## 4. Chalets de la Colagne")
                st.image("https://cf.bstatic.com/xdata/images/hotel/max500/307858226.webp?k=fb5cb88a312f9677ff65"
                         "dd16fb5c70de18cdfba5f4ca384f915e556878e36403&o=",
                         caption="Chalets de la Colagne")
                st.write(
                    "The resort has a seating area, a TV with satellite channels, a kitchen, a dining area and a "
                    "private bathroom with a hairdryer and a shower. All guest rooms will provide guests with a "
                    "wardrobe and a kettle.")

                if st.button("Book Now", "4(id)"):
                    webbrowser.open_new_tab(url='https://www.booking.com/hotel/fr/les-chalets-de-la-colagne.en-gb.htm'
                                                'l?aid=376614;label=country-fr-Lrixzo0kGWPaIvKfqB5R1gS37790047040%3Ap'
                                                'l%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-297480555031%3Alp100778'
                                                '3%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YdK51rZczkDIdTwCMKOeD'
                                                'j8;sid=a776e9a5aa98deb6766a63d6cfecf461')

                st.write("## 6. Le Domaine de Wail - Legend Resort")
                st.image("https://cf.bstatic.com/xdata/images/hotel/max500/243475499.webp?k=eeb5f1b786fc92f15a10"
                         "125e32a0b50de14dc7c3fd38c0d19c481ce1c97831f9&o=",
                         caption="Le Domaine de Wail - Legend Resort")
                st.write(
                    "Featuring free WiFi and a sun terrace, Le Domaine de Wail - Legends Resort offers accommodation "
                    "in Wail. Guests can enjoy the on-site restaurant. Free private parking is available on site. "
                    "An array of activities are offered in the area, such as cycling and fishing. Le "
                    "Touquet-Paris-Plage is 42 km from Le Domaine de Wail - Legends Resort")

                if st.button("Book Now", "6(id)"):
                    webbrowser.open_new_tab(url='https://www.booking.com/hotel/fr/le-domaine-de-wail.en-gb.html?aid='
                                                '376614;label=country-fr-Lrixzo0kGWPaIvKfqB5R1gS37790047040%3Apl%3Ata%3'
                                                'Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-297480555031%3Alp1007783%3Ali%'
                                                '3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YdK51rZczkDIdTwCMKOeD'
                                                'j8;sid=a776e9a5aa98deb6766a63d6cfecf461')








    if countryselect == 'Norway':

        st.sidebar.title("...Norway...")
        st.sidebar.image("https://cdn.britannica.com/01/3101-004-506325BB/Flag-Norway.jpg", width=150)
        sidbar = st.sidebar.radio("", ("About", "Best beaches", "Best cities", "Activities",
                                       "Best national Parks","Tourist Attractions","Best Resorts"))

        if sidbar == 'About':
            st.title("Welcome to Norway")

            col11, col22 = st.beta_columns(2)

            with col11:
                st.balloons()
                st.image("https://assets.wego.com/image/upload/v1611848131/country-pages/no.jpg", width=500)
                st.write(
                    """Norway is best known for its outstanding natural beauty, 
                    particularly the fjords along its west coast.Once a haven for marauding 
                    Vikings, these deep inlets are now the country’s most popular tourist attraction.
                    This is a country shaped by the ice age, with towering mountains, thunderous waterfalls and dense 
                    forests."""
                    )
                st.write(
                   """Norway is located on the west of the Scandinavian Peninsula in northern Europe. Although a third 
                   of the country sits in the Arctic Circle, a length of 1,089 miles means that Norway is a year round 
                   destination. The summer months are perfect for hiking and mountain biking, 
                   while the in winter the skiing and winter sports are unparalleled."""
                   )
                st.write(
                    """The country is frequently ranked as one of the best places in the world to live, and one of the 
                    main reasons is the excellent infrastructure and the quality of local services. The capital city of 
                    Oslo offers visitors a stunning contrast of picturesque history and spectacular 
                    modern architecture.""")

                if st.button("View location","1(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Norway/@4.1279224,105.1196274,1837433m/'
                            'data=!3m2!1e3!4b1!4m5!3m4!1s0x3034d3975f6730af:0x745969328211cd8!8m2!3d4.21'
                            '0484!4d101.975766!5m1!1e2')

            with col22:
                st.image("https://i.natgeofe.com/k/679e983c-4461-4398-bb6d-9b508fe3e4de/norway-northern-lights.jpg", width=500)
                st.title("")
                st.image("https://cdn.britannica.com/01/3101-004-506325BB/Flag-Norway.jpg",width=500)
                st.write("")
                st.image("https://www.worldatlas.com/upload/fc/43/fe/no-01.jpg",width=500)



            st.video("https://www.youtube.com/watch?v=uXyy7lgDj9k&t=5s")
            st.video("https://www.youtube.com/watch?v=uWPYQll3Q5Y")

        if sidbar == 'Best beaches':
            st.title("10 Best Beaches in Norway......")

            col1, col2 = st.beta_columns(2)

            with col1:

                # Beach1
                st.write("## 1. Paradisbukta, Oslo ")
                st.image("https://tellusdmsmedia.newmindmedia.com/wsimgs/D1E197E34FC761852B8A933E26484F0E60099BE4.jpg", width=500, caption="Paradisbukta, Oslo")
                st.write("Oslo is one of the most popular beach locations in Norway. The word Paradisbukta means "
                         "‘Paradise Bay’ in the local Norwegian language. It is known for its stunning sunset views, "
                         "calm waters, and active adventures such as beach sports, and a lot more. Often the beach is "
                         "seen having a long queue because the best spots close to the water will fill up quickly on a "
                         "sunny day.")


                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Paradisbukta+Beach/'
                                                '@59.9019532,10.6634684,17z/data=!3m1!4b1!4m5!3m4!1s0x46416c4481c751af:'
                                                '0xd7ce6cc900c522a4!8m2!3d59.9019708!4d10.665654')

                # Beach3
                st.write("## 3. Godalen Beach, Stavanger")
                st.image("https://media-cdn.tripadvisor.com/media/photo-s/04/57/57/e0/godalen-badeplass.jpg", width=500, caption="Godalen Beach, Stavanger")
                st.write(
                    "Stavanger is a popular destination for water sports including swimming, volleyball at the beach, "
                    "sunbathing, beach side barbeques and for just getting the tan. It is a serene peaceful beach which "
                    "is usually not very crowded but still has a variety of options for everyone. One can relax, swim,"
                    " cook or just enjoy the ambrosial view this beach offers. If you have seen photos of Norway beaches"
                    " the are popular on the internet, you would definitely recognize the Godalen Beach in Stavanger.")
                if st.button("View location", "3(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/search/Godalen+Beach,+Stavanger/'
                                                '@58.9541195,5.7489765,15z/data=!3m1!4b1')


                # Beach5
                st.write("## 5.Seljesanden, Nordfjord ")
                st.image("https://live.staticflickr.com/6123/5926663530_5e2112a6d8_b.jpg", width=500, caption="Seljesanden, Nordfjord")
                st.write(
                    "Selje is a romantic town along the western coastline of Norway. There’s a secret that this town "
                    "lives with – a nice sandy beach area called Seljesanden. Seljesanden Beach is a popular tourist "
                    "destination in Selje. It is not just famous for beach and beauty, but also for traditional guided "
                    "tours to the Monastery of Selja, and the amazing nightlife. Swimming, fishing, and recreational"
                    " activities make this beach one of the most relaxing places on the earth.")
                if st.button("View location", "4(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Seljesanden+Beach/@61.8909796,5.'
                                                    '4887981,10z/data=!4m6!1m2!2m1!1sSeljesanden,+Nordfjord!3m2!1s0'
                                                    'x46170b968dc9b607:0xfe6ffde88e1892c1!15sChZTZWxqZXNhbmRlbiwgTm9yZGZqb3JkkgEFYmVhY2g')


                # Beach7
                st.write("## 7.  Hellesto Beach, Stavanger")
                st.image("https://www.wallpaperup.com/uploads/wallpapers/2014/12/20/559634/5c6ac06142b80d539cf24bc03d110556-700.jpg", width=500, caption=" Hellesto Beach, Stavanger")
                st.write(
                    "This is another beach that makes the city of Stavanger popular. It is a favorite destination for "
                    "swimming and sunbathing. Also, it is popular for hosting an annual kite festival. There is grass,"
                    "rocks or sand all around to sit and start a picnic on. Additionally, you can see fishes, crabs, "
                    "and clams as the tides wash the shores. There are many big trees, shelters across the beach –"
                    " very helpful if there are strong wind currents.")
                if st.button("View location", "5(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/search/Hellesto+Beach,+Stavanger/'
                                                    '@58.859925,5.355,10z/data=!3m1!4b1')


                # Beach9
                st.write("## 9. Bunes Beach, Lofoten")
                st.image("https://www.worldbeachguide.com/photos/bunes-beach-lofoten.jpg", width=500, caption="Bunes Beach, Lofoten")
                st.write(
                    "It is one of the Lofoten most scenic beaches. With its turquoise waters and the white sandy beach,"
                    " it is a must-see location when visiting the Lofoten islands in Northern Norway. Besides the vivid "
                    "scenery that it has, it is also loved by hikers as it is surrounded by hills. You can visit all "
                    "year round, but it is especially nice during summer when you can enjoy a sunny day at Bunes Beach.")
                if st.button("View location", "6(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Bunes+Beach/'
                                                    '@67.9797749,12.9579039,15z/data=!3m1!4b1!4m5!3m4!'
                                                    '1s0x45de237d31c40c9f:0x91b55acc0e6bb0f1!8m2!3d67.9797675!4d12.9666587')

            with col2:


                # Beach2
                st.write("## 2.  Huk Beach, Oslo")
                st.image("https://images.rove.me/w_1920,q_85/w1ueovbdfx7lbgcvyi94/oslo-huk-beach-season.jpg", width=500, caption=" Huk Beach, Oslo")
                st.write(
                    "Oslo’s Bygdoy peninsula is a sure shot destination for people of the metropolitan city to find "
                    "some time for themselves. Huk beach is quite charming because it is one of Norway’s "
                    "clothing-optional beaches. You can walk on the Huk beach without clothes and enjoy the sun. "
                    "Besides this, you can bicycle and play beach volleyball with your loved ones. Huk Beach in "
                    "Oslo is one of the best beaches in Norway for if you want to go boating.")
                if st.button("View location", "7(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Huk/@59.8956161,10.6721606,17z/'
                                                    'data=!3m1!4b1!4m5!3m4!1s0x46416c4170fe25f1:0xdca00e08a4a07cec!8m2!'
                                                    '3d59.8949009!4d10.6755109')

                # Beach4
                st.write("## 4. Mjelle Beach, Bodo")
                st.image("https://en.nordlandturselskap.no/content/uploads/sites/2/2017/12/Mjelle-Christian-Str%C3%B8mhaug-tursiden.no-5.jpg", width=500, caption="Mjelle Beach, Bodo")
                st.write(
                    "Mjelle beach is a popular swimming spot in the summers. It is not the only thing that makes it"
                    " famous. The beach has a mixture of colors – the red sand and white sand mix with each other, "
                    "presenting hues all along the shore. While being there, you can see how winds and tides along "
                    "the shore create the hues. After a heavy storm, the red sand is so much visible that the beach "
                    "appears almost purple.")
                if st.button("View location", "8(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Mjelle/@67.4091821,14.6181063,15z/'
                                                    'data=!3m1!4b1!4m5!3m4!1s0x45df1ebdf28f9009:0xaf3921076bd55340!8m2!'
                                                    '3d67.4103918!4d14.6257647')
                # Beach6
                st.write("## 6. Haukland Beach, Lofoten")
                st.image("https://img3.oastatic.com/img2/56039265/max/t.jpg", width=500, caption="Haukland Beach, Lofoten")
                st.write(
                    "The Lofoten islands in Norway, Europe have enough spectacular beaches. This beach has crystal blue"
                    " waters and white sand making it serene and perfect for a day out. It’s also one of the best places"
                    " in Norway to witness an incredible sunrise and sunset. You can walk along the ocean next to a hill."
                    " It has a very less population coming in as it is not discovered by many people yet.")
                if st.button("View location", "9(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Hauklandstranda/@68.1986236,13.'
                                                    '5199544,15z/data=!3m1!4b1!4m5!3m4!1s0x45de0da5b5de86e3:'
                                                    '0xc16fa329db8b549b!8m2!3d68.1986162!4d13.5287092')
                # Beach8
                st.write("## 8.  Kvalvika Beach, Moskenesoya")
                st.image("https://media-cdn.tripadvisor.com/media/photo-s/07/a5/03/6a/getlstd-property-photo.jpg", width=500, caption=" Kvalvika Beach, Moskenesoya")
                st.write(
                    "The beach at Kvalvika is ideal for its hiking trails and some outdoor activities. It provides "
                    "challenging climbs and breathtaking views, in between the mountains that surround it. It gives a"
                    " wonderful feeling of isolation and natural beauty. It might take you about an hour to get to the"
                    " Kvalvika Beach, but it will be worth it. While on the beaches, you can see the sun, sand, and sea"
                    " coming together to exhibit the unknown scenic hues of nature.")
                if st.button("View location", "10(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Kvalvika+Beach/@68.0774102,13.'
                                                    '0895008,15z/data=!3m1!4b1!4m5!3m4!1s0x45de19c203387e97:'
                                                    '0xa98bcbe8be9f0dc4!8m2!3d68.0774028!4d13.0982556')

                # Beach10
                st.write("## 10.  Unstad Beach, Lofoten")
                st.image("https://img.locationscout.net/images/2019-07/unstad-beach-norway-0sif_l.jpeg", width=500, caption=" Unstad Beach, Lofoten")
                st.write(
                    "Unstad Beach is one of the most beautiful places on earth. The beach has large smooth rocks with"
                    " water surrounding them and glorious waves beating. There is white sand in the middle of them and"
                    " only brave people go to do surfing there. It is ideal to spot the stars there at night and not"
                    " try any act of chivalry! You can unwind and appreciate each snapshot of nature – exotic, dramatic,"
                    " beautiful, romantic, serene and idyllic.")
                if st.button("View location", "11(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Unstad+Beach/'
                                                    '@68.2689976,13.5761143,16z/data=!3m1!4b1!4m5!3m4!1s0x45de0b834453836d:'
                                                    '0xeec58625105736a9!8m2!3d68.2687586!4d13.5810711')

        if sidbar == 'Best cities':
            st.title("15 Best Cities to Visit in Norway......")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1.Haugesund")
                st.image("http://res.cloudinary.com/simpleview/image/upload/v1614091801/clients/norway/haugesund_fjord_norway_photo_nordic_drone_2_1_42c9d080-4ec3-4e28-bad9-eb1ee0c87ef9.jpg", width=500, caption="Haugesund")
                st.write(
                    """Once an important fishing port, it is now the oil industry that fuels Haugesund and keeps it 
                    moving. A lively place, the waterfront area around the port has some interesting bars and 
                    restaurants which are worth checking out.""")
                st.write(
                    """As the area has been inhabited for thousands of years, there are loads of interesting historical
                     sights to visit, with the ancient church and viking farm being particularly noteworthy. When 
                     visiting Haugesund, a great thing to do is take a boat trip to the nearby Karmoy island –
                     a picturesque place to explore.""")

                if st.button("View location", "12(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Haugesund,+Norway/@59.4155759,'
                                                    '5.2168586,12z/data=!3m1!4b1!4m5!3m4!1s0x463b9e2daa5b77ff:'
                                                    '0xc124394a88e63a66!8m2!3d59.413581!4d5.2679869')


                st.write("## 3. Tonsberg")
                st.image("https://upload.wikimedia.org/wikipedia/commons/f/fc/T%C3%B8nsberg_domkirke_2.jpg", caption="Tonsberg")
                st.write(
                    """Although relatively few remnants of the past remain, Tonsberg is actually the oldest town in the 
                    whole of Norway. As such, history lovers will enjoy stopping by when traveling from Oslo along the
                     coast, to see all that it has to offer."""
                    )
                st.write(
                    """There is a crumbling old castle, some Viking ruins and graves, as well as a cool museum with the
                     skeleton of a blue whale in it. A lively town, the landscapes surrounding Tonsberg are also nice, 
                     if people fancy taking a trip into the nearby countryside.""" )
                if st.button("View location", "13(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/T%C3%B8nsberg+Municipality,'
                                                    '+Norway/@59.3550662,10.0365233,10z/data=!3m1!4b1!4m5!'
                                                    '3m4!1s0x4646b723254a629d:0xac4b8cd46f51d971!8m2!3d59.364988!4d10.3037633')

                st.write("## 5. Drammen")
                st.image("https://upload.wikimedia.org/wikipedia/commons/8/85/Winter_In_Drammen_Norway_%28240873317%29.jpeg", caption="Drammen")
                st.write(
                   """Traditionally an industrial center with a bustling port and a reputation as a grimy, grey and grim
                    city, Drammen has cleaned up a lot in recent years, and as a result, is a lot more tourist 
                    friendly."""
                   )
                st.write(
                    """Lying not too far from Oslo, the city has some lovely walks and trails on both sides of the river
                     that splits Drammen in two, and the center of town is easily traversed on foot. Visitors nearly 
                     always use this city as a stepping stone to the interior of the country, or as a stop-off on the 
                     way to the nearby mines at Blafarvevaerket.""")
                if st.button("View location", "14(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Drammen,+Norway/@59.7340896,'
                                                    '10.1140128,12z/data=!3m1!4b1!4m5!3m4!1s0x46413cb4aa728419:'
                                                    '0xc578916649a336d9!8m2!3d59.7440738!4d10.2044565')


                st.write("## 7. Larvik")
                st.image("https://nordicsafecities.org/wp-content/uploads/Forside-larvik.no_-768x344.jpg.webp", width=500, caption="Larvik")
                st.write(
                """Lying on the southern coast of Norway, Larvik has a busy port and, although it is not a very popular 
                tourist destination, there is more than enough to warrant a visit. There are a couple of fantastic 
                historical museums in town and a new cultural center has recently opened up, while the old baroque 
                lighthouse looks impressively out over the sea.""")
                st.write(
                    """From here you can visit the country´s largest beech forest at Bokeskogen, and the surrounding 
                    area has some great viking excavations for visitors to enjoy.""")
                if st.button("View location", "15(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Larvik,+Norway/'
                                                    '@59.0530277,9.9756525,12z/data=!3m1!4b1!4m5!3m4!1s0x4646e99720e47099:'
                                                    '0x41469061c5106c79!8m2!3d59.0538363!4d10.0295463')


                st.write("## 9.Lillehammer ")
                st.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/Lillehammer_City.jpg", width=500, caption="Lillehammer")
                st.write(
                    """Having hosted the Winter Olympics in 1994, it is unsurprising that Lillehammer has such a 
                    fantastic array of winter sport activities on offer. Lying on the edge of Lake Mjosa, there are some
                     great museums and galleries about town, as well as a number of lovely restaurants."""
                    )
                st.write(
                    """One of the most popular ski resorts in the country, Lillehammer has a picturesque setting, with 
                    roving hills and forests all around it. Although there are interesting things to see and do 
                    throughout the year, winter is when Lillehammer really comes alive."""
                    )
                if st.button("View location", "16(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Lillehammer,+Norway/@61.1123102,'
                                                    '10.4037432,12z/data=!3m1!4b1!4m5!3m4!1s0x466a62a7f7b5288d:'
                                                    '0x32273ad34a5bed34!8m2!3d61.1152713!4d10.4662306')


                st.write("## 11.Hamar ")
                st.image("https://cdn.pixabay.com/photo/2019/05/30/00/46/norway-4238898_960_720.jpg", width=500, caption="Hamar")
                st.write(
                    """Set on the banks of the largest lake in Norway, Hamar has a surprising amount to do given its 
                    size. It’s not a bad option if you are looking to stop off somewhere when traveling to the north 
                    from Oslo."""
                    )
                st.write(
                    """It has the largest glass building in Europe, which remarkably has the ruins of a cathedral inside
                    . The accompanying museum about the vikings is captivating. Apart from this, Hamar is a charming, 
                    laid-back place where you can also head out for some fishing and kayaking on the lake."""
                    )
                if st.button("View location", "17(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/search/Hamar/@61.1124398,10.4037431,12z/data=!3m1!4b1')


                st.write("## 13.Kristiansand")
                st.image("https://pyt-blogs.imgix.net/2020/07/Bystranda_Kristiansand.png?auto=format&ixlib=php-3.3.0", width=500, caption="Kristiansand")
                st.write(
                    """The fifth largest city in Norway, Kristiansand is a charming place with a lovely marina and 
                    lively ambiance. With lots of shopping options and some great restaurants and bars along the 
                    waterfront, the city has some pretty sandy beaches and claims to be Norway´s most popular holiday
                     resort."""

                    )
                st.write(
                    """While Norwegians do indeed head here in large numbers, it is often to stop by on the way to other
                     destinations in the south. The nearby archipelago is lovely to explore and the southern coast is 
                     not too far away either."""

                    )
                if st.button("View location", "18(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Kristiansand,+Norway/'
                                                    '@58.153082,7.8914055,11z/data=!3m1!4b1!4m5!3m4!1s0x46380258d5607a5b'
                                                    ':0xdf0c0d6fc81c58a4!8m2!3d58.1599119!4d8.0182064')

                st.write("## 15. Fredrikstad")
                st.image("https://upload.wikimedia.org/wikipedia/commons/c/c1/Fredrikstad_bryggepromenade_fra_Kr%C3%A5ker%C3%B8ybroa.JPG", width=500, caption="Fredrikstad")
                st.write(
                   """Lying on the banks of the Glomma river, Fredrikstad is a lovely, old fortified city that has been 
                   very well-preserved. A picturesque place to wander around – when the sun is shining, the modern 
                   waterfront is particularly delightful; there are a number of coffee shops, restaurants and bars for
                    visitors to enjoy."""
                   )
                st.write(
                    """On the opposite bank, the old town, with its impressive Kongsten fort and distinctive moat,
                     is the undoubted highlight, and is what makes Fredrikstad a popular haunt for tourists."""
                    )
                if st.button("View location", "19(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Fredrikstad,+Norway/'
                                                    '@59.2264545,10.8100301,11z/data=!3m1!4b1!4m5!3m4!1s0x464402de0bc9bcdb:'
                                                    '0xeeba626d338204fc!8m2!3d59.2205369!4d10.9347012')

            with col2:


                st.write("## 2. Bodo")
                st.image("https://planetofhotels.com/guide/sites/default/files/styles/paragraph__live_banner__lb_image__1880bp/public/live_banner/Bodo.jpg", width=500, caption="Bodo")
                st.write(
                    """As the largest city in the Nordic region, Bodo is an important commercial center and transport
                     hub to the area around it. Although the city itself is uninspiring, architecturally speaking -it
                     was almost completely destroyed in the Second World War – Bodo´s beautiful location, with 
                     snow-capped peaks off in the distance, makes up for its drab buildings.""")
                st.write(
                    """Situated at the end of the incredible Kystriksveien Coastal Route, many people visit Bodo to get
                     to the mesmerizing Lofoten Islands nearby. From here you can explore the wild and rugged north of
                      the country – that in itself makes Bodo worth visiting."""
                    )
                if st.button("View location", "20(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Bod%C3%B8,+Norway/'
                                                    '@67.2916,14.4125185,12z/data=!3m1!4b1!4m5!3m4!1s0x45df10f55b63f17d:'
                                                    '0x8e785b93b25d3c53!8m2!3d67.2803556!4d14.404916')


                st.write("## 4. Tromso")
                st.image("http://res.cloudinary.com/simpleview/image/upload/v1585560261/clients/norway/northern_lights_tromso_vegard_stien_visit_tromso__ac989cc1-0858-4e31-bd7c-d6334122e8b5.jpg", width=500, caption="Tromso")
                st.write(
                    """Located in the far north of Norway, Tromso is set on an island amidst lovely blue fjords and 
                    spectacular snow-capped mountains. One of the northernmost places that you can visit in Europe, the 
                    city actually lies around 350-kilometres north of the Arctic Circle. As such, it is one of the 
                    better sites in Norway from which to view the Northern Lights."""
                   )
                st.write(
                    """With loads of pubs on offer, a healthy cultural scene and lively nightlife, visiting Tromso can 
                    be great fun. There are lots of winter sports available and loads of scenic landscapes in which to 
                    pursue them. Tour organizers in the city can arrange trips to the Arctic if you´re after 
                    an adventure."""
                    )
                if st.button("View location", "21(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Troms%C3%B8,+Norway/'
                                                    '@69.6653119,18.7776686,11z/data=!3m1!4b1!4m5!3m4!1s0x45c4c4526c3b71fd:'
                                                    '0x23dca858e6ebed3!8m2!3d69.6492047!4d18.9553239')


                st.write("## 6.Stavanger ")
                st.image("http://res.cloudinary.com/simpleview/image/upload/v1561544595/clients/norway/Stavanger_fjord_norway_2d1e7ad1-ebb8-4fe2-8309-592774db7568.jpg", width=500, caption="Stavanger")
                st.write(
                    """A dynamic place, Stavanger´s economy is booming due to the nearby oil fields. As such, the 
                    dreaded urban sprawl has taken over much of the outskirts of the city. Accompanying this has been 
                    an upsurge in prices, and it is now one of the most expensive places in the country."""
                    )
                st.write(
                    """The center of Stavanger has managed to avoid being engulfed by modern developments and is full of
                     old wooden buildings which are very pretty to walk around. The nearby waterfront is very lively 
                     during the summer and there are lots of great restaurants to choose from, as well as some lively 
                     nightlife. Many people stop by Stavanger on their way to the fantastic sights at Lysefjorden and 
                     Preikestolen."""
                    )
                if st.button("View location", "22(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Stavanger,+Norway/'
                                                    '@58.9487548,5.5402534,11z/data=!3m1!4b1!4m5!3m4!1s0x463a3549dd29f795:'
                                                    '0xad7aeb21b80a9259!8m2!3d58.9699756!4d5.7331074')


                st.write("## 8.Alesund ")
                st.image("https://cdn.britannica.com/13/190113-050-C414934F/Alesund-Norway.jpg", width=500, caption="Alesund")
                st.write(
                    """A slightly bizarre place to visit, due to its eclectic mix of architectural styles, the city was
                     destroyed by a fire in 1904. Its hasty reconstruction accounts for the mix of mock-Gothic, Art 
                     Nouveau and folkloric embellishments which you find when wandering its streets."""
                    )
                st.write(
                   """Built on a few islands lying next to each other, the glittering harbor adds to Alesund´s
                    attractiveness. From the nearby hills, there are some breathtaking panoramic views of the 
                    surrounding fjords and mountains. A lively city, Alesund has lots of magnificent restaurants and a 
                    thriving bar scene.""")
                if st.button("View location", "23(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Alesund,+Norway/'
                                                    '@62.4681493,6.1013653,11z/data=!3m1!4b1!4m5!3m4!1s0x4616da471047fb4b:'
                                                    '0xe82562ee3bc08fea!8m2!3d62.4722284!4d6.1494821')


                st.write("## 10. Trondheim")
                st.image("https://shapeenergy.eu/wp-content/uploads/2017/09/Trondheim.jpg", width=500, caption="10. Trondheim")
                st.write(
                   """One of the most picturesque cities in the whole country, Trondheim is a pleasure to walk around, 
                   as forest-clad hills and glistening waterways surround its colorful buildings and sweet, old harbor.
                    The historic capital of Norway has an amazing medieval cathedral. There is a sense of timelessness 
                    about its laid-back streets, as people leisurely go about their lives.""")
                st.write(
                    """There´s more than enough to keep you entertained for a few days, and you´ll soon discover its 
                    fine museums, great restaurants and atmospheric cafes. Alongside its rich cultural heritage, 
                    there is a contemporary arts and music scene, due to the large university campus. After Trondheim, 
                    head north to explore all the wild landscapes that northern Norway has to offer.""")
                if st.button("View location", "24(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Trondheim,+Norway/'
                                                    '@63.4188213,10.2986797,11z/data=!3m1!4b1!4m5!3m4!1s0x466d319747037e53:'
                                                    '0xbf7c8288f3cf3d4!8m2!3d63.4305149!4d10.3950528')


                st.write("## 12. Bergen")
                st.image("http://res.cloudinary.com/simpleview/image/upload/v1574085889/clients/norway/bryggen_wharf_bergen_hordaland_fjord_norway_photo_florian_olbrechts_34ad36ea-f7bc-4150-b48b-af2c2c14628f.jpg", width=500, caption="Bergen")
                st.write(
                   """Formerly a part of the Haneseatic league and once the capital of Norway, Bergen sits in a 
                   spectacular location and visitors will love the plethora of sights on offer. With seven hills 
                   surrounding it, as well as seven fjords, the city´s brightly-colored buildings tumble down the slopes 
                   until they reach Bryggen – the fantastic wooden houses at the city center which were once used for 
                   trading and commerce.With some great art museums, a lively music scene and upbeat nightlife, Bergen 
                   has a nice atmosphere to it – although it unfortunately rains nearly every day of the year. Hiking 
                   in the surrounding mountains is glorious, and taking a boat ride amidst the nearby fjords offers up 
                   some stunning panoramas.""")
                if st.button("View location", "25(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Bergen,+Norway/'
                                                    '@60.3652306,5.1489903,10z/data=!3m1!4b1!4m5!3m4!1s0x46390d4966767d77:'
                                                    '0x9e42a03eb4de0a08!8m2!3d60.3912628!4d5.3220544')


                st.write("## 14. Oslo")
                st.image("https://www.theagilityeffect.com/app/uploads/2019/06/00_VINCI-ICONOGRAPHIE_GettyImages-673112427-1280x680.jpg", width=500, caption="Oslo")
                st.write(
                    """The capital of the country is full of amazing architectural designs that highlight the 
                    contemporary feel about the place, as do the educational museums, interesting galleries and 
                    evocative art pieces. Lying next to the sea, with mountains surrounding it, Oslo is one of the 
                    greenest cities in the world, thanks to its forward-thinking eco-friendly policies – this makes it 
                    lovely to walk around. In actual fact, residents can find themselves skiing, trekking the forests, 
                    or sailing along the Oslo fjord’s waterways in no time at all."""
                    )
                st.write(
                    """A lively place, Oslo has a fantastic gastronomic scene as well as a raucous nightlife with lots 
                    of trendy bars and nightclubs."""
                    )
                if st.button("View location", "26(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Oslo,+Norway/'
                                                    '@59.8939529,10.6450333,11z/data=!3m1!4b1!4m5!3m4!1s0x46416e61f267f039:'
                                                    '0x7e92605fd3231e9a!8m2!3d59.9138688!4d10.7522454')



            st.write("# ---Map of cities in Norway---")
            st.image("https://www.touropia.com/gfx/b/2018/07/cities_norway_map.jpg", width=800)

        if sidbar == 'Activities':
            st.title("10 Top Reasons Why You Should Visit Norway")
            st.write("""The Scandinavian country of Norway is known for its remote location, its incredible scenery and
             its surreal fjords. Although it borders Russia, Finland and Sweden, much of Norway’s coast is right 
             alongside the Arctic Ocean, offering chilly but impressive views over the water. Norway boasts large
             historic cities, magnificent cathedrals, a progressive population and unending ways to stay active
             outdoors. If you’re eager to start planning a Scandinavian getaway, here are some of the top reasons to
             visit Norway.""")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1.  Skiing")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_skiing.jpg?v=1")
                st.write("""During the winter months, many places in Norway are ideal for both downhill and 
                cross-country skiing. If you’re looking for a place that can compete with Alpine runs, however, be sure
                to check out Hemsedal, which is home to several world-class ski resorts, dozens of slopes and more
                than 20 ski lifts. Hafjell is another winter sports destination that boasts alpine and cross-country
                tracks as well as family fun areas for sledding and tubing.""")






                st.write("## 3.  Fisherman's Cabins")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_fishermans_cabins.jpg?v=1")
                st.write(
                    """Another collection of islands off the northern coast of Norway is the Lofoten Archipelago. These
                    islands are considered to be among the most scenic spots in the country, but some of their most
                    popular attractions are actually manmade. Be sure not to miss the traditional red fishermen’s
                    cabins built right along the coastline. Some are built on stilts and called rorbu, and a few are
                    even available to tour or stay in overnight. Not only are these cabins historic and beautiful,
                    they are often located on remote, secluded and breathtaking beaches.""")

                st.write("## 5. Hiking")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_hiking.jpg?v=1")
                st.write(
                    """To get out and see as much of Norway’s natural beauty as possible, hiking is a fantastic choice.
                     Hiking in Norway is also made easier thanks to laws about right to access, making it simple to
                     find walking paths as well as camping spots. If you’re up for a serious challenge, you can tackle
                     hikes leading to the peak of Galdhøpiggen, the highest mountain in Norway. For something far less
                     intense but just as scenic, set off on a trek through the Rondane National Park, where you may be
                     able to spot reindeer in their natural habitats.""")

                st.write("## 7. Stave Churches")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_stave_churches.jpg?v=1")
                st.write(
                    """Large churches in Europe tend to be made from stone, but in Norway it is possible to find grand
                    and intricately designed churches made entirely from wood. These stave churches are representative 
                    of the woodworking industry that has long been a part of Norwegian culture and history. There are
                    many stave churches located around Norway, but one of the most impressive is the Heddal Stave
                    Church. Heddal was constructed in the 13th century and is the largest of the wooden stave churches
                    in the country.""")

                st.write("## 9. Waterfalls")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_waterfalls.jpg?v=ed7faf3933a142991aa11b2ea09abaa4")
                st.write(
                    """Thanks in part to the sheer number of glaciers in Norway, there is also an abundance of
                    waterfalls. Some are mere trickles in certain seasons, but others are powerful, breathtaking
                    attractions throughout the year. Although the greatest concentration of waterfalls are in the
                    western fjords and the mountains, they can be found scattered throughout the country. Arguably
                    one of the most incredible waterfalls in Norway is Mardalsfossen, which is a large, powerful 
                    and year-round waterfall where you can stand quite close and even feel the spray of the water.""")

            with col2:


                st.write("## 2. Coastal Towns")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_coastal_towns.jpg?v=1")
                st.write(
                    """Norway boasts hundreds of miles of coastline, so there is no shortage of charming coastal towns
                    worth visiting. These traditional coastal towns are often places where architecture is simple,
                    residents work in industries like fishing and local culinary staples include things like dried
                    and salted cod. Ålesund is a fantastic example of a coastal town located on a row of islands
                    that boasts breathtaking views and amazing hiking opportunities. Henningsvær is another
                    wonderful coastal town where the brightly colored houses in a row along the water look more
                    like gingerbread out of a fairytale than actual residences.""")

                st.write("## 4. Polar Bears")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_polar_bears.jpg?v=1")
                st.write(
                    """Directly north of the Norwegian mainland is the Svalbard Archipelago, a collection of islands
                    with a very small population of people but a large population of incredible wildlife. Guided tours
                    are readily available from settlements like Longyearbyen where you can set off and spot polar bears
                    in the wild. This incredible, majestic creatures are amazing to behold, but don’t forget that they
                    are wild and dangerous animals. It is vital that you see them with an experienced guide in Svalbard.""")


                st.write("## 6. Spectacular Photo Opportunities")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_spectacular_photo_opportunities.jpg?v=1")
                st.write(
                    """Whether you’re a frequent social media poster or a serious photographer, Norway boasts a 
                    staggering array of spectacular photo opportunities. Kjeragbolten, for instance, is an iconic
                    boulder caught between two cliffs that you have to see to believe. At Pulpit Rock, you can take a
                    selfie on a sheer cliff face that overlooks pristine blue water. At Trolltunga, snap a pic of the 
                    rocky outcropping perched hundreds of feet above a river. Each of these photo opportunities is
                    unique, and there are dozens more than you can capture on film while in Norway.""")

                st.write("## 8. Northern Lights")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_northern_lights.jpg?v=adf0d47cf94a5163cbc314e4d2b164ee")
                st.write(
                    """Aurora borealis, also known as the northern lights, are undoubtedly a major reason to visit 
                    Norway. The best chance to spot them will be in the winter, when the nights are longer. The further
                    north you go, and the further you travel away from cities, the better your view will be. Many people
                    regard Tromsø as the best place in Norway to see the northern lights, thanks to its northern
                    location and its proximity to the Arctic Circle. Dry weather and a lack of clouds will make
                    conditions perfect for spotting the northern lights""")

                st.write("## 10. Fjords")
                st.image("https://www.touropia.com/gfx/d/reasons-to-visit-norway/norway_fjords.jpg?v=1")
                st.write(
                    """A fjord is where a long sea inlet is found between high cliffs, and it is typically the result 
                    of a submerged glacier valley. In Norway, the fjords are some of the most beautiful natural 
                    attractions around, and no trip to Scandinavia would be complete without seeing some of them up 
                    close. Most of Norway’s fjords are along the western coastline, including Sognefjorden, which is 
                    the longest fjord in all of Europe.""")




        if sidbar == 'Best national Parks':

            st.title("12 Most Beautiful National Parks in Norway")

            st.write("""A land of outstanding beauty, Norway’s wild and untamed landscapes are simply spectacular. 
            In this sparsely populated part of the world, the air is fresh, the environment is clean and you really feel
             at one with all of the pristine wilderness around you. The most iconic images of Norway all involve the 
             stunning fjords that scar the scenery and make for such picturesque and beautiful views. The deep waters 
             that weave their way between the landmasses and the rocky mountains that dominate its shores only add to 
             the perfect scenes on show."""
                    )
            st.write("""Exploring these incredible settings is to really immerse yourself in nature, away from the 
            world. With such an abundance of natural wonders on display, here are the most beautiful national parks in 
            Norway for you to discover and delight in.""")

            col1, col2 = st.beta_columns(2)

            with col1:


                st.write("## 1. Breheimen National Park")
                st.image("https://upload.wikimedia.org/wikipedia/commons/8/83/P1000154Gamle_Strynefjellsvegen.JPG", caption="Breheimen National Park")
                st.write("A land of ever-changing scenery, the various landscapes in Breheimen National Park seamlessly"
                         " intertwine and mix before you emerge in a completely different world. "
                         "Named after the mountain range that dominates the park, there are a plethora of delightful "
                         "sights for visitors to enjoy.")
                st.write("The snow-capped mountains give way to forest coated valleys which in turn trundle down to icy "
                         "cold rivers that run into the deep lakes hidden amidst the scenery. With hiking, skiing and "
                         "mountaineering on offer, the diverse attractions will leave you with a new sense of"
                         "appreciation for the pristine environment all around you.")
                st.write("Located high up in the mountains, glaciers lie in wait for adventurous explorers to discover "
                         "them all over again, recapturing that sense of awe and astonishment at the gigantic expanses "
                         "of ice.")

                if st.button("View location", "27(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Breheimen+National+Park,+2693,'
                                                    '+Norway/@61.7693419,7.3608409,9z/data=!3m1!4b1!4m5!3m4!'
                                                    '1s0x4615b20990122c93:0x7a4dc122a8ba6831!8m2!3d61.8037007!4d7.8584951')

                st.write("## 3. Dovrefjell-Sunndalsfjella National Park")
                st.image("https://assets.simpleviewcms.com/simpleview/image/fetch/c_fill,f_jpg,h_400,q_65,w_587/https://media.newmindmedia.com/TellUs/image/%3Ffile%3D9386C33FF7DADB06BFF28214C5E63BB003B9C697.jpg%26dh%3D600%26dw%3D800%26t%3D4",caption="Dovrefjell-Sunndalsfjella National Park")
                st.write("""Established to preserve and protect the pristine alpine ecosystem of this wild and untouched
                 area, the national park is a wonderful place to get lost amidst the abundance of natural sights on show.
                 The sprawling mountains make for delightful trekking and, alone in the wild, you will feel a sense of 
                 peace and tranquillity come over you.""")
                st.write("""Walking through this rich and ancient landscape, you will hardly fail to notice the 
                  abundance of fauna and flora that dots the park. Lucky visitors may also catch a glimpse of some of the
                  animals such as the reindeer, musk oxen and wolverines that call the park their home. Two of the main
                  draws of Dovrefjell-Sunndalsfjella are the highest peak in the park, Snohetta, and the beautiful 
                  Amotan Waterfall.""")
                st.write("""While the former’s lofty peak towers at over 2200 meters in height, it is the heady heights 
                of Amotan that are the standout feature of the park. Plunging down over 150 meters, this lovely 
                waterfall is mesmerising in its beauty.""")

                if st.button("View location", "28(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Dovrefjell%E2%80%93Sunndalsfjella'
                                                    '+National+Park/@62.3952215,8.502023,9z/data=!3m1!4b1!4m5!3m4!'
                                                    '1s0x4614a25c68884b71:0x942a46c54c850b05!8m2!3d62.3662329!4d9.106266')

                st.write("## 5.  Sor-Spitsbergen National Park")
                st.image("https://sites.google.com/a/miamioh.edu/geo121f15/_/rsrc/1442420312771/home/soer-spitsbergen-np-svalbard-norway-12/sor%20spits.jpg?height=240&width=320",caption="Sor-Spitsbergen National Park")
                st.write("""Located far north of the mainland of Norway in the Svalbard archipelago, this huge national
                  park consists mainly of sprawling, interminable ice caps and glaciers that stretch as far the eye can 
                  see. This sea of white is incredible to behold and it is this untouched beauty that makes 
                  Sor-Spitsbergen National Park so worth visiting despite its remote location.""")
                st.write("""Sparsely vegetated areas, tundra and wetlands punctuate the almost endless white wilderness 
                  and give the landscape some variation. Only the hardiest of animals and birds eke out a living here yet
                  despite that, the area is home to numerous types of birds who flock above the desolate scenery.
                  Huge ice covered mountains and cliffs rise dramatically amidst all this, forming a stunning backdrop 
                  to this incredible landscape.""")

                if st.button("View location", "29(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/S%C3%B8r-Spitsbergen+National'
                                                    '+Park/@77.2625916,16.0715953,17z/data=!3m1!4b1!4m5!3m4!'
                                                    '1s0x459bc2baa476cb47:0x3917f0a6c49da4f!8m2!3d77.2625904!4d16.073784')


                st.write("## 7.Sor-Spitsbergen National Park")
                st.image("https://media-cdn.tripadvisor.com/media/photo-s/0d/2f/41/3a/the-suspension-bridge.jpg", caption="Sor-Spitsbergen National Park")
                st.write("""The largest national park in the country; it is fair to say that Hardangervidda has a 
                correspondingly diverse array of attractions and activities to stun and delight any visitor to the 
                park.""")
                st.write("""Hiking, cycling or horseback riding through the wilderness of the gigantic mountain plateau 
                that dominates the area makes you feel like you are stepping back in time as you are unlikely to meet 
                many people on your travels.""")
                st.write("""Huge herds of reindeer make their way between the rivers and lakes that dot this expansive
                 landscape that varies from barren rock to grassy wetlands. Canoeing or kayaking along its waterways is 
                 a fantastic experience as looking out over the expanse you can see the herds of reindeer off in the 
                 distance.""")

                if st.button("View location", "30(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Hardangervidda+National+Park/@59.'
                                                '9846213,7.5736512,10z/data=!4m9!1m2!2m1!1sHardangervidda+National+Park!'
                                                '3m5!1s0x463ee4512cafa9d1:0xbd0bc34b78d87122!8m2!3d60.1542843!4d7.4430461!'
                                                '15sChxIYXJkYW5nZXJ2aWRkYSBOYXRpb25hbCBQYXJr'
                                                'Wh4iHGhhcmRhbmdlcnZpZGRhIG5hdGlvbmFsIHBhcmuSAQ1uYXRpb25hbF9wYXJr')


                st.write("## 9. Rondane National Park")
                st.image("https://assets.simpleviewcms.com/simpleview/image/upload/c_limit,h_1200,q_75,w_1200/v1/clients/norway/norway_asset_import_jvt8xjdrpu_e3147d1a-d337-9645-69e8d9a602a274fe.jpg", caption="Rondane National Park")
                st.write("If you are a lover of lofty peaks, indomitable mountains and sprawling plateaus then look no "
                         "further as Rondane has these in abundance as well as many other natural sights to enjoy. With"
                         " ten peaks in the park towering over 2000 meters in height, the national park is perfect for "
                         "hikers wanting to lose themselves among the mountains and take in the stunning scenery on "
                         "show.")
                st.write("Interspersed between these peaks are a series of rolling valleys, small canyons and low-lying"
                         " forest and scrubland. The highest mountain, Rondeslottet, is barren, rocky and unwelcoming "
                         "to behold which is in actual fact what makes it so scenic. Wild reindeer maraud around the "
                         "park and only add to the picturesque scenery on display. Well worth a visit, the wealth of "
                         "things to do and see in Rondane National Park make it a delightful place to explore and get "
                         "lost in.")

                if st.button("View location", "31(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Rondane+National+Park/@61.9315189,9.'
                                                '7866922,17z/data=!3m1!4b1!4m5!3m4!1s0x466b2fb4478e6a1f:'
                                                '0xa17e476510d26599!8m2!3d61.9315164!4d9.7888809')




            with col2:



                st.write("## 2. Forlandet National Park")
                st.image("https://cdn.britannica.com/31/170931-050-01221459/Summer-landscape-Spitsbergen-Svalbard-Norway.jpg",caption="Forlandet National Park")
                st.write("""Wow. The landscapes of Forlandet National Park are bewitching in their beauty. Located right
                 on the west coast of the Svalbard archipelago, the park comprises huge swathes of sea as well as the 
                 entirety of Prins Karls Forland Island.""")
                st.write("""Its striking features are awe-inspiring and you will find yourself lost in thought trying to
                 take in every last detail of this magnificent natural realm. The huge alpine mountains and colossal 
                 glaciers dominate Forlandet and sweeping beaches stretch away from them into the distance.""")
                st.write("""Home to the northernmost populations of stone seals and guillemots, they and the walruses 
                who bask on the beaches are amazing to behold in their natural environment. Taking a boat trip around 
                the sea cliffs that tower imposingly above you makes for an unforgettable experience in this wild and 
                beautiful national park.""")

                if st.button("View location", "32(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Forlandet+National+Park,+Svalbard+'
                                                'and+Jan+Mayen/@78.5512159,9.0501493,7z/data=!3m1!4b1!4m5!3m4!'
                                                '1s0x4582da49153a114f:0x22de8c5457641cab!8m2!3d78.5594505!4d11.1614007')

                st.write("## 4.  Femundsmarka National Park")
                st.image("http://www.graenslandet.se/images/stories/nio_skyddade/femundsmarka/topp_MG_2463.jpg", caption="Femundsmarka National Park")
                st.write("""The picturesque sprawling wilderness of Femundsmarka National Park is just begging to be 
                explored. Untouched and untamed, its stunning scenery gives off a feeling of serenity as you traipse 
                your way along the beautiful trails and paths that weave their way among the marshes and lakes that 
                dominate the park.""")
                st.write("""The sparse forests in Femundsmarka add variety to the endless lakes and waterways that so 
                stunningly reflect the clouds and sky above. Slowly paddling along the waterways will soothe your soul 
                and make you want to return time and time again to bask in its peaceful ambiance. Low-lying hills and 
                mountains form a lovely backdrop to the glittering bodies of water and the lonely birds flying overhead 
                complete the incredible scene.""")

                if st.button("View location", "33(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Femundsmarka+National+Park/'
                                                '@62.3193276,12.1495044,17z/data=!3m1!4b1!4m5!3m4!1s0x466c07a044134719:'
                                                '0x6b587e4e00576863!8m2!3d62.3193251!4d12.1516931')


                st.write("## 6. Jostedalsbreen National Park")
                st.image("https://cdn.theculturetrip.com/wp-content/uploads/2018/09/-frank-optun-smedegard.jpg",caption="Jostedalsbreen National Park")
                st.write("Home to the largest glacier in mainland Europe, this natural park is breathtakingly beautiful "
                         "to behold. Gazing over the incredible panoramas that lie before you, your heart will ache with "
                         "the beauty of the scenery such is the splendor on show.")
                st.write("The rocky grey mountains lie impressively between the clear blue skies above and the deep blue"
                         " waters below, while the blindingly bright white snow mesmerizingly reflects in the crystal "
                         "clear lakes and rivers.")
                st.write("Lush green valleys slope away from the peaks and pinnacles, adding color and life to the"
                         " picturesque scenes. Hiking through the diverse landscapes will never cease to amaze even "
                         "regular visitors to the park such are the endless array of awe-inspiring views to enjoy each "
                         "and every time.")

                if st.button("View location", "34(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Jostedalsbreen+National+Park/'
                                                '@61.6565957,6.5428942,9z/data=!4m9!1m2!2m1!1sJostedalsbreen+National'
                                                '+Park!3m5!1s0x461676175364f35f:0xb915a3bc502f8b8b!8m2!3d61.6599253!4d7'
                                                '.0441205!15sChxKb3N0ZWRhbHNicmVlbiBOYXRpb25hbCBQYXJrWh4iHGpvc3RlZGFsc'
                                                '2JyZWVuIG5hdGlvbmFsIHBhcmuSAQ1uYXRpb25hbF9wYXJr')

                st.write("## 8. Folgefonna National Park")
                st.image("https://folgefonna.info/wp-content/uploads/Bondhusdalen-med-bergfrue-1000x664.jpg",caption="Folgefonna National Park")
                st.write("Located on a peninsula from which it draws its name, Folgefonna National Park has a number of"
                         " incredible natural wonders that will entice and delight visitors. Three huge glaciers "
                         "dominate the park’s features and they can impressively reach up to 400 meters in thickness.")
                st.write("As always, the scenic mountains that are so characteristic of Norway protrude and pop up from "
                         "amidst the ice, reaching towards the heavens and dominating the skyline. In summer, the park"
                         " becomes a sea of colors as verdant green grasses, flora and fauna spring to life in the "
                         "sloping valleys that stretch towards the bare and rocky mountains.")
                st.write("Delightful rivers rush between the mountains, hurtling and tumbling their way down to the sea "
                         "and adding their spray to this wet and wild landscape.")

                if st.button("View location", "35(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Folgefonna/@60.0000099,6.3245785,15z'
                                                '/data=!3m1!4b1!4m5!3m4!1s0x463c193d18c1d255:0xe3ea4e55c899292d!8m2!'
                                                '3d60!4d6.3333333')

                st.write("## 10. Jotunheimen National Park")
                st.image("https://storage.googleapis.com/cdn1.jotunheimen.com/sites/7/2019/11/Bridge-near-Gjendebu-1024x683.jpg",caption="Jotunheimen National Park")
                st.write("The glacier scarred terrain of Jotunheimen National Park is fascinating to explore and with "
                         "over 250 peaks reaching above 1900 meters in height; you will have your hands full trying to "
                         "take in all that there is to do and see. The highest peaks in the park, Galdhopiggen and "
                         "Glittertind, are just two of the park’s striking features that are arrestingly beautiful with "
                         "their snow-capped pinnacles glinting in the sun.")
                st.write("Turquoise lakes fill the ravines left behind by the slow-moving glaciers all those eons again"
                         " and they only add to the picturesque scenery on show. Waterfalls and rivers also weave their "
                         "way down the steep and barren mountainsides, their trickling waters ringing out like music in "
                         "the still and peaceful surroundings.")
                st.write("With a plethora of unbelievable sights just waiting to be discovered, head along the winding"
                         " paths to find the ultimate view. One of the most popular national parks in Norway,"
                         " the undoubted highlight of Jotunheimen is the view from Besseggen ridge; breathtakingly "
                         "beautiful it will leave long-lasting memories such is its natural splendor.")

                if st.button("View location", "36(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Jotunheimen+National+Park/'
                                                '@61.5673268,8.407259,11z/data=!4m9!1m2!2m1!1sJotunheimen+National'
                                                '+Park!3m5!1s0x461509455dbac7fb:0x87094ec417f71924!8m2!3d61.5535919!4d8.'
                                                '4842061!15sChlKb3R1bmhlaW1lbiBOYXRpb25hbCBQYXJrWhsiGWpvdHVuaGVpbWVuIG'
                                                '5hdGlvbmFsIHBhcmuSAQ1uYXRpb25hbF9wYXJr')


        if sidbar == 'Tourist Attractions':
            st.title("10 Top Tourist Attractions in Norway")

            st.write("""It’s easy to picture pillaging Vikings and scenic fjords when thinking about Norway.
                                    This land of the summer midnight sun, however, offers much more than that, including picturesque
                                    waterfronts, well-preserved wooden churches and great hiking trails. Quaint medieval towns,
                                    filled with modern amenities, are just waiting to be explored. An overview of the top tourist
                                    attractions in Norway:""")

            col1, col2 = st.beta_columns(2)

            with col1:
                st.write("## 1. Roros")
                st.image(
                    "https://www.fjordtravel.no/wp-content/uploads/2018/08/Christmas-in-Roros-by-Thomas-Rasmus-Juell-Skaug-Visit-Norway.jpg",caption="Roros")
                st.write(
                    """Roros is a good place to learn about copper mining as it occurred a few centuries ago. 
                    Copper mining started there in the 17th century and continued for more than 300 years, 
                    until 1977. The town has about 2,000 wooden houses that have been preserved in their 
                    blackened state, suggesting a medieval look. The town itself was established in 1646 by the
                     Roros Copper Works. Farmlands surround the former mining operation, which include the 
                     remains of a smelter. The town is on the Winter Transport Route that used frozen lakes, 
                     streams and rivers to move people and goods.""")

                if st.button("View location", "37(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/R%C3%B8ros+Municipality,+Norway/'
                                                '@62.5690339,11.129197,9z/data=!3m1!4b1!4m5!3m4!1s0x466c6c3d7bf32c5b:'
                                                '0x892bda66c4a6f3bb!8m2!3d62.5749358!4d11.3842621')

                st.write("## 3. Urnes Stave Church")
                st.image(
                    "https://upload.wikimedia.org/wikipedia/commons/1/12/Urnes_Stave_Church_1.jpg",caption="Urnes Stave Church")
                st.write("""The Urnes Stavkyrkje, or Urnes Stave Church, blends several architectural styles
                                        into a medieval church that is still standing after 900 years. What is remarkable about this
                                         church, however, is the building material used: wood, instead of the traditional stone. 
                                         Located on Norway’s west coast, the church blends Celtic, Viking and Romanesque features in 
                                         a church that stands majestically in the woods. Urnes is one of 28 stave (wooden) churches 
                                         in Norway as well as one of the oldest, having been built in the 12th century. Artifacts 
                                         link pre-Christian Norse culture with medieval Christianity.""")

                if st.button("View location", "38(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Urnes+Stave+Church/'
                                                '@61.2979798,7.320766,17z/data=!3m1!4b1!4m5!3m4!1s0x4615f21ebe9d2f03:'
                                                '0xbc6c60d01e4a5d74!8m2!3d61.2979982!4d7.3228119')

                st.write("## 5.  Voringfossen")
                st.image(
                    "https://upload.wikimedia.org/wikipedia/commons/f/fb/V%C3%B8ringfossen.jpg",caption="Voringfossen")
                st.write("""Vøringfossen is Norway’s most famous waterfall, cascading down 180 meters (600 feet)4
                                       in a series of drops, though it ranks only 83rd on the list of Norway’s highest waterfalls. 
                                       Vøringfossen is located at Mabodelen, a narrow valley between Oslo and Bergen. 
                                       Tourists have been visiting Vøringfossen for almost 200 years; a hotel built in 1880 at the top 
                                       required guests to walk up 1,500 steps to reach their accommodations. The top is easier to 
                                       reach these days, but the falls aren’t as powerful as they once were because of a hydroelectric
                                       plant built upstream.""")

                if st.button("View location", "39(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/V%C3%B8ringfossen/'
                                                '@60.4258078,7.2497179,17z/data=!3m1!4b1!4m5!3m4!1s0x463e5fb3c511f01f:'
                                                '0x922df9ae6d08d909!8m2!3d60.4265721!4d7.2514658')

                st.write("## 7. Nidaros Cathedral")
                st.image(
                    "https://afar-production.imgix.net/uploads/images/post_images/images/bN5tLU4BUu/original_a09a3913571ee7964d6b6118cf65cbfd.jpg?1509128544?ixlib=rails-0.3.0&auto=format%2Ccompress&crop=entropy&fit=crop&h=719&q=80&w=954",caption="Nidaros Cathedral"
                    )
                st.write("""While William the Conqueror was busy invading Great Britain in 1066, the Vikings
                                       were occupied with building Nidaros Cathedral in Trondheim. Nearly 1,000 years later, the
                                       cathedral is Norway’s most important church and Scandinavia’s largest medieval building.
                                       The cathedral was built to honor Olav, a Viking chieftain who later became a king and a
                                       saint. Olav was killed in a battle near Trondheim in 1030; his nephew began constructing
                                       the Nidaros Cathedral in 1066 to house his body; it was basically finished in 1090, though
                                       enlargements continued until the 1300s. The cathedral soon became an important pilgrimage
                                       destination in Norway.""")

                if st.button("View location", "40(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Nidaros+Cathedral/'
                                                '@63.4268824,10.3883313,16z/data=!4m9!1m2!2m1!1sNidaros+Cathedral!3m5!'
                                                '1s0x466d31908505a019:0xb965bfe4f7eb71fd!8m2!3d63.4271125!4d10.3969237!'
                                                '15sChFOaWRhcm9zIENhdGhlZHJhbFoTIhFuaWRhcm9zIGNhdGhlZHJhbJIBCWNhdGhlZHJhbA')

                st.write("## 9. Nordkapp")
                st.image(
                    "https://thumbs.dreamstime.com/b/nordkapp-globe-monument-north-cape-norway-midnight-nordkapp-92988717.jpg",caption= "Nordkapp")
                st.write(
                    """Nordkapp, or North Cape, is a must for travelers who want to frolic under the midnight
                    sun, since the sun never sets between May 14 and July 29. It is the northernmost point in
                    Europe connected with the international road network. Because it’s in the far north, rising
                    300 meters (1,000 feet) above the Arctic Ocean, Nordkapp is mainly a summer destination,
                    attracting about 200,000 visitors annually. Nordkapp offers stunning scenic views, with
                    plenty of opportunities to hike under the Arctic sun or see puffin in their native
                    habitat.""")

                if st.button("View location", "41(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Nordkapp+Municipality,+Norway/'
                                                '@71.018112,24.8694219,8z/data=!3m1!4b1!4m5!3m4!1s0x45c9ac1de7e8bee7:'
                                                '0xef6625f3cd0ce069!8m2!3d71.169493!4d25.7831639')

            with col2:
                st.write("## 2. Jostedalsbreen Glacier")
                st.image(
                    "https://i.pinimg.com/originals/aa/70/ff/aa70ff29d7ede9ca91451657c34e2346.jpg",caption="Jostedalsbreen Glacier")
                st.write("""Icy and scenic is perhaps the best way to describe Jostedalsbreen Glacier, the
                                       largest glacier in Europe. Situated in southern Norway, the glacier is surrounded by
                                       Jostedalsbreen Glacier National Park. Many, many years ago, locals could cross the glacier
                                       on foot, perhaps herding animals on their way to market, but this isn’t possible today as
                                       the glacier has shrunk significantly. Hiking and glacial skiing is allowed, but sportsmen
                                       need to be well prepared as these activities can be dangerous. It is much safer, and just
                                       as pretty, to take one of the walking tours around the park.""")

                if st.button("View location", "42(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Jostedalsbreen/'
                                                '@61.7105654,6.9154122,15z/data=!3m1!4b1!4m5!3m4!1s0x46167787ce10e3bb:'
                                                '0x5263bfe8f27add72!8m2!3d61.710556!4d6.924167')

                st.write("## 4. Viking Ship Museum ")
                st.image("https://image.sciencenorway.no/1574030.jpg?imageId=1574030&width=480&height=274",caption=" Viking Ship Museum")
                st.write("""Many centuries ago, the Vikings sailed the northern seas, striking fear in the
                                       hearts of the region these fierce warriors were about to invade. Today, visitors can view,
                                       unafraid, some of these terror-causing vessels as the Viking Ship Museum in Oslo showcases
                                       some of these great ninth century ships. The list includes ships from Gokstad, Oseberg and
                                       Tune, including two of the best preserved wooden ships in the world from that era. The
                                       Oseberg ship is the best preserved and was found in a burial mound on a farm near Oseberg.
                                       The museum also displays textiles, tools and household items as well as items found in
                                       Viking tombs.""")

                if st.button("View location", "43(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Viking+Ship+Museum/'
                                                '@59.9049475,10.6822188,17z/data=!3m1!4b1!4m5!3m4!1s0x46416c38363f15fd:'
                                                '0x43a6abff981ee007!8m2!3d59.9046057!4d10.6848567')

                st.write("## 6. Heddal Stave Church")
                st.image("https://upload.wikimedia.org/wikipedia/commons/d/d5/Stavechurch-heddal.jpg",caption=" Heddal Stave Church")
                st.write(
                    """The Heddal Stave Church is Norway’s largest stave church, with triple naves that stand
                    proudly against the sky. The church, made entirely of wood, was built in the 13th century;
                    according to local legend, it was built in three days by five farmers. After restorations
                    in the 19th and 20th centuries, the church is still in use today for weddings and Sunday
                    services during the summer months. Located in Notodden, the church is dedicated to the
                    Virgin Mary.""")

                if st.button("View location", "44(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Heddal+stave+church/'
                                                '@59.5795791,9.1740784,17z/data=!3m1!4b1!4m5!3m4!1s0x4640b44d9f2a2ac7:'
                                                '0x6cdec98823674361!8m2!3d59.5795764!4d9.1762671')

                st.write("## 8. Bryggen")
                st.image(
                    "http://res.cloudinary.com/simpleview/image/upload/v1450085114/clients/norway/2-1_a20a4c7b-983a-44ff-8eb6-8e9a21af9149.jpg",caption=" Bryggen")
                st.write(
                    """Travelers who get “museumed” out may enjoy a visit to the Bryggen waterfront, an
                    informal museum that doesn’t seem like a museum. Traditional buildings line the waterfront
                    with boats tied just feet away on Bergen’s seaside. The scene is so picturesque, visitors
                    can easily forget Bryggen is linked to Bergen’s importance as a trading center for 400
                    years during the Middle Ages, when it was part of the Hanseatic League. Today’s traders can
                    shop in trendy boutiques, visit craftsmen’s studios or enjoy a bite to eat down a narrow
                    alleyway.""")

                if st.button("View location", "45(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Bryggen/'
                                                '@60.3973512,5.3204671,16z/data=!4m9!1m2!2m1!1sBryggen!3m5!1s0x463cf'
                                                'c1d80be31e1:0xf278657d7d75232e!8m2!3d60.3975672!4d5.3245493!15sCgdCcn'
                                                'lnZ2VuWgkiB2JyeWdnZW6SAQ1oaXN0b3JpY19zaXRl')

                st.write("## 10.  Geirangerfjord")
                st.image("http://res.cloudinary.com/simpleview/image/upload/v1450117455/clients/norway/unesco-geirangerfjord-skagefla-waterfall-2-1_6cc6a64a-a204-432e-8753-01ef2080f24e.jpg",caption="Geirangerfjord")
                st.write(
                    """The most famous tourist attractions in Norway are probably it fjords. Among the most 
                    beautiful of these fjords is Geirangerfjord, located in southwestern Norway near the 
                    coastal town of Ålesund. Stretching for more than 15 km (9 miles) long, Geirangerfjord is a 
                    natural wonder of deep blue water surrounded by majestic cliffs and lush green mountains 
                    towering more than 1,000 meters (3,500 feet) high. Adding to the spectacular scenery are 
                    several stunning waterfalls and lush countryside dotted with picturesque farms.""")

                if st.button("View location", "46(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Geirangerfjord/'
                                                '@62.1049113,7.0051735,12z/data=!3m1!4b1!4m5!3m4!1s0x46169d427b268c51:'
                                                '0xb8c99540dcc397fe!8m2!3d62.101506!4d7.0940817')

        if sidbar == 'Best Resorts':

            st.title("10 Best Resorts in Norway......")

            col1, col2 = st.beta_columns(2)

            with col1:



                st.write("## 1.  Walaker Hotel")
                st.image("https://images.squarespace-cdn.com/content/v1/5a3a61a24c326d14dc9fcc90/1576146685784-QWBBTNDQMHZZJQ1YZ6WV/Walaker+Hotell+2019+Nettside.jpg", width=500, caption="Walaker Hotel")
                st.write("""Make yourself at home in one of the 22 individually decorated guestrooms. Your room comes 
                         with a pillowtop bed. Complimentary wireless Internet access is available to keep you connected. Private 
                         bathrooms with bathtubs or showers feature complimentary toiletries and hair dryers.
                         Take in the views from a terrace and a garden and make use of amenities such as complimentary wireless 
                         Internet access. This hotel also features concierge services, wedding services, and a picnic area.
                         Located in Luster, Walaker Hotel is by the sea, a 1-minute drive from Sogne Fjord and 8 minutes from 
                         Sogn Ski Center.""")


                if st.button("View location", "47(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Walaker+Hotell/@61.301878,7.2455906,'
                                                '17z/data=!3m1!4b1!4m8!3m7!1s0x4615f0351e222f23:0x76828644169701d3!5m2!'
                                                '4m1!1i2!8m2!3d61.3018744!4d7.2477864')

                if st.button("Book now", "60(id)"):
                    webbrowser.open_new_tab(url='https://theculturetrip.com/europe/norway/bookable/walaker-hotel-e24330450')


                st.write("## 3. Snowhotel Kirkenes")
                st.image("https://www.uniqhotels.com/media/hotels/13/1.jpg", width=500, caption="Snowhotel Kirkenes")
                st.write(
                    """Make yourself at home in one of the 20 individually decorated guestrooms. Complimentary wireless
                     Internet access is available to keep you connected. Bathrooms feature shower/tub combinations, 
                     complimentary toiletries, and hair dryers. Conveniences include free tea bags/instant coffee,
                     and housekeeping is provided daily.
                     Take advantage of recreation opportunities such as a sauna, or other amenities including complimentary
                     wireless Internet access and concierge services.
                     Located in South Varanger, Snowhotel Kirkenes is in the mountains, within a 15-minute drive of 
                     Varanger Museum and Savio Museum.""")
                if st.button("View location", "48(id)"):
                    webbrowser.open_new_tab(url='https://www.google.com/maps/place/Snowhotel+Kirkenes+%26+Gamme+'
                                                'Northern+Lights+Cabins/@69.6768271,29.9023945,17z/data=!3m1!4b1!4m8!'
                                                '3m7!1s0x45cb4f72b09eb325:0x949074e2ce426bd0!5m2!4m1!1i2!8m2!3d69.'
                                                '6767922!4d29.9048842')
                if st.button("Book now", "59(id)"):
                    webbrowser.open_new_tab(url='https://theculturetrip.com/europe/norway/bookable/snowhotel-kirkenes-e33802052')



                st.write("## 5. Det Hanseatiske Hotel")
                st.image("https://i.travelapi.com/hotels/2000000/1540000/1532900/1532876/adb00270_z.jpg", width=500, caption="Det Hanseatiske Hotel")
                st.write(
                    """Make yourself at home in one of the 37 individually decorated guestrooms. Complimentary wireless
                     Internet access keeps you connected, and satellite programming is available for your entertainment. 
                     Conveniences include safes and desks, and housekeeping is provided daily.
                     Make use of convenient amenities such as complimentary wireless Internet access, tour/ticket assistance, and a banquet hall.
                     A stay at Det Hanseatiske Hotel places you in the heart of Bergen, within a 15-minute walk of Bryggen and Hurtigruten Terminal.""")
                if st.button("View location", "49(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/The+Hanseatic+Hotel/@60.3960386,'
                                                    '5.324114,17z/data=!3m2!4b1!5s0x463cfea7bf95421b:0xa146d7d1a4cb9587!'
                                                    '4m8!3m7!1s0x463cfea7bf372f0d:0xf8cb4a930313dc56!5m2!4m1!1i2!8m2!'
                                                    '3d60.396036!4d5.3263027')

                if st.button("Book now", "58(id)"):
                    webbrowser.open_new_tab(url='https://en.dethanseatiskehotel.no/?gclid=CjwKCAjw55-HBhAHEiwARMCszocW5b'
                                                'QJP70NNAwV8v311OyXUenqojN6QmwadKcFVfcUKfd6OuS3CRoCMWwQAvD_BwE&gclsrc=aw.ds')

            with col2:



                st.write("## 2. Gudvangen Fjordtell ")
                st.image("https://i.travelapi.com/hotels/4000000/3960000/3952800/3952777/cc6e84d1_z.jpg", width=500, caption="Gudvangen Fjordtell")
                st.write(
                    """Make yourself at home in one of the 37 guestrooms. Complimentary wireless Internet access keeps 
                    you connected, and cable programming is available for your entertainment. Private bathrooms with 
                    showers feature complimentary toiletries and hair dryers. Conveniences include coffee/tea makers, 
                    housekeeping is provided daily, and cribs/infant beds (surcharge) can be requested.Take in the views 
                    from a terrace and a garden and make use of amenities such as complimentary wireless Internet access. 
                    Additional amenities at this hotel include gift shops/newsstands, a fireplace in the lobby, 
                    and tour/ticket assistance.With a stay at Gudvangen Fjordtell, you'll be centrally located in 
                    Aurland, steps from Car Ferry Cruise Kaupanger - Gudvangen and within a 5-minute walk of Viking Valley.""")
                if st.button("View location", "52(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Gudvangen+Fjordtell/@60.9360676,'
                                                    '6.7943671,11z/data=!4m12!1m2!2m1!1sGudvangen++Fjordtell!3m8!'
                                                    '1s0x463e0964f2448295:0xa02c18b2883db199!5m2!4m1!1i2!8m2!3d60.'
                                                    '8808756!4d6.8415657!15sChRHdWR2YW5nZW4gRmpvcmQgVGVsbFoRIg9ndWR2Y'
                                                    'W5nZW4gZmpvcmSSAQVob3RlbJoBI0NoWkRTVWhOTUc5blMwVkpRMEZuU1V'
                                                    'Nd2EyOHRWa1JuRUFF')

                if st.button("Book now", "57(id)"):
                    webbrowser.open_new_tab(url='https://theculturetrip.com/europe/norway/bookable/gudvangen-fjordtell-e3952777')

                st.write("## 4. Hotel Brosundet")
                st.image("https://i.travelapi.com/hotels/1000000/900000/891800/891768/3f1048e4_z.jpg", width=500, caption="Hotel Brosundet")
                st.write(
                    """Stay in one of 131 guestrooms featuring flat-screen televisions. Your room comes with a 
                    pillowtop bed. Complimentary wireless Internet access keeps you connected, and cable programming is
                    available for your entertainment. Bathrooms have showers and hair dryers.Take advantage of
                    recreation opportunities such as a fitness center, or other amenities including complimentary
                    wireless Internet access and concierge services.A stay at Hotel Brosundet places you in the heart
                    of Alesund, steps from Jugendstilsenteret and 5 minutes by foot from Alesund Church.""")
                if st.button("View location", "53(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Hotel+Brosundet/@62.4724542,6.'
                                                    '1500454,17z/data=!4m16!1m6!2m5!1sHotel++Brosundet!5m3!5m2!4m1!1i2!'
                                                    '3m8!1s0x4616da38955f5a8b:0xd938d3ad26b4a8c!5m2!4m1!1i2!8m2!3d62.'
                                                    '4724575!4d6.1522579!15sChBIb3RlbCAgQnJvc3VuZGV0WhEiD2hvdGVsIGJyb3N'
                                                    '1bmRldJIBBWhvdGVs')

                if st.button("Book now", "56(id)"):
                    webbrowser.open_new_tab(url='https://theculturetrip.com/europe/norway/alesund/bookable/hotel-brosundet-e891768')

                st.write("## 6. The Arctic Hideaway")
                st.image("https://img.theculturetrip.com/768x/smart/wp-content/uploads/2020/12/the-arctic-hideaway.jpg", width=500, caption="The Arctic Hideaway")
                st.write(
                    """The Arctic Hideaway offers an experience like no other. Found on the remote northern Norwegian
                    island of Sorvaer, this car- and shop-free destination has only a twice-daily ferry to and from
                    the mainland. There are ten small, eco-friendly, highly designed houses here. Four are for
                    sleeping, while the rest are for bathing, cooking, eating and relaxing. There is also a
                    wood-fired sauna.""")
                if st.button("View location", "54(id)"):
                        webbrowser.open_new_tab(url='https://www.google.com/maps/place/Fordypningsrommet+Fleinv%C3%A6r'
                                                    '-+the+Arctic+hideaway/@67.1612415,13.7647731,17z/data=!3m1!4b1!4m8'
                                                    '!3m7!1s0x45df9ffb08cf61b7:0xb865945224b113f8!5m2!4m1!1i2!8m2!3d67.'
                                                    '1612394!4d13.7669618')

                if st.button("Book now", "55(id)"):
                    webbrowser.open_new_tab(url='https://thearctichideaway.com/en/')








    if countryselect == 'Spain':

        st.sidebar.title("...Spain...")
        st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/500px-Flag_of_Spain.svg.png", width=150)
        sidbar = st.sidebar.radio("", ("About", "Best beaches", "Best cities", "Best resorts",
                                       "Best national Parks"))

        if sidbar == 'About':
            st.title("Welcome to Spain")

            col11, col22 = st.beta_columns(2)

            with col11:
                st.balloons()
                st.image("https://www.mapsland.com/maps/europe/spain/large-physical-map-of-spain-with-roads-cities-and-airports.jpg", width=500)
                st.write(
                    "Splendid beaches, delicious cuisine, vibrant nightlife and lively fiestas all make Spain one of Europe’s best getaways." 
                    "Because Spain encompasses several autonomous regions and islands, the country boasts one of the most widely diverse cultures and landscapes on the continent. From the unique Basque Country in the North to the Costa del Sol beach resorts and Sierra Nevada mountain range in the South to the exotic beauty of the Canary Islands"
                     "Spain offers a wide variety of geographical contrasts and cultural diversity.")
                st.write(
                    "Some of Spain’s most visited cities include the capital, Madrid, with its Royal Palace, dazzling plazas and vibrant nightlife while Barcelona boasts its Gothic Quarter, intriguing architecture, beautiful beaches and the world’s largest football stadium. Not to be overlooked are the bustling cities of Seville, Cordoba and Granada in Andalusia.")
                st.write(
                    "It would be impossible to see all of Spain’s marvelous attractions during one vacation, so tourists are recommended to pick one region as a base and explore popular sites by day trips. Some of the most visited attractions around the country include Madrid’s Palacio Real, the lavish residence of the Spanish Royal family, and the Sagrada Familia in Barcelona, Antonio Gaudi’s uncompleted masterpiece.")

            with col22:
                st.image("https://th.bing.com/th/id/OIP.6bAOlQsttufO_OjxXwfEhAHaEK?pid=ImgDet&rs=1", width=500)
                st.title("")
                st.image("https://q-xx.bstatic.com/xdata/images/hotel/max1280x900/111621689.jpg?k=75b85879ad9fc07bf534148aa873201e93c5a67d8099f764e88eada18c27ad95&o=")
                st.write("")
                st.image("https://img.theculturetrip.com/1440x807/wp-content/uploads/2020/04/gettyimages-638351438.jpg")

                if st.button("View location", "1(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Spain/@40.6502907,-3.9661501,7.75z/data=!4m5!3m4!1s0xc42e3783261bc8b:0xa6ec2c940768a3ec!8m2!3d40.463667!4d-3.74922')

            st.video("https://www.youtube.com/watch?v=L5JORXmV_A0")
            st.video("https://www.youtube.com/watch?v=KnLsngMT5Eg")

        if sidbar == 'Best beaches':
            st.title("10 Best Beaches in Spain......")

            col1, col2 = st.beta_columns(2)

            with col1:

                # Beach1
                st.write("## 1. Burriana Beach, Nerja")
                st.image(
                    "https://www.touropia.com/gfx/d/best-beaches-in-spain/burriana_beach_nerja.jpg?v=5e2e86a4278e61d9bbaae0d83b6fe966",
                    width=500, caption="Burriana Beach,")
                st.write(
                    "Edged by a long promenade that brims with shops and popular restaurants and bars, this 800-metre-long beach is a favorite of many of the locals in the area. As such, you can find a large range of people enjoying socializing and spending time with friends and family.")
                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/search/Burriana+Beach,+Nerja/@36.7507898,-3.8702097,17z/data=!3m1!4b1')

                st.write(
                    "Burriana has really excellent amenities: showers, playgrounds for children, as well as toilets and a lifeguard, which makes it a really excellent place for families with small children to visit on holiday. If you fancy something a little more exciting, there’s the chance to take out jet-skis or try parasailing. And at the end of the day, check out the spectacular sea-views from clifftop Balcón de Europa.")

                # Beach3
                st.write("## 3. Cala D’en Serra, Ibiza")
                st.image(
                    "https://www.touropia.com/gfx/d/best-beaches-in-spain/cala_d_en_serra.jpg?v=56a1c274454159b688f020bf577722ce",
                    width=500, caption="Cala D’en Serra")
                if st.button("View location", "3(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Cala+d%E2%80%99en+Serra/@39.1071768,1.5207571,14z/data=!3m1!4b1!4m5!3m4!1s0x129917ca302d49b5:0xa882d6aa82a08eaf!8m2!3d39.1071454!4d1.5382667')
                st.write(
                    "Everyone knows Ibiza is party central, but what do you do once the party’s over and you need to rejuvenate yourself? Head to the beach of course and Cala D’en Serra is the ideal spot. One of those beaches that isn’t an obvious tourist spot, Cala d’en Serra is an egg-shaped beach that needs a little insider knowledge to find.")
                st.write(
                    "One singular beach bar serves up fresh fish and sangria straight to your sunbed as you soak up the sublimely sleepy and chilled out atmosphere and secret beach spot. It may not have popping beach clubs or even any amenities, but away from the buzz of the main beaches on the island, Cala D’en Serra offers a slice of sun-soaked seclusion.")

                # Beach5
                st.write("## 5.  Sitges")
                st.image(
                    "https://www.touropia.com/gfx/d/day-trips-from-barcelona/sitges.jpg?v=a5fd543ef49a0dd5b2e5f2728de154f2",
                    width=500, caption=" Sitges")
                if st.button("View location", "4(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/08870+Sitges,+Barcelona,+Spain/@41.2359475,1.7684434,13z/data=!3m1!4b1!4m5!3m4!1s0x12a3804720b208fb:0x7061f1fb2907c8f9!8m2!3d41.2371851!4d1.805886')
                st.write(
                    "With a beautiful natural backdrop of Parc Natural del Garraf and mansions lining the seafront boulevard, Sitges is a liberal town famous for its coastline, sun-worshipers and gay-friendly atmosphere, including bars, nightclubs – and, of course, beache")
                st.write(
                    "The most renowned of these is the Platja de la Bassa Rodona, a 285-metre stretch of soft sand and calm water where the atmosphere is surprisingly relaxed. Elsewhere, the Platja de la Fragata is a buzzing, family-friendly beach overlooked by the charming church of Sant Bartomeu. Near to town, Platja de la Ribera is one of the most popular beaches and is the place to go to people-watch on the sand.")
                st.write(
                    "Away from the coastline, however, there are ample opportunities to explore the island’s dense "
                    "vegetation, thanks to a number of hiking trails that crisscross through it.")

                # Beach7
                st.write("## 7. La Concha, Perhentian Kecil")
                st.image("https://www.touropia.com/gfx/d/tourist-attractions-in-spain/la_concha.jpg?v=1", width=500,
                         caption=" La Concha")
                if st.button("View location", "5(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Beach+of+La+Concha/@43.3174306,-2.0001452,15z/data=!3m1!4b1!4m5!3m4!1s0xd51baa91847a353:0x2cdefc6d7978bef3!8m2!3d43.3186188!4d-1.9860118')
                st.write(
                    "This small beach in the Basque country is edged by green mountains and boasts views of pretty islands and white boats that bob on the gentle waves. La Concha beach is part of a charming town that is full of elegant Belle Epoque-style architecture and is almost overflowing with excellent dining options.")
                st.write(
                    "The beach itself is tucked away in a sheltered bay and has even sometimes been referred to as the most beautiful city beach in Europe. Protected by the mountainous countryside, La Concha is a huge 1350 meters long and as it is affected by tides, there’s more than enough room for everyone to enjoy its beauty.")
                st.write(
                    "Snorkeling, splashing around in the water and catching some rays are the order of the day at"
                    " this exquisite beach.")

                # Beach9
                st.write("## 9. Isuntza Beach, Lekeitio")
                st.image(
                    "https://www.touropia.com/gfx/d/best-beaches-in-spain/isuntza_beach.jpg?v=da41db08d80158beacaaabb90e20f7af",
                    width=500, caption="Isuntza Beach, Lekeitio")
                if st.button("View location", "6(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Isuntza/@43.3632968,-2.5023682,17z/data=!3m1!4b1!4m5!3m4!1s0xd4e26df4147cab5:0x48858924f190fa46!8m2!3d43.3634474!4d-2.5003011')
                st.write(
                    "Situated midway between Bilbao and San Sebastian, this tiny little town is home to a very picturesque beach. The magic of this pretty part of the coast is revealed at low tide when a sandy path is uncovered that leads all the way to the ever-intriguing San Nicolás Islan.")
                st.write(
                    "Walk over the stony pathway and explore the island – just be sure to make it back before the tide starts coming in again! Isunza Beach’s landscape is shaped by the mouth of the Lea River that opens out into the sea here, which adds to the unique appeal of the already pretty scenery")
                st.write(
                    "Staying in the town means a rare glimpse into the culture of the Basque country, enjoy its amazing food and gothic architecture – there’s even a mountain to climb where you can take in views over the beach and across to the island.")

            with col2:

                # Beach2
                st.write("## 2. Tossa De Mar")
                st.image("https://www.touropia.com/gfx/d/best-beaches-in-spain/tossa_de_mar.jpg?v=1", width=512,
                         caption=" Tossa De Mar")
                if st.button("View location", "7(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Tossa+de+Mar,+17320,+Girona,+Spain/@41.7393936,2.8493258,12z/data=!3m1!4b1!4m5!3m4!1s0x12bb10014aa10459:0x4a381fc677e338d8!8m2!3d41.7225184!4d2.9302653')
                st.write(
                    "Tossa De Mar is a special little town in the Costa Brava with a whole host of beaches to choose from. Protected by a large bay, the wide horseshoe-shaped, family-friendly beach of Playa Gran has soft golden sands and deep blue waters that are a favorite with swimmers")
                st.write(
                    "But the most special thing about this elegant beach is the 14th-century fortifications that sit up on the rocky headlands overlooking the bay. These are stunningly illuminated at night. For a different vibe, Platja d’es Codolar is a small beach with a bar set in cove at the bottom of towering cliffs.")
                st.write(
                    "If you want to escape from all the touristy beaches of the area, head to north along the coast: the seclusion at the relaxed and natural-feeling Cala Pola just outside of town easily beats them all.")

                # Beach4
                st.write("## 4. Playa de Bolonia, Tarifa")
                st.image(
                    "https://www.touropia.com/gfx/d/best-beaches-in-spain/playa_de_bolonia.jpg?v=2d3799e4f238791261981ad7011198de",
                    width=500, caption="Playa de Bolonia, Tarifa")
                if st.button("View location", "8(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/11391+Bolonia,+Spain,+C%C3%A1diz,+Spain/@36.0887444,-5.7766973,17z/data=!3m1!4b1!4m5!3m4!1s0xd0c60f8fee9e237:0xe076c14f80a37b6d!8m2!3d36.0887959!4d-5.7745904')
                st.write(
                    "Untouched and idyllic, Playa de Bolonia is a quiet beach that is part of a tiny traditional fishing village which also plays host to the 2,000-year-old ruins of the Roman city of Baelo Claudia. A favorite among many Spanish people, the beach is gaining popularity with international tourists, but still somehow remains a hidden gem of beaches; the area is actually within the boundaries of the Estrecho Natural Park.")
                st.write(
                    "The town hasn’t undergone much of the highrise construction that many of Spain’s beach towns have seen and as such the village is undeveloped and still charmingly old fashioned. With Tarifa poised as the home of Spain’s kitesurfing scene, there is also a small chilled out surfing scene at Bolonia with a couple of surf schools and small bars serving travelers.")

                # Beach6
                st.write("## 6. Platja de Ses Illetes, Formentera")
                st.image(
                    "https://www.touropia.com/gfx/d/best-beaches-in-spain/platja_de_ses_illetes.jpg?v=b3dbfdc38c6aca165a0ec14c3ba53fa7",
                    width=500, caption="Platja de Ses Illetes")
                if st.button("View location", "9(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Platja+de+Ses+Illetes/@38.7595965,1.4335382,17z/data=!3m1!4b1!4m5!3m4!1s0x12995b8e03e6d0a1:0x414fe98c309524f9!8m2!3d38.7595283!4d1.4356921')
                st.write(
                    "Crystalline waters lap onto pure white sands where you can lay for hours immersed in paradise. The beach is actually only a small strip sand that juts out into the ocean and divides the sea in two.")
                st.write(
                    "This beautiful beach has to be seen to be believed. Often cited as one of the most beautiful beaches in Spain, Platja de Ses Illetes is up there in terms of beauty with some Caribbean counterparts.")
                st.write(
                    "Whilst the beach is unreal, it’s also known for the conservation of sea turtles, with the Juara "
                    "Turtle Project managing a hatchery here.")

                # Beach8
                st.write("## 8. Maspalomas, Gran Canaria")
                st.image(
                    "https://www.touropia.com/gfx/d/best-beaches-in-spain/platja_de_ses_illetes.jpg?v=b3dbfdc38c6aca165a0ec14c3ba53fa7",
                    width=500, caption="Maspalomas")
                if st.button("View location", "1(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/35100+Maspalomas,+Las+Palmas,+Spain/@27.7565914,-15.6404122,12z/data=!3m1!4b1!4m5!3m4!1s0xc3f62bb27da5c45:0x682c6281a96f26a2!8m2!3d27.7605619!4d-15.5860172')
                st.write(
                    "Sophisticated and stylish, Maspalomas beach on the southern part of Gran Canaria is all about its sand. A huge 6-kilometre stretch of golden sand which is incredibly 100 meters wide at some points, Maspalomas is fringed by a desert landscape of huge sand dunes that will make it seem like you are soaking up the sun in the Saharan desert rather than along a Spanish coastline")
                st.write(
                    "The gold of the dunes set against the dazzling blue of the sea creates spectacular scenery, further along beachgoers sleep on sunloungers and cafes sell snacks and soft drinks")
                st.write(
                    "A great beach for families to spend time together, there is a space here for everyone. If sunbathing for hours isn’t your thing, there’s also the opportunity to hire a pedalo or a jet-ski and have an adventure out at sea")

                # Beach10
                st.write("## 10.Praia da Rodas, Galicia")
                st.image(
                    "https://www.touropia.com/gfx/d/beach-holiday-destinations-in-spain/maspalomas.jpg?v=75994e6f94b880a149bb59ecc66af7dd",
                    width=500, caption="Praia da Rodas")
                if st.button("View location", "10(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Playa+de+Roda/@42.2240096,-8.9037615,17z/data=!3m1!4b1!4m5!3m4!1s0xd2f5f6a6fc00439:0x2ca549a4f14d683d!8m2!3d42.2238459!4d-8.9028051')
                st.write(
                    "This beach is one of those amazing places that once you’ve been to you will never forget. A perfectly curved sandy crescent, Praia da Rodas is a breathtakingly beautiful beach that could be one of the best in the whole of the world. Located in Galicia along the more untamed Atlantic coastline, Praia da Rodas is a romantically attractive swathe of powdery sand.")
                st.write(
                    "Often referred as ‘Caribbean beach’ by local people, the water is dazzlingly turquoise, clean and calm, although very cold compared to the Mediterranean. Spend long summer days lazing on the sand, taking in the beauty of the surrounding nautical scenery; enjoy fresh seafood served on the shore and then spend the night under the stars at the nearby campsite.")

        if sidbar == 'Best cities':
            st.title("15 Best Cities to Visit in Spain......")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1. Barcelona")
                st.image("https://www.touropia.com/gfx/b/2018/02/Magic_Fountain.jpg", width=500, caption="Barcelona")
                st.write(
                    "Bathed in sunshine, the capital city of Catalunya is mesmerizing to navigate, thanks to its incredible architecture that spans the ages. The old Gothic quarter is an intriguing mishmash of narrow alleys, huge cathedrals and peaceful plazas, while other neighborhoods are home to some of Gaudi’s inspired creations, such as La Sagrada Familia – the iconic landmark of the ci")
                st.write(
                    "Lying next to the sea, there are some great seafood restaurants to check out, as well as the city’s lovely beaches with a range of water activities to enjoy. Dripping with culture, fine cuisine, and with a lively buzz to it, wandering along streets such as the famous Ramblas makes Barcelona a delight to visit.")

                if st.button("View location", "1(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Barcelona,+Spain/@41.3949627,2.0086849,11z/data=!3m1!4b1!4m5!3m4!1s0x12a49816718e30e5:0x44b0fb3d4f47660a!8m2!3d41.3850639!4d2.1734035')

                st.write("## 3. Malacca")
                st.image("https://www.touropia.com/gfx/b/2018/07/madrid.jpg", width=500, caption="Malacca")
                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Malacca,+Malaysia/@2.2377154,102.1114189,11z/data=!3m1!4b1!4m5!3m4!1s0x31d1ee278e8c65dd:0x32a7281769e016a!8m2!3d2.189594!4d102.2500868')
                st.write(
                    "Lying on the west coast of the Spainn peninsula, Malacca  is a unique place to"
                    " visit due to the , Dutch and Portuguese all having ruled here at one point. As such, there"
                    " is a wealth of lovely architecture to explore, with each nation having left its mark in "
                    "terms of the buildings left behind and the cultural impact that they had.")

                st.write(
                    "With a lively night market and a wide range of different cuisines on offer, this charming city is"
                    " understandably a popular tourist destination in Spain.")

                st.write("## 5. Madrid")
                st.image(
                    "https://www.touropia.com/gfx/d/where-to-stay-in-gran-canaria/las_palmas_gran_canaria.jpg?v=ce3594ce2a8441806610574d2c34d281",
                    width=500, caption="Madrid")
                if st.button("View location", "3(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Madrid,+Spain/@40.4381388,-3.9597174,10z/data=!3m1!4b1!4m5!3m4!1s0xd422997800a3c81:0xc436dec1618c2269!8m2!3d40.4167754!4d-3.7037902')
                st.write(
                    "Once funded by the Spanish royals, its incredible galleries and museums are home to the best of Picasso, Dali, Goya, and more, with sumptuous masterpieces everywhere you look. It’s gastronomic scene is one to savor, as creative and innovative food styles make the restaurants a culinary delight. If you’re looking for some fun well into the early hours, Madrid has a thriving and lively nightlife scene.")
                st.write(
                    "The capital of Andalusia has some fascinating palaces, churches and streets to explore, with the medieval Jewish quarter the area that most tourists gravitate towards. With Moorish influences on show, Seville has a rich cultural heritage to delve into.")

                st.write("## 7. Seville")
                st.image("https://www.touropia.com/gfx/b/2018/07/seville.jpg", width=500, caption="Seville")
                if st.button("View location", "4(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Seville,+Spain/@37.3754865,-6.025098,12z/data=!3m1!4b1!4m5!3m4!1s0xd126c1114be6291:0x34f018621cfe5648!8m2!3d37.3890924!4d-5.9844589')
                st.write(
                    "With its cavernous Gothic cathedral lying at the heart of a picturesque historic center, Seville perfectly mixes the old with the new as life courses through its streets. With some great bars, restaurants and nightclubs, the city is especially fun to visit during the Feria de April and the Semana Santa festivals, which are absolutely huge")
                st.write(
                    "The capital of Andalusia has some fascinating palaces, churches and streets to explore, with the medieval Jewish quarter the area that most tourists gravitate towards. With Moorish influences on show, Seville has a rich cultural heritage to delve into.")

                st.write("## 9. Valencia")
                st.image("https://www.touropia.com/gfx/b/2018/07/valencia.jpg", width=500, caption=" Valencia")
                if st.button("View location", "5(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Valencia,+Spain/@39.4078969,-0.431551,12z/data=!3m1!4b1!4m5!3m4!1s0xd604f4cf0efb06f:0xb4a351011f7f1d39!8m2!3d39.4699075!4d-0.3762881')
                st.write(
                    "Lying alongside the Mediterranean, the third largest city in the country is often overlooked in favor of Barcelona and Madrid, although it has plenty of attractions to woo visitors. Great to live in, Valencia’s vibrant cultural scene, hopping nightlife and fine beaches mean that there’s something for everyone to enjoy.")
                st.write(
                    "MWith lovely, leafy parks snaking their way along the old riverbed that cuts through its center, the old quarter is great to explore, and there are lots of interesting museums to visit and many fine dining options available.")

                st.write("## 11. Granada")
                st.image("https://www.touropia.com/gfx/b/2018/07/granada.jpg", width=500, caption="Granada")
                if st.button("View location", "6(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Granada,+Spain/@37.1810624,-3.6613115,12z/data=!3m1!4b1!4m5!3m4!1s0xd71fce62d32c27d:0x9258f79dd3600d72!8m2!3d37.1773363!4d-3.5985571')
                st.write(
                    "TWith the enchanting Alhambra set amidst such gorgeous scenery, most visitors to Granada descend upon the city to explore the breathtaking palace fortress that once housed the Moorish rulers. Spectacular to behold and stroll around, its amazing gardens and lovely Islamic architecture is the undoubted highlight of what Granada has to offer.")
                st.write(
                    "TThe city center itself is wonderful to get lost in, as impressive churches and atmospheric bars are interspersed among fantastic Islamic architecture; the old Arab quarter is particularly beautiful due to its alluring alleys. Set on the lower slopes of the Sierra Nevada, Granada is a lively place that should not be missed.")

                st.write("## 13. Bilbao")
                st.image(
                    "https://www.touropia.com/gfx/d/destinations-in-northern-spain/bilbao.jpg?v=81afec6981f5f8f7e1396819c6fcce78",
                    width=500, caption="Bilbao")
                if st.button("View location", "7(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Bilbao,+Biscay,+Spain/@43.2634271,-3.003604,12z/data=!3m1!4b1!4m5!3m4!1s0xd4e4e27664b89b9:0x6534acc41e95a645!8m2!3d43.2630126!4d-2.9349852')
                st.write(
                    "Lying alongside the banks of the Rio Nervion in northern Spain, Bilbao’s iconic Guggenheim museum is probably what the city is best known for, although it certainly has much more to offer and is a bastion of Basque culture. Numerous architectural wonders line its lovely waterfront, highlighting a mix of traditional and contemporary styles, with some delightful cathedrals spread around the city.")
                st.write(
                    "Leafy parks and atmospheric plazas are surrounded by world-class restaurants and atmospheric eateries, showing off the best of Basque cuisine. The vibrant local culture is fascinating to learn about in its brilliant museums, galleries and theatres. Lying in Basque Country, the city has some picturesque hills overlooking it, from which there are some stunning views of the buildings below.")

                st.write("## 15. Malaga")
                st.image(
                    "https://www.touropia.com/gfx/d/destinations-in-southern-spain/malaga.jpg?v=68c5e2f432dc6b2d893e0b9147defc01",
                    width=500, caption="Alor Setar")
                if st.button("View location", "8(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/M%C3%A1laga,+Spain/@36.7650537,-4.7043714,10z/data=!3m1!4b1!4m5!3m4!1s0xd72f6698d30d151:0x403d278a576e680!8m2!3d36.7211784!4d-4.4217199')
                st.write(
                    "Located along the Costa del Sol, Malaga’s soulless high-rises hide a city that is rapidly reimagining itself. Numerous art galleries have sprung up in recent years – which seems appropriate since it is Picasso’s birthplace. Coupled with some delightful historic sites, such as an amphitheater dating back to Roman times and a Moorish fortress, it has a thriving culinary scene, as well as some great nightlife for visitors to let their hair down")
                st.write(
                    "The recently renovated port area is breathing fresh life into this already lively city. On top of this there are some nice beaches to lounge around on")

            with col2:

                st.write("## 2. Cordoba")
                st.image("https://www.touropia.com/gfx/b/2018/07/cordoba.jpg", width=500, caption="Cordoba")
                if st.button("View location", "9(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/M%C3%A1laga,+Spain/@36.7650537,-4.7043714,10z/data=!3m1!4b1!4m5!3m4!1s0xd72f6698d30d151:0x403d278a576e680!8m2!3d36.7211784!4d-4.4217199')
                st.write(
                    "Once the largest city in Western Europe, Córdoba’s stunning Mezquita testifies to the city’s former prestige and grandeur and is the undoubted highlight to see. The incredible Moorish mosque has lavish architecture and beautiful arches.")
                st.write(
                    "It is located in the middle of the historic part of Córdoba, which is an exciting area to explore – just be warned that its immediate surroundings are often full of tourists. A charming place, there are lots of historic sites to get lost in and the architecture on show is divine.")

                st.write("## 4.  Zaragoza")
                st.image("https://www.touropia.com/gfx/d/underrated-destinations-in-spain/zaragoza.jpg?v=1", width=500,
                         caption=" Zaragoza")
                if st.button("View location", "10(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Zaragoza,+Spain/@41.6517983,-0.9650206,12z/data=!3m1!4b1!4m5!3m4!1s0xd5914dd5e618e91:0x49df13f1158489a8!8m2!3d41.6488226!4d-0.8890853')
                st.write(
                    "The beautiful Basilica del Pilar is the city’s main landmark and, imperiously rising above the waters of the Rio Ebro, it really does look spectacular. The fifth largest city in the country, Zaragoza has a wealth of fantastic architecture to explore, with some ancient Roman remains and an old castle just a fraction of what it has to offer")
                st.write(
                    "With the famous painter, Goya, born nearby, there are many galleries showcasing fantastic art pieces. Add to this a great tapas and bar scene and you’ll find that Zaragoza is certainly worth visiting.")

                st.write("## 6. Palma de Mallorca")
                st.image("https://www.touropia.com/gfx/d/best-places-to-visit-in-mallorca/palma_de_mallorca.jpg?v=1",
                         width=500, caption="Palma de Mallorca")
                if st.button("View location", "11(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Palma,+Balearic+Islands,+Spain/@39.5701332,2.540672,11z/data=!3m1!4b1!4m5!3m4!1s0x12979259c61ac757:0xc40d5406c3d058c6!8m2!3d39.5696005!4d2.6501603')
                st.write(
                    "The capital of the Balearic Islands, Palma is a beautiful sight. It features a lovely old cathedral that towers over the waterfront and numerous historical sites dating back to the Moors, Romans and Talayotics.")
                st.write(
                    "While the Gothic cathedral is arguably a highlight, wandering its medieval streets lined with old townhouses and churches is delightful, and there are lots of galleries, cafes, bars and restaurants to check out. You’ll be pleasantly surprised at all that Palma de Mallorca has to offer.")

                st.write("## 8. Alicante")
                st.image(
                    "https://www.touropia.com/gfx/d/best-cities-to-visit-in-spain/alicante.jpg?v=00d7ea35fd1bcd19f9201a9dff7fc04a",
                    width=500, caption="Alicante")
                if st.button("View location", "12(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Alicante,+Spain/@38.3579546,-0.5425639,12z/data=!3m1!4b1!4m5!3m4!1s0xd6235da3b9dab4b:0x1d7da872ac0b81e3!8m2!3d38.3459963!4d-0.4906855')
                st.write(
                    "With an international airport and numerous resorts along its coastline, Alicante welcomes scores of tourists to its shores every year. Its lovely Mediterranean waterfront and picturesque old quarter, as well as a castle, museums and more, prove that the alluring, sandy beaches are just one aspect of it.")
                st.write(
                    "A lively place with great eating options and legendary nightlife, Alicante’s bars and clubs make it an upbeat place to hang out for a few days..")

                st.write("## 10. San Sebastian")
                st.image("https://www.touropia.com/gfx/b/2018/07/san_sebastian.jpg", width=500,
                         caption="10. San Sebastian")
                if st.button("View location", "13(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Donostia-San+Sebastian,+Gipuzkoa,+Spain/@43.3073962,-2.0439226,12z/data=!3m1!4b1!4m5!3m4!1s0xd51affe3b68fe15:0xe43ec55994864649!8m2!3d43.318334!4d-1.9812313')
                st.write(
                    "With an idyllic setting alongside beautiful beaches and lovely verdant hills, San Sebastián is an attractive place full of grand buildings and numerous cultural attractions. Formerly a favorite with the Spanish monarchy, its lavish architecture and sense of grandeur is befitting, while its delightful parks and plazas only add to the charm.")
                st.write(
                    "With a myriad of music, arts and cultural festivals taking part throughout the year, its rich Basque culture is on show for all to enjoy. In addition to this, the world-renowned dining options make San Sebastián a city to savor")

            st.write("# ---Map of cities in Spain---")
            st.image(
                "https://www.mapsland.com/maps/europe/spain/large-physical-map-of-spain-with-roads-cities-and-airports.jpg",
                width=800)

        if sidbar == 'Best resorts':
            st.title("10 Best Spain Beach Resorts......")
            st.image("https://maps-spain.com/img/1200/map-of-spain-holiday-resorts.jpg")

            st.write(
                "A popular European holiday destination, Spain is famous for it’s rich culture and stunning natural scenery; its beaches attract tourists looking for spend time relaxing in the sunshine on summer holidays. With so many beaches and a vast array of landscapes, Spain’s coastline is as diverse as it is beautif")

            col1, col2 = st.beta_columns(2)

            with col1:

                st.write("## 1. Praia da Rodas, Galicia")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-spain/Parador_de_Ronda.jpg?v=1")
                st.write(
                    "This beach is one of those amazing places that once you’ve been to you will never forget. A perfectly curved sandy crescent, Praia da Rodas is a breathtakingly beautiful beach that could be one of the best in the whole of the world. Located in Galicia along the more untamed Atlantic coastline, Praia da Rodas is a romantically attractive swathe of powdery sand. "
                    "Often referred as ‘Caribbean beach’ by local people, the water is dazzlingly turquoise, clean and calm, although very cold compared to the Mediterranean. Spend long summer days lazing on the sand, taking in the beauty of the surrounding nautical scenery; enjoy fresh seafood served on the shore and then spend the night under the stars at the nearby campsite.")

                if st.button("View location"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Playa+de+Roda/@42.2240056,-8.9059502,16z/data=!3m1!4b1!4m5!3m4!1s0xd2f5f6a6fc00439:0x2ca549a4f14d683d!8m2!3d42.2238459!4d-8.9028051')

                if st.button("Book now"):
                    webbrowser.open_new_tab(
                        url='https://www.touropia.com/bookingcom/es/alhambrapalace/u_amazing-hotels-in-spain')

                st.write("## 3. Maspalomas, Gran Canaria")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-spain/Hotel_Alhambra_Palace.jpg?v=1")
                st.write(
                    "There is over a century of luxurious indulgence to be experienced at the Hotel Alhambra Palace. Guests will feel amazed just walking into the lobby full of high ceilings and expansive archways, colorful tiled murals and elegant gold accents. Located just outside the Alhambra’s ancient walls, the hotel towers above the city of Granada, about a ten minute walk from the historical downtown. It has an excellent rooftop cafe that allows guests to sit for a meal and enjoy one of the city’s best views.")
                if st.button("View location", "1(id)"):
                    webbrowser.open_new_tab(
                        url='https://maps.google.co.in/maps?q=Maspalomas,+Gran+Canaria&gs_lcp=Cgdnd3Mtd2l6EAMyBwguEEMQkwIyAggAMgIIADICCAAyAggAMgUIABDJAzICCAAyAggAMgIIADICCABKBAhBGABQ04YBWNOGAWCnmgFoAHAAeACAAYcBiAGLApIBAzAuMpgBAKABAqABAaoBB2d3cy13aXrAAQE&uact=5&um=1&ie=UTF-8&sa=X&ved=2ahUKEwju84SooN_xAhUh-nMBHQOZBuUQ_AUoAnoECAEQBA')

                if st.button("Book now", "1(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.touropia.com/bookingcom/es/parador-de-ronda/u_amazing-hotels-in-spain')

                st.write("## 5. Parador de Cuenca")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-spain/Parador_de_Cuenca.jpg?v=1")
                st.write(
                    "The Parador de Cuenca is a great choice for those who want to experience history in an authentic way. It is clear that this hotel is an ancient historic treasure just looking at the sandstone walls and tiled roofs– the building is in a renovated monastery that sits above the sheer vegetated walls of Huecar Gorge. It provides an excellent view of the enchanted hanging houses from inside the glassed-in cloister. The on-site chapel is now a cozy cafe. The hotel is walking distance from many of the historic sites in Cuenca.")
                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Parador+de+Cuenca/@40.078989,-2.1287437,17z/data=!3m1!4b1!4m8!3m7!1s0xd5d67723cc9ac85:0xbcdea1593d9469cc!5m2!4m1!1i2!8m2!3d40.078989!4d-2.126555')

                if st.button("Book now", "2(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.touropia.com/tripadvisor/Hotel_Review-g262065-d271762-Reviews-Parador_de_Cuenca-Cuenca_Province_of_Cuenca_Castile_La_Mancha.html/u_amazing-hotels-in-spain')

                st.write("## 7.Hotel Alfonso XIII, Seville")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-spain/Hotel_Alfonso_XIII.jpg?v=1")
                st.write(
                    "The Hotel Alfonso XIII was originally built between 1916 and 1928, and sits in the heart of Seville, near the Santa Cruz quarter and the Guadilquivir river. Architecturally, this renovated gem is a city landmark, and a perfect example of the combined Moorish and European influences that epitomize Sevillian style. There is an expansive garden and pool area to enjoy the sunny outdoors, as well as rooms ranging from deluxe single beds to your choice of royal grand suites. Four restaurants ranging from outdoor cafe to gourmet are also available onsite.")
                if st.button("View location", "3(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Spain/@40.6502907,-3.9661501,7.75z/data=!4m5!3m4!1s0xc42e3783261bc8b:0xa6ec2c940768a3ec!8m2!3d40.463667!4d-3.74922')

                if st.button("Book now", "3(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Hotel+Alfonso+XIII,+a+Luxury+Collection+Hotel,+Seville/@37.381488,-5.9948479,17z/data=!3m1!4b1!4m8!3m7!1s0xd126c18410cd0df:0xe2c752b78be19f46!5m2!4m1!1i2!8m2!3d37.3814679!4d-5.9926015')

                st.write("## 9.  Barcelo La Bobadilla, Andalusia")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-spain/Barcelo_La_Bobadilla.jpg?v=1")
                st.write(
                    "The Barcello is located partway between the Costa del Sol and Granada, in a rustic natural setting. Reminiscent of a romantic recreation of a tiny Mudejar village, the hotel’s rambling sections are interconnected by a labyrinth of quaint path-ways, flowering courtyards, vaulted passageways and a soaring marble colonnade. It has an eclectic room style with marble bathtubs and a combination of concrete and wood floorings, to enhance the rustic feel. This Andalusian gem prides itself on being a part of the slow traveler movement, and offers many chances to forget time tables and remember a love of life.")
                if st.button("View location", "4(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/La+Bobadilla,+a+Royal+Hideaway+Hotel/@37.1641603,-4.2933257,17z/data=!3m1!4b1!4m8!3m7!1s0xd72769d7e738d25:0x4422ae396732d7d8!5m2!4m1!1i2!8m2!3d37.164156!4d-4.291137')

                if st.button("Book now", "4(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.touropia.com/tripadvisor/Hotel_Review-g580276-d232731-Reviews-Barcelo_La_Bobadilla-Loja_Province_of_Granada_Andalucia.html/u_amazing-hotels-in-spain')

            with col2:

                st.write("## 2. W Barcelona")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-spain/W_Barcelona.jpg?v=1")
                st.write(
                    "Rising like a sail from the Mediterranean sands of Barcelonetta, W Barcelona is as much a work of modern art as it is a luxury brand hotel. Locally known as Hotel Vela, architect Ricardo Bofill’s W is a stunner, inside and out. Rooms and suites are designed to maximize city views. Features like the infinity-edge pool, and the fully equipped gym and spa add to the feeling of luxury here. Additionally, the W offers a number of special events like a rooftop balcony concert series and onsite fashion shows.")
                if st.button("View location", "5(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/W+Barcelona/@41.3683664,2.1878343,17z/data=!3m2!4b1!5s0x12a4a3b19af80f11:0xc5905b70e753c2de!4m8!3m7!1s0x12a4a3b185625025:0x59e80c780f7e2f0b!5m2!4m1!1i2!8m2!3d41.3683624!4d2.190023')

                if st.button("Book now", "5(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.touropia.com/tripadvisor/Hotel_Review-g187497-d1465497-Reviews-W_Barcelona-Barcelona_Catalonia.html/u_amazing-hotels-in-spain')

                st.write("## 4. Hotel Hacienda Na Xamena, Ibiza")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-spain/Hotel_Hacienda_Na_Xamena.jpg?v=1")
                st.write(
                    "Ibiza, known as the playground of the rich, is a great place to discover the splendor of the Mediterranean. Hacienda Na Xamena does a great job of creating rooms that celebrate the natural beauty of the coastline. Simple, elegant furnishings are designed to be pleasing to the eye without competing with the external views, and large windows and balconies on the suites and haciendas allow guests to take full advantage of the natural beauty. Food is available at a gourmet restaurant, poolside cafe, and bar and nightclub onsite. The spa is top-notch and includes a set of cliffside cascading pools.")
                if st.button("View location", "6(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/La+Posidonia,+Spa/@39.0788591,1.4181825,17z/data=!3m1!4b1!4m5!3m4!1s0x12993b5aff475051:0xd9300dc4cf3e921f!8m2!3d39.0788585!4d1.4204253')

                if st.button("Book now", "6(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g1096282-d307707-Reviews-Casa_del_'
                            'Mar_Langkawi-Pantai_Cenang_Langkawi_Langkawi_District_Kedah.html')
                st.write("")

                st.write("## 6. Hotel Viura, Villabuena De Alava")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-spain/Hotel_Viura.jpg?v=1")
                st.write(
                    "Hotel Viura is a precarious-looking cubist stack located in a traditional Spanish wine village in the Rioja Alavesa region. The contrast is only heightened by the fact that its next-door neighbor is an 18th-century church. The cube-stack layout ensures that most of the thirty-three rooms have panoramic, corner-office views of the village and the surrounding Sierra de Cantabria mountains. Rooms are classic, simple, and elegant to the last detail. There is a winotech that highlights the best of the local wineries, with three featured local wines chosen each month as tasting samples.")
                if st.button("View location", "7(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Hotel+Viura/@42.5479635,-2.6671183,17z/data=!3m1!4b1!4m8!3m7!1s0xd4ff78c1257df0f:0x521315025ccb7aae!5m2!4m1!1i2!8m2!3d42.5479568!4d-2.6647632')

                if st.button("Book now", "7(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.touropia.com/tripadvisor/Hotel_Review-g1753653-d1751161-Reviews-Hotel_Viura-Villabuena_de_Alava_Alava_Province_Basque_Country.html/u_amazing-hotels-in-spain')

                st.write("## 8. ME Madrid Reina Victoria")
                st.image("https://www.touropia.com/gfx/d/amazing-hotels-in-spain/ME_Madrid_Reina_Victoria.jpg?v=1")
                st.write(
                    "The towering palace-like structure of Reina Victoria sits in Madrid’s Plaza de Santa Ana. It offers a spectacular rooftop to see many of the city’s iconic sites, as well as a large meeting space for events and gatherings. Almost 200 designer rooms range are available, including a number of pet-friendly options. In addition to the typical restaurants, bars, pool, spa and athletic facilities, the ME Madrid Reina Victoria offers a supplement bar which allows guests to create a custom-made serum to maximize each individual’s natural beauty and correct troubling issues.")
                if st.button("View location", "8(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/ME+Madrid+Reina+Victoria/@40.4145679,-3.7036359,17z/data=!3m1!4b1!4m8!3m7!1s0xd4228804396690d:0x740a44ffb5e88af4!5m2!4m1!1i2!8m2!3d40.4145638!4d-3.7014472')

                if st.button("Book now", "8(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.touropia.com/tripadvisor/Hotel_Review-g187514-d630305-Reviews-ME_Madrid_Reina_Victoria-Madrid.html/u_amazing-hotels-in-spain')

                st.write("## 10.  Parador Hostal Dos Reis Catolicos")
                st.image(
                    "https://www.touropia.com/gfx/d/amazing-hotels-in-spain/Parador_Hostal_Dos_Reis_Catolicos.jpg?v=1")
                st.write(
                    "The Parador Hostal Dos Reis Catolicos is located in one of the oldest buildings in the Pilgrimage town of Santiago de Compostela. It was built in 1499 as a hospital and temporary lodging for traveling pilgrims. Because it allowed overnight stays, it has the honor of being known as the oldest hotel in the world. As a hotel, this is a lovely combination of modern and luxurious amenities in a building that is over 500 years old, making it a rare and amazing opportunity as a place to stay. Food is local Galican, and in addition to being deliciously unique, the hotel is well-known throughout the region for specacular breakfasts..")
                if st.button("View location", "9(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Hospital+Real+de+Santiago+de+Compostela/@42.8814146,-8.5481119,17z/data=!3m1!4b1!4m8!3m7!1s0xd2efe43c122cc21:0x23b40e881437e6d9!5m2!4m1!1i2!8m2!3d42.8814107!4d-8.5459232')

                if st.button("Book now", "9(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.com/Hotel_Review-s1-g187508-d195761-Reviews-Parador_Hostal_Dos_Reis_Catolicos-Santiago_de_Compostela_Province_of_A_Coruna_Galici.html')

        if sidbar == 'Best national Parks':
            st.title("12 Most Beautiful National Parks in Spain")

            st.write(
                "Although Spain is only home to a limited number of National Parks, they really pack a punch! These parks hold the drama and beauty of some of the world’s most pristine and interesting landscapes, and have become distinct for their ecological wealth. The national parks in Spain range from picturesque scenes of leafy green pastures, blue waterways, and dense forests, to snow capped mountains, and arid, alpine regions")
            st.write("Whether it is pristine beaches you are after, the pumping nightlife of Spain’s bustling "
                     "They host desolate volcanic deserts, tropical islands, and underwater havens for marine life. Many of the nation’s parks have committed themselves to sustainable conservation and tourism, with some even winning awards and designations for their efforts.")
            st.write(
                "Flora and fauna are abundant no matter what park you venture into and several parks have been cited as having some of the world’s best birds of prey watching opportunities. So don’t forget your binoculars, and get out there and explore Spain’s beautiful national parks.")
            st.image("https://www.touropia.com/gfx/b/2018/05/spain_national_parks_map-2.jpg")

            col1, col2 = st.beta_columns(2)

            with col1:
                st.write("## 1. Tablas de Daimiel National Park")
                st.image(
                    "https://www.touropia.com/gfx/d/national-parks-in-spain/tablas_de_daimiel_national_park.jpg?v=1")
                if st.button("View location", "2(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Tablas+Daimiel/@39.1380324,-3.6992256,17z/data=!3m1!4b1!4m5!3m4!1s0xd697cafb4acd4db:0xae6ba3bd5910d696!8m2!3d39.1380283!4d-3.6970369')
                st.write(
                    "This park is nothing if not a bird-watcher’s paradise. Flat, wooden walkways make it easy to explore the park by foot, which is made up of wetlands, rivers, and rich flora. The wetlands here remain an important stopover for many migratory bird species such as ducks, and geese. Some of which chose to stay for the winter, or nest in the area.")

                st.write(
                    "Year-round residents include a variety of waterfowl such as the purple, and grey heron, little egret, and red-crested pochard. A healthy population of fish species can sometimes be spotted from the tall platforms that dot the park. Otherwise, the park is popular for its impressive sunsets over the areas waterways.")

                st.write("## 3. Cabaneros National Park")

                st.image("https://www.touropia.com/gfx/d/national-parks-in-spain/cabaneros_national_park.jpg?v=1")
                st.write(
                    "Cabaneros Park is often dubbed the ‘Spanish Serengeti’ for its abundance of animals. It is a refuge for deer, the Iberian lynx, wild boars, foxes, otters, and a number of bird species including the rare black stork, endangered Spanish Imperial Eagle, colorful bee-eaters and the Eurasian black vulture.")
                st.write(
                    "During mating season, it is not uncommon to see male deer locking horns and dueling for female attention. The landscape is one of the few remaining examples of unspoiled Mediterranean forest, which is made up of lush vegetation. Otherwise this huge park is savannah-esque, with intermingling mountain ranges which offer astounding views of the park from their summits.")
                if st.button("View location", "3(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Caba%C3%B1eros+National+Park/@39.4007449,-4.4953718,17z/data=!3m1!4b1!4m5!3m4!1s0xd6afa30ac5566c9:0x2d0b3e98744b24da!8m2!3d39.4007408!4d-4.4931831')

                st.write("## 5. Timanfaya National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-spain/timanfaya_national_park.jpg?v=1")
                if st.button("View location", "4(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Caba%C3%B1eros+National+Park/@39.4007449,-4.4953718,17z/data=!3m1!4b1!4m5!3m4!1s0xd6afa30ac5566c9:0x2d0b3e98744b24da!8m2!3d39.4007408!4d-4.4931831')
                st.write(
                    "This national parks backdrop is truly otherworldly, and in pictures it might even be mistaken for Mars. Over the course of history, the red and black landscape was formed by the parks resident volcanos who blanketed the area in now solidified lava.")
                st.write(
                    "Rare flora and fauna have found special ways to thrive in this area, which initially inspired conservationist to advocate for protection of the area. Nasa even found a special interest in this park. They used the barren landscape to help train the Apollo 17 crew.")
                st.write("7. Similajau National Park")

                st.write("## 7. Aiguestortes National Park")
                st.image(
                    "https://www.touropiThis national park is the definition of pristine nature. The landscape is dominated by visions of green, blue and white, as snow capped mountains give way to dense forests, and crystal clear waterways.a.com/gfx/d/national-parks-in-spain/aiguestortes_national_park.jpg?v=1")
                if st.button("View location", "5(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Aig%C3%BCestortes+i+Estany+of+Saint+Maurici+National+Park/@42.5719827,0.93022,17z/data=!3m1!4b1!4m5!3m4!1s0x12a8a0439424b7e3:0xec5b0ad0c3170aec!8m2!3d42.5719788!4d0.9324087')
                st.write("Located on the coast of the island of Borneo, this national park is a delightful combination"
                         " of a number of diverse ecosystems and has a huge catalogue of different activities for "
                         "visitors to choose from.")
                st.write(
                    "Close to 200 lakes can be found within the confines of the park, and the forests are home to an ancient variety of pine trees, birch, beech, and conifer trees. This national park is the only one of its kind in the Catalonia region, and an excellent example of the Spanish Pyrenees mountain range.")
                st.write(
                    "While wildlife can be difficult to spot in this area, lucky visitors will be transfixed by the parks wild goats, bearded vultures, and marmots.")
                st.write("")
                st.write("")
                st.write("")

                st.write("## 9. Monfrague National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-spain/monfrague_national_park.jpg?v=1")
                if st.button("View location", "6(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Monfrag%C3%BCe+National+Park/@39.8130181,-5.9392621,17z/data=!3m1!4b1!4m5!3m4!1s0xd1588507ed0f17b:0x9875704c675573a5!8m2!3d39.813014!4d-5.9370734')
                st.write(
                    "Monfrague Park is truly unique. It is known for its typical Iberian landscape, which is home to an abundance of flora and fauna. It is said to be one of the best bird-watching sites in Europe, and is steeped in rich history.")
                st.write(
                    "Over 400 birds of prey call Monfrague home. Vultures, and eagles can be spotted nesting in the mountainside, while kingfishers, and nightingales can be spotted by one of the parks two rivers, the Tagus and Tietar. The ruins of Monfrague castle remain on-site, which are associated with local legends, and cave paintings still endure from pre-historic times.")
                st.write("The lush verdant forests that slowly give way to dazzling white beaches that slip into the"
                         " waters around them make these islands a must-see in Spain.")

                st.write("## 11. Atlantic Islands of Galicia National Park")
                if st.button("View location", "1(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Galician+Atlantic+Islands+Maritime-Terrestrial+National+Park/@42.377723,-8.9388752,17z/data=!3m1!4b1!4m5!3m4!1s0xd2f5f6a7355118d:0x54114c4c90f6ec4e!8m2!3d42.3777191!4d-8.9366865')
                st.image(
                    "https://www.touropia.com/gfx/d/national-parks-in-spain/atlantic_islands_of_galicia_national_park.jpg?v=1")
                st.write(
                    "The four uninhabited islands that comprise the Atlantic Islands of Galicia is a maritime-terrestrial park. As well as a leader in sustainable tourism. The park is only open to the public during the summer months to ensure conservation of the natural landscape. Above the water white sandy beaches, clear blue skies, and pine woods dominate the landscape.")
                st.write(
                    "While under the crystal clear seawater over 200 species of seaweed thrive, alongside healthy coral reefs, and unique sea caves. Marine life that call these waters home include diverse shellfish, dolphins, whales, and basking sharks. This chain of islands was once a popular pirate haunt, so there is abundance of seafaring tales to be told")
                st.write("Within the boundaries of the park lies a Canopy Walk which offers you the chance to see the"
                         " forest from a different perspective as you walk along the flimsy walkways fifteen meters "
                         "above the ground.")

            with col2:

                st.write("## 2. Caldera de Taburiente National Park")
                st.image("https://www.touropia.com/gfx/b/2018/05/la_caldera_de_taburiente_national_park.jpg")
                if st.button("View location", "7(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Caldera+de+Taburiente+National+Park/@28.7294944,-17.8724234,17z/data=!3m1!4b1!4m5!3m4!1s0xc6bf032a8607315:0x98675a3cd18c3370!8m2!3d28.7294897!4d-17.8702347')
                st.write(
                    "Huge mountain peaks, the impressive caldera, and rare native Canary Pines characterize this stunning national park. The caldera, a large flat valley between steep mountain ranges, and the parks namesake is 10km across. The area was created over 2 million years ago, by a volcanic eruption and severe erosion")
                st.write(
                    "Mornings are typically bright and clear within in the park, but afternoons bring seas of cloud that descend upon the caldera and result in an entirely different vista. The highest mountain face reaches 2000m upwards from the floor of the caldera, making visitors feel unequivocally small no matter the time of day.")

                st.write("## 4.Cabrera Archipelago National Park")
                st.image(
                    "https://www.touropia.com/gfx/d/national-parks-in-spain/cabrera_archipelago_national_park.jpg?v=533cf7c38424fcf91d1e3ed6654040a4")
                if st.button("View location", "8(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/search/Cabrera+Archipelago+National+Park/@39.1500314,2.9323631,14z/data=!3m1!4b1')
                st.write(
                    "Due to the remoteness of this national park, the area has been largely untouched for millenniums. The islands are largely blanketed in fields of Neptune Grass, and host numerous endemic plant species..")
                st.write(
                    "However, the islands biodiversity doesn’t stop there, many animals that are difficult to find in other parts of the Balearics thrive here including the black lizard, and sea snails. In the surrounding ocean large populations of turtles, dolphins, and whales take refuge, while impressive sea bird colonies live along the coasts.")

                st.write("## 6. Sierra Nevada National Park")
                st.image(
                    "https://www.touropia.com/gfx/d/national-parks-in-spain/sierra_nevada_national_park.jpg?v=71ac938fe48ef173a66f72a85d1a3a81")
                if st.button("View location", "9(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Sierra+Nevada+National+Park/@37.0871164,-3.1486879,17z/data=!3m1!4b1!4m5!3m4!1s0xd71e37cf7fd697f:0x444b806b0cdc2126!8m2!3d37.0871121!4d-3.1464992')
                st.write(
                    "Wow! Sierra Nevada national park is Spain’s largest national park, and home to some of Europe’s biggest mountains. As such, one of the most appealing aspects of this national park is its incredible natural diversity.")
                st.write(
                    "The parks ground floor is made up of lush valleys, forests, and river ways. However, trails leading upwards give way to alpine forest and barren mountain peaks. On a clear day, views of the Mediterranean Sea, and Morocco are visible from the Sierra Nevada mountain range. Plants that thrive in these rugged alpine conditions include the Sierra Nevada violet, juniper and barberry species.")

                st.write("## 8. Teide National Park")
                st.image(
                    "https://www.touropia.com/gfx/d/national-parks-in-spain/teide_national_park.jpg?v=e1088a5b5b38148d96733707cdcbf2ce")
                if st.button("View location", "10(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Teide+National+Park/@28.2538834,-16.6204569,17z/data=!3m1!4b1!4m5!3m4!1s0xc6a8398062de729:0x67633a63c20a292d!8m2!3d28.2538787!4d-16.6182682')
                st.write(
                    "Located in the Canary Islands, Teide National Park is home to Spain’s highest mountain. Mount Teide is a stark contrast to the rest of the parks somewhat, low lying lands. It is the Europe’s most visited national park with over 3 million visitors each year and with good reason.")
                st.write(
                    "The landscape is reminiscent of another world, which is entirety dominated by volcanic soil, and due to the size of the park nearly never crowded. Caves, craters, and lava rivers are petrified in stone in this area, and visitors with still be delighted with the diversity of vistas around every corner.")

                st.write("## 10. Ordesa National Park")
                st.image("https://www.touropia.com/gfx/d/national-parks-in-europe/ordesa_national_park.jpg?v=1")
                if st.button("View location", "11(id)"):
                    webbrowser.open_new_tab(
                        url='https://www.google.co.in/maps/place/Teide+National+Park/@28.2538834,-16.6204569,17z/data=!3m1!4b1!4m5!3m4!1s0xc6a8398062de729:0x67633a63c20a292d!8m2!3d28.2538787!4d-16.6182682')
                st.write(
                    "Ordesa was Spain’s first national park, and its beauty is truly undeniable. Here waterfalls, rivers, and streams are plentiful. They are strung among rich green pastures, dense woods, and steep summits. However, the Pyrenees mountain range is the true prize of the park. They form a magnificent skyline, that excites both visitors and locals alike. "
                    "due its beautiful scenery that look like something out of Jurassic Park.")
                st.write(
                    "The highest mountain in this range is Mount Perdido, which ironically stands at over 3330 meters above sea level. It is the highest limestone summit in Europe, and distinct among the skyline. Many animals live among Mount Perdido and his neighboring massifs including the bearded vulture, griffon vulture, and golden eagle that fly overhead.")
                st.write("Slowly wandering along the paths that are dwarfed by the enormous trees on either side is a "
                         "liberating experience as you feel free and unfettered, alone in the wild.")







    if countryselect == "India":
        st.sidebar.title("...India...")

        sidbar = st.sidebar.radio("", ("About", "Best beaches", "Best cities", "Best Hill Station",
                                       "Best national Parks", 'Best Resorts'))
        if sidbar == 'About':
            st.title("Welcome to India")
            st.image("images/india2.jpg", width=700)
            st.write("""
                               India takes pride in flaunting its unsurpassed heritage; eras over eras have influenced, moulded and face 
                               lifted the rich heritage of which we all are part of. Distinctive edifices, perennial culture and the determination
                               to keep this incredibility have preserved for us an era no short of marvels. With a startling number of 
                               places and monuments enlisted in the list of UNESCO World Heritage Sites, India has made an indelible mark in world history.
                               """
                     )
            st.write("""
                               The natural splendor maintaining its domain over many parts of the country boasts of magnificent wildlife 
                               heritage. From the float of crocodiles at Sunderban National Park to the home of snow leopards at Nanda 
                               Devi Biosphere Reserve, from the majestic Manas Wildlife Sanctuary to the Keoladeo National Park and Kaziranga 
                               National Park, India humbly possess the most diverse heritage in the world. The lush flora and the tailored 
                               landscape around it has been the prime attraction in the country, right from the red rhododendrons to the 
                               Neelakurinji, which bloom once every 12 years and from the moonscape Ladakh to the river island Majuli, 
                               the kaleidoscope of wildlife and natural heritage never ceases to amaze us in India.

                               """
                     )
            st.video("https://www.youtube.com/watch?v=0LQAO8Y2BGQ&t=5s")
            st.video("https://www.youtube.com/watch?v=XleHgd5mOec")

        if sidbar == 'Best beaches':
            st.title("Best Beaches in India......")

            col1, col2 = st.beta_columns(2)

            with col1:

                # Beach1
                st.title("")
                st.write("## 1. Radhanagar Beach, Havelock Island")
                st.write("""
                   The beauty of Radhanagar beach cannot be described in words. This was once voted as the best beach in entire Asia. 
                   It is indeed one of the best beaches in India, and a must-visit for all the beach lovers.
                   """)
                if st.button("View location"):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Radhanagar+Beach/@11.9830673,92.9309396,14z/data=!3m1!4b1!4m5!3m4!1s0x3088d212164bb773:0x9715637d9a7265b3!8m2!3d11.9844552!4d92.9508454')
                st.image("images/beaches/1.jpg", width=500, caption="Radhanagar Beach, Havelock Island")
                st.title("")
                st.title("")

                st.write("## 3. Gokarna, Karnataka ")
                st.write("""
                   The tranquility of the Gokarna beach is worth a visit. It is also a well-known pilgrimage site with a perfect
                   blend of beach fun and divinity! Plan a trip with your friends, family or even solo and enjoy sunbathing at 
                   the beach, taking a dip or visiting the temple.
                   """)
                if st.button("View location", id(3)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Gokarna,+Karnataka/@14.5372468,74.3066308,14z/data=!3m1!4b1!4m5!3m4!1s0x3bbe83d65b0a4c71:0xe9e09fd076bb41c0!8m2!3d14.5478586!4d74.318841?hl=en-GB')

                st.image("images/gokarna.jpg", width=500, caption="Gokarna, Karnataka")

                st.write("## 5. Yarada Beach, Andhra Pradesh")
                st.write("""
                       If you are a beach lover, Yarada beach will be love at first sight for you. It is a lovely unspoiled
                       beach, famous for its serenity and water sports. Luckily the beach is not super crowded, so you 
                       can also enjoy some solitude time here with your family, friends or loved one.
                             """)
                if st.button("View location", id(5)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Yarada+Beach/@17.6578658,83.2643518,15z/data=!3m1!4b1!4m5!3m4!1s0x3a39421da4370733:0xa4ef41bc1f76ebe8!8m2!3d17.6549368!4d83.26923?hl=en-GB')
                st.image("images/yarada.jfif", width=500, caption="Yarada Beach, Andhra Pradesh")

                st.write("## 7. Puri Beach, Orissa")
                st.write("""
                   One of the best beaches in India, Puri beach is not only a beautiful beach with a palm-fringed but also 
                   is a pilgrim spot for people who come to visit Lord Jagannath. Do not miss the spectacular sunrise and 
                   sunset of this beach.
                   """)
                if st.button("View location", id(99)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Golden+Beach/@19.7952288,85.7942681,13z/data=!3m1!4b1!4m5!3m4!1s0x3a19c419b6847af9:0x4ae140e6a993c45e!8m2!3d19.794749!4d85.8252882')
                st.image("images/puri2.jpg", width=500, caption="Puri Beach, Orissa")

            with col2:
                st.title("")
                st.write("## 2. Tarkarli beach, Maharashtra")
                st.write("""
                                   Spend some solitude time at Tarkarli beach. It is one of the most famous beaches in India. The white sand 
                                   and the stunning view of the Sindhudurg fort around is worth your attention. Here you can also enjoy adventurous 
                                   water sports activities like parasailing, snorkelling, and even scuba diving.
                                   """)
                if st.button("View location", id(2)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Tarkarli+Beach/@16.015607,73.4687946,14z/data=!3m1!4b1!4m5!3m4!1s0x3bc002678e3801d1:0xa2cb4081dd152476!8m2!3d16.0136864!4d73.4898334?hl=en-GB')

                st.image("images/tarkali.jpg", width=500, caption="Tarkarli beach, Maharashtra")
                st.title("")
                st.title("")

                st.write("## 4. Mandrem, North Goa ")
                st.write("""
                                                   Goa, former Portuguese Colony, has earned its reputation for its beautiful beaches. Mandrem 
                                                   is one such remarkable beach, known for its beauty and pleasant climate. Come here to spend 
                                                   time with your friends at one of the best beaches in India.
                                                   """)
                if st.button("View location", id(4)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Mandrem,+Goa+403519/@15.6669404,73.7027149,13z/data=!3m1!4b1!4m5!3m4!1s0x3bbfee9a64960627:0x728e355b9ea77639!8m2!3d15.6631077!4d73.7419017?hl=en-GB')

                st.image("images/mandrem.jpg", width=500, caption="Mandrem, North Goa")
                st.write("## 6. Light House Beach, Kovalam")
                st.write("""
                                           The lighthouse beach is one of the most famous beaches in India. To enjoy the nightlife and have 
                                           a gala time in Kerala, one must definitely visit this beach. Even if you want to spend some time 
                                           away from the city’s crowd, you can visit here as the serenity is amazing.
                                             """)
                if st.button("View location", id(6)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Light+House+Beach,+Kerala/@8.3847304,76.9776993,17z/data=!3m1!4b1!4m5!3m4!1s0x3b05a5bb0c57147d:0xc81f5219dd722fb5!8m2!3d8.3853546!4d76.9797876?hl=en-GB')

                st.image("images/light.webp", width=500, caption="Light House Beach, Kovalam")

        if sidbar == 'Best cities':
            st.title("Best Cities to Travel in India......")
            col11, col22 = st.beta_columns(2)
            with col11:

                st.write("## 1. Varanasi")
                st.write("""
                           A city that may seem strange to many Westerners, Varanasi is of great religious importance. 
                           The holy city sits on the banks of the divine Ganges and is believed by Hindus to be a sacred place of pilgrimage.

                           The city is known for the religious practices that take place on the ghats alongside the river – 
                           pilgrims wash themselves in the waters of the Ganges and the bodies of Hindus are cremated. The 
                           sights of life and death along the riverside can be shocking, but a visit to Varanasi is also rousing, 
                           contemplative, and ultimately, helps visitors to further understand India’s deep cultural and spiritual practices.
                                   """)
                if st.button("View location", id(7)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Varanasi,+Uttar+Pradesh/@25.3207461,82.9210686,12z/data=!3m1!4b1!4m5!3m4!1s0x398e2db76febcf4d:0x68131710853ff0b5!8m2!3d25.3176452!4d82.9739144')

                st.image("images/varanasi.jpg", width=500, caption="Varanasi")

                st.write("## 3. Banglore ")
                st.write("""
                              India’s high-tech hub city sits in the south and has become a booming cosmopolitan center of 
                              industry, nightlife and open spaces. This developing and dynamic city has emerged as a cultural 
                              bastion of shopping, food, drinking, and altogether good times.

                              Bangalore’s modern outlook means it’s a place for visitors to relax and let their hair down. 
                              Enjoy lunches at independent cafes, take walks in its plethora of parks – but don’t forget to 
                              visit Krishnarajendra Market for that taste of all things Indian.
                           """)
                if st.button("View location", id(9)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Bengaluru,+Karnataka/@12.9538477,77.3507371,10z/data=!3m1!4b1!4m5!3m4!1s0x3bae1670c9b44e6d:0xf8dfc3e8517e4fe0!8m2!3d12.9715987!4d77.5945627')

                st.image("images/bangalore.jpg", width=500, caption="Banglore")

                st.title("")

                st.title("")
                st.write("## 5. Mumbai ")
                st.write("""
                    Mumbai is well known for being a city on the edge – its slums overflow with life as its skyscrapers soar 
                    to the sky. This strange and extraordinary blend of rich and poor creates a city that strives to move 
                    India forward – this most populated city in India has to be seen to be believed.

                   The center for India’s creative culture, fashion, food and finance, Mumbai has some of the most expensive homes in the 
                   world and some of the biggest slums in Asia. This beguiling composite of Indian proportions is where the gateway to India 
                   is located – a stone arch built on the waterfront in 1923. Take a trip out of town for some time out and visit the cave 
                   temple complex of Elephant Caves.
                             """)
                if st.button("View location", id(11)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Mumbai,+Maharashtra/@19.0821978,72.7410982,11z/data=!3m1!4b1!4m5!3m4!1s0x3be7c6306644edc1:0x5da4ed8f8d648c69!8m2!3d19.0759837!4d72.8776559')
                st.image("images/mumbai.jpg", width=500, caption="Mumbai")

                st.write("## 7. Delhi ")
                st.write("""
                              Delhi is surging mix of crumbling history, gleaming modernity and, of course, traffic. The Indian 
                              capital has long held a reputation as being jammed full of life – a place where the past and the 
                              future combine. Despite of – or perhaps because of – its cramped streets, packed markets and 
                              overflowing train stations, Delhi has a lot going for it.

                             The astonishing patchwork of people and culture provides a tempting combination for many visitors, who travel to the city 
                             to absorb the frenzied Indian atmosphere.

                          Visit the 17th-Century Red Fort and be awestruck by the scale of the Mughal architecture. Then take a tuk-tuk to Delhi’s 
                          Jama Masjid, where you can soak up the peaceful atmosphere and be greeted by a wealth of welcoming smiles. Climb to the 
                          top of the mosque’s tower for a small fee and catch a view of the city from above.   
                                       """)
                if st.button("View location", id(13)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Delhi/@28.6921165,76.8111531,10z/data=!3m1!4b1!4m5!3m4!1s0x390d047309fff32f:0xfc5606ed1b5d46c3!8m2!3d28.6862738!4d77.2217831')
                st.image("images/delhi.cms", width=500, caption="Delhi")
            with col22:
                st.write("## 2. Kolkata ")
                st.write("""
                                   The old capital of India, Kolkata has a long and complex history. The East India Company founded 
                                   the city as a trading center in 1773. Since then, the city has grown and developed to become the vast megacity of today.

                                   Known as the Tea Capital, Kolkata is a friendly place where poverty and modernity live side by side. Sights in the city 
                                   include the ornate Dakshineswar Kali Temple, as well as the Taj Mahal-esque Victoria Memorial Museum and the monumental Howrah Bridge.
                                           """)
                if st.button("View location", id(8)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Kolkata,+West+Bengal/@22.6757521,88.0495293,10z/data=!3m1!4b1!4m5!3m4!1s0x39f882db4908f667:0x43e330e68f6c2cbc!8m2!3d22.572646!4d88.363895')

                st.image("images/kolkata.jpg", width=500, caption="Kolkata")
                st.title("")
                st.write("## 4. Agra ")
                st.write("""
                                   Agra is known for one thing – the iconic and ultimately impressive Taj Mahal. Set on the south bank of the 
                                   Yamuna River in Agra, the Taj draws millions of tourists a year to the city. Built by an emperor as an 
                                   extravagant memorial to his wife, the mausoleum’s porcelain white marble is an emblem of romance, love and adventure

                                   Agra itself sits in the shadow of its imposing monument, but is a small and welcoming city. The ancient Mughal-era Agra 
                                   Fort is an attractive spot to visit – peer over the walls here and catch your first hypnotizing glimpse of the Taj.
                                           """)
                if st.button("View location", id(10)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Agra,+Uttar+Pradesh/@27.1761571,77.9099722,12z/data=!3m1!4b1!4m5!3m4!1s0x39740d857c2f41d9:0x784aef38a9523b42!8m2!3d27.1766701!4d78.0080745')

                st.image("images/agra.jpg", width=500, caption="Agra")

                st.write("## 6. Jaipur ")
                st.write("""
                                             The Pink City of Jaipur is the capital of Rajasthan and is where you can find the beautiful Amber 
                                             Fort – a sprawling, stunning complex set in the hillside overlooking a lake. Located just outside 
                                             of the city and built in 1592, the grandiose citadel was also a palace for some time but is now an 
                                             impressive tourist attraction.

                                             Make sure to take a trip to the opulent city palace with its stunning courtyards and gardens, 
                                             plus the amazingly intricate Palace of Winds.      
                                                             """)
                if st.button("View location", id(12)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Jaipur,+Rajasthan/@26.8851417,75.6504706,11z/data=!3m1!4b1!4m5!3m4!1s0x396c4adf4c57e281:0xce1c63a0cf22e09!8m2!3d26.9124336!4d75.7872709')

                st.image("images/jaipur.jpg", width=500, caption="Jaipur")

        if sidbar == 'Best Hill Station':
            st.title("Best Hill stations to Travel in India......")
            col4, col5 = st.beta_columns(2)
            with col4:
                st.title("")
                st.write("## 1. Manali")
                st.write("""
                           Regarded to be one of the best hill stations in India, Manali is a heaven for all the snow lovers. 
                           With delicate temperatures during the summers, and chilling weather during the winters, Manali is 
                           one of the peaceful places to visit in North India. There are many things to do in Manali, which is
                           fondly known as the Valley of the Gods. Whether you are an adventure and sports enthusiast or love 
                           calm and tranquil surroundings, Manali has something for everyone. 

                            Located at the northern end of the Kullu Valley, in between the mountains of Himachal Pradesh, 
                            it is the most stunning hill station that is at an altitude of 2,050m. The natural scenic beauty, 
                            culture and snow-capped mountains are sure to enthral you and hypnotise you no end. Visiting this 
                            place will make you realise why it is termed as such a major attraction in the Himachal tour packages.

                             A.] Nearest airport: At Srinagar (56 km)\n
                            B.] Must visit places: Khilanmarg, Alpather Lake, Gulmarg Gondola, Gulmarg Biosphere Reserve, 
                            Seven Springs, Maharani Temple etc.\n
                            C.] Activities to do: Skiing at Gulmarg Backcountry Ski Lounge, snowboarding at Apharwat Peak, 
                            camping at Ningle Nallah etc.\n
                            D.] Known for: Fairly untouched and with supreme beauty, Gulmarg is a heavely region in Baramula 
                            district of the country which is most known for being a skiing hub of the state.
                                   """)
                st.image("images/manali.jpg", width=500, caption="Manali")
                if st.button("View location", id(1)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Manali,+Himachal+Pradesh/@32.2394708,77.1696102,14z/data=!3m1!4b1!4m5!3m4!1s0x39048708163fd03f:0x8129a80ebe5076cd!8m2!3d32.2431872!4d77.1891761')

                st.title("")
                st.write("## 3. Shimla ")
                st.write("""
                             With the hill stations in Himachal Pradesh being such beauties, why should the capital of the 
                             state be left far behind? Set against oak, deodar and pine forests, Shimla makes for one fascinating 
                             sight! While you are there, you can check out the Chadwick Falls, The Ridge, Mall Road, Christ Church 
                             and Jaku Hill. Shimla tourism is always at an all time high so you get to know about the best 
                             attractions and places to stay no matter when you plan to visit.
                                                                   """)
                st.image("images/shimla.jpg", width=500, caption="Shimla")
                if st.button("View location", id(2)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Shimla,+Himachal+Pradesh/@31.0782147,77.1240017,13z/data=!3m1!4b1!4m5!3m4!1s0x390578e3e35d6e67:0x1f7e7ff6ff9f54b7!8m2!3d31.1048145!4d77.1734033')

                st.write("## 5. Munnar ")
                st.write("""
                            The rolling hills of Munnar in Kerala have always provided people with the ultimate haven for 
                            achieving utter bliss and respite. Blessed with vast stretches of tea and spice plantations, 
                            magnificent wildlife and exhaustive natural beauty at every corner, Munnar undoubtedly lies among 
                            the top Best Hill Stations in India. Sought by romantics and honeymooners in large number every year 
                            the place doesn’t just appease you with its natural magnificence but also with productive activities 
                            that you can enjoy here including trekking, yoga, Ayurvedic spa treatments, food trails and shopping.     """)
                st.image("images/munnar.jpg", width=500, caption="Munnar")
                if st.button("View location", id(3)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Munnar,+Kerala+685612/@10.0806491,77.0466683,14z/data=!3m1!4b1!4m5!3m4!1s0x3b0799794d099a6d:0x63250e5553c7e0c!8m2!3d10.0889333!4d77.0595248')

                st.write("## 7.Mussoorie")
                st.write("""
                   Mussoorie is a sight to behold! Almost everyone has heard of it and it is on every traveller’s wish list 
                   when exploring the top hill stations in North India. It is way up, above the mountains of Garhwal and on 
                   top of a horseshoe crest. You will certainly be in for a treat as you check out the spectacular view of 
                   the majestic Himalayas and the Doon Valley.

                   """)
                st.image("images/mussorie.jpg", width=500, caption="Mussoorie")
                if st.button("View location", id(7)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Mussoorie,+Uttarakhand/@30.4547186,78.0414205,13z/data=!3m1!4b1!4m5!3m4!1s0x3908d0cfa61cda5b:0x197fd47d980e85b1!8m2!3d30.4597892!4d78.0643723')

            with col5:
                st.title("")
                st.write("## 2.  Gulmarg")
                st.write("""
                                          Boasting the scenic beauty of the ever-wonderful Jammu and Kashmir, Gulmarg stands on a different
                                           level among all the hill stations in North India. This beautiful hill station in India is the most 
                                           sought-after place among all the travellers in India and abroad as well. Set at an altitude of 
                                           2,730m, Gulmarg is a hill town that is engulfed by deep ravines, meadows, snow-capped peaks, lush 
                                           hills and serene valleys. If you are not afraid to try something adventurous, you can even indulge 
                                           in some skiing that is a popular winter sport here. Gulmarg carries the glory of the ever charming 
                                           Jammu and Kashmir, making it one of the best hill stations in India.

                                           A.] At Bhuntar (50 km)\n
                                           B.] Must visit places: Hidimba Devi Temple, Bhrigu Lake, Pin Valley National Park, Manali Sanctuary, 
                                           Vashishth Temple, Jogni Falls etc..\n
                                           C.] Activities to do: Paragliding at Rohtang Pass, camping and winter sports at Solang Valley, 
                                           river rafting at Pandoh Dam\n
                                           D.] Known for: One of the best Hill Stations in North India, Manali has an unassailable reputation 
                                           for being a backpacker’s paradise at a truly romantic honeymoon destination.

                                                                  """)
                st.image("images/gulmarg1.jpg", width=500, caption="Gulmarg")
                if st.button("View location", id(4)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Gulmarg+193403/@34.0506347,74.3642863,15z/data=!3m1!4b1!4m5!3m4!1s0x38e1af91308dd977:0x7a5cc65c8fb01df7!8m2!3d34.0483704!4d74.3804791')

                st.write("## 4. Nainital ")
                st.write("""
                                 Nainital is a heaven on earth. Well recognised as the Lake District of India, it is one of the best places to beat 
                                 the heat in the scorching summer. With ancient temples and jaw dropping sceneries to its credit, you can 
                                 also check out the Jim Corbett National Park which is the oldest national park in India and indulge in 
                                 exploring caves and boating activities.
                                                                                                   """)

                st.image("images/nainital.jpg", width=500, caption="Nainital")
                if st.button("View location", id(5)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Nainital,+Uttarakhand/@29.3824491,79.4377611,14z/data=!3m1!4b1!4m5!3m4!1s0x39a0a1bc28fd9d61:0x7cae7ba916987db3!8m2!3d29.3919202!4d79.4542033')

                st.write("## 6. Srinagar")
                st.write("""
                   Lying on the banks of the river Jhelum, Srinagar is certainly a beauty owing to its lovely houseboats, 
                   historic gardens, wandering rivers and impeccable climate. The place boasts of the largest tulip garden 
                   in Asia and while here, you can visit the Dachigam Wildlife Sanctuary, Dal Lake, Amarnath Cave, Wular Lake,
                    Jama Masjid and the Mughal Gardens.
                   """)
                st.image("images/srinagar.jpg", width=500, caption="Srinagar")
                if st.button("View location", id(112)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Srinagar/@34.106639,74.6666688,11z/data=!3m1!4b1!4m5!3m4!1s0x38e1855686e3c5ef:0x66244b7cc1e305c6!8m2!3d34.0836708!4d74.7972825')

                st.write("## 8.McLeodganj")
                st.write("""
                   This charming Tibetan town in the hills of Himachal is one of the Best Hill Stations in India. A small 
                   settlement in Dharamshala, another hill resort in the state, it is perfect to visit any time of the year 
                   owing to its splendid and balanced but perennially cool climate. The laidback charm, numerous beautiful 
                   Buddhist Monasteries and gorgeous landscape of snow-draped mountains make McLeodganj the ideal choice for
                    a great holiday surrounded by hills.
                   """)
                st.image("images/McLeodganj.jpg", width=500, caption="McLeodganj")
                if st.button("View location", id(888)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/McLeod+Ganj,+Dharamshala,+Himachal+Pradesh/@32.2450192,76.3068294,15z/data=!3m1!4b1!4m5!3m4!1s0x391b56d4e3d36d19:0xa3e8725f0584be76!8m2!3d32.2425758!4d76.3212781')

        if sidbar == 'Best national Parks':
            st.title("Best Hill stations to Travel in India......")
            col6, col7 = st.beta_columns(2)
            with col6:

                st.write("## 1. Corbett National Park, Uttarakhand")
                st.write("""
                           India's first national park, Corbett was established in 1936 by legendary tiger hunter Jim Corbett. 
                           It's located around three hours from Nainital and seven hours from Delhi. The park is a large one 
                           and has five zones. One zone, Jhirna, is open all year round. The rest of the park closes during the monsoon. 
                           The chances of seeing a tiger at Corbett aren't great but there are other animals, and elephant 
                           safaris are possible. For the best wildlife viewing, stay deep in the reserve in the Dhikala zone. 
                           However, if you're a foreigner be prepared to pay double the rates for accommodation, with the cheapest 
                           rates around 2,500 rupees a night for a private cabin at a forest rest house. More information is 
                           available from the park's website.
                                   """)
                st.image("images/corbet.jpg", width=500, caption="Corbett National Park")
                if st.button("View location", id(8)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Corbet,+Banbridge+BT32+3SW,+UK/@54.3395452,-6.2213518,14z/data=!3m1!4b1!4m5!3m4!1s0x4860e1098cb782ef:0x915eafff783cbc91!8m2!3d54.339547!4d-6.2038422')

                st.write("## 3. Kanha National Park, Madhya Pradesh")
                st.write("""
                     Kanha National Park, Madhya Pradesh has the honor of providing the setting for Rudyard Kipling's classic 
                     novel, The Jungle Book. It's rich in lush saal and bamboo forests, lakes, streams and open grasslands. 
                     This large park is well regarded for its research and conservation programs, and many endangered species 
                     have been saved there. As well as tigers (the chance of seeing one has increased dramatically in recent years),
                      the park is known for its barasingha (swamp deer) and an extensive variety of other animals and birds. 
                      It's perfect for nature lovers.
                                                                   """)
                st.image("images/kanha.jpg", width=500, caption="Kanha National Park")
                if st.button("View location", id(9)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Madhya+Pradesh+Tourism/@22.2409935,80.5018677,12z/data=!4m9!1m2!2m1!1skanha+national+park!3m5!1s0x3a2a08913000b8c7:0xd01c3cd4d6ccac31!8m2!3d22.2831218!4d80.6185975!15sChNrYW5oYSBuYXRpb25hbCBwYXJrkgEfdG91cmlzbV9kZXZlbG9wbWVudF9jb3Jwb3JhdGlvbg')

                st.write("## 5. Sundarbans National Park, West Bengal ")
                st.write("""
                   Sundarbans, one of the top tourist places in West Bengal, has a magnificent tangle of mangrove jungle that's 
                   the largest in the world.. The Indian part is made up of 102 islands and just over half of them are inhabited. 
                   The Sundarbans is only accessible by boat and exploring it this way is a thrilling experience that shouldn't be missed. 
                   Don't be hopeful of seeing any tigers though. They're very shy and usually remain well hidden in the reserve. 
                   A highlight is staying in eco-friendly village accommodations and enjoying community-based tourism.
                   """)
                st.image("images/sundar.jpg", width=500, caption="Sundarbans National Park")
                if st.button("View location", id(10)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Sundarban+National+Park/@21.8358595,88.8820124,17z/data=!3m1!4b1!4m5!3m4!1s0x3a018264f05cd269:0xe99cba5218a4be78!8m2!3d21.8358595!4d88.8842011')

                st.write("## 7.Great Himalayan National Park, Himachal Pradesh")
                st.write("""
                   One of the top places to visit in Himachal Pradesh, the Great Himalayan National Park became a UNESCO World
                    Heritage Site in 2014. The park has four valleys and covers more than 900 square kilometers. Its remote,
                     rugged and untamed terrain makes it sought after by trekkers but only the fittest and most adventurous 
                     reach deep inside the core area.
                   """)
                st.image("images/great.jpg", width=500, caption="Great Himalayan National Park, Himachal Pradesh")
                if st.button("View location", id(7)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/The+Great+Himalayan+National+Park(office)/@31.8917917,77.1407128,17z/data=!3m1!4b1!4m5!3m4!1s0x3904345539963725:0x3930505b5e390442!8m2!3d31.8918161!4d77.1429258')

            with col7:
                st.write("## 2. Ranthambore National Park, Rajasthan")
                st.write("""
                                    Ranthambore National Park, Rajasthan is a fascinating blend of history and nature. Inside the park is a
                                     formidable fort that was built in the 10th century and coveted by many rulers due to its strategic position
                                      between north and central India. The park itself is characterized by rocky plains and steep cliffs. It supports a diverse range of flora 
                                    and fauna, including around 30 tigers. This park is very popular due to its proximity to Delhi and the 
                                    fact that tigers are relatively easy to spot there. However, the park's popularity has resulted in 
                                    overcrowding and mismanagement of safaris, which is a problem and something to be aware of.
                                                                   """)
                st.image("images/ranthambore.jpg", width=500, caption="Ranthambore National Park")
                if st.button("View location", id(11)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Ranthambore+National+Park/@26.0288382,76.424082,12z/data=!3m1!4b1!4m5!3m4!1s0x3971d8f668d65517:0x6eb9f78b60bac925!8m2!3d26.0173274!4d76.5025742')

                st.write("## 4. Kaziranga National Park, Assam ")
                st.write("""Much of Kaziranga National Park consists of swamp and grasslands, making it the perfect habitat
                                    for the one-horned rhinoceros. The largest population in the world of these prehistoric looking creatures exists 
                                    there, along with almost 40 major mammals. This picturesque park can be explored by elephant safari. It sits on 
                                    the banks of the Brahmaputra River in India's Northeast, approximately six hours from Guwahati.
                                  """)

                st.image("images/kaziranga.jpg", width=500, caption="Kaziranga National Park, Assam")
                if st.button("View location", id(12)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Kaziranga+National+Park/@26.5827288,93.1559421,14z/data=!3m1!4b1!4m5!3m4!1s0x3744412d379f65df:0x8b2b74b6e7c99458!8m2!3d26.577531!4d93.171122')
                st.title("")

                st.write("## 6. Valley of Flowers National Park, Uttarakhand")
                st.write("""
                   This high altitude alpine valley is a glacial corridor that comes alive during the monsoon season with 
                   around 300 different varieties of alpine flowers. They appear as a bright carpet of color against a mountainous
                    snow capped background. The Valley of Flowers requires a strenuous hike but you'll feel on top of the world 
                    in this magical and enchanting place!
                   """)
                st.image("images/valley.jpg", width=500, caption="Valley of Flowers National Park, Uttarakhand")
                if st.button("View location", id(555)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Valley+of+Flowers+National+Park/@30.72804,79.6031143,17z/data=!3m1!4b1!4m5!3m4!1s0x39a791153bd771ef:0x1f42050f9b6c125f!8m2!3d30.72804!4d79.605303')

        if sidbar == 'Best Resorts':
            st.title("Best Resorts In India......")
            col34, col35 = st.beta_columns(2)

            with col34:
                st.write("## 1.Radisson Blu Udaipur Palace Resort & Spa")
                st.write("""
                   Radisson Blu Udaipur Palace Resort & Spa Boasting a location near Fateh Sagar Lake, our hotel in Udaipur
                    is moments from the shopping districts of Hathi Pol and close to the City Palace. Resort guests enjoy 
                    on-site dining two restaurants and a poolside bar, as well as features like an on-site spa, a concierge
                     and three flexible meeting and event spaces.
                   """)
                st.image("images/radisson.jpg", width=500, caption="Radisson Blu Udaipur Palace Resort & Spa")
                if st.button("View location", id(1)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Radisson+Blu+Udaipur+Palace+Resort+and+Spa/@24.59,73.6651942,17z/data=!3m1!4b1!4m8!3m7!1s0x3967e547b9828855:0x258344463865cdcf!5m2!4m1!1i2!8m2!3d24.5899088!4d73.6673825?hl=en-GB')
                if st.button("Booking", id(2)):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.in/Hotel_Review-g297672-d1853086-Reviews-Radisson_Blu_Udaipur_Palace_Resort_Spa-Udaipur_Udaipur_District_Rajasthan.html')

                st.write("## 3. Taj Lake Palace")
                st.write("""
                   The ethereal Taj Lake Palace affords guests the pleasures of India's bygone princely era. Over the centuries, 
                   it has played host to royalty, poets and writers and the Maharana's guests. Trappings like a welcoming vintage 
                   car ride to the charming city of Udaipur, the Jiva Spa boat, royal butlers, recipes from traditional Mewari 
                   cuisine and arrival by boat - all little facets that make this former pleasure palace the celebrated luxury 
                   hotel it is today.
                   """)
                st.image("images/taj.jpg", width=500, caption=" Taj Lake Palace")
                if st.button("View location", id(3)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps?q=Taj+Lake+Palace&source=lmns&bih=664&biw=1536&hl=en-GB&sa=X&ved=2ahUKEwii1eKDidjxAhXCMrcAHWyXAm4Q_AUoAnoECAEQAg')
                if st.button("Booking", id(4)):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.in/Hotel_Review-g297672-d302377-Reviews-Taj_Lake_Palace-Udaipur_Udaipur_District_Rajasthan.html')

                st.write("## 5. Anantya Resorts")
                st.write("""
                   Anantya is a quiet lush tropical retreat nestled within 1000 acres of rubber plantations. Anantya is perched
                    on the banks of the Chittar Lake where the Western Ghats give way to "Alli Kulams" and "Tamara Kulams" 
                    (Lily and Lotus Ponds) in beautiful Kanyakumari district located very close to Trivandrum and Nagercoil.
                   """)
                st.image("images/anantya.jpg", width=500, caption=" Taj Lake Palace")
                if st.button("View location", id(5)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Anantya+Resort/@8.4323228,77.2408192,17z/data=!3m1!4b1!4m8!3m7!1s0x3b0452618e37c0d7:0x65b1b20925d28e7d!5m2!4m1!1i2!8m2!3d8.4323228!4d77.2430079?hl=en-GB')
                if st.button("Booking", id(6)):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.in/Hotel_Review-g608476-d5011936-Reviews-Anantya_Resorts-Kanyakumari_Kanyakumari_District_Tamil_Nadu.html')

            with col35:
                st.write("## 2. The Ananta Udaipur")
                st.write("""
                   Set against the breathtaking backdrop of the Aravalli Hills, Ananta Udaipur creates a fairy tale-like experience
                    by offering the best of five-star luxuries. From blossoming verdure to contemporary villas coupled with 
                    service excellence, the picturesque façade of Ananta aesthetically captures the beauty of your sojourn. 
                    Be it leisure stays, destination weddings or corporate off-sites, the hotel promises to craft a unique 
                    escape in this beautiful city of lakes. Spread across 95 acres of lush greenery the resort encompasses:
                     • 234 contemporary villas 
                     • Two eclectic dining outlets 
                     • Special kids' activity area 
                     • Outdoor swimming pool 
                     •Spa and fitness center 
                     • Largest divisible banquet halls in Rajasthan
                   """)
                st.image("images/Ananta.jpg", width=500, caption="The Ananta Udaipur")
                if st.button("View location", id(11)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps?q=The+Ananta+Udaipur&source=lmns&bih=664&biw=1536&hl=en-GB&sa=X&ved=2ahUKEwiVqJrmi9jxAhVwhEsFHaDYDeEQ_AUoAXoECAEQAQ')
                if st.button("Booking", id(12)):
                    webbrowser.open_new_tab(url='https://www.anantahotels.com/')

                st.write("## 4. Club Mahindra Assonora")
                st.write("""
                   Welcome to Club Mahindra Assonora, Goa, your home away from home. Idyllically located in North Goa, 12 km
                    away from Mapusa and 24 km away from Panaji. This place offers the perfect mix of value, comfort, and 
                    convenience with luxurious amenities at your doorstep. From top-notch fitness & spa centre to mouth-watering 
                    cuisine, Assonora is the place to be for your weekend getaways. What better way to make the most of your stay 
                    than enjoying some unique amenities like, a water-themed park with a lazy river, a plunge pool with slides, 
                    and a manmade cave with a waterfall. Along with that, we have our very own Happy Hub activities organized to
                     entertain our lovely guests with some team-building exercises, cocktail-making sessions, and an Organic 
                     farm tour. And of course a 24-hour front desk. While you’re here, make sure to visit these beautiful 
                     attractions – Chapora Fort, Basilica of Bom Jesus, Shantadurga Temple, and Divar Island which are at a
                      short distance from our resort. So choose between lounging in your private balcony or engage in activities
                       ensuring you never have a dull moment on your holiday. At Club Mahindra - Assonora, your comfort, 
                       and satisfaction come first.
                   """)
                st.image("images/mahindra.jpg", width=500, caption="Club Mahindra Assonora")
                if st.button("View location", id(13)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/Club+Mahindra+Assonora/@15.6293642,73.9038939,17z/data=!3m1!4b1!4m8!3m7!1s0x3bbf95a10951e01d:0x14b6e197e0af3410!5m2!4m1!1i2!8m2!3d15.6295399!4d73.9060887?hl=en-GB')
                if st.button("Booking", id(14)):
                    webbrowser.open_new_tab(url='https://www.clubmahindra.com/our-resorts/club-mahindra-assonora-goa')

                st.write("## 6. The Tamara Kodai")
                st.write("""
                               The Tamara Kodai is a luxury heritage, all-suite resort envisioned to completely transform 
                               the tourist experience in Kodaikanal. Each of our 53 suites is designed to provide our guests 
                               with comfort, convenience, security & luxury. The Luxury & Superior Luxury suites can be provided
                                with either king-sized or twin beds & fitted with mattresses & pillows of firmness according to our guests’ preferences.
                                   """)
                st.image("images/mahindra.jpg", width=500, caption="Club Mahindra Assonora")
                if st.button("View location", id(14)):
                    webbrowser.open_new_tab(
                        url='https://www.google.com/maps/place/The+Tamara+Kodai/@10.2241028,77.4806713,17z/data=!3m1!4b1!4m8!3m7!1s0x3b07666de109ef95:0xeabc00d02edddfaa!5m2!4m1!1i2!8m2!3d10.2241028!4d77.48286?hl=en-GB')
                if st.button("Booking", id(15)):
                    webbrowser.open_new_tab(
                        url='https://www.tripadvisor.in/Hotel_Review-g303890-d14130196-Reviews-The_Tamara_Kodai-Kodaikanal_Dindigul_District_Tamil_Nadu.html')