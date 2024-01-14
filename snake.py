import turtle
import time
import random

#Velocidad
velocidad = 0.1

#Marcador
score = 0
high_score = 0

#Tiempo
seg = 0
start = time.time()
tiempo_anterior = start


#Interfaz de la ventana gráfica
wn = turtle.Screen()
wn.title("Juego snake")
wn.bgcolor("#7620EF")
wn.setup(width = 800, height = 800)
wn.tracer(0)

#Borde o límites jugables
borde = turtle.Turtle()
borde.goto(-300,300)
borde.color("green")
borde.begin_fill()
for i in range(0,4):    
    borde.forward(600)
    borde.right(90)
borde.end_fill()
borde.color("black")
borde.width(3)
for i in range(0,4):    
    borde.forward(600)
    borde.right(90)
borde.hideturtle()

#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo de la serpiente (segmentos)
cuerpo = []

#Texto marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,-360)
texto.write("Score : 0      High Score: 0", align = "center", font =("Courier", 24, "normal"))

#Texto controles
texto_controles = turtle.Turtle()
texto_controles.speed(0)
texto_controles.color("black")
texto_controles.penup()
texto_controles.hideturtle()
texto_controles.goto(0,320)
texto_controles.write("Mover: ↑ ↓ → ← \nSalir: Esc", align = "left", font =("Courier", 24, "normal"))

#Texto tiempo
texto_tiempo = turtle.Turtle()
texto_tiempo.speed(0)
texto_tiempo.color("black")
texto_tiempo.penup()
texto_tiempo.hideturtle()
texto_tiempo.goto(-60,320)
texto_tiempo.write("Tiempo: {}s".format(seg), align = "right", font =("Courier", 24, "normal"))

#Texto pausa
texto_pausa = turtle.Turtle()
texto_pausa.speed(0)
texto_pausa.color("white")
texto_pausa.penup()
texto_pausa.hideturtle()
texto_pausa.goto(0,0)
#texto_pausa.write("Pausa: ", align = "center", font =("Courier", 24, "normal"))

#FUNCIONES

#Salir del juego
def salir():
    wn.bye()

#Pausar el juego
juego_en_pausa = False
def pausa():
    global juego_en_pausa
    juego_en_pausa = not juego_en_pausa
    if juego_en_pausa == True:
        x = texto_pausa.xcor()
        y = texto_pausa.ycor()
        texto_pausa.setx(-280)
        texto_pausa.sety(280)
        texto_pausa.goto(x,y)
    else:
        x = texto_pausa.xcor()
        y = texto_pausa.ycor()
        texto_pausa.setx(800)
        texto_pausa.sety(800)
        texto_pausa.goto(x,y)
    

#Actualizar tiempo
def tiempo():
    global tiempo_actual
    global tiempo_anterior
    global seg
    
    # Calcular la diferencia de tiempo
    tiempo_actual = time.time()
    diferencia_tiempo = tiempo_actual - tiempo_anterior

    # Actualizar el tiempo en pantalla
    if diferencia_tiempo >= 1:
        seg += int(diferencia_tiempo)
        texto_tiempo.clear()
        texto_tiempo.write("Tiempo: {}s".format(seg), align="right", font=("Courier", 24, "normal"))
        tiempo_anterior = tiempo_actual

#Resetear el tiempo
def tiempo_reset():
    global tiempo_actual
    global tiempo_anterior
    global seg
    seg = 0

#Resetear marcador
def reset():
    global score  
    score = 0
    texto.clear()
    texto.color("black")
    texto.write("Score: {}      High_score: {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))

# Direcciones
def up():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def down():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def left():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def right():
    if cabeza.direction != "left":
        cabeza.direction = "right"

#Movimiento
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
    
#Teclado (teclas direccionales)
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(salir, "Escape")
wn.onkeypress(pausa, "space")

if not juego_en_pausa:
    #Bucle para que funcione el juego
    while True:
        #Actualizamos constantemente la pantala
        wn.update()

        #Actualizar el tiempo
        tiempo()

        #Colisiones con los bordes (si sale por uno, entra por el opuesto)
        if cabeza.xcor() > 280:
            y = cabeza.ycor()
            cabeza.goto(-280,y)
        if cabeza.xcor() < -280:
            y = cabeza.ycor()
            cabeza.goto(280,y)
        if cabeza.ycor() > 280:
            x = cabeza.xcor()
            cabeza.goto(x,-280)
        if cabeza.ycor() < -280:
            x = cabeza.xcor()
            cabeza.goto(x,280)

        #Pausar el juego
        if juego_en_pausa:
            time.sleep(0.1)  # Añadir un pequeño retraso para no consumir recursos en exceso
            continue
            

        #Cuando la serpiente come
        if cabeza.distance(comida) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            comida.goto(x, y)

            #Aumnetamos el cuerpo
            nuevo_cuerpo = turtle.Turtle()
            nuevo_cuerpo.speed(0)
            nuevo_cuerpo.shape("square")
            nuevo_cuerpo.color("grey")
            nuevo_cuerpo.penup()
            cuerpo.append(nuevo_cuerpo)

            #Actualizamos el marcador
            score += 10
            if score > high_score:
                high_score = score

                if score >= 0:
                    texto.color("purple")
                if score >= 1:
                    texto.color("red")
                if score >= 100:
                    texto.color("brown")
                if score >= 200:
                    texto.color("gray")
                if score >= 300:
                    texto.color("yellow")
            
            #Mostramos las variables del marcador
            texto.clear()
            texto.write("Score : {}      High Score: {}".format(score,high_score), align = "center", font =("Courier", 24, "normal"))

        #Movimiento del cuerpo
        totalCuerpo = len(cuerpo)
        for index in range(totalCuerpo - 1, 0, -1):
            x = cuerpo[index -1].xcor()
            y = cuerpo[index -1].ycor()
            cuerpo[index].goto(x, y)
        
        if totalCuerpo > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            cuerpo[0].goto(x, y)

        #Movimiento
        mov()

        #Colisión con el cuerpo
        for parte in cuerpo:
            if parte.distance(cabeza) < 20:
                time.sleep(1)
                cabeza.goto(0,0)
                cabeza.direction = "stop"

                #borrar cuerpo
                for parte in cuerpo:
                    parte.hideturtle()
                
                #limpiar cuerpo
                cuerpo.clear()

                #Resetear el marcador
                reset()

                #Resetear el tiempo
                tiempo_reset()
        
        time.sleep(velocidad)

    #Para que se quede abierta la pantalla
    wn.mainloop()