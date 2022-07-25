import java.util.*;

class MaxFruitCountOf2Types {
  public static int findLength(char[] arr) {
    // TODO: Write your code here
    // environment variables
    int length = arr.length;

    // solution variables
    int maxFruit = 0;

    // hashmap
    Map<Character, Integer> basket = new HashMap<Character, Integer>();
    
    // initiating window
    int windowStart = 0;

    for (int windowEnd = 0; windowEnd < length; windowEnd++) {
      //define current fruit
      char current = arr[windowEnd];
      
      // adding fruit to basket
      if (basket.containsKey(current) == false) {
        basket.put(current, 0);
      }
      basket.put(current, basket.get(current) + 1);

      // while size is bigger than 2, shrink window
      while (basket.size() > 2) {
        //define current starting character
        char startCurrent = arr[windowStart];
        //removing one instance from value in hashmap
        basket.put(startCurrent, basket.get(startCurrent) - 1);
        //removing empty keys
        if (basket.get(startCurrent) == 0) {
          basket.remove(startCurrent);
        }
        //update start index
        windowStart++;
      }

      // compare window size to maxFruit
      maxFruit = Math.max(maxFruit, windowEnd - windowStart + 1);
    }

    return maxFruit;
  }

  public static void main(String[] args) {
    System.out.println("Maximum number of fruits: " + 
                          MaxFruitCountOf2Types.findLength(new char[] { 'A', 'B', 'C', 'A', 'C' }));
    System.out.println("Maximum number of fruits: " + 
                          MaxFruitCountOf2Types.findLength(new char[] { 'A', 'B', 'C', 'B', 'B', 'C' }));
  }
}