class Solution {

    int[][] dp;
    int minL;
    int maxR;
    int maxLength = 0;

    private boolean solve(int l, int r, String s) {
        if (l >= r)
            return true;

        if (dp[l][r] != -1)
            return dp[l][r] == 1;

        // if current chars match, check if substring also match
        boolean palindrome = s.charAt(l) == s.charAt(r) &&
                solve(l + 1, r - 1, s);

        dp[l][r] = palindrome ? 1 : 0;

        //update answer
        if (palindrome && r - l > maxR - minL) {
            minL = l;
            maxR = r;
        }

        solve(l + 1, r, s);
        solve(l, r - 1, s);

        return palindrome;
    }

    public String longestPalindrome(String s) {
        dp = new int[s.length()][s.length()];

        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        solve(0, s.length() - 1, s);

        return s.substring(minL, maxR + 1);

    }
}