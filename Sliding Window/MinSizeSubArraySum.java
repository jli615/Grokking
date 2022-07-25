public class MinSizeSubArraySum {
    public static int findMinSubArray(int S, int[] arr) {
      // TODO: Write your code here
      int minlen = Integer.MAX_VALUE;
      int movingSum = 0;
      int windowStart = 0;
      for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        movingSum += arr[windowEnd];
        while (movingSum >= S) {
          minlen = Math.min(minlen, windowEnd - windowStart + 1);
          movingSum -= arr[windowStart];
          windowStart++;
        }
      }
      return minlen;
    }

    public static void main(String[] args) {
        int result = MinSizeSubArraySum.findMinSubArray(7, new int[] { 2, 1, 5, 2, 3, 2 });
        System.out.println("Smallest subarray length: " + result);
        result = MinSizeSubArraySum.findMinSubArray(8, new int[] { 3, 4, 1, 1, 6 });
        System.out.println("Smallest subarray length: " + result);
        result = MinSizeSubArraySum.findMinSubArray(8, new int[] { 2, 1, 5, 2, 3, 2});
        System.out.println("Smallest subarray length: " + result);
      }
  }
