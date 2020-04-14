// #define ENCODER_DO_NOT_USE_INTERRUPTS
#include <Encoder.h>
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library for ST7735

#define TFT_CS        10
#define TFT_RST        9
#define TFT_DC         8

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

int timer1_counter;
int eyeHeight = 0;

Encoder base(4, 5);
Encoder shoulder(6, 7);
Encoder elbow(2, 3
);



void drawEyes(int hOffset, int vOffset){

  // Left Eye
  tft.fillCircle(32, 64, 24, ST7735_WHITE);
  tft.fillCircle((32 + hOffset), (64 + vOffset), 16, ST7735_BLUE);
  tft.fillCircle((32 + hOffset), (64 + vOffset), 8, ST7735_BLACK);
  tft.fillCircle((28 + hOffset), (60 + vOffset), 4, ST7735_WHITE);
  // tft.fillCircle(32, 100, 24, ST7735_BLACK);

  // Right Eye
  tft.fillCircle(96, 64, 24, ST7735_WHITE);
  tft.fillCircle((96 + hOffset), (64 + vOffset), 16, ST7735_BLUE);
  tft.fillCircle((96 + hOffset), (64 + vOffset), 8, ST7735_BLACK);
  tft.fillCircle((92 + hOffset), (60 + vOffset), 4, ST7735_WHITE);
  // tft.fillCircle(96, 100, 24, ST7735_BLACK);

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
  drawEyes(0, 0);
  drawMouth();

  noInterrupts();
  TCCR1A = 0;
  TCCR1B = 0;
  timer1_counter = 60000;

  TCNT1 = timer1_counter;
  TCCR1B |= (1 << CS12);
  TIMSK1 |= (1 << TOIE1);
  interrupts();
}

ISR(TIMER1_OVF_vect) {
  TCNT1 = timer1_counter;
  Serial.println("BASE");
  Serial.println(base.read());
 
  Serial.println("SHOULDER");
  Serial.println(shoulder.read());

  Serial.println("ELBOW");
  Serial.println(elbow.read());
}

void loop() {
  
  /*
  while (eyeHeight < 6) {
    drawEyes(0,eyeHeight);
    eyeHeight++;
    delay(20);
  }

  while (eyeHeight > -6) {
    drawEyes(0,eyeHeight);
    eyeHeight--;
    delay(20);
  }
  */
}
