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
    String c = Serial.readStringUntil('\n');
    Serial.print("deeplearning result : ");
    //Serial.println(c);
    char ch[100] = {0};
    c.toCharArray(ch,c.length()+1);
  //  int index1 = c.indexOf(','); 
  //  int tmp = c.substring(0,index1).toInt();
    Serial.println(ch);
    /*
    char tmps[5];
    c.toCharArray(tmps, c.length());
    int tmp = atoi(tmps);
*/
    rf95.send(ch,sizeof(ch));
    
    Serial.println();
  }