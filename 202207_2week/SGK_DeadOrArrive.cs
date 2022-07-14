using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    public class SGK_DeadOrArrive
    {
        public void GetCarNumber()
        {
            string filePath = @"C:\Users\20220074\Desktop\inputfile\deadorarrive_8.txt";
            string[] lines = System.IO.File.ReadAllLines(filePath);
            int number = Int32.Parse(lines[0]);

            Dictionary<int, int[]> dicVWI = new Dictionary<int, int[]>();

            for (int i = 1; i <= number; i++)
            {
                int v = Int32.Parse(lines[i].Split(' ')[0]);
                int w = Int32.Parse(lines[i].Split(' ')[1]);

                if (dicVWI.ContainsKey(v) == false || dicVWI[v][0] <= w)
                {
                    dicVWI[v] = new int[] { w, i };
                }
            }

            int sumCarNum = 0;
            dicVWI.Values.ToList().ForEach(v => sumCarNum += v[1]);

            Console.WriteLine(sumCarNum);
        }
    }
}
