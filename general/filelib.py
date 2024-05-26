from datetime import datetime
from constants import ERRORS_FILE, BUFFER_FILE, CSV_FILE

def show_labels(filename:str)->list:
    with open(filename, 'r', encoding='utf-8-sig') as file:
        return file.readline().strip().split(";")

def show_table() -> str:
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as file:
        string = ""
        data = file.readlines()[1::]
        for line in data:
            for word in line.strip().split(";"):
               string += word + " "
            string += '\n'
    return string


def buffer_enable():
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as file:
        var = file.readlines()
        with open(BUFFER_FILE, 'w', encoding='utf-8-sig') as buffer:
            for line in var:
                buffer.write(line)

def save():
    with open(BUFFER_FILE, 'r', encoding='utf-8-sig') as file:
        var = file.readlines()
        with open(CSV_FILE, 'w', encoding='utf-8-sig') as buffer:
            for line in var:
                buffer.write(line)

def send_error_log(error_message:str)->None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERRORS_FILE, 'a', encoding="utf-8") as file:
        file.write(error_message + " " + now + '\n')

def read_csv_column(filename:str, column_name:str, start=0, end=1000):
    """Показывает весь столбец"""
    founded = False
    column_index = 0
    result_column = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        line = str(file.readline().strip()).split(';')
        for label in line:
            if label == column_name:
                founded = True
                break
            column_index += 1
        if founded:
            i = 0
            while (i < start):
                file.readline()
                i += 1
            for line in file:
                if i > end:
                    break
                i += 1
                ln = line.strip().split(';')
                if len(ln) >= column_index:
                    result_column.append(ln[column_index])
                else:
                    result_column.append(None)
        else:
            result_column.append(None)
    return result_column

def delete_line(filename:str, linenum:int)->bool:
    max = csv_lines_len(filename)
    if max-1 < linenum:
        send_error_log("Invalid line number ")
        return False
    with open(filename, 'r') as fr:
        lines = fr.readlines()
        ptr = 0
        with open(filename, 'w') as fw:
            for line in lines:
                if ptr != linenum:
                    fw.write(line)
                ptr += 1
    return True

def in_csv_column(filename:str, column_name:str, data:str)->bool:
    """Показывает весь столбец"""
    founded = False
    column_index = 0
    with open(filename, 'r', encoding='utf-8-sig') as file:
        line = str(file.readline().strip()).split(';')
        for label in line:
            if label == column_name:
                founded = True
                break
            column_index += 1
        if founded:
            for line in file:
                ln = line.strip().split(';')
                if len(ln) >= column_index:
                    if ln[column_index] == data:
                        return True
    return False


def write_csv_line(filename:str, line:list)->None:
    try:
        if csv_columns_len(filename) != len(line):
            raise "Len Error"
        with open(filename, 'a', encoding='utf-8') as file:
            string = ""
            for item in line:
              string += item + ";"
            file.write("\n"+string[0:-1])
    except:
        send_error_log("Error adding into csv file")
        return None

#TODO: Разбить на 2 функции: саму сортировку и перевод в из csv в list
def sort_by_label(filename:str, sorting_label:str)->list:
    with open(filename, 'r', encoding='utf-8-sig') as file:
        #data = [string.strip().split() for string in string1.strip().split() for string1 in file.readlines()]
        data = list()
        for lines in file.readlines():
            data.append(lines.strip().split())
        data = data[1::]
        for i in range(len(data)):
            data[i] = data[i][0].strip().split(";")
        labels = show_labels(filename)
        for i,label in enumerate(labels):
            if label == sorting_label:
                break
        else:
            send_error_log("Label not found")
            return list()
        data = sorted(data, key=lambda x: x[0][i])
        return data

def csv_columns_len(filename:str)->int:
    with open(filename, 'r', encoding='utf-8-sig') as file:
        line = str(file.readline().strip()).split(';')
        return len(line)

def csv_lines_len(filename:str)->int:
    """Длина с учётом заголовочных файлов"""
    i = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for _ in file:
            i += 1
    return i
