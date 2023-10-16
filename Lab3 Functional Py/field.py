def field(items, *args):
    assert len(args) > 0, 'Empty parameter sweep'
    result = []
    for item in items:
        if len(args)==1:
            result.append(item[arg])
        else:
            line = {}
            for arg in args:
                line[arg] = item [arg]
            result.append(line)
    return result
