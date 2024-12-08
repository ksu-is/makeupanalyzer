'''
Telegram Bot Interface.
'''

#Import the needed libraries
import telebot
from telebot import types
from vision_api import Cream
from dataset_ADT import DataframeDataset

#Enter API_KEY from file 'Keys' 
#has now been updated with our actual API key
ingredients = None
API_KEY = '8083137281:AAGQiXiBuXorqrVt3QV7hiSW_g5UeefP0WI'

#Create and activate bot-service instance.
bot = telebot.TeleBot(API_KEY)

#Markups for the interface.
markup_for_yes_no = types.InlineKeyboardMarkup()

item_yes = types.InlineKeyboardButton(text='YES', callback_data='yes')
item_no = types.InlineKeyboardButton(text='NO', callback_data='no')

markup_for_yes_no.add(item_yes, item_no)

#Create a 'Cream' ADT-service instance.
cream_processor = Cream()

#Create storage-service ADTs for the datasets.
pore_clogging_dataset = DataframeDataset()
pore_clogging_dataset.read_data('Ingredients_Makeup.xlsx')

#Global storage for demand
ingredients = None

#Handle the initial message.
@bot.message_handler(commands=['start'])
def start(message):
    """
    Start the dialog with the bot.

    Args:
        message ([telebot.types.Message]): [message interface-service].
    """
    bot.send_message(message.chat.id, "Hi! I`m a Cosmetics Advisor Bot. \
I can analyze your cosmetic product for pore-clogging ingredients and explain why it not acne-safe.")
    bot.send_message(message.chat.id, 'To use the following service take next actions:\n\
----------------------------------------------------------\n\
- enter the a command \'/sendphoto\' to start the program;\n\
----------------------------------------------------------\n\
- take a picture of the back of the product with wits decription and chemical composition list;\n\
----------------------------------------------------------\n\
- send it in chat after the message request from the bot;\n\
----------------------------------------------------------\n\
- you\'ll get a response with results of the analysis on any found pore-clogging ingredients;\n\
and an \'yes\'-\'no\' request: whether you want to get more info on the ingredients effects;\n\
----------------------------------------------------------\n\
- choose desirable option and wait a second for an answer;\n\
        _______________________________________________')
    bot.send_message(message.chat.id, 'To start -> send a command: /sendphoto"')

#Handle the sending communication-message process.
@bot.message_handler(commands=['sendphoto'])
def add_photo(message):
    """
    Receives a photo from the user.

    Args:
        message ([telebot.types.Message]): [message with user's photo].
    """
    bot.send_message(message.chat.id, 'Please send a photo of your cosmetic ingredients.')

    #Activate the handler of the new messages.
    bot.register_next_step_handler(message, photo)

#analyzing the uploaded photo
def photo(message):
    global ingredients
    try:
        #getting photo file
        file_info = bot.get_file(message.photo[-1].file_id)
        photo_file = bot.download_file(file_info.file_path)
        
        #notifying user
        bot.reply_to(message, "Processing your photo...")

        #Extracting and analyzing ingredients
        ingredients = cream_processor.check_ingredients(photo_file, pore_clogging_dataset)
        pore_clogging_ingredients = []

        head = ingredients.next
        while head is not None:
            if head.element is not None:
                pore_clogging_ingredients.append(head.element)
            head = head.next
        if pore_clogging_ingredients:
            bot.send_message(
                message.char.id,
                "Here are the following pore-clogging ingredients in your product:"
            )    
            for ingredients in pore_clogging_ingredients:
                bot.send_message(
                    message.chat.id,
                    decorate_ingredient_display(ingredients)
                )
            bot.send_message(message.chat.id, "Do you want an explanation for each pore-clogging ingredient?", reply_markup=markup_for_yes_no)
        else:
            bot.send_message(message.chat.id, "No pore-clogging ingredients were found in this product.")
    except Exception as e:
        bot.send_message(message.char.id, f"An error occurred: {str(e)}. Please try again.")

#decorate ingredient details for display
def decorate_ingredient_display(ingredient):
    ingredient_name = ingredient['ingredient']
    reason = ingredient['reason']
    comedogenic_grade = ingredient['comedogenic_grade']
    impact_description = ingredient['impact_description']

    return f"""
    ___________________________________________
    Ingredients: {ingredient_name.capitalize()}
    -------------------------------------------
    Comedogenic Grade: {comedogenic_grade}
    -------------------------------------------
    Reason: {reason}
    -------------------------------------------
    Impact Description: {impact_description}
    ___________________________________________
    """

#Handler for the answering-dialog interface.
@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    """
    Programs the 'Yes'-'No' answer interface.

    Args:
        call ([telebot.types.Message]): [call-answer from the user].
    """
    #Access global ingredients storage-variable.
    global ingredients

    #'Yes' condition.
    if call.data == 'yes':
        #Provide detailed explanations
        head = ingredients.next
        while head is not None:
            if head.element is not None:
                bot.send_message(call.message.chat.id, decorate_ingredient_display(head.element))
            head=head.next
    bot.send_message(call.message.chat.id, "Thanks for using the bot! Send /sendphoto to analyze another product. \n")



if __name__ == "__main__":
    bot.polling()
