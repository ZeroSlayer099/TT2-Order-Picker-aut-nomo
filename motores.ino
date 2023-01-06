#include <AFMotor.h>
#include <Servo.h> 

String dato;

Servo myservo;
AF_DCMotor motor1(1); //para motor 1
AF_DCMotor motor2(2); //para motor 2
AF_DCMotor motor3(4); //para motor 3
const int avance=A0;
int valavance;
const int reversa=A1;
int valreversa;
const int derecha=A2;
int valderecha;
const int izquierda=A3;
int valizquierda;
const int abrir=A4;
int valabrir;
const int cerrar=A5;
int valcerrar;

void setup() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  myservo.attach(9); //servo 1
  myservo.attach(10);//servo 2
  Serial.begin(9600);
}

void loop() {
  
  valavance=analogRead(avance);
  valreversa=analogRead(reversa);
  valderecha=analogRead(derecha);
  valizquierda=analogRead(izquierda);
  valabrir=analogRead(abrir);
  valcerrar=analogRead(cerrar); 

  if (Serial.available()>0){
    dato=Serial.readStringUntil('\n');  

      if (dato == "adelante") 
    {
      motor1.setSpeed(180);
      motor2.setSpeed(180);
      motor1.run(FORWARD); //adelante
      motor2.run(FORWARD); //adelante
    }
      else  if (dato == "atras") 
    {
      motor1.setSpeed(180);
      motor2.setSpeed(180);
      motor1.run(BACKWARD); //adelante
      motor2.run(BACKWARD); //adelante
    } 
      else if (dato == "stop")
    {
      motor1.setSpeed(0);
      motor2.setSpeed(0);
    }   

    if (dato == "abrir") 
    {
      motor3.setSpeed(180);
      motor3.run(FORWARD); //adelante
      delay (500);
      motor3.setSpeed(0);
    }
      else  if (dato == "cerrar") 
    {
      motor3.setSpeed(180);
      motor3.run(BACKWARD); //adelante
      delay (500);
      motor3.setSpeed(0);
    } 
      else if (dato == "stop2")
    {
      motor3.setSpeed(0);
    } 

        if (dato == "derecha") 
    {
        myservo.write(20);
    }
      else  if (dato == "izquierda") 
    {
        myservo.write(150);
    } 
      else if (dato == "centro")
    {
        myservo.write(90);
    } 
    delay (100); 
  }
}