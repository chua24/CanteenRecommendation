import pygame,sys
import time
import random
import math
from collections import OrderedDict
from operator import itemgetter

#-------------------- Welcome Message --------------------

def welcomeMsg():
    print ("Welcome to the Ask Panda system! Please enter your option!")
    print ("1: Search by Location")
    print ("2: Search by Price")
    print ("3: Search by Food/Cuisine")
    print ("4: Sort by Rank")
    print ("5: Search by Hours")
    print ("6: Exit")

#-------------------- All Options --------------------

def allOption():
    
    if option == LOCATION:
        if __name__ == '__main__':
            main()
        print()
        continu()
    
    elif option == PRICE:
        getPrice(restinfo)
        print()
        continu()
    
    elif option == CUISINE:
        searchFood(restinfo)
        print()
        continu()
        
    elif option == RANK:
        sortrank(canteenlist)
        print()
        continu()

    elif option == HOURS:
        print (searchhours(canteenlist))
        print()
        continu()

#-------------------- Prompt Continue --------------------

def continu():
    print()
    try:
        print("Would you want to continue asking Panda?")
        print("1: Continue")
        print("2: Exit")
        CONTINUE = 1
        OUT = 2

        userInput = CONTINUE
    
        while userInput != OUT:
            userInput= int(input("Choose an option: "))
            if userInput == CONTINUE:
                print()
                welcomeMsg()
                option = int (input ("Option: "))
                if option == LOCATION:
                    if __name__ == '__main__':
                        main()
                    continu()
            
                elif option == PRICE:
                    getPrice(restinfo)
                    continu()
            
                elif option == CUISINE:
                    searchFood(restinfo)
                    continu()
            
                elif option == RANK:
                    sortrank(canteenlist)
                    continu()

                elif option == HOURS:
                    print(searchhours(canteenlist))
                    continu()
                
                elif option == EXIT:
                    print("Thank you for playing this game! Panda hopes to see you again!")
                    sys.exit()

            elif userInput == OUT:
                print("Thank you for playing this game! Panda hopes to see you again!")
                sys.exit()

    except ValueError:
        print("Input Error! Please enter a number!")
        continu()
        
#-------------------- 1: Search by Location / Mouseclick --------------------

places = {"Starbucks":(311,266), "McDonald":(361,287),"Bakery":(382,310),\
          "Each-A-Cup":(377,333),"Peach Garden":(317,239),"Paik's Bibimbap":(366,362),\
          "Koufu":(254,674),"Quad Cafe":(249,404),"Ananda Kitchen":(1050,326),\
          "NIE Canteen":(338,79),"Pioneer Canteen":(793,788),"Canteen 2":(756,513)}

def MouseClick():
    finish = False
    while finish == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                newD = {}
                for i,j in places.items():
                    newD.update({i : round(calculate_distance(mouseX, mouseY,j[0],j[1]),2)})  #add to newD the distance j[0] = xpos j[1] = ypos and round to 2 digits
                sorted_places = {k: v for k, v in sorted(newD.items(), key=lambda x: x[1])} #sort by the distance (key) for each location
                od = OrderedDict(enumerate(sorted_places))  #to give sorted_places all indexes
                sortedNames = list(od.values())[0:5]    #to list the values of the top 5 sorted_places 
                sortedValues = []    
                for k in sortedNames:
                	distanceKM = round((sorted_places.get(k)*3.0277)/1000,2) #get the value and convert it to real location
                	sortedValues.append(distanceKM)
                finalResult = zip(sortedNames, sortedValues) #combine the restaurant and the new value 
                print ("Top 5 places closest to you:")
                n = 1 #number the recommendations
                for tup in finalResult:
                    print(n,".", tup[0], "is", str(tup[1]) + "km away from your current location")
                    n += 1
                finish = True
    return (mouseX, mouseY)

def label_map(screen):
    font = pygame.font.SysFont("monospace", 20 , bold = True)
    label1 = font.render("Starbucks", True, (255,255,255) , (0,0,0))
    label2 = font.render("McDonald", True, (255,255,255) , (0,0,0))
    label3 = font.render("Bakery", True, (255,255,255) , (0,0,0))
    label4 = font.render("Each-A-Cup", True, (255,255,255) , (0,0,0))
    label5 = font.render("Peach Garden", True, (255,255,255) , (0,0,0))
    label6 = font.render("Paik's Bibimbap", True, (255,255,255) , (0,0,0))
    label7 = font.render("Koufu", True, (255,255,255) , (0,0,0))
    label8 = font.render("Quad Cafe", True, (255,255,255) , (0,0,0))
    label9 = font.render("Ananda Kitchen", True, (255,255,255) , (0,0,0))
    label10 = font.render("NIE Canteen", True, (255,255,255) , (0,0,0))
    label11 = font.render("Pioneer Canteen", True, (255,255,255) , (0,0,0))
    label12 = font.render("Canteen 2", True, (255,255,255) , (0,0,0))
    
    screen.blit(label1, (311,266))
    screen.blit(label2, (361,287))
    screen.blit(label3, (382,310))
    screen.blit(label4, (377,333))
    screen.blit(label5, (317,239))
    screen.blit(label6, (366,362))
    screen.blit(label7, (254,674))
    screen.blit(label8, (249,404))
    screen.blit(label9, (1050,326))
    screen.blit(label10, (338,79))
    screen.blit(label11, (793,788))
    screen.blit(label12, (756,513))

def calculate_distance(buttonX,buttonY,x,y):
    distance = math.sqrt((buttonX-x)**2 + (buttonY-y)**2)
    return distance

def get_user_location():

# make necessary initializations for Width, Height
    W = 1221
    H = 862
    
#initialize display window, call it screen
    screen = pygame.display.set_mode((W, H))

# read image file and rescale it to the window size
    screenIm = pygame.image.load("NTU Campus.png")
    screenIm = pygame.transform.scale(screenIm, (W, H))

#add the image over the screen object
    screen.blit(screenIm, (0, 0))

# add the text over the screen object
    label_map(screen)

# will update the contents of the entire display window
    pygame.display.flip()

# get outputs of Mouseclick event handler
    buttonX, buttonY = MouseClick()


def main():
	pygame.init()
	get_user_location()
	
#-------------------- Restaurant Dictionary --------------------

restinfo = {'Mcdonalds': {'burger' : '4', 'fries': '3','fried chicken':'4'},
            'Koufu': {'pasta': '5', 'japanese': '5','yong tau foo': '4'},
            'Bakery': {'bread' : '2', 'waffle': '2', 'cake': '3'},
            'Each-A-Cup': {'bubble tea': '2'},
            'Canteen 2': {'chinese': '8', 'ayam penyet': '5', 'xiao long bao':'7', 'mixed rice':'4'},
            'Ananda Kitchen': {'chicken': '6' , 'naan' : '3', 'indian': '6'},
            'Quad Cafe': {'korean': '5', 'yong tau foo': '4', 'mixed rice' :'4'},
            'Pioneer Canteen': {'thai': '5' ,'mixed rice': '4'},
            'NIE': {'ban chor mee': '3', 'mixed rice': '3'},
            "Paik's Bibimbap": {'bibimbap': '9', 'korean': '10'},
            'Peach Garden': {'chinese': '15'}
            }


mcdonald = {"name": "Mcdonalds",
            "hours": "Mon to Sat: 7am to 12am | Sun & PH: 10am to 10pm",
            "rank": 1}


starbucks = {
            "name": "Starbucks",
            "hours": "Mon to Fri: 7am to 10pm | Sat & Sun: 7am to 5pm | PH: Closed",
            "rank": 2}


bakerycuisine = {"name": "Bakery Cuisine",
            "hours": "Mon to Fri: 7am to 9pm | Sat, Sun & PH: 9am to 7pm",
            "rank": 7}


eachacup = {"name": "Each A Cup",
            "hours": "Mon to Fri: 9am to 9pm | Sat & Sun: 9am to 6pm | PH: Closed",
            "rank": 6}

canteen2 = {"name": "Canteen 2",
    'hours': "Daily: 7am - 9pm",
    'rank': 4}

ananda = {"name": "Ananda Kitchen",
    'hours': "Daily: 12pm - 1030pm",
    'rank': 10}

quad = {"name": "Quad Cafe",
    'hours': "Mon to Fri: 7am - 9pm | Sat: 7am - 3pm | Sun & PH: Closed",
    'rank': 9}

pioneer = {"name": "Pioneer Canteen",
    'hours': "Daily: 7am - 9pm",
    'rank': 8}

nie = {"name": "NIE Canteen",
    'hours': "Daily: 7am - 9pm",
    'rank': 5}

paiks = {"name": "Paiks Bibimbap",
    'hours': "Mon to Fri: 10am - 9pm | Sat: 10am - 3pm | Sun & PH: Closed",
    'rank': 12}


peachgarden = {"name": "Peach Garden",
    'hours': "Daily: 11am to 2.30pm / 5pm to 10pm",
    'rank': 11}

koufu = {"name": "Koufu Canteen",
    'hours': "Mon to Fri: 7am to 9pm | Sat: 7am to 3pm | PH: Open (except Sun)",
    'rank': 3}

canteenlist = [mcdonald, starbucks, bakerycuisine, eachacup, canteen2, ananda, quad, \
               pioneer, nie, paiks, peachgarden,koufu ]

#-------------------- 2: Search by Price --------------------

def getPrice(fooddict):

    print()
    userInput = input("Please enter your maximum budget: ")
    
    restlist = []
    for rest in fooddict:     # iterates key (restaurant) in dictionary
        for food in fooddict[rest]:     # iterates key (food) in dictionary (restaurant)
            x = fooddict[rest][food]     # assign x to the values (price) in dictionary
            #print ('x = ' , x)
            if int(userInput) >= int(x):
                if rest not in restlist:     # if rest is in restlist, will not append
                    restlist.append(rest)

    if len(restlist) == 0:
        print("There is no food within the budget.")
    else:
        print()
        print("Restaurants within your budget:")
        for li in restlist:
            print(li)
                
        
#-------------------- 3: Search by Food --------------------

def searchFood(diction):
    
    print()
    userInput = str(input("Type your preferred food/cuisine: "))

    listofrest= []
    for rest in diction:    # iterates key (restaurant) in dictionary   
        if userInput in diction[rest]:
            listofrest.append(rest)      # adds to the list
        
    if len(listofrest)==0:
        print ("Panda apologizes. Food is not available in any of the canteens.")
    else:
        print()
        print ("Available in:")
        for li in listofrest:
            print (li)

#-------------------- 4: Sort by Rank --------------------

def sortrank(li):
    
    finish = True
    while finish:
        ranklist = sorted(canteenlist, key = itemgetter('rank')) #sorted according to rank

        ranknames = [n['name'] for n in ranklist]
        rankno = [i['rank'] for i in ranklist]

        finallist = zip(ranknames,rankno)

        print()
        for tup in finallist:
            print("Rank", tup[1], ":" , tup[0])
        finish = False

    
#-------------------- 5: Search by Hours --------------------

def searchhours(li):
    print()
    print ("List of Canteens:")
    for can in canteenlist:
        print (can['name'])

    print()
    while True:
        userInput = input("Enter a canteen in the list: ")
    
        for canteen in li:
            if str(userInput) == str(canteen['name']):
                return canteen['hours']
                break
        else:
            print ("Please input the canteens on the list.")
            return searchhours(li)

        
#-------------------- Main Block Includes Pygame Startmenu GUI --------------------

pygame.init()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption('F&B Recommendation Game')   #for the window caption

font = pygame.font.SysFont("Goudy Stout", 30)

text2 = font.render("The", True, (200,200,0))
text = font.render("ASK PANDA", True, (200,200,0))
text3 = font.render("Game", True, (200,200,0))

font = pygame.font.SysFont("franklin gothic", 30)

buttontext = font.render("Press to Start!", True, (255,255,255))  
    
LOCATION = 1
PRICE = 2
CUISINE = 3
RANK = 4
HOURS = 5
EXIT = 6

option = LOCATION     # initialise option


startmenu = True
while startmenu:   #to pop up start menu

    for event in pygame.event.get():
        if event.type == EXIT:
            pygame.quit()
            sys.exit()
            
    screen.fill((0, 0, 20))
    screen.blit(text,
    (250 - text.get_width() // 2, 200 - text.get_height() // 2))
    screen.blit(text2,
    (340 - text.get_width() // 2,130))
    screen.blit(text3,
    (320 - text.get_width() // 2,230))
    mouse = pygame.mouse.get_pos()  #mouse position
    click = pygame.mouse.get_pressed()  #detect click

    if 150+200 > mouse[0] > 150 and 350+50 > mouse[1] > 350:   #if mouse is within the boundaries of the button
        pygame.draw.rect(screen, (0,255,0) ,(150,350,200,50)) #button color becomes brighter (x,y, width, length)  
        
        if click[0] == 1:  #if there is a click in the button, goes to Alloption function
            while option != EXIT:
                welcomeMsg()
                print()
                option = int (input ("What option would you want to ask Panda to do: "))
                allOption()
                if option == EXIT:
                    print("Thank you for playing this game! Panda hopes to see you again!")
                    sys.exit()

            startmenu = False


    else:
        pygame.draw.rect(screen, (0,100,0) ,(150,350,200,50)) #button stays the same color (x,y, width, length)

    screen.blit(buttontext, (150+25, 350+15))
    screenIma = pygame.image.load("panda.png")
    screenIma = pygame.transform.scale(screenIma, (150, 150))
    screen.blit(screenIma, (340, 300))


    pygame.display.flip()  



