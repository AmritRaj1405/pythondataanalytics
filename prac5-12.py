
movies=['bahubali','jab tak hi jhaan','milkha singh','pk']
stars=['⭐⭐⭐⭐⭐','⭐','⭐⭐⭐⭐⭐','⭐⭐']
#msg1=movies.replace('s',' ')
for movie,star in zip(movies,stars):
    print(f'{movie.ljust(16)} | {star}')
  