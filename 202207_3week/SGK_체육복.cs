﻿using System;
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
            // 분실자 중에서 여유분을 가지고 있던 학생은 
            // 분실자와 여유분 소지자 배열에서 학번 삭제
            List<int> lostList = lost.Except(reserve).ToList();
            List<int> reserveList = reserve.Except(lost).ToList();
            
            // 체육복을 잃어버리지 않은 학생 수
            int attend = n - lostList.Count;

            // 정렬 : 학생들의 번호가 정렬되지 않은 상태가 존재함
            lostList.Sort();
            reserveList.Sort();

            // 여유분 중 빌릴 수 있는지 체크
            foreach (int num in lostList)
            {
                if(reserveList.Contains(num - 1) == true)
                {
                    reserveList.Remove(num - 1);
                    attend++;
                    continue;
                }

                if(reserveList.Contains(num + 1) == true)
                {
                    reserveList.Remove(num + 1);
                    attend++;
                }
            }

            return attend;

        }
    }
}
