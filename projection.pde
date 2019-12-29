import processing.video.*;
Movie background;

String path = "";
String[] lines;
Table table;
String text = "";
String file_name;
PFont myFont;
int fontSize = 17;
//int fontSize = 70;
long current_time;
long starting_time;
long elapsed_time;
int slide_delay = 4290;
int row_number = 0;
String date = "";
ArrayList<Mover> movers = new ArrayList();

void setup(){
  size(1300,800,P3D);
  //  size(1000,400,P3D);
  background(0);
  myFont = createFont("Rubik-BoldItalic.ttf", fontSize);
  textFont(myFont);
  textSize(fontSize);
  noStroke();
  date = year() + "-" + month() + "-" + day();
  get_new_file();
  boolean loaded = false;
  while (loaded == false){
    try {
        table = loadTable(path + file_name);
        loaded = true;
    }
    catch (Exception e) {
        println("couldn't load file");
        get_new_file();
        loaded = false;
    }
  }
  get_new_text();
  starting_time = millis();
  background = new Movie(this, "water.mov");
  background.loop();
}

void draw(){ 
  //slide_delay = int(map(mouseX, 0, width, 3000, 6000));
  //println(slide_delay);
  current_time = millis();
  elapsed_time = current_time - starting_time;
  // set off get_new_text every so often  
  if (elapsed_time >= slide_delay){
      get_new_text();
      starting_time = millis();
  }
  fill(0);
  //tint(255, 20);
  image(background, 0, 0);
  for (Mover m : movers) {
    m.updateBall();
    m.display();
  }
}


void get_new_file(){
  table = loadTable(path + date + ".csv");
  boolean foundfile = false;
  while (foundfile == false){
     try {
          TableRow row = table.findRow("NO", 0);
          row.setString(0, "YES");
          file_name = row.getString(1);
          println(path + file_name);
          foundfile = true;
      }
      catch (Exception e) {
          println("no more files :(");
          for (int i = 1; i < table.getRowCount(); i++){
            table.setString(i, 0, "NO");
          }
          foundfile = false;
      }
    }
  saveTable(table, path + date + ".csv");
}

void get_new_text(){
  row_number += 1;
  if (row_number > 103){
    get_new_file();
    boolean loaded = false;
    while (loaded == false){
      try {
          table = loadTable(path + file_name);
          loaded = true;
      }
      catch (Exception e) {
        println("couldn't load file");
          get_new_file();
          loaded = false;
      }
    }
  }
  else {
    text = table.getString(row_number, 2);
    String[] lines = splitTokens(text, "\n");
    //String[] lines={"NUANCE/DRIFT"};
    movers.clear();
    for (int i=0; i<lines.length; i++){
      //movers.add(new Mover( lines[i], height/2, i*.1 ) );
      movers.add(new Mover( lines[i], 30+ i*60, i*.1 ) );
    }
  }
}

void movieEvent(Movie m){
  m.read();
}  

class Mover{
 
  PVector location;
 
  // used in the sin formula :
  float locationX;
  float angle; // = random(0, 5*TWO_PI);
  //float radius = 20; // random(40, 390);
  float radius = 10; // random(40, 390);
  float angleSpeed = .02; // random (.01, .1);
 
  String text1;
 
  //constr
  Mover(String text_, float y_, float angle_) {
    text1=text_;
    location = new PVector(-1, y_);
 
    //locationX=random(-100, width-55); 
 
    angle=angle_;
 

    stroke(0);
    strokeWeight(2);
    fill(127);
    noStroke();
  } //constr
 
  void updateBall() {
    //location.x = radius * sin (angle) + width/2 - 300;
    location.x = radius * sin (angle) + 20;
    //location.x = radius * sin (angle) +locationX;
    angle+=angleSpeed;
  }
 
  void display() {
    textSize(fontSize);
    text(text1, location.x, location.y, 1200, 1000);
  }
}
