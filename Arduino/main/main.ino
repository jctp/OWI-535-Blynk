// #define ENCODER_DO_NOT_USE_INTERRUPTS
#include <Encoder.h>
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library for ST7735

#define TFT_CS        10
#define TFT_RST        9
#define TFT_DC         8

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);


Encoder base(4, 5);
Encoder shoulder(6, 7);
Encoder elbow(2, 3
);

void drawEyes(){

  // Left Eye
  tft.fillCircle(32, 64, 24, ST7735_WHITE);
  tft.fillCircle(32, 64, 16, ST7735_BLUE);
  tft.fillCircle(32, 64, 8, ST7735_BLACK);
  tft.fillCircle(28, 60, 4, ST7735_WHITE);
  tft.fillCircle(32, 100, 24, ST7735_BLACK);

  // Right Eye
  tft.fillCircle(96, 64, 24, ST7735_WHITE);
  tft.fillCircle(96, 64, 16, ST7735_BLUE);
  tft.fillCircle(96, 64, 8, ST7735_BLACK);
  tft.fillCircle(92, 60, 4, ST7735_WHITE);
  tft.fillCircle(96, 100, 24, ST7735_BLACK);

}

void drawBlink(){
  tft.fillRect(8, 40, 113, 48, ST7735_BLACK);
  tft.fillRect(8, 60, 49, 8, ST7735_WHITE);
  tft.fillRect(72, 60, 49, 8, ST7735_WHITE);
}

void drawMouth() {
  tft.fillCircle(64, 96, 10, ST7735_WHITE);
  tft.fillRect(54, 86, 21, 10, ST7735_BLACK);
}

void setup() {
  Serial.begin(9600);
  tft.initR(INITR_144GREENTAB);
  tft.fillScreen(ST7735_BLACK);
  // tft.println("Serial link up");
  drawEyes();
  drawMouth();

}

void loop() {

  // int blinkCounter = 0;

  while(true) {
    Serial.println("BASE");
    Serial.println(base.read());
 
    Serial.println("SHOULDER");
    Serial.println(shoulder.read());

    Serial.println("ELBOW");
    Serial.println(elbow.read());
 
    /*
    blinkCounter++;

    if (blinkCounter >= random(50, 100)) {
      blinkCounter = 0;
      drawBlink();
      delay(50);
      drawEyes();

    */
  }
}
