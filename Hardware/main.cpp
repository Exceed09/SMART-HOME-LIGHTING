#include <Arduino.h>
#include <Bounce2.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include "Connect_Wifi.h"

#define builtin 5
#define red 26
#define yellow 25
#define green 33
#define button 27
#define switch_room1 2
#define switch_room2 15
#define switch_room3 13
#define ldr 32

void Connect_Wifi();

// void GET_data(void *param);
void manual_input(void *param);

void room1(void *param);
void room2(void *param);
void room3(void *param);

TaskHandle_t TaskA = NULL;
TaskHandle_t TaskB = NULL;
TaskHandle_t TaskC = NULL;
TaskHandle_t TaskD = NULL;
TaskHandle_t TaskE = NULL;

Bounce debouncer = Bounce();
bool disco_mode = false;

//room1(red), room2(yellow), room3(green)
bool modeauto_room[3] = {true, false, false}; 
int brightness_room[3] = {255, 255, 0};
bool onstatus_room[3] = {false, false, false};
bool change_room[3] = {false, false, false};

//touch sensor
const int threshold = 20;
int touch_value_room1, touch_value_room2, touch_value_room3;
int ready_room1 = 1, ready_room2 = 1, ready_room3 = 1;

String url = "http://ecourse.cpe.ku.ac.th/exceed09/rooms";

void setup() {
  Serial.begin(115200);

  Connect_Wifi();

  ledcSetup(0, 5000, 8);
  ledcSetup(1, 5000, 8);
  ledcSetup(2, 5000, 8);
  ledcSetup(3, 5000, 8);
  ledcAttachPin(builtin, 0);
  ledcAttachPin(red, 1);
  ledcAttachPin(yellow, 2);
  ledcAttachPin(green, 3);

  pinMode(ldr, INPUT);

  debouncer.attach(button, INPUT_PULLUP);
  debouncer.interval(25);

  // xTaskCreatePinnedToCore(GET_data, "GET_data", 20*1024, NULL, 1, &TaskB, 0);
  xTaskCreatePinnedToCore(manual_input, "manual_input", 10*1024, NULL, 1, &TaskA, 0);

  xTaskCreatePinnedToCore(room1, "room1", 3000, NULL, 1, &TaskC, 1);
  xTaskCreatePinnedToCore(room2, "room2", 3000, NULL, 1, &TaskD, 1);
  xTaskCreatePinnedToCore(room3, "room3", 3000, NULL, 1, &TaskE, 1);
}

void loop() {
  
}

void manual_input(void *param) {
  while (1) {
    debouncer.update();
    if (debouncer.fell()) {
      disco_mode = !disco_mode;
    } else {
      touch_value_room1 = touchRead(switch_room1);
      touch_value_room2 = touchRead(switch_room2);
      touch_value_room3 = touchRead(switch_room3);
      
      if (touch_value_room1 >= threshold) {
        ready_room1 = 1;
      } else if (touch_value_room1 < threshold && ready_room1) {
        if (!modeauto_room[0]) {
          onstatus_room[0] = !onstatus_room[0];
          ready_room1 = 0;
          change_room[0] = true;
        } 
      }

      if (touch_value_room2 >= threshold) {
        ready_room2 = 1;
      } else if (touch_value_room2 < threshold && ready_room2) {
        if (!modeauto_room[1]) {
          onstatus_room[1] = !onstatus_room[1];
          ready_room2 = 0;
          change_room[1] = true;
        } 
      }

      if (touch_value_room3 >= threshold) {
        ready_room3 = 1;
      } else if (touch_value_room3 < threshold && ready_room3) {
        if (!modeauto_room[2]) {
          onstatus_room[2] = !onstatus_room[2];
          ready_room3 = 0;
          change_room[2] = true;
        } 
      }
      vTaskDelay(100/portTICK_PERIOD_MS);
    }
  }
}

// void GET_data(void *param) {
//   while (1) {
//     Serial.println("GET_data");
//     DynamicJsonDocument doc(2048);
//     HTTPClient http;
    
//     http.begin(url);
//     int httpCode = http.GET();
//     Serial.println(httpCode);
//     if (httpCode >= 200 && httpCode < 300) {
//       String payload = http.getString();
//       deserializeJson(doc, payload);
      
//       for (int i = 0; i < 3; i++) {
//         modeauto_room[i] = doc["message"][i]["mode_auto"];
//         brightness_room[i] = doc["message"][i]["brightness"];
//         onstatus_room[i] = doc["message"][i]["on_status"];
//         change_room[i] = doc["message"][i]["is_change"];
//         // Serial.print("------ room_id: ");
//         // Serial.println(doc["message"][i]["room_id"]);
//         // Serial.print("modeauto: ");
//         // Serial.println(modeauto_room[i]);
//         // Serial.print("brightness: ");
//         // Serial.println(brightness_room[i]);
//         // Serial.print("onstatus: ");
//         // Serial.println(onstatus_room[i]);
//         // Serial.print("change: ");
//         // Serial.println(change_room[i]);
//       }
//     } else {
//       Serial.println("Error on HTTP request");
//     }
//     http.end();
//     vTaskDelay(5/portTICK_PERIOD_MS);
//   }
// }

void room1(void *param) {
  while (1) {
    if (disco_mode) continue;
    if (modeauto_room[0]) {
      //auto mode
      if (analogRead(ldr) > 2500) {
        ledcWrite(1, 0);
      } else {
        ledcWrite(1, brightness_room[0]);
      }
      vTaskDelay(5/portTICK_PERIOD_MS);
    } else if (change_room[0]) {
      //manual mode
      if (onstatus_room[0]) {
        ledcWrite(1, brightness_room[0]);
      } else {
        ledcWrite(1, 0);
      }
      change_room[0] = false; 
    }
    vTaskDelay(50/portTICK_PERIOD_MS);
  }   
}

void room2(void *param) {
  while (1) {
    if (disco_mode) continue;
    if (modeauto_room[1]) {
      //auto mode
      if (analogRead(ldr) > 2500) {
        ledcWrite(2, 0);
      } else {
        ledcWrite(2, brightness_room[1]);
      }
      vTaskDelay(5/portTICK_PERIOD_MS);
    } else if (change_room[1]) {
      //manual mode
      if (onstatus_room[1]) {
        ledcWrite(2, brightness_room[1]);
      } else {
        ledcWrite(2, 0);
      }
      change_room[1] = false; 
    }
    vTaskDelay(50/portTICK_PERIOD_MS);
  }   
}

void room3(void *param) {
  while (1) {
    if (disco_mode) continue;
    if (modeauto_room[2]) {
      //auto mode
      if (analogRead(ldr) > 2500) {
        ledcWrite(3, 0);
      } else {
        ledcWrite(3, brightness_room[2]);
      }
      vTaskDelay(5/portTICK_PERIOD_MS);
    } else if (change_room[2]) {
      //manual mode
      if (onstatus_room[2]) {
        ledcWrite(3, brightness_room[2]);
      } else {
        ledcWrite(3, 0);
      }
      change_room[2] = false; 
    }
    vTaskDelay(50/portTICK_PERIOD_MS);
  }   
}

