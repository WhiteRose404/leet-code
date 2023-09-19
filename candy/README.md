# Candy Distribution


<div style="display: flex; justify-content: flex-end;align-items: center; gap: 0.5rem; margin-bottom: 20px;">
    <span 
        style="
            background-color: #ff1110;
            color: #fff;
            font-size: 0.9em;
            border: 1px solid #ffa1f0;
            padding: 5px 7px;
            border-radius: 12px;
            text-align: center;
            font-weight: bold;
        ">Hard</span>  
    <span
        style="
            background-color: #f2f0f0;
            color: #333;
            font-size: 0.9em;
            border: 1px solid #ddd;
            padding: 5px 7px;
            border-radius: 12px;
            text-align: center;
        ">Interview</span>
</div>


There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to distribute to the children.

## Example 1:

**Input:** `ratings = [1,0,2]`
**Output:** `5`
**Explanation:** You can allocate to the first, second, and third child with 2, 1, 2 candies respectively.

## Example 2:

**Input:** `ratings = [1,2,2]`
**Output:** `4`
**Explanation:** You can allocate to the first, second, and third child with 1, 2, 1 candies respectively. The third child gets 1 candy because it satisfies the above two conditions.

## Constraints:

- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`
