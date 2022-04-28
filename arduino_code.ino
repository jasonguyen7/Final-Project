void setup(){
 pinMode(2, INPUT); 
 pinMode(3, INPUT);

 Serial.begin(9600);        
}

void loop(){
    if (digitalRead(2) == HIGH) {
      Serial.println("d");
    }

    else {
      Serial.println("!d");
    }

    if (digitalRead(3) == HIGH) {
      Serial.println("a");
    }

    else {
      Serial.println("!a");
    }
    delay(50);
}
