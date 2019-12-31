String path = "/Users/ericajewell/Downloads/NUANCE-DRIFT/";
String article_path = "/Users/ericajewell/Downloads/NUANCE-DRIFT/articles/";
String[] lines;
Table table;
String text = "";
String english_text = "";
String native_text = "";
String native_lang = "";
String title = "";
float titlewidth;
String file_name;
PFont normal_font;
PFont georgian;
PFont greek;
PFont gujarati;
PFont hebrew;
PFont hindi;
PFont japanese;
PFont kannada;
PFont kazakh;
PFont khmer;
PFont korean;
PFont kurdish;
PFont kyrgyz;
PFont lao;
PFont macedonian;
PFont malayalam;
PFont marathi;
PFont mongolian;
PFont myanmar;
PFont nepali;
PFont pashto;
PFont persian;
PFont punjabi;
PFont russian;
PFont serbian;
PFont sindhi;
PFont sinhala;
PFont tajik;
PFont tamil;
PFont telugu;
PFont thai;
PFont ukranian;
PFont urdu;
PFont uzbek;
PFont vietnamese;
PFont yiddish;
PFont amharic;
PFont arabic;
PFont armenian;
PFont azerbaijani;
PFont belarusian;
PFont bengali;
PFont bulgarian;
PFont chinese;
int fontSize = 17;
long current_time;
long starting_time;
long elapsed_time;
int slide_delay = 1000; //4290;
int row_number = 0;
int number_of_rows;
//String date = "";

void setup(){
  size(1300,800,P3D);
  normal_font = createFont("Rubik-BoldItalic.ttf", fontSize);
  textFont(normal_font);
  textSize(fontSize);
  georgian = createFont("NotoSansGeorgian-CondensedBlack.ttf", fontSize);
  greek = createFont("NotoSans-BlackItalic.ttf", fontSize);
  gujarati = createFont("NotoSansGujarati-Bold.ttf", fontSize);
  hebrew = createFont("NotoSansHebrew-Black.ttf", fontSize);
  hindi = createFont("NotoSansDevanagari-CondensedBold.ttf", fontSize);
  japanese = createFont("NotoSansCJKjp-Black.otf", fontSize);
  kannada = createFont("NotoSansKannada-Bold.ttf", fontSize);
  kazakh = createFont("NotoSans-BlackItalic.ttf", fontSize);
  khmer = createFont("NotoSansKhmer-Bold.ttf", fontSize);
  korean = createFont("NotoSansCJKkr-Bold.otf", fontSize);
  lao = createFont("NotoSansLao-Bold.ttf", fontSize);
  malayalam = createFont("NotoSansMalayalam-Bold.ttf", fontSize);
  marathi = createFont("NotoSansDevanagari-CondensedBold.ttf", fontSize);
  myanmar = createFont("NotoSansMyanmar-Medium.ttf", fontSize);
  nepali = createFont("NotoSansDevanagari-CondensedBold.ttf", fontSize);
  pashto = createFont("NotoKufiArabic-Bold.ttf", fontSize);
  persian = createFont("NotoKufiArabic-Bold.ttf", fontSize);
  punjabi = createFont("NotoSansGurmukhi-Bold.ttf", fontSize);
  sindhi = createFont("NotoKufiArabic-Bold.ttf", fontSize);
  sinhala = createFont("NotoSansSinhala-Medium.ttf", fontSize);
  tamil = createFont("NotoSansTamil-Medium.ttf", fontSize);
  telugu = createFont("NotoSansTelugu-Bold.ttf", fontSize);
  thai = createFont("NotoSansThai-Bold.ttf", fontSize);
  urdu = createFont("NotoNaskhArabic-Bold.ttf", fontSize);
  vietnamese = createFont("NotoSans-BlackItalic.ttf", fontSize);
  amharic = createFont("NotoSansEthiopic-Bold.ttf", fontSize);
  arabic = createFont("NotoKufiArabic-Bold.ttf", fontSize);
  armenian = createFont("NotoSansArmenian-Bold.ttf", fontSize);
  bengali = createFont("NotoSansBengali-Bold.ttf", fontSize);
  chinese = createFont("NotoSansCJKsc-Bold.otf", fontSize);
   noStroke();
  //date = year() + "-" + month() + "-" + day();
  get_new_file();
  boolean loaded = false;
  while (loaded == false){
    try {
        table = loadTable(article_path + file_name);
        loaded = true;
    }
    catch (Exception e) {
        e.printStackTrace();
        println("couldn't load file");
        get_new_file();
        loaded = false;
    }
  }
  get_new_text();
  number_of_rows = table.getRowCount() - 1;
  starting_time = millis();
}

void draw(){ 
  current_time = millis();
  elapsed_time = current_time - starting_time;  
  if (elapsed_time >= slide_delay){
      get_new_text();
      number_of_rows = table.getRowCount() - 1;
      starting_time = millis();
  }
  background(255,255,255);
  fill(50);
  textFont(normal_font);
  text(title, (width/2)-(titlewidth/2), 30);
  text(native_lang, 30, 70);
  text("English", 610, 70);
  text(english_text, 610, 90, 550, 650);
  if (row_number == 9) textFont(georgian);
  if (row_number == 11) textFont(greek);
  if (row_number == 12) textFont(gujarati);
  if (row_number == 16) textFont(hebrew);
  if (row_number == 17) textFont(hindi);
  if (row_number == 25) textFont(japanese);
  if (row_number == 27) textFont(kannada);
  if (row_number == 28) textFont(kazakh);
  if (row_number == 29) textFont(khmer);
  if (row_number == 30) textFont(korean);
  if (row_number == 33) textFont(lao);
  if (row_number == 41) textFont(malayalam);
  if (row_number == 44) textFont(marathi);
  if (row_number == 46) textFont(myanmar);
  if (row_number == 47) textFont(nepali);
  if (row_number == 49) textFont(pashto);
  if (row_number == 50) textFont(persian);
  if (row_number == 53) textFont(punjabi);
  if (row_number == 61) textFont(sindhi);
  if (row_number == 62) textFont(sinhala);
  if (row_number == 71) textFont(tamil);
  if (row_number == 72) textFont(telugu);
  if (row_number == 73) textFont(thai);
  if (row_number == 76) textFont(urdu);
  if (row_number == 78) textFont(vietnamese);
  if (row_number == 86) textFont(amharic);
  if (row_number == 87) textFont(arabic);
  if (row_number == 88) textFont(armenian);
  if (row_number == 92) textFont(bengali);
  if (row_number == 98) textFont(chinese);
  
  text(native_text, 30, 90, 550, 650);
}

void get_new_file(){
  //table = loadTable(path + date + ".csv");
  table = loadTable(path + "article_titles.csv");
  boolean foundfile = false;
  while (foundfile == false){
     try {
          TableRow row = table.findRow("NO", 0);
          row.setString(0, "YES");
          file_name = row.getString(1);
          title = file_name.replace (".csv", "");
          titlewidth = textWidth(title);
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
  saveTable(table, path + "article_titles.csv");
  //saveTable(table, path + date + ".csv");
}

void get_new_text(){
  row_number += 1;
  if (row_number > number_of_rows){
    get_new_file();
    boolean loaded = false;
    while (loaded == false){
      try {
          table = loadTable(article_path + file_name);
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
    english_text = table.getString(row_number, 2);
    native_text = table.getString(row_number, 1);
    native_lang = table.getString(row_number, 0);
    //println(text);
  }
}
