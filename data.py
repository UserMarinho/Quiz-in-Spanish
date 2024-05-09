import pandas as pd

questions = [
    ['Con unos zapatos grandes y la cara muy pintada, soy el que hace reír a toda la chiquillada.', 'Futbolista', 'Payaso', 'Panadero', 'Cocinero', 2],
    ['Preparo ricos manjares, mi lugar es la cocina de restaurantes y hoteles. Veamos quién me adivina.', 'Camarero', 'Panadero', 'Cocinero', 'Enfermero', 3],
    ['Riega contento el jardín, amapolas y un jazmín. Cuida la flor con esmero, ¿a quién espero?', 'jardinero', 'Carpintero', 'Electricista', 'Contador', 1],
    ['Recojo frutos sin siembra y mi tractor viene y va, allí por donde trabajo, nadie puede caminar.', 'Arquitecto', 'Pescador', 'Maquinista', 'Agricultor', 4],
    ['Sobre lienzos o en papel, ¡qué bien emplea el color con lápices o pincel!', 'Carpintero', 'Pintor', 'Arquitecto', 'Médico', 2],
    ['Trabajo en el hospital, pero soy médico no soy. Si no lo adivinas, un pinchazo te doy.', 'Recepcionista', 'Farmacêutico', 'Enfermero', 'Terapeuta', 3],
    ['Conduzco por la ciudad, en mi coche te llevo a cualquier lugar, pero después me tendrás que pagar.', 'Bombero', 'Taxista', 'Profesor', 'Panadero', 2],
    ['Tengo chistera y una varita. Si me lo propongo puedo hacer aparecer cositas.', 'Cocinero', 'Bibliotecario', 'Mago', 'Mecánico', 3],
    ['Con madera de pino, de haya o de nogal, construyo los muebles para tu hogar.', 'Masón', 'Dentista', 'Carpintero', 'Jardinero', 3],
    ['Si vas al supermercado, yo te atenderé, pasando por caja te diré lo que te cobraré.', 'Cajero', 'Panadero', 'Mecánico', 'Cocinero', 1],
    ['Con cariño y mucho amor, en el cole te espero, con juegos y actividades con los que aprenderemos.', 'Cajero', 'Actor', 'Profesor', 'Deportivo', 3],
    ['Con mi pluma yo escribo, miles de libros y cuentos, para que tú los disfrutes. ¡Qué gran invento!', 'Jardinero', 'Profesor', 'Músico', 'Escritor', 4],
    ['Trabajo bajo tierra, pico y pala todo el día. Mi segunda casa es la mina. ¿Adivinas?', 'Músico', 'Minero', 'Arquitecto', 'Jardinero', 2],
    ['En los bares estoy y no soy el cocinero. Ayudo a servir las mesas y lo hago con esmero', 'Dj', 'Abogado', 'Camarero', 'Bailarín', 3],
    ['Sumergido entre las aguas, me gusta trabajar. Con mi bombona de oxígeno me encontrarás.', 'Profesor', 'Buzo', 'Electricist', 'Jardinero', 2],
    ['En televisión trabajo, me gusta comunicar, presento programas, ¿me conoces ya?', 'Médico', 'Carpintero', 'Músico', 'Presentador', 4],
    ['Si tienes una tubería atascada o un grifo roto, me tendrás que llamar, a tu casa iré corriendo para poderlo arreglar.', 'Plomero', 'Médico', 'Buzo', 'Camarero', 1],
    ['A las olimpiadas yo iré y con esfuerzo y mucho trabajo una medalla ganaré.', 'Actor', 'Abogado', 'Deportista', 'Músico', 3],
    ['El pelo arreglo en mi bonito local, si vienes a visitarme te dejaré genial.', 'Deportista', 'Actor', 'Profesor', 'Peluquero', 4]
]

#pandas dataframe creation
df = pd.DataFrame(questions, columns=['image', 'option 1', 'option 2', 'option 3', 'option 4', 'answer'])
#saving dataframe
df.to_excel('questions.xlsx', index=False)
print('questions ok')
