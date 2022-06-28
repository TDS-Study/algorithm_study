class Solution {    
    //게산 방식 : 가로거리 + 세로거리의 합으로 계산하기
    
    val leftHandNums  = arrayOf(1,4,7)
    val rightHandNums = arrayOf(3,6,9)      
        
    //행 기준으로 번호 매기기
    val firstRow  = arrayOf(1,2,3)
    val secondRow = arrayOf(4,5,6)
    val thirdRow  = arrayOf(7,8,9)
    val fourthRow = arrayOf(-1,0,-2)
    
    //열 기준으로 번호 매기기
    val firstColumn  = arrayOf(1,4,7, -1)
    val secondColumn = arrayOf(2,5,8,0)
    val thirdColumn  = arrayOf(3,6,9,-2)    
        
    fun solution(numbers: IntArray, hand: String): String {
        var answer = ""          
        var leftHandPos  = -1 //*를 임의로 -1이라 지칭
        var rightHandPos = -2 //#을 임의로 -2라고 지칭        
        
        numbers.forEach{
            var result:String = if(hand=="right") "R" else "L"
            
            if (leftHandNums.contains(it)) result = "L"
            else if (rightHandNums.contains(it)) result = "R" 
            else{
                val lDistance = distance(leftHandPos, it)
                val rDistance = distance(rightHandPos, it)
                                
                if(lDistance<rDistance) result = "L"
                else if(rDistance<lDistance) result = "R"
            }   
            
            when(result){
                "L" -> leftHandPos = it
                "R" -> rightHandPos = it
            }
            
            answer += result
        }
        
        return answer
    }
    
    fun distance(fromPos:Int, toPos:Int):Int
    {
        var returnValue:Int = 0
        
        //행 기준으로 두 번호 사이의 거리 구하기
        var fromRowNo = getRowNum(fromPos)
        var toRowNo = getRowNum(toPos)
        returnValue += Math.abs(fromRowNo-toRowNo)
        
        //열 기준으로 두 번호 사이의 거리 구하기
        var fromColumnNo = getColumnNum(fromPos)
        var toColumnNo = getColumnNum(toPos)
        returnValue += Math.abs(fromColumnNo-toColumnNo)
        
        //행 기준 두 번호 사이거리 + 열 기준 두 번호사이 거리 = 실제 두 번호 사이 거리
        return returnValue        
    }
    
    fun getColumnNum(pos:Int):Int
    {
        var returnValue:Int = 0
        
        if (firstColumn.contains(pos)) returnValue = 1
        else if (secondColumn.contains(pos)) returnValue = 2
        else if (thirdColumn.contains(pos)) returnValue = 3        
        
        return returnValue
    }
    
    fun getRowNum(pos:Int):Int
    {
        var returnValue:Int = 0
        
        if (firstRow.contains(pos)) returnValue = 1
        else if (secondRow.contains(pos)) returnValue = 2
        else if (thirdRow.contains(pos)) returnValue = 3
        else if (fourthRow.contains(pos)) returnValue = 4
        
        return returnValue
    }
}
