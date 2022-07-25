public class MaxSumSubArrayOfSizeK {
  public static int findMaxSumSubArray(int k, int[] arr) {
    // TODO: Write your code here
    int max = 0;
    int sum = 0;

    for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
      sum += arr[windowEnd];

      if (windowEnd >= k - 1) {

        if (sum >= max) {
          max = sum;
        }

        sum -= arr[windowEnd - k + 1];
      }
    }

    return max;
  }

  public static void main(String[] args) {
    System.out.println("Maximum sum of a subarray of size K: "
        + MaxSumSubArrayOfSizeK.findMaxSumSubArray(3, new int[] { 2, 1, 5, 1, 3, 2 }));
    System.out.println("Maximum sum of a subarray of size K: "
        + MaxSumSubArrayOfSizeK.findMaxSumSubArray(2, new int[] { 2, 3, 4, 1, 5 }));
  }
}