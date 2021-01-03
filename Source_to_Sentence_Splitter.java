import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SentenceSpliter {

public static void main(String[] args) throws IOException {

File dir = new File("");
String str = "", text = "";
List<String> enSentences = new ArrayList<String>();
List<String> urSentences = new ArrayList<String>();

List<String> urWords = new ArrayList<String>();

for(File file : dir.listFiles()){
if(file.getName().endsWith("urdu.txt")){
BufferedReader br = new BufferedReader(new FileReader(file));

while((str = br.readLine()) != null){
text = text + " " + str.trim();
}
br.close();

for(String s:text.split("[؟۔!]"))
urSentences.add(s);

System.out.println(file.getName() + "  =  " + urSentences.size());

for(int i=0;i<enSentences.size();i++)
System.out.println(enSentences.get(i) + "\n" + urSentences.get(i));



FileWriter writer_en = new FileWriter("");
for(String s: enSentences) {
s = s.trim();
writer_en.write(s.trim() + " ." + "\n");
}
writer_en.close();

FileWriter writer_ur = new FileWriter("");
for(String s: urSentences) {
s = s.trim();
writer_ur.write(s.trim() + " ۔" + "\n");
}
writer_ur.close();


System.exit(0);


}

if(file.getName().endsWith("english.txt")){
BufferedReader br = new BufferedReader(new FileReader(file));

while((str = br.readLine()) != null){
text = text + " " + str.trim();
}
br.close();

for(String s:text.split("[.?!]"))
enSentences.add(s);

System.out.println(file.getName() + "  =  " + enSentences.size());


}

text = "";
}



}

}