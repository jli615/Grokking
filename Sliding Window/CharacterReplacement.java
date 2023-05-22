import java.util.*;

class CharacterReplacement {
  public static int findLength(String str, int k) {
    // TODO: Write your code here

    // environment variables
    int length = str.length();
    int windowStart = 0;

    // problem variables
    int maxlen = 0;
    // int charCount = 0;
    Map<Character, Integer> charCount = new HashMap<Character, Integer>();

    for (int windowEnd = 0; windowEnd < length; windowEnd++) {
      //define current character
      char current = str.charAt(windowEnd);

      // add character to hashmap
      if (charCount.containsKey(current) == false) {
        charCount.put(current, 0);
      }
      charCount.put(current, charCount.get(current) + 1);

      // check if it is over k
      char currentStart = str.charAt(windowStart);
      while ((windowEnd - windowStart + 1 - charCount.get(current)) > k) {
        charCount.put(currentStart, charCount.get(currentStart) - 1);
        if (charCount.get(currentStart) == 0) {
          charCount.remove(currentStart);
        }
        windowStart++;
      }

      // compare maxlen to lenght of current string
      maxlen = Math.max(maxlen, windowEnd - windowStart + 1);
    }

    return maxlen;
  }

  public static void main(String[] args) {
    System.out.println(CharacterReplacement.findLength("aabccbb", 2));
    System.out.println(CharacterReplacement.findLength("abbcb", 1));
    System.out.println(CharacterReplacement.findLength("abccde", 1));
  }
}
