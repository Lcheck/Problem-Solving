class Solution {
    int varTarget;
    int[] result = new int[2];
	public int[] twoSum(int[] nums, int target) {

		//1.주어진 배열로 브루트포스
		// -> 2중 for문으로 모든 경우의 수 탐색하다가 tartget과 일치하는 합이 나오면 출력력
        
			for (int i = 0; i < nums.length; i++) {
				varTarget = 0;
				for (int k = i+1; k < nums.length; k++) {

					varTarget = nums[i] + nums[k];
					if (target == varTarget) {

						result[0]=i;
						result[1]=k;

						return result;
					}
				}
				
		}

        return result;
	}
}