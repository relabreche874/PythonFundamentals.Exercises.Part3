def lang_select() :
    int(choice) = input("Please choose 1-English 2-Japanese 3-Spanish ")
    
    if choice == 1 :
        name = input("Please enter your name ")
        print(f"Hello {name}")
    
    elif choice == 2 :
        name = input("お名前を入力してください ")
        print(f"こんにちは {name}")
    
    else :
        name = input("Por favor, escriba su nombre ")
        print(f"Hola {name}")


lang_select()



