import java.util.HashMap;
import java.util.Map;


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

class Solution2 {
 
	int[] result = new int[2];
	Map<Integer, Integer> map = new HashMap<>();
	public int[] twoSum(int[] nums, int target) {

		//2.해시맵 활용
		// -> 현재 인덱스, 값매핑 하여 "기록" 후 다음 순회에 활용
        
			for (int i = 0; i < nums.length; i++) 
			{	

				if(map.containsKey(target-nums[i]))
				{
					
					result[0]=map.get((target-nums[i]));
                    result[1]=i;
				}

                map.put(nums[i],i);
                //put이 앞에있으면 중복값있는 경우 현재 값의 인덱스가 출력됨
			}

        return result;
	}
}