import pickle

with open('colors.pickle','rb') as file:
    favorite_colors = pickle.load(file)
    print(type(favorite_colors))
    print(favorite_colors)