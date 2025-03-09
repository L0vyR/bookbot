
def WordsCounter(book_content):
    words_list = book_content.split()
    print("----------- Word Count ----------")
    print(f"Found {len(words_list)} total words")

def CharacterCounter(book_content):
    character_count_result = {}
    already_counted_list = []
    
    text = book_content.lower()

    for selected_character in text:
        if selected_character not in already_counted_list:
            
            count = 0

            for counted_character in text:
                if selected_character == counted_character:
                    count += 1

            already_counted_list.append(selected_character)
            
            character_count_result[selected_character] = count
    
    return character_count_result

def PrintReport(dictionnary_input):
    
    sort_list = []
    
    for entry in dictionnary_input:
        temp_dict = {}
        temp_dict["letter"] = entry
        temp_dict["count"] = dictionnary_input.get(entry)
        sort_list.append(temp_dict)
    
    def sort_on(dict):
        return dict["count"]
    
   
    print("--------- Character Count -------")
    
    sort_list.sort(reverse=True, key=sort_on)

    for couple in sort_list:
        if couple['letter'].isalpha():
            print(f"{couple['letter']}: {couple['count']}")
    
    print("============= END ===============")