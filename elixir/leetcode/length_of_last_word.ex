defmodule LengthOfLastWord do
  @spec length_of_last_word(s :: String.t) :: integer
  def length_of_last_word(s) do
    s |> String.graphemes
      |> Enum.reduce({0, 0}, &update_count/2)
      |> elem(1)
  end

  # char, acc
  def update_count(char, {curr_count, last_word_length} = _acc) do
    case char do
      " " -> {0, last_word_length}
      _ -> {curr_count + 1, curr_count + 1}
    end
  end
end

tests = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]
for test <- tests do
  IO.puts(LengthOfLastWord.length_of_last_word(test))
end
