using System;
using System.Collections.Generic;
using System.Text;

namespace GitHub_Project
{
    public class SGK_2016년_레벨1
    {
        List<int> dayList = new List<int> { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        public string Solution(int a, int b)
        {
            string answer = "";
            int days = b;

            for(int i = 0; i + 1 < a; i++)
            {
                days += dayList[i];
            }

            int value = days % 7;

            switch(value)
            {
                case 1: answer = "FRI"; break;
                case 2: answer = "SAT"; break;
                case 3: answer = "SUN"; break;
                case 4: answer = "MON"; break;
                case 5: answer = "TUE"; break;
                case 6: answer = "WED"; break;
                case 0: answer = "THU"; break;
            }

            Console.WriteLine(answer);

            return answer;
        }

    }
}
