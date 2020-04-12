// #define ENCODER_DO_NOT_USE_INTERRUPTS
#include <Encoder.h>

Encoder base(10, 11);
Encoder shoulder(6, 7);
Encoder elbow(8, 9);


void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.println("BASE");
  Serial.println(base.read());
  Serial.println("SHOULDER");
  Serial.println(shoulder.read());
  Serial.println("ELBOW");
  Serial.println(elbow.read());
}
