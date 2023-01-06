#include <esp32cam.h>
#include <WebServer.h>
#include <WiFi.h>

static const char* WIFI_SSID = "NETGEAR46";
static const char* WIFI_PASS = "hungrysheep502";

WebServer server(80);

static auto lowRes = esp32cam::Resolution::find(320,240);
static auto highRes = esp32cam::Resolution::find(800,600);

void serverJPG()
{
  auto frame = esp32cam::capture();
  if (frame==nullptr){
    Serial.println("Fallo captura");
    server.send(503,"","");
    return;
  }
  Serial.printf("Captura OK %dx%d %db\n",frame->getWidth(),frame->getHeight(),static_cast<int>(frame->size()));

  server.setContentLength(frame->size());
  server.send(200,"image/jpeg");
  WiFiClient client = server.client();
  frame->writeTo(client);
}

void jpglow()
{
  if(!esp32cam::Camera.changeResolution(lowRes)){
    Serial.println("Resolucion baja");
  }
  serverJPG();
}

void jpghigh()
{
  if(!esp32cam::Camera.changeResolution(highRes)){
    Serial.println("Resolucion alta");
  }
  serverJPG();
}

void setup() {
  Serial.begin(115200);
  Serial.println();

  {
    using namespace esp32cam;
    Config cfg; 
    cfg.setPins(pins::AiThinker);
    cfg.setResolution(highRes);
    cfg.setBufferCount(2);
    cfg.setJpeg(80);

    bool ok=Camera.begin(cfg);
    Serial.println(ok ? "!Camara lista! \n Usa las siguientes direcciones: " : "Fallo de camara");
  }

  WiFi.persistent(false);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID,WIFI_PASS);
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
  }

  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/cam-low.jpg");

  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/cam-high.jpg");

  server.on("/cam-low.jpg",jpglow);
  server.on("/cam-high.jpg",jpghigh);

  server.begin();
}

void loop() {
  server.handleClient();
}
