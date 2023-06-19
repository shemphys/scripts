def replace_backslashes(string):
    return string.replace("\\", "/")

# Ejemplo de uso
input_string = r"C:\Users\mykje\Documents\GitHub\counter_TDAH\reminder\recordings\sever_espabila.ogg"
output_string = replace_backslashes(input_string)

print(output_string)
