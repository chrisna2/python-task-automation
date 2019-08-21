import pickle

favorite_colors = ['red','blue','white','black']

with open('colors.pickle','wb') as file:
    pickle.dump(favorite_colors, file)

print('save to pickle')