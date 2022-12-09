import re
import blog.long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses 
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how','are'])
    response('Happy to see you!', ['well', 'good', 'best', 'amazing', 'super', 'great'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'likes', 'your', 'services'], required_words=['likes','services'])
    response('we are providing the instant health solution', ['which', 'kind', 'of', 'services', 'you', 'are', 'providing'], required_words=['which', 'services', 'providing'])
    response('thank you for asking, i am a bot', ['what', 'is', 'your', 'name'], required_words=['what','your', 'name'])
    response("i don't know as i am a bot", ['what', 'is', 'your', 'age'], required_words=['what', 'your','age'])
    response('Please tell me the problem', ['i', 'am', 'not', 'able', 'to','access','website'], required_words=['not','able', 'access','website'])
    response('sorry for having the problem, please refresh your page', ['i', 'am', 'not', 'able', 'to', 'load','the','webpages'], required_words=['not','able','load','webpages'])
    response('it means you can have the facilities very fast', ['what', 'does', 'mean', 'by','instant'], required_words=['what','mean','instant'])
    response('By providing the solutions of your problems', ['How', 'your', 'website','can' 'help','me'], required_words=['help'])
    response('Regarding your problems', ['which', 'kinds', 'of', 'solution'], required_words=['which','solution'])
    response('Thank you!', ['i', 'like', 'your', 'services'], required_words=['like'])
    response('1.NGO, 2.Hospital, 3.Blogs', ['tell', 'me', 'your', 'services'], required_words=['services'])
    response('You can see the available ngo near to you for your solutions', ['facilities', 'of', 'NGO'], required_words=['facilities','ngo'])
    response('You can see the available hospitel near to you for your solutions and book the appointment', ['facilities', 'of', 'hospital'], required_words=['facilities','hospital'])
    response('Blog gives you basic idea to prevent the health issues', ['facilities', 'of', 'blog'], required_words=['facilities','blog'])
    
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    ''' print(highest_prob_list)
     print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')'''

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# #Testing the response system
# while True:
#     print('Bot: ' + get_response(input('You: ')))
