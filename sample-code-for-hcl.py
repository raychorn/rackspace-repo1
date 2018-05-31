class Greeting():
    def __init__(self, greetings=[]):
        self.greetings = greetings
    
    def greeting(self, aWord):
        if (aWord ==  'Hi'):
            response = 'Greetings for %s.' % (aWord)
        elif (aWord ==  'Hello'):
            response = 'Greetings for %s.' % (aWord)
        elif (aWord ==  'Hola'):
            response = 'Greetings for %s.' % (aWord)
        else:
            found_word = False
            for gr in self.greetings:
                if (gr == aWord):
                    response = 'Greetings for %s.' % (aWord)
                    found_word = True
                    break
            if (not found_word):
                response = 'Sorry I do not understand "%s".' % (aWord)

        return  response
        
        
if (__name__ == '__main__'):
    greetings = []
    greetings.append('Hey')
    greetings.append('Hey there')
    greetings.append("How's it going?")
    greetings.append("How's it hanging?")
    greetings.append("How are you doing?")
    greetings.append("How's trix?")
    # Obviously the list of greetings could be extended to contain as many as can fit in memory.

    gr = Greeting(greetings)
    
    while (1):
        user_entered_this = raw_input("Enter something I can understand? or stop to make me stop. >> ")
        if (str(user_entered_this).strip().lower() == 'stop'):
            break
        print gr.greeting(user_entered_this)

    if (0):
        gr = Greeting()
        
        print gr.greeting('Hi')
        
        print gr.greeting('Hello')
        
        print gr.greeting('Hola')
        
        print gr.greeting('Gibberish')
        
        print 'End of test 1.'
        
        gr = Greeting(greetings)
        
        print gr.greeting('Hi')
        
        print gr.greeting('Hello')
        
        print gr.greeting('Hola')
    
        for aGreeting in greetings:
            print gr.greeting(aGreeting)
    
        print gr.greeting('Gibberish')
        
        print 'End of test2.'
    