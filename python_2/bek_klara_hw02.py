import json

title = 'title'
directors = 'director'
cast = 'cast'
genres = 'genres'
decade = 'decade'

seznam_dict = []

with open(r'python_2\netflix_titles.tsv', mode='r', encoding='utf-8') as netflix_file:
    header = netflix_file.readline().strip().split('\t')

    title_idx = header.index('PRIMARYTITLE')
    directors_idx = header.index('DIRECTOR')
    cast_idx = header.index('CAST')
    genres_idx = header.index('GENRES')
    startyear_idx = header.index('STARTYEAR')

    for row in netflix_file:
        info = row.strip().split('\t')
        info_dict = {
            title: info[title_idx],
            directors: (info[directors_idx]).split(", ") if info[directors_idx] else [],
            cast: (info[cast_idx]).split(", ") if (info[cast_idx]) else [],
            genres: (info[genres_idx]).split(","),
            decade: (info[startyear_idx])[:3] + '0',
        }
        seznam_dict.append(info_dict)

with open(r'python_2\hw02_output.json', mode='w', encoding='utf-8') as jsn_output_file:
    json.dump(seznam_dict, jsn_output_file, ensure_ascii=False, indent=4)
