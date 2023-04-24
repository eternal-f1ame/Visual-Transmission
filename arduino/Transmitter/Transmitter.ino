#define LED_PIN 3
#define PERIOD 4

const char *string = "REV";
int string_length;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  // int string_length = strlen(string);
}

void loop() {
  string_length = strlen(string);
  for(int i = 0; i < string_length; i++)
  {
    send_byte(string[i]);
  }
  delay(100);
}

void send_byte(char my_byte){
  digitalWrite(LED_PIN, LOW);
  delay(PERIOD);

  uint8_t bin;

  for(int i = 0; i < 8; i++){
    int led_state = bitRead(my_byte, i);
    digitalWrite(LED_PIN, led_state != 0);
    delay(PERIOD);
  }

  digitalWrite(LED_PIN, HIGH);
  delay(PERIOD);
}