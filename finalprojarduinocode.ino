
int sensorVal;
int sensorPin = A0;
int sensorValue;

void setup() {
  // put your setup code here, to run once:
  pinMode(sensorPin, INPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop()
{
  sensorValue = analogRead(sensorPin);  // read pin A0   
  Serial.println(sensorValue);         // send data to serial
  delay(20);
}
