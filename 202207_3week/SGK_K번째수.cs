using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    public class SGK_K번째수
    {
        public int[] Solution(int[] array, int[,] commands)
        {
            List<int> answer = new List<int>();

            for(int i = 0; i < commands.GetLength(0); i++)
            {
                int from = commands[i, 0];
                int to = commands[i, 1];
                int pick = commands[i, 2];

                List<int> saveList = new List<int>();

                for(int k = 0; k < array.Length; k++)
                {
                    if( k + 1  >= from && k + 1 <= to)
                    {
                        saveList.Add(array[k]);
                    }
                }

                saveList.Sort();
                answer.Add(saveList[pick - 1]);

            }

            return answer.ToArray();
        }

    }
}
