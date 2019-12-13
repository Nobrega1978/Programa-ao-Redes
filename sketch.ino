#include <dht.h>
#include <string.h>
dht DHT;
int pin_gas = A0;

void setup() {
     Serial.begin(9600);
     DHT.read11(4);
     pinMode(pin_gas, INPUT);
}

void loop() {
  DHT.read11(4);
  int gas = analogRead(pin_gas);
  int gas_p = gas / 10;
  int umidade = DHT.humidity;
  int temperatura = DHT.temperature;
  
  String gas2 = String(gas_p);
  String umidade2 = String(umidade);
  String temperatura2 = String(temperatura);
  
   Serial.print("A");
   if (umidade == 100)
         Serial.print(int(99));
         delay(10);
   if (umidade2.length() == 1 ){
         Serial.print("0");
         Serial.print(umidade);
         delay(10);
   }
   else
         Serial.print(int(DHT.humidity));
         delay(10);

   if (temperatura2.length() == 1 ){
         Serial.print("0");
         Serial.print(temperatura);
         delay(10);
   }
   else
         Serial.print(temperatura);
         delay(10);

    if (gas_p == 100)
         Serial.print(int(99));
         delay(10);
    if (gas2.length() == 1 ){
         Serial.print(int(0));
         Serial.print(gas_p);
         delay(10);
    } 
    else
         Serial.print(gas_p);
         delay(10); 
}
