# codewars https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/solutions/python solution
def html_special_chars(data):
    output = ""
    for i in range(0, len(data)):
        if data[i] == '<':
            output += "&lt;"
        elif data[i] == '>':
            output += "&gt;"
        elif data[i] == '"':
            output += "&quot;"
        elif data[i] == '&':
            output += "&amp;"
        else:
            output += data[i]
    print(output)
    return output

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    html_special_chars('<h2>Hello World</h2>')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
