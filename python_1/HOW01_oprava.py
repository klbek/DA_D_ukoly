import json

alice_dict = dict()

with open('alice.txt', mode='r', encoding='utf-8') as alice_file:
    alice_words = alice_file.read()
    alice_words = alice_words.replace(' ', '').replace('\n', '').lower()
    
    for single_letter in alice_words:
        if single_letter not in alice_dict:
            alice_dict[single_letter] = 1
        else:
            alice_dict[single_letter] += 1

with open("hw01_output2.json", mode="w", encoding='utf-8') as outfile:
    json.dump(alice_dict, outfile, ensure_ascii=False, indent=4, sort_keys=True)
