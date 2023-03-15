def greet(name) :
    print("Hello", name);
    
def name_input() :
    name = input("Please enter your name: ")
    return name

def language_input() :
    name = input("Please enter your name: ")
    lang_in = input("Choose English, Japanese, or Spanish ")
    if lang_in == "English" :
        print("Hello " + name)
    elif lang_in == "Japanese" :
        print ("Konichiwa " + name)
    elif lang_in == "Spanish" :
        print("Hola " + name)
    

# namae = name_input()

language_input()


# greet(namae)