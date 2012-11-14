from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.lista = []
        self.lista_temp = []
        self.in_td = False

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_td = True
        else:
            self.in_td = False

    def handle_endtag(self, tag):
        if tag == 'tr':
             self.lista.append(self.lista_temp)
             self.lista_temp = []

    def handle_data(self, data):
        if self.in_td and data <> '\r\r\n':
            self.lista_temp.append(data)

if __name__ == '__main__':
    f = open('D_LOTFAC.HTM', 'r')
    lista_para_ordenar = []
    lista = []
    resultados = f.read()
    parser = MyHTMLParser()
    parser.feed(resultados)
    meus_numeros = [
        ['01', '03', '04', '05', '08', '09', '10', '14', '15', '17', '18', '19', '20', '22', '23'],
        ['03', '04', '06', '07', '08', '09', '10', '11', '12', '14', '16', '17', '18', '19', '23'],
        ['01', '03', '04', '05', '06', '07', '08', '09', '12', '13', '19', '20', '22', '24', '25'],
    ]
    for item in parser.lista:
        s = item[2:17]
        s.sort()
        for numeros in meus_numeros:
            resultado = [i for i, j in zip(s, numeros) if i == j]
            if len(resultado) >= 15:
                print('Ganhei com 15 pontos em %s o premio R$ %s' % (item[1], item[23]))
            elif len(resultado) == 14:
                print('Ganhei com 14 pontos em %s o premio R$ %s' % (item[1], item[24]))
            elif len(resultado) == 13:
                print('Ganhei com 13 pontos em %s o premio R$ %s' % (item[1], item[25]))
            elif len(resultado) == 12:
                print('Ganhei com 12 pontos em %s o premio R$ %s' % (item[1], item[26]))
            elif len(resultado) == 11:
                print('Ganhei com 11 pontos em %s o premio R$ %s' % (item[1], item[24]))
