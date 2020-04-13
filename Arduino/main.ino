// #define ENCODER_DO_NOT_USE_INTERRUPTS
#include <Encoder.h>
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library for ST7735

#define TFT_CS        10
#define TFT_RST        9 // Or set to -1 and connect to Arduino RESET pin
#define TFT_DC         8

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

Encoder base(4, 5);
Encoder shoulder(6, 7);
Encoder elbow(2, 3
);


void setup() {
  Serial.begin(9600);
  tft.initR(INITR_144GREENTAB);
}

void loop() {
  Serial.println("BASE");
  Serial.println(base.read());
  Serial.println("SHOULDER");
  Serial.println(shoulder.read());
  Serial.println("ELBOW");
  Serial.println(elbow.read());
  tft.fillScreen(ST77XX_GREEN);
}
