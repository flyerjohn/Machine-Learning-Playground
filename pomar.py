from sklearn import tree 

lisa = 1
rugosa = 0
maca = 1
laranja = 0

pomar = [[140, lisa], [150, lisa], [130, lisa], [160, rugosa], [170, rugosa], [182, rugosa]]

resultado = [maca, maca, maca, laranja, laranja, laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

peso = input('Entre com o peso: ')
superficie = input('Entre com a superficie: ')


resultadoUsuario= clf.predict([[peso, superficie]])

if resultadoUsuario == 1:
    print('Maca')
else:
    print('laranja')