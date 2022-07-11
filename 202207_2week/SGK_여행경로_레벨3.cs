using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestConsole1
{
    class SGK_여행경로_레벨3
    {
        public string[] Solution(string[,] tickets)
        {
            // Sort
            SortArray(tickets);

            // Input Root
            List<string> answer = new List<string>();
            answer.Add("ICN");

            // Instance Flag
            bool[] usedTicket = new bool[tickets.GetLength(0)];

            // RouteCheck
            RouteCheck(tickets, answer[0], usedTicket, answer, 0);

            return answer.ToArray();
        }

        /// <summary>
        /// Route설정
        /// </summary>
        /// <param name="tickets"></param>
        /// <param name="departure"></param>
        /// <param name="usedTicket"></param>
        /// <param name="answer"></param>
        /// <param name="level"></param>
        /// <returns></returns>
        public bool RouteCheck(string[,] tickets, string departure, bool[] usedTicket, List<string> answer, int level)
        {
            if(usedTicket.ToList().TrueForAll(v => v == true) == true)
            {
                return true;
            }

            for(int i = 0; i < tickets.GetLength(0); i++)
            {
                if(usedTicket[i] == false && departure == tickets[i, 0])
                {
                    usedTicket[i] = true;
                    answer.Add(tickets[i, 1]);

                    if (RouteCheck(tickets, tickets[i, 1], usedTicket, answer, level + 1) == true)
                    {
                        return true;
                    }

                    usedTicket[i] = false;
                }
            }

            answer.RemoveAt(answer.Count - 1);
            return false;

        }

        /// <summary>
        /// 2차원 배열 정렬(arrival기준)
        /// </summary>
        /// <param name="tickets"></param>
        public void SortArray(string[,] tickets)
        {
            string[] keys = new string[tickets.GetLength(0)];
            string[] values = new string[tickets.GetLength(0)];

            for (int i = 0; i < tickets.GetLength(0); i++)
            {
                keys[i] = tickets[i, 0];
                values[i] = tickets[i, 1];
            }

            Array.Sort(values, keys);

            for (int i = 0; i < keys.Length; i++)
            {
                tickets[i, 0] = keys[i];
                tickets[i, 1] = values[i];
            }
        }
    }
}
