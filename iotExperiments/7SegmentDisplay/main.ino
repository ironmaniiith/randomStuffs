/*

0 - a,b,c,d,e,f
1 - b,c
2 - a,b,d,e,g
3 - a,b,c,d,g
4 - b,c,f,g
5 - a,c,d,f,g
6 - a,c,d,e,f,g
7 - a,b,c
8 - a,b,c,d,e,f,g
9 - a,b,c,d,f,g
. - d,f

a - Pin 6
b - Pin 7
c - Pin 8
d - Pin 9
e - Pin 10
f - Pin 11
g - Pin 12

*/

String S[10] = {"abcdef", "bc", "abdeg", "abcdg", "bcfg", "acdfg", "acdefg", "abc", "abcdefg", "abcdfg"};

void setup(){
    Serial.begin(9600);

    for(int i=6;i<=13;i++){
        pinMode(i, OUTPUT);
    }
    
    for(int i=0;i<=10;i++){
        reset();
        display(i);
        Serial.println(i);
        delay(500);
    }
    Serial.println("Give desired input");
}

void loop(){
   while(Serial.available()){
        char a = Serial.read();
        int num = a - '0';
        reset();
        if(num>=0 && num<10){
            display(num);
        }
        else if(a == '.'){
          display(10);
        }
        else if(a == 'r'){
            reset();
        }
  } 
}

void reset(){
    for(int j=6;j<=13;j++){
        digitalWrite(j, LOW);
    }
    delay(50);
}

void display(int num){
    if(num>=0 && num<=9)
        glow(S[num]);
    else{
        digitalWrite(13, HIGH);
    }
}

void glow(String A){
    for(int i=0;i<A.length();i++){
        digitalWrite(A[i]-'a'+6, HIGH);
        delay(10);
    }
}