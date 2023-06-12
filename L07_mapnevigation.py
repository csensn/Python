# https://www.google.com/maps/dir/Ajmer,+Rajasthan/Sikar,+Rajasthan/@27.0315063,74.6516424,9z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x396be6d8fcb7cd01:0xcbaf8f12eb8100ee!2m2!1d74.6399163!2d26.4498954!1m5!1m1!1s0x396ca4b82334472b:0x7f485cce3a6bf355!2m2!1d75.1397935!2d27.6093912?entry=ttu

import webbrowser
# s_loc = input("Enter source location: ")
# d_loc = input("Enter destination location: ")
# url = 'https://www.google.com/maps/dir/'
# url = url + s_loc.title() + "/" + d_loc.title()
# webbrowser.open(url)

print("1.Youtube \n2.Instagram \n3.Facebook")
choice = int(input("What you want to run: "))

youtube_url = "youtube.com"
insta_url = "instagram.com"
facebook_url = "facebook.com"

if choice ==1:
    ser = input("What you want to listen: ")
    url = "https://www.youtube.com/results?search_query="
    url = url + ser
    webbrowser.open(url)
elif choice == 2:
    webbrowser.open(insta_url)
elif choice == 3:
    webbrowser.open(facebook_url)

# music

# url = url + s_loc.title() + "/" + d_loc.title()