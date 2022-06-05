def parseData(filename: str) -> (list, list):
    with open(filename, encoding='utf-8') as f:
        data = f.read()

    data = data.split('\n')

    data = list(map(lambda x: x.split(), data))

    time_mjd = []
    time_value = []
    data.pop()  # remove last /n
    for i in data:
        time_mjd.append(i[1])
        time_value.append(i[2])

    time_mjd = list(map(float, time_mjd))
    time_value = list(map(float, time_value))


    if len(time_mjd) != len(time_value):
        raise Exception('len of time is not equal to len of data')

    return time_mjd, time_value
