#include <SPI.h>
#include <RH_RF95.h>

RH_RF95 rf95;

void setup() 
{   
  Serial.begin(9600);
  while (!Serial) ;
  if (!rf95.init())
    Serial.println("init failed");
}

void loop()
{ 
  if (rf95.available())
  {  
    char buf[255];
    char len = sizeof(buf);

    if (rf95.recv(buf, &len))
    {
 
      Serial.println(buf);
    }
  }
}