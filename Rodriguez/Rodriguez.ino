
#include <TimerOne.h>

#define BASE_OUT_PIN 9
#define COLLECTOR_OUT_PIN 10
#define SWITCHF 10000 //Generate PWM at 10kHz.  
//Minimum pulse width is about 130 microseconds, so higher frequencies lose duty cycle steps at the low end.
//At 10kHz, pulse widths 0 and 1 generate no pulse, above 2 generates a pulse.

//trying for 4 extra bits from the ADC (equivalent of 14 bits instead of 10.) 
//Oversample by 4^n to get n extra bits.  4^4=256
#define OVERSAMPLING 256


float fperiod=(1/((float)SWITCHF))*1000000;
unsigned long period=(int)fperiod;
String message_buffer;
unsigned long dutycycle=1; //Start at zero volts output



void setup() {
  Serial.begin(1000000);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  pinMode(BASE_OUT_PIN, OUTPUT);
  Timer1.initialize(period);
  Timer1.pwm(BASE_OUT_PIN,dutycycle);
  Timer1.pwm(COLLECTOR_OUT_PIN,dutycycle);
}

void loop() {
  if (Serial.available() > 0){
    int numChar = Serial.available();
    byte received_byte=0;
    while (numChar--){
      received_byte=Serial.read();

       //discard line feeds
      if (received_byte==10){
        continue;
      }
      //Set Base output on "B" (66)
      if (received_byte==66){
        handle_message(BASE_OUT_PIN);
        makeMeasurementsAndSendMessage();
        continue;
      }
      //Set Collector output on "C" (67)
      if (received_byte==67){
        handle_message(COLLECTOR_OUT_PIN);
        makeMeasurementsAndSendMessage();
        continue;
      }
     
      if (received_byte!=10 && received_byte!=13 &&isDigit(received_byte)) {
          message_buffer=message_buffer + char(received_byte);
          continue;
      }       
    }
  }
}

void handle_message(int pin){
  if (message_buffer==""){
    return;
  }
  dutycycle=message_buffer.toInt();

  message_buffer="";
  if (dutycycle<0){
    dutycycle=0;
  }
  if (dutycycle>1023){
    dutycycle=1023;
  }

  Timer1.pwm(pin,dutycycle); //,period);
}

void makeMeasurementsAndSendMessage(){
    long counter = OVERSAMPLING;
    unsigned long VBias = 0;
    unsigned long VBase = 0;
    unsigned long VCollector = 0;
    unsigned long VCollectorBias = 0;
    
    while (counter--){
      VBias = VBias + analogRead(A0);
      VBase = VBase + analogRead(A1);
      VCollector = VCollector + analogRead(A2);
      VCollectorBias = VCollectorBias + analogRead(A3);
    }
    Serial.println(String(VBias) + "\t" + String(VBase) + "\t" + String(VCollector) + "\t" + String(VCollectorBias));    
}
