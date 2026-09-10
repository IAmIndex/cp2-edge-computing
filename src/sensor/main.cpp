#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Galaxy_A55_5G";
const char* password = "12345678";

const char* mqtt_server = "test.mosquitto.org";
const int mqtt_port = 1883;

const char* mqtt_topic = "vibe_e_codas";

WiFiClient espClient;
PubSubClient client(espClient);

int valorSensor = 0;

void conectarWiFi() {

  Serial.print("Conectando ao WiFi");

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi conectado!");

  Serial.print("IP do ESP32: ");
  Serial.println(WiFi.localIP());
}

void conectarMQTT() {

  while (!client.connected()) {

    Serial.print("Conectando ao MQTT...");

    if (client.connect("ESP32_Client")) {

      Serial.println(" conectado!");

    } else {

      Serial.print(" erro = ");
      Serial.println(client.state());

      delay(2000);
    }
  }
}

void setup() {

  Serial.begin(115200);

  conectarWiFi();

  client.setServer(mqtt_server, mqtt_port);

  randomSeed(42);
}

void loop() {

  if (!client.connected()) {
    conectarMQTT();
  }

  client.loop();

  valorSensor = random(0, 101);

  char mensagem[10];
  sprintf(mensagem, "%d", valorSensor);

  client.publish(mqtt_topic, mensagem);

  Serial.print("Valor do sensor enviado: ");
  Serial.println(valorSensor);

  delay(5000);
}
