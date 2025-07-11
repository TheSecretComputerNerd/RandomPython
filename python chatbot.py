import re
import long_responses
def message_probability(user_message, recognised_words, single_response=False, required_words = []):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    
    #calculates the percent of recognised words in a user message
    persentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_requiredwords = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_repsonse, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_resonse, required_words)

# Response ---------------------------------------------------------------------------------------------------------
        response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
        response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_word=['how'])
        response('Thank you', ['you', 'you\'re' 'are', 'very', 'impressive', 'cool', 'awesome'], required_word=['are'])

        best_match = max(highest_prob_list, key=highest_prob_list.get())
        print(highest_prob_list)

        return best_match
        
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#testing the response system
while True:
    print("Bot" +   get_response int((input("You: "))))
    
