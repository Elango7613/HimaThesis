import pandas as pd

def loadData():
    filenames = []
    COLUMNS = ['Filenames', 'desert', 'mountains', 'sea', 'sunset', 'trees']
    PATH = "C:/Users/elang/Desktop/DBS/DataProject-Temp/Pavi-Python/results.csv"
    df_result = pd.read_csv(PATH,
                           skipinitialspace=True,
                            header=None,
                           names=COLUMNS,
                           index_col=False)
    for index, row in df_result.iterrows():
        if index == 0:
            print('Header')
        else:
            filenames.append(row['Filenames'])
    return filenames

def getImageData(imgID):
    return_text = ''
    COLUMNS = ['Filenames', 'desert', 'mountains', 'sea', 'sunset', 'trees']
    PATH = "C:/Users/elang/Desktop/DBS/DataProject-Temp/Pavi-Python/results.csv"
    df_result = pd.read_csv(PATH,
                           skipinitialspace=True,
                            header=None,
                           names=COLUMNS,
                           index_col=False)
    filteredrow = df_result[(df_result['Filenames'] == imgID)]
    print(filteredrow)
    if (filteredrow['desert'] == '1').bool():
        return_text += "#Desert"
    if (filteredrow['mountains'] == '1').bool():
        return_text += "#Mountains"
    if (filteredrow['sea'] == '1').bool():
        return_text += "#Sea"
    if (filteredrow['sunset'] == '1').bool():
        return_text += "#Sunset"
    if (filteredrow['trees'] == '1').bool():
        return_text += "#Trees"
    print(return_text)
    return return_text