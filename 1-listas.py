'''
joaquim coleciona filmes no computador, mas quer gravar alguns em cd,
precisar organizar sua lista por ordem alfabetica e gravar os cinco 
primeiros. (mae, vida, nos, eli, vidro, resgate, close, o poço, fragmentado, parasita).
'''

filmes = ["mae", "vida", "nos", "eli", "vidro", "resgate", "close", "o poço", "fragmentado", "parasita"]
ordem = sorted(filmes)

print("os cinco primeiros foram: ")

i = 0
while i <= 4 :
    print(ordem[i])
    i += 1