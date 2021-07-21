import datetime
n=True
title_try = 1
thumb_try = 1
author_try = 1
footer_try = 1
now = datetime.datetime.now()
real_time = now.strftime("%Y-%m-%d %H:%M")
file = open('embed.txt','a')
file.write(real_time+"\n\n")
file.close



while n==True:
    print("\n1.title\n2.thumbnail_url\n3.author\n4.footer\n5.set_image\n6.add_field\n7.quit\n")
    value = int(input())
    #quit
    if value == 7:
        n=False

    elif value == 6:
        ask = input("if want in inline reply with 'y' else 'n' --\n")
        if ask == 'y' or ask == 'Y':
            print("Its in inline now ")
            name = input("Enter name --\n")
            value = input("Enter value --\n")
            test = f"embed.add_field( name = '{name}' , value = '{value}' , inline = {True} )"
            file = open("embed.txt","a")
            file.write( test +'\n')
            file.close
            print(test)
        elif ask == 'n' or ask == 'N':
            print("It is not in inline now ")
            name = input("Enter name --\n")
            value = input("Enter value --\n")
            test = f"embed.add_field( name = '{name}' , value = '{value}' , inline = {False} )"
            file = open("embed.txt","a")
            file.write( test +'\n')
            file.close
            print(test)

    #footer
    elif value == 4:
        if footer_try ==1:
            name = input("enter text --\n")
            icon = input("Enter icon url for author ==\n")
            test = f"embed.set_footer(text = '{name}' , icon_url = '{icon}')"     
            file = open("embed.txt","a")
            file.write( test +'\n')
            file.close
            print(test)      
            footer_try =0
        elif footer_try ==0:
            print("Sorry cant add more than once. ")


    elif value == 3:
        if author_try == 1:
            name = input("enter author name --\n")
            icon = input("Enter icon url for author ==\n")
            test = f"embed.set_author(name = '{name}' , icon_url = '{icon}')"
            file = open("embed.txt","a")
            file.write( test +'\n')
            file.close
            print(test)

            author_try=0
        elif author_try ==0:
            print("Author can be added only once. ")

    #set_image
    elif value == 5:
        img = input("Enter image url you want to set --\n")
        test = f'embed.set_image( url = "{img}")'
        file = open("embed.txt","a")
        file.write( test +'\n')
        file.close
        print(test)

    #title
    elif value == 1:
        if title_try == 1:
            print("Enter your embed title --")
            data = input()
            print("Enter your embed description --")
            discrip = input()
            print("Enter your embed colour --")
            clr = input()
            test = f"embed = discord.Embed(title = '{data}',description = '{discrip}',color = {clr})"
            file = open("embed.txt","a")
            file.write( test +'\n')
            file.close
            print(test)
            title_try=0
        elif title_try == 0:
            print("sorry title can be added only once")
    
    #thumbnail
    elif value == 2:
        if thumb_try == 1:
            print("Enter your thubnail url --")
            url = input()
            test = f"embed.set_thumbnail(url = '{url}')"
            file = open("embed.txt","a")
            file.write( test +'\n')
            file.close       
            print(test)
            thumb_try = 0
        elif thumb_try == 0:
            print("Thubnail cann be added only once")
    



