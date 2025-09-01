import java.io.*;
import java.util.*;

public class Main {

    public static boolean is_aeiou(char x) {
        if (x == 'a' ||x == 'e' ||x == 'i' ||x == 'o' ||x == 'u') {
            return true;
        }
        else return false;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String target = st.nextToken();
            if (target.equals("end")) break;
            
            
            StringBuilder letter = new StringBuilder();

            boolean is_acceptable = false;

            char[] split_t = target.toCharArray();

            if (target.contains("a") || target.contains("e") || target.contains("i") || 
            target.contains("o") || target.contains("u")) is_acceptable = true;
            else is_acceptable = false;

            if (target.length() < 2) {
                if (is_acceptable){
                    System.out.println("<"+target+"> is acceptable.");
                    continue;
                }
                else {
                    System.out.println("<"+target+"> is not acceptable.");
                    continue;
                }
            } else {
                if (is_acceptable){
                    if (split_t[0] == split_t[1]) {
                        if (split_t[0] == 'e' || split_t[0] == 'o') is_acceptable = true;
                        else is_acceptable = false;
                    }
                    else is_acceptable = true;
                    

                }
                else is_acceptable = false;
            }
            
            // System.out.println(target.toString());
            if (is_acceptable) {
                letter.append(Character.toString(split_t[0])+Character.toString(split_t[1]));
                
                for (int i = 2; i<target.length(); i++) {
                    if (!is_acceptable) break;
                    letter.append(Character.toString(split_t[i]));

                        if (is_aeiou(split_t[i])) {
                            for (int j = 1 ; j<=2; j++) {
                                // System.out.println(Character.toString(letter.charAt(i-j)));
                                if (is_aeiou(letter.charAt(i-j))) {
                                    if (split_t[i] == letter.charAt(i-j) && j == 1 && (split_t[i] == 'e' ||split_t[i] == 'o')) {
                                        is_acceptable = true;
                                    }
                                    else if (split_t[i] != letter.charAt(i-j) && j < 2) {
                                        is_acceptable = true;
                                        // System.out.println("!!!no!!!");
                                    }
                                    else {
                                        is_acceptable = false;
                                        // System.out.println("!!!no!!!");
                                        break;
                                    }
                                }
                                else {
                                        is_acceptable = true;
                                        break;
                                }
                            }
    
                        } else {
                            for (int j = 1 ; j<=2; j++) {
                                // System.out.println(Character.toString(letter.charAt(i-j)));
                                if (is_aeiou(letter.charAt(i-j))) {
                                        is_acceptable = true;
                                        break;
                                }
                                else {
                                    if (split_t[i] == letter.charAt(i-j)) {
                                        is_acceptable = false;
                                        // System.out.println("!!!no!!!");
                                        break;
                                    }
                                    else {
                                        if (j == 2) {
                                            is_acceptable = false;
                                            // System.out.println("!!!no!!!");
                                            break;
                                        }
                                        else is_acceptable = true;
                                    }
                                }
                            }
                        }
                    }

                

            }
            if (is_acceptable) System.out.println("<"+target+"> is acceptable.");
            else System.out.println("<"+target+"> is not acceptable.");

    }
    }}