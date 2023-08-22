# https://leetcode.com/problems/third-maximum-number
defmodule ThirdMaximumNumber do
  def third_max(nums) do
    nums
        |> MapSet.new
        |> MapSet.to_list
        |> Enum.sort
        |> Enum.reverse
        |> third
  end

  def third(sorted_nums) when length(sorted_nums) >= 3 do
    Enum.at(sorted_nums, 2)
  end

  def third(sorted_nums) do
    hd(sorted_nums)
  end
end

tests = [[3, 2, 1], [1, 2], [2, 2, 3, 1]]
for test <- tests do
  IO.puts(ThirdMaximumNumber.third_max(test))
end
