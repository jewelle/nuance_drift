String list_path = "/Users/ericajewell/Downloads/NUANCE-DRIFT/";
String article_path = "/Users/ericajewell/Downloads/NUANCE-DRIFT/articles/";
Table table;
String english_text = "";
String native_text = "";
String native_lang = "";
String title = "";
float title_width;
String file_name;
int font_size = 17;
long current_time;
long starting_time;
long elapsed_time;
int slide_delay = 1500; //4290;
int row_number = 0;
int number_of_rows;
PFont normal_font, georgian, greek, gujarati, hebrew, hindi, japanese, kannada, 
      kazakh, khmer, korean, kurdish, lao, macedonian, malayalam, marathi, 
      myanmar, nepali, pashto, persian, punjabi, sindhi, sinhala, tamil, telugu, 
      thai, urdu, vietnamese, amharic, arabic, armenian, bengali, chinese;
//String date = "";

void setup(){
  size(1300,800);
  textSize(font_size);
  normal_font = createFont("Rubik-BoldItalic.ttf", font_size);
  georgian = createFont("NotoSansGeorgian-CondensedBlack.ttf", font_size);
  greek = createFont("NotoSans-BlackItalic.ttf", font_size);
  gujarati = createFont("NotoSansGujarati-Bold.ttf", font_size);
  hebrew = createFont("NotoSansHebrew-Black.ttf", font_size);
  hindi = createFont("NotoSansDevanagari-CondensedBold.ttf", font_size);
  japanese = createFont("NotoSansCJKjp-Black.otf", font_size);
  kannada = createFont("NotoSansKannada-Bold.ttf", font_size);
  kazakh = createFont("NotoSans-BlackItalic.ttf", font_size);
  khmer = createFont("NotoSansKhmer-Bold.ttf", font_size);
  korean = createFont("NotoSansCJKkr-Bold.otf", font_size);
  lao = createFont("NotoSansLao-Bold.ttf", font_size);
  malayalam = createFont("NotoSansMalayalam-Bold.ttf", font_size);
  marathi = createFont("NotoSansDevanagari-CondensedBold.ttf", font_size);
  myanmar = createFont("NotoSansMyanmar-Medium.ttf", font_size);
  nepali = createFont("NotoSansDevanagari-CondensedBold.ttf", font_size);
  pashto = createFont("NotoKufiArabic-Bold.ttf", font_size);
  persian = createFont("NotoKufiArabic-Bold.ttf", font_size);
  punjabi = createFont("NotoSansGurmukhi-Bold.ttf", font_size);
  sindhi = createFont("NotoKufiArabic-Bold.ttf", font_size);
  sinhala = createFont("NotoSansSinhala-Medium.ttf", font_size);
  tamil = createFont("NotoSansTamil-Medium.ttf", font_size);
  telugu = createFont("NotoSansTelugu-Bold.ttf", font_size);
  thai = createFont("NotoSansThai-Bold.ttf", font_size);
  urdu = createFont("NotoNaskhArabic-Bold.ttf", font_size);
  vietnamese = createFont("NotoSans-BlackItalic.ttf", font_size);
  amharic = createFont("NotoSansEthiopic-Bold.ttf", font_size);
  arabic = createFont("NotoKufiArabic-Bold.ttf", font_size);
  armenian = createFont("NotoSansArmenian-Bold.ttf", font_size);
  bengali = createFont("NotoSansBengali-Bold.ttf", font_size);
  chinese = createFont("NotoSansCJKsc-Bold.otf", font_size);
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
  text(title, (width/2)-(title_width/2), 30);
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
  //table = loadTable(list_path + date + ".csv");
  table = loadTable(list_path + "article_titles.csv");
  boolean foundfile = false;
  while (foundfile == false){
     try {
          TableRow row = table.findRow("NO", 0);
          row.setString(0, "YES");
          file_name = row.getString(1);
          title = file_name.replace (".csv", "");
          title_width = textWidth(title);
          println(article_path + file_name);
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
  saveTable(table, list_path + "article_titles.csv");
  //saveTable(table, list_path + date + ".csv");
}

void get_new_text(){
  row_number += 1;
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
  }
}
