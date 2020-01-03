import processing.video.*;
Movie background;

String list_path = "";
String article_path = "";
Table table;
String text = "";
String file_name = "";
String title = "";
float title_width;
int font_size = 30;
int margin_LR = 180;
int margin_TB = 130;
long current_time;
long starting_time;
long elapsed_time;
int slide_delay = 10000;
int row_number = 0;
int number_of_rows;
PFont normal_font;

void setup(){
  //size(500, 500);
  fullScreen();
  background(0);
  textSize(font_size);
  normal_font = createFont("Rubik-BoldItalic.ttf", font_size);
  textFont(normal_font);
  noStroke();
  get_new_file();
  boolean loaded = false;
  while (loaded == false){
    try {
        table = loadTable(article_path + file_name);
        loaded = true;
    }
    catch (Exception e) {
        e.printStackTrace();
        get_new_file();
        loaded = false;
    }
  }
  get_new_text();
  number_of_rows = table.getRowCount() - 1;
  starting_time = millis();
  background = new Movie(this, "water.mp4");
  background.loop();
}

void draw(){ 
  current_time = millis();
  elapsed_time = current_time - starting_time;  
  if (elapsed_time >= slide_delay){
      get_new_text();
      number_of_rows = table.getRowCount() - 1;
      starting_time = millis();
  }
  tint(0, 153, 204, 126);
  //tint(255, 20);
  image(background, 0, 0);
  fill(255); // white
  textAlign(LEFT, TOP);
  text(text, margin_LR, margin_TB, width-(margin_LR*2), height-(margin_TB*2));
}

void get_new_file(){
  table = loadTable(list_path + "projection.csv");
  boolean foundfile = false;
  while (foundfile == false){
     try {
          TableRow row = table.findRow("NO", 0);
          row.setString(0, "YES");
          file_name = row.getString(1);
          println(file_name);
          foundfile = true;
      }
      catch (Exception e) {
          println("no more files");
          for (int i = 1; i < table.getRowCount(); i++){
            table.setString(i, 0, "NO");
          }
          foundfile = false;
      }
    }
  saveTable(table, list_path + "projection.csv");
}

void get_new_text(){
  row_number += 1;
  if (row_number == 1){
    title = file_name.replace (".csv", "");
    title_width = textWidth(title);
  }
  if (row_number > number_of_rows){
    row_number = 0;
    get_new_file();
    boolean loaded = false;
    while (loaded == false){
      try {
          table = loadTable(article_path + file_name);
          loaded = true;
      }
      catch (Exception e) {
          get_new_file();
          loaded = false;
      }
    }
  }
  else {
    text = table.getString(row_number, 2);
  }
}

void movieEvent(Movie m){
  m.read();
}  
