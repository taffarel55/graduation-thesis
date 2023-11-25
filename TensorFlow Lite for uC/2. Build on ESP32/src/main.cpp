#include <EloquentTinyML.h>
// sine_model.h contains the array you exported from the previous step
#include "sine_model.cc"

#define NUMBER_OF_INPUTS 1
#define NUMBER_OF_OUTPUTS 1
// in future projects you may need to tweek this value: it's a trial and error process
#define TENSOR_ARENA_SIZE 2*1024
Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> ml;

#define NUMBER_OF_POINTS_INFERING 100

void setup() {
    Serial.begin(115200);
    delay(1000);

    ml.begin(sine_model);
    unsigned long tic, toc, total_latency = 0, latency = 0;
    
    Serial.println("------- DEBUG csv ---------");
    for(int i=0; i<=NUMBER_OF_POINTS_INFERING; i++) {
      float x = 2*PI*i/NUMBER_OF_POINTS_INFERING;
      float y = sin(x);
      float input[1] = { x };
      tic = micros();
        float predicted = ml.predict(input);
      toc = micros();
      total_latency += toc - tic;
      Serial.print(x,8);
      Serial.print(",");
      Serial.println(predicted,8);
    }
    Serial.println("------- END csv ---------");
    latency = total_latency / NUMBER_OF_POINTS_INFERING;

    Serial.println("Latência média da inferência: ");
    Serial.println(latency);
}

void loop() {

}