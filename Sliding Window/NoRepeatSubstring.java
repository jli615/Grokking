import java.util.*;

class NoRepeatSubstring {
  public static int findLength(String str) {
    // TODO: Write your code here

    // environment variables
    int length = str.length();
    int windowStart = 0;

    // problem variables
    int maxlen = 0;
    Map<String, Integer> indexes = new HashMap<String, Integer>();

    // sliding the End of the window
    for (int windowEnd = 0; windowEnd < length; windowEnd++) {
      
      // establishing current character
      String current = str.substring(windowEnd, windowEnd + 1);

      // checking if it is in the hashmap
      if (indexes.containsKey(current) == false) {
        indexes.put(current, windowEnd);
      } else {
        // sliding the beginning of the window
        windowStart = indexes.get(current) + 1;
        // change dictionary index
        indexes.put(current, windowEnd);
      }

      // comparing string length to maxlen
      maxlen = Math.max(maxlen, windowEnd - windowStart + 1);
    }

    return maxlen;
  }

  public static void main(String[] args) {
    System.out.println("Length of the longest substring: " + NoRepeatSubstring.findLength("aabccbb"));
    System.out.println("Length of the longest substring: " + NoRepeatSubstring.findLength("abbbb"));
    System.out.println("Length of the longest substring: " + NoRepeatSubstring.findLength("abccde"));
  }
}
