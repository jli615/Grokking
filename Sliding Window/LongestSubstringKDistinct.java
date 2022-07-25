import java.util.*;

public class LongestSubstringKDistinct {
  public static int findLength(String str, int k) {
    // TODO: Write your code here
    int n = str.length();
    int maxlen = 0;
    int windowStart = 0;
    //String order = "";

    Map<String, Integer> characters = new HashMap<String, Integer>();



    for (int windowEnd = 0; windowEnd < n; windowEnd++) {
      String current = str.substring(windowEnd, windowEnd + 1);
      if (str.substring(windowStart, windowEnd).contains(current) != true) {
        characters.put(current, 1);
        //order += current;
      } else {
        characters.put(current, characters.get(current) + 1);
      }

      //change everything
      
      
      while (characters.size() > k) {
        String currentStart = str.substring(windowStart, windowStart + 1);
        if (characters.get(currentStart) > 1) {
          characters.put(currentStart, characters.get(currentStart) - 1);
        } else {
          characters.remove(currentStart);
        }
        windowStart++;
      }

      maxlen = Math.max(maxlen, windowEnd - windowStart + 1);

    }

    return maxlen;
  }

  public static void main(String[] args) {
    System.out.println("Length of the longest substring: " + LongestSubstringKDistinct.findLength("araaci", 2));
    System.out.println("Length of the longest substring: " + LongestSubstringKDistinct.findLength("araaci", 1));
    System.out.println("Length of the longest substring: " + LongestSubstringKDistinct.findLength("cbbebi", 3));
  }
}
