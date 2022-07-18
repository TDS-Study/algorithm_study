using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestConsole1
{
    class SGK_안전영역
    {

        public void Solution()
        {
            int result = GetMaxSafetyArea();

            Console.WriteLine("최대안전영역 : " + result);

        }

        /// <summary>
        /// 안전영역의 최대값 구하기
        /// </summary>
        /// <returns></returns>
        private int GetMaxSafetyArea()
        {
            // 외부파일 읽기
            string filePath = @"D:\inputFile\test01.txt";
            string[] lines = System.IO.File.ReadAllLines(filePath);
            int n = Int32.Parse(lines[0]);

            // 지역의 높이정보를 areaList로 저장
            List<List<int>> areaList = new List<List<int>>();

            for(int i = 1; i < lines.Length; i++)
            {
                List<int> tmpList = new List<int>();

                lines[i].Split(' ').ToList().ForEach(v =>
                {
                    tmpList.Add(Int32.Parse(v));
                });

                areaList.Add(tmpList);
            }

            // 최대영역 개수 지정
            int maxValue = 0;

            // 1 이상 100이하의 높이정보에 대한 안전영역을 처리
            for(int h = 1; h <= 100; h++)
            {
                // 높이 별 지정좌표의 방문정보 저장
                bool[,] isVisited = new bool[n, n];

                // 높이 별 안전영역 구하기
                int areaCount = 0;

                for (int x = 0; x < n; x++)
                {
                    for (int y = 0; y < n; y++)
                    {
                        if (isVisited[x, y] == false && areaList[x][y] >= h)
                        {
                            areaCount++;
                            GetSafetyArea(areaList, x, y, n, h, isVisited);
                        }
                    }
                }

                // 최대값을 저장
                maxValue = maxValue <= areaCount ? areaCount : maxValue;

            }

            return maxValue;
        }

        /// <summary>
        /// 연속된 안전영역의 방문Flag를 True로 변경
        /// </summary>
        /// <param name="areaList"></param>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <param name="n"></param>
        /// <param name="target"></param>
        /// <param name="isVisited"></param>
        private void GetSafetyArea(List<List<int>> areaList, int x, int y, int n, int target, bool[,] isVisited)
        {
            // 지정높이값 이상일 경우만 GetSafetyArea함수전달 됨으로 true
            isVisited[x, y] = true;

            // 상, 하, 좌, 우 1Set
            // 좌표[x, y]의 값이 true면 1Set단위로 체크하며 
            // 지정높이값 이상인 좌표의 isVisit의 Flag를 true로 변경
            for (int i = 0; i < 4; i++)
            {
                int ix = x, iy = y;

                switch(i)
                {
                    case 0: ix -= 1; break;
                    case 1: ix += 1; break;
                    case 2: iy -= 1; break;
                    case 3: iy += 1; break;
                }

                // outRangeException 회피
                if(ix < 0 || iy < 0 || ix > n -1 || iy > n-1)
                {
                    continue;
                }

                // Set단위 좌표[ix][iy]에 안전영역이 추가로 존재하는지 확장체크 
                if(isVisited[ix, iy] == false && areaList[ix][iy] >= target)
                {
                    GetSafetyArea(areaList, ix, iy, n, target, isVisited);
                }
            }    
        }

    }
}
