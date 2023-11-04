class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  # Sort the array in ascending order
        min_diff = float('inf')  # Initialize min_diff with a large value
        result = []

        # Iterate through the sorted array
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]

            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result

        