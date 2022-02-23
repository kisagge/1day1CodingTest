def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for e in new_id:
        if not (e.isalpha() or e.isdecimal() or e in ['-', '_', '.']):
            new_id = new_id.replace(e, "")
            continue
    for i in range(5):
        new_id = new_id.replace("...", ".")
        new_id = new_id.replace('..', '.')
        
    if new_id[0] == '.':
          new_id = new_id[1:]
            
    if len(new_id) >= 1:
        if new_id[-1] == '.':
            new_id = new_id[:len(new_id)-1]

    if new_id == '':
        new_id += 'a'

    if len(new_id) >= 16:
            new_id = new_id[:15]
            if new_id[-1] == '.':
                new_id = new_id[:len(new_id)-1]

    while len(new_id) <= 2:
        new_id += new_id[len(new_id)-1]
    answer += new_id
    return answer