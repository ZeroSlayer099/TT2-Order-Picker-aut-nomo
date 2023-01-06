from operator import itemgetter, attrgetter

def rutas(listaprod):
    
    Lista_pedidos = listaprod

    lista_final=sorted(Lista_pedidos, key=itemgetter(2,3,4))
    print(lista_final)

    def multisort(xs, specs):
         for key, reverse in reversed(specs):
             xs.sort(key=itemgetter(key), reverse=reverse)
         return xs

    print(multisort(list(lista_final), ((0, False), (1, False))))

# def multisort(xs, specs):
# 	for key, reverse in reversed(specs):
# 		lfff=sorted(list(xs),key=itemgetter(key), reverse=reverse)
# 		print(lfff)
# 	return xs
	
# multisort(list(Lista_pedidos), ((2, True), (0, False)))