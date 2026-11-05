#DVLA programme to check and generate licence plate
#define my CONSTANTS
SEPFEB_ADD_ON = 50
CURRENT_YR = 26
SECOND_CURRENT_YR = 76
REQ_CHARS = 7
INVALID_LETTERS = 'QIZ'
VALID_FIRST_LETTERS = 'ABCDEFGHKLNMOPRSVWY'
VALID_SECOND_LETTERS = 'ABCDEFGHJKLNMOPRSTUVWXY'
REGIONS = ['Anglia','Birmingham','Cymru','Deeside','Essex','Forest & Fens','Garden of England','Hampshire & Dorset',
         '(No official mnemonic)','London','Manchester','North','Oxford','Preston','Reading','Scotland','Severn Valley','West of England','Yorkshire']
FIRST_LETTER = ['A','B','C','D','E','F','G','H','K','L','M','N','O','P','R','S','V','W','Y'] 

LIST_OF_DVLA_OFFICES = [
['Anglia','Peterborough','ABCDEFGHJKLMN'],
['Anglia','Norwich','OPRSTU'],
['Anglia','Ipswich','VWXY'],

['Birmingham','Birmingham','ABCDEFGHJKLMNOPRSTUVWXY'],

['Cymru','Cardiff','ABCDEFGHJKLMNO'], 
['Cymru','Swansea','PRSTUV'],
['Cymru','Bangor','WXY'] ,

['Deeside', 'Chester','ABCDEFGHJK'], 
['Deeside', 'Shrewsbury', 'LMNOPRSTUVWXY'],

['Essex','Chelmsford','ABCDEFGHJKLMNOPRSTUVWXY'],

['Forest & Fens','Nottingham','ABCDEFGHJKLMNOP'], 
['Forest & Fens','Lincoln', 'RSTUVWXY'],

['Garden of England','Maidstone', 'ABCDEFGHJKLMNO'], 
['Garden of England','Brighton', 'PRSTUVWXY'],

['Hampshire & Dorset','Bournemouth', 'ABCDEFGHJ'], 
['Hampshire & Dorset','Portsmouth', 'KLMNOPRSTUVXY'],
['Hampshire & Dorset','Portsmouth (Isle of Wight)','W'],

['(No official mnemonic)', 'Luton', 'ABCDEFGHJKL'], # Also known as k
['(No official mnemonic)','Northampton', 'MNOPRSTUVWXY'],

['London','Wimbledon', 'ABCDEFGHJ'], 
['London','Stanmore','KLMNOPRST'], 
['London','Sidcup', 'UVWXY'],

['Manchester','Manchester','ABCDEFGHJKLMNOPRSTUVWXY'],

['North','Newcastle','ABCDEFGHJKLMNO'], 
['North','Stockton', 'PRSTUVWXY'], 

['Oxford','Oxford','ABCDEFGHJKLMNOPRSTUVWXY'],

['Preston','Preston', 'ABCDEFGHJKLMNOPRST'], 
['Preston','Carlisle','UVWXY'],

['Reading','Reading','ABCDEFGHJKLMNOPRSTUVWXY'],

['Scotland','Glasgow','ABCDEFGHJ'], 
['Scotland','Edinburgh','KLMNO'], 
['Scotland','Dundee','PRST'], 
['Scotland','Aberdeen', 'UVW'], 
['Scotland','Inverness','XY'], 

['Severn Valley','Worcester','ABCDEFGHJKLMNOPRSTUVWXY'],# also known as V 

['West of England','Exeter', 'ABCDEFGHJ'], 
['West of England','Truro', 'KL'], 
['West of England','Bristol', 'MNOPRSTUVWXY'], 

['Yorkshire','Leeds','ABCDEFGHJK'], 
['Yorkshire','Sheffield', 'LMNOPRSTU'], 
['Yorkshire','Beverley','VWXY']
]

#generates a random number plate
def rand_plate():
   import random 
   char1 = random.choice(VALID_FIRST_LETTERS) 
   char2 = random.choice(VALID_SECOND_LETTERS)
   random_gen = random.randint(1,2)
   if random_gen == 1:
       char34 = random.randint (2,26) 
       char34 = str(char34)
       if len(char34) == 1:
        char34 = '0' + char34
   else:
      char34 = random.randint(51,76)
      char34 = str(char34)
   char5 = random.choice(VALID_SECOND_LETTERS)
   char6 = random.choice(VALID_SECOND_LETTERS)
   char7 = random.choice(VALID_SECOND_LETTERS)

   generated_plate = char1+char2+char34+char5+char6+char7
   print (generated_plate,'is the generated plate')

def find_Office():
   user_licence_plate = input('Enter licence plate').upper()
   user_licence_plate = user_licence_plate.replace(" ","")
   while len(user_licence_plate) != 7:
      user_licence_plate = input('Enter licence plate that is 7 letters long').upper()
   if user_licence_plate[0] in FIRST_LETTER:
      print(f'User licence plate in region : {REGIONS[FIRST_LETTER.index(user_licence_plate[0])]}')
      region = REGIONS[FIRST_LETTER.index(user_licence_plate[0])]
      for i in range(len(LIST_OF_DVLA_OFFICES)):
         if LIST_OF_DVLA_OFFICES[i][0] == region:
            if user_licence_plate[1] in LIST_OF_DVLA_OFFICES[i][2]:
               print('The office is located in', LIST_OF_DVLA_OFFICES[i][1])
   else:
      print('Invalid first letter for region')
   
           

#figure out age of vehicle
def car_age():
   user_licence_plate = input ('Enter your licence plate : ').upper()
   user_licence_plate = user_licence_plate.replace(' ', '')
   plate_numbers = user_licence_plate[2:4]
   if len(user_licence_plate) != REQ_CHARS:
      print ('Plate wrong length')
      main_menu()
   
   if plate_numbers.isdigit() == True:
      plate_numbers = int(user_licence_plate[2:4])
      if plate_numbers < 50:
         plate_age = 2026 - (2000 + (plate_numbers))
         print(f'Your car is registered from March 1st to August 31st {2026-plate_age} so is between {plate_age-0.5} and {plate_age} years old')
      else:
         plate_age = 2026 - (2000 + (plate_numbers - 50))
         print(f'Your car was registered between September 1st {2026-plate_age} and February 28th {2026-plate_age+1} so is between {plate_age-0.5} and {plate_age} years old')
   else:
      print('Numbers in wrong spot')

def check_plate():        
   #this function takes a string and strips out the spaces
   user_licence_plate = input ('Enter your licence plate').upper()
   #This lineof code here successfully checks an user enterd licen

   def strip_spaces(plate):
    plate = plate.replace(' ', '') # removes the spaces by replacing them with no gaps
    return plate

   #this function returns True if the final three letters are valid, False otherwise
   def validEnd(valid_letters):
    for char in valid_letters: 
      if char in INVALID_LETTERS:
        return False
     
    return True
 
   user_licence_plate = strip_spaces(user_licence_plate)

   #license plate length check
   if len(user_licence_plate) != REQ_CHARS:
      print ('Plate wrong length - PLATE CHECK END')
      main_menu()

   if  user_licence_plate[0] not in VALID_FIRST_LETTERS or user_licence_plate[1] not in VALID_SECOND_LETTERS:
      print ('Licence plate has the invalid letters I J Q T U W X inside it - PLATE CHECK END ')
      main_menu()

   plate_numbers = user_licence_plate [2:4]
   if plate_numbers.isdigit() == False:
      print('Numbers in wrong spot - PLATE CHECK END')
      main_menu()

   plate_numbers = int(plate_numbers)
   if not (2 <= plate_numbers <= CURRENT_YR or 51 <= plate_numbers <= SECOND_CURRENT_YR):
      print('Invalid plate numbers - PLATE CHECK END')
      main_menu()

   final_letters = user_licence_plate[4:7]
   if (validEnd(final_letters)) and final_letters.isalpha():
      print('VALID LICENCE PLATE WOOHOOO !!!!')
      print('Your licence plate is',user_licence_plate)            
   else:
      print('That is  NOT valid final 3 letters for a licence plate')
      print('LICENCE PLATE INCORRECT')

def main_menu(): 
   #for main menu of dvla
   import time
   time.sleep(1)
   validChoice = ['Q','C','G','A','L','1','2','3','4','5']
   print ('\n1. (Q)uit the program \n2. (C)heck is licence plate is valid \n3. (G)enerate licence plate')
   print ('4. (A)ge of licence plate \n5. (L)octaion of licence plate')
   
   #get users choice
   choice = input('Enter your choice from Q C G O L : ').upper()
   while choice not in validChoice:
         choice = input('Enter your choice with valid options : ').upper()

   if choice == 'Q' or choice =='1':
      print ('Thanks for using me ! quitting program')
      quit()
   elif choice =='C' or choice == '2':
      print ('You have choosen to check if the licence plate is valid \n')
      check_plate()
   elif choice =='G' or choice ==  '3':
      print ('You have choosen to generate a licence plate\n')
      rand_plate()
   elif choice =='A' or choice == '4' :
      print ('You have choosen to out put the age of a car based on plate\n')
      car_age()
   elif choice =='L' or choice == '5' :
      print ('You have choosen to check location of a licence plate\n')
      find_Office()
   while choice != 'Q':
      main_menu()
main_menu()