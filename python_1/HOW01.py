import json

alice_dict = dict()

with open('alice.txt', mode='r', encoding='utf-8') as alice_file:
    for alice_words in alice_file:
        alice_words = alice_words.replace(' ', '').replace('\n', '')

        for single_letter in alice_words:
            cleaned_letter = single_letter.strip().lower()

            if cleaned_letter not in alice_dict:
                alice_dict.update({cleaned_letter: 1})
            else:
                alice_dict[cleaned_letter] += 1

alice_sorted_dict = dict(sorted(alice_dict.items()))

with open("hw01_output.json", mode="w", encoding='utf-8') as outfile:
    json.dump(alice_sorted_dict, outfile, ensure_ascii=False, indent=4)
