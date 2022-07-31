from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capitals.txt') as file:
        for line in file:
            line = line.rstrip('/n')
            country,city = line.split('/')
            the_world[country] = city

def write_to_file(country_name, city_name):
    with open('capitals.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)

print("Ask the expert: Capital cities of the world.")

# start Tkinker and hide empty window
root = Tk()
root.withdraw()
# create a dictionary
the_world = {}

read_from_file()

while True:
    query_country = simpledialog.askstring('Country','Type the name of the country:')
    query_country = query_country.capitalize()

    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer','The capital of ' + query_country + ' is ' + result + '!')
    else:
        new_city = simpledialog.askstring('Teach me','I don\'t know! what is the capital of ' + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

root.mainloop()


