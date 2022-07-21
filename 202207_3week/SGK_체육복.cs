using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    class SGK_체육복
    {
        public int solution(int n, int[] lost, int[] reserve)
        {
            List<int> tmpList = new List<int>();
            List<int> lostList = lost.ToList();
            List<int> reserveList = reserve.ToList();

            // 체육복을 잃어 버렸는데 여유분을 가지고 있는 학생은 제외
            lostList.ForEach(v =>
            {
                if (reserveList.Contains(v) == true)
                {
                    tmpList.Add(v);
                    reserveList.Remove(v);
                }
            });

            // 분실자에서 여유분을 가지고 있던 학생을 제외
            tmpList.ForEach(v =>
            {
                lostList.Remove(v);
            });

            // 체육복을 잃어버리지 않은 학생 수
            int attend = n - lostList.Count;

            // 정렬 : 학생들의 번호가 정렬되지 않은 상태가 존재함
            lostList.Sort();
            reserveList.Sort();

            // 여유분 중 빌릴 수 있는지 체크
            foreach (int num in lostList)
            {
                int idx = reserveList.FindIndex(v => v == num - 1);

                if (idx > -1)
                {
                    reserveList.RemoveAt(idx);
                    attend++;
                    continue;
                }

                idx = reserveList.FindIndex(v => v == num + 1);

                if (idx > -1)
                {
                    reserveList.RemoveAt(idx);
                    attend++;
                }
            }

            return attend;

        }
    }
}
