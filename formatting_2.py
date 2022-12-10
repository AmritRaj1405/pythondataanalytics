movies=['dhol','bhaubali','jab tak hai jaan','pk']
stars=['❤❤❤❤❤','❤❤❤❤❤','❤❤❤','❤❤❤❤']
for movie,star in zip(movies,stars):
    print(f'{movie.ljust(16)} | {star}')
