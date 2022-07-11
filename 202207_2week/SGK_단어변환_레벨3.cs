namespace TestConsole1
{
    public class SGK_단어변환_레벨3
    {
        int count = 0;

        public int Solution(string begin, string target, string[] words)
        {
            bool[] isCheckList = new bool[words.Length];
            ChangeWord(begin, target, words, isCheckList, 0);
            return count;
        }

        private void ChangeWord(string begin, string target, string[] words, bool[] isCheckList, int sum)
        {
            for(int i = 0; i < words.Length; i++)
            {
                if(isCheckList[i] == false)
                {
                    if(CompareStr(begin, words[i]) == true)
                    {
                        begin = words[i];
                        isCheckList[i] = true;

                        if(begin == target)
                        {
                            count = sum + 1;
                        }
                        else
                        {
                            ChangeWord(begin, target, words, isCheckList, sum + 1);
                        }
                    }
                }

            }
        }

        private bool CompareStr(string begin, string str)
        {
            int charCount = 0;
            for (int i = 0; i < begin.Length; i++)
            {
                if (begin[i] == str[i])
                {
                    charCount++;
                }
            }

            return charCount == begin.Length - 1 ? true : false;

        }
    }
}

