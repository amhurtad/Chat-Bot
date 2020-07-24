import random
import string
import nltk

#initialize variables I will be using later in a function to make these into dictionary and will be added into by functions. 

planner_day = []
planner_activity = []



def remove_punctuation(input_string):
    """ Removes punctuation from a string
    
    Parameters
    
    ----------
    
    input_string = str
    
        input message from user
        
    Returns
    
    -------
    
    out_string = str
      
      input_string without punctuation
      """
    out_string = ""
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char
    return out_string


def selection_day(input_string, check_list, return_string):
    """ inputs new day into planner_day variable and checks if this
        
        string is inside list of days of the week to return a second string
        
    Parameters:
    
    ----------
    
    input_string = str
    
    check_list = list
    
    return_string = str
    
    Returns:
    
    -------
    
    return_string[0] = str
    
    phrase that asks user if they wish to make either dinner or movie plans for that certain day
    """
    global planner_day
    input_string = remove_punctuation(input_string)
    input_string = input_string.lower()
    planner_day.append(input_string)
    if input_string in check_list:
        return return_string[0]

    
def selector(input_string, check_list, return_list):
    """ checks if input string is in a list and if it is return random choice of another list
    
    Parameters:
    
    ----------
    
    input_string = str
    
    check_list = list
    
    return_list - list
    
    Returns:
    
    --------
    
    random.choice(return_list) = string
    
    random string from return_list is returned
    """
    
    input_string = remove_punctuation(input_string)
    input_string = input_string.lower()
    if input_string in check_list:
        return random.choice(return_list)
    

def selection_genre_and_cuisine(input_string, check_list, my_dict, full_phrase):
    """ inputs activity into planner_activity and checks if string is in list
    
    Parameters:
    
    ----------
    
    input_string = str
    
    check_list = list
    
    my_dict = dictionary
    
    full_phrase = str
    
    Returns:
    
    --------
    
    full phrase + "" + input_string + ":" + "" + my_dict[input_string]
    
    full phrase that restates the input_string and finds values of that input string keys of my_dict
    """
    global planner_activity
    input_string = remove_punctuation(input_string)
    input_string = input_string.lower()
    planner_activity.append(my_dict[input_string])
    if input_string in check_list:
        return full_phrase + " " + input_string + ":" + " " + my_dict[input_string]
    

def make_dict(exit_message):
    """ Uses planner_day and planner_activity that have been added into by previous functions
    
    to zip together into dictionary
    
    Parameters:
    
    ----------
    
    exit_message = string
    
    Returns:
    
    end_phrase = string
    
    will output an ending message that also gives dictionary of days as keys and planned events as values
    """
    global planner_day
    global planner_activity
    my_dict = dict(zip(planner_day, planner_activity))
    end_phrase = exit_message + str(my_dict)
    return end_phrase


def end_chat(input_string):
    """ Ends the chatbot 
    
    Parameters:
    
    ----------
    
    input_string = string
    
    Returns:
    
    output = bool
    """
    
    if "im done" in input_string:
         output = True
    else:
         output = False
    return output
    
    
def is_in_list(string_one, list_one):
    """ Finds if one string is inside another list
    
    Parameters:
    
    ----------
    
    string_one = string
    
    list_one = list
    
    Returns:
    
    --------
    
    Boolean
    """
    if string_one in list_one:
        return True
    return False
   
    
def find_in_list(string_two, list_two):
    """ finds string in list and returns in
    
    Parameters:
    
    -----------
    
    string_two = string
    
    list_two = list
    
    Returns:
    
    string_two = string
    
    returns string found in the other list
    """
    if string_two in list_two:
        return string_two
    return None
   
    
#main chatbot function that incorporates all these functions    
def chat_bot():
    chat = True

    planner_day = []
    planner_activity = []
    while chat: 
        
        
        msg = input('\t')
        out_msg = None
        
        #if chat is ended then the chatbot will return a dictionary of planned activities for the week
        if end_chat(msg):
            closing_phrase = "Here are your week plans: "
            out_msg = make_dict(closing_phrase)
            chat = False
        
        #this will test if the there is an out_msg and what the chatot should check for and respond to
        if not out_msg:
            outs = []
            
            #check for greetings and return the appropriate greeting
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            
            #check for initializer (ie "ok", "yeah") that will make chatbot start asking questions
            outs.append(selector(msg, RECOMMENDER_INPUT, RECOMMENDER_OUTPUT))
            
            #checks if day input is in a list and if it is then it returns the appropriate phrase from the chatbot
            if is_in_list(msg, DAY_INPUT):
                day = find_in_list(msg, DAY_INPUT)
                outs.append(selection_day(day, DAY_INPUT, DAY_OUTPUT))
        
            #see if "dinner" input inside list then return phrase
            outs.append(selector(msg, DINNER_INPUT, DINNER_OUTPUT))
            
            #see if "movie" input inside list then return phrase
            outs.append(selector(msg, MOVIE_INPUT, MOVIE_OUTPUT))
            
            # this will see if the user's genre input for movie is inside list then return a set of recomended moies in La Jolla
            if is_in_list(msg, MOVIES_GENRE_INPUT):
                genre = find_in_list(msg, MOVIES_GENRE_INPUT)
                outs.append(selection_genre_and_cuisine(genre, MOVIES_GENRE_INPUT, MOVIE_OPTIONS, MOVIE_PHRASE_OUT))
                
            #this will see if the user's input for cuisine is inside list then return a set of recomended restaurants in La Jolla
            if is_in_list(msg, FOOD_CUISINE_INPUT):
                outs.append(selection_genre_and_cuisine(msg, FOOD_CUISINE_INPUT, FOOD_OPTIONS, FOOD_PHRASE_OUT))
                    
            # checks to see if the input is some sort of grateful response such as "thank you" and asks if they wanna keep making plans
            # and if they do it will restart process
            outs.append(selector(msg, GRATEFUL_INPUT, GRATEFUL_OUTPUT))
            
            # will filter out of all options that we have appended into outs and find random one to output 
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)
            
        
        # if the input is completely unknown it will choose an unknown output   
        if not out_msg:
            out_msg = random.choice(UNKNOWN_OUTPUT)
        
        print(out_msg)
    
        
  
        
#greeting input and output for what chatbot can say and respond to

GREETINGS_IN = ['hi', "hey", "hello", "hola", "hi whats up", "hello there", "hi", "whattup", "hello"]
GREETINGS_OUT = ["Hi! Today I will be your La Jolla guide to plan a fun week! Once you are happy with your plans, just say 'im done' and I will repeat back your plans to you!",
                 
   "Hi! I am here to help you plan your week! Are you ready? Once you are happy with your plans, just say 'im done' and I will repeat back your plans to you!"]

#Chatbot inputs and outputs - How it will respond to the user with questions for them to respond to

RECOMMENDER_INPUT = [ "okay", "sure", "okay", "yes", "sounds good", "ok"]
RECOMMENDER_OUTPUT = ["What day of the week would you like to plan for?"]

DAY_INPUT = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_OUTPUT = ["Would you like to look at dinner or movie plans?"]


DINNER_INPUT = ["dinner"]
DINNER_OUTPUT = ["Okay! What kind of cuisine are you in the mood for?"]

MOVIE_INPUT = ["movie"]
MOVIE_OUTPUT = ["Awesome! What kind of movie are you looking to watch?"]

#Unknown outputs for chatbot

UNKNOWN_OUTPUT = ["I'm a little bit shy right now ask later", "Hmmmm...", "Don't know sorry", "I can't answer that"]

#Movie input and outputs for chatbot to say or to respond to

MOVIE_PHRASE_OUT = "Great choice! I have found these movies currently playing in theaters near you under"

MOVIES_GENRE_INPUT = ["comedy", "horror", "thriller", "drama", "family"]

MOVIE_OPTIONS = {"comedy":"Once Upon a Time in Hollywood",
                 
                 "horror":"It: Chapter 2", "thriller": "Parasite, Knives Out",
                 
                 "drama": "A Beautiful Day in the Neighborhood, Once Upon a Time in Hollywood, Queen & Slim",
                 
                 "family": "Frozen 2, Lion King, Playing with Fire"}


#Food input and output for things the chatbot can say or respond to

FOOD_PHRASE_OUT = "Sounds good!  I found the top rated restaurants on Yelp in the La Jolla area known for their"

FOOD_CUISINE_INPUT = ["italian", "mexican", "chinese", "thai", "indian", "american", "vietnamese", "korean",
                      "japanese", "vegetarian"]

FOOD_OPTIONS = {"italian": "Piatti, Bernini's Bistro, Osteria Romantica, Pizza Pronto",
                
                 "mexican": "Puesto La Jolla, The Taco Stand, Vallarta's, Pueblo",
                
                 "chinese": "Din Tai Fung, Shan Xi Magic Kitchen, Mandarin Wok Restaurant, Spicy City",
                
                 "thai": "Spice and Rice Thai Kitchen, Turmeric Thai Kitchen, Lanna Thai Cuisine",
                
                 "indian": "Royal India, Himalayan Kitchen, Punjabi Tandoor", 
                
                 "american": "The Promiscuous Fork, The Spot La Jolla, Duke's La Jolla",
                
                 "vietnamese": "Pho La Jolla, Pho Cow Cali Express, Phuong Trang",
                
                 "korean": "Bonchon, Friend's House, Buga Korean BBQ",
                
                 "japanese": "Blue Ocean Sushi, Himitsu, Sushi Otsa",
                
                 "vegetarian": "Green Door Cafe, True Food Kitchen, Don Carlos Taco Shop"}

GRATEFUL_INPUT = ["thanks", "thank you", "thanks", "thanks so much", "thx", "ty"]
GRATEFUL_OUTPUT = ["You're welcome! Would you like to make more plans?"]