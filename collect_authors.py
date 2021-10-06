import re

# Collects the authors from the individual sections' tex file.
# Take the union and order by last name and output it to `authors.tex`.

all_names = set()
exclude_names = ['Rishi Bommasani', 'Percy Liang']

def process_section(path):
    names = None
    for line in open(path):
        m = re.search('sectionauthors{(.+)}', line)
        if m:
            names = [name.replace('*', '') for name in m.group(1).split(', ')]
            for name in names:
                if name not in exclude_names:
                    all_names.add(name)
            break
    print(f'{path}: {names}')

for line in open('sections.txt'):
    process_section(line.strip() + '.tex')

def with_last_name_first(name):
    tokens = name.split(' ')

    # Add your last name if it consists of multiple words
    multi_words_last_names = ['Arad Hudson', 'A. Hudson']
    lasts = " ".join(tokens[1:])
    if lasts in multi_words_last_names:
        out = [lasts, tokens[0]]
    else:
        out = [tokens[-1]] + tokens[:-1]
    return out

with open('authors.tex', 'w') as out:
    print('% WARNING: this is an automatically generated file - do not edit!', file=out)
    author_list = [exclude_names[0] + '*'] + \
        sorted(all_names, key=with_last_name_first) + \
        [exclude_names[1] + '*']
    for name in author_list:
        extra = '\\footnote{Corresponding author: pliang@cs.stanford.edu \hfill *Equal contribution.}' if name == 'Percy Liang*' else ''
        print('\\author{\\mbox{' + name + '}' + extra + '}', file=out)
