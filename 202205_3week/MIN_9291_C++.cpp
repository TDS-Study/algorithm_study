#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n;
	int ca = 1;
	
	cin >> n;
	
	int sdoq[9][9];
	bool check = true;
	string str[n] = {""};

	
	if (n <= 100 )
	{
	
		for(int k = 0; k < n; k++)
		{
			check = true;
			
			for(int i = 0; i < 9; i++)
			{
				for(int j = 0; j < 9; j++)
				{
					cin >> sdoq[i][j];
				}
			}
			
			
			for(int i = 0; i < 9; i++)
			{
				bool number1[10] = {false};
				
				for(int j = 0; j < 9; j++)
				{
					if(number1[sdoq[i][j]])
					{
						check = false;
						break;
					}
					else
					{
						number1[sdoq[i][j]] = true;
					}
				}
				
				if(check == false)
				{
					break;
				}
			}
			
			
			if(check)
			{
				for(int i = 0; i < 9; i++)
				{
					bool number2[10] = {false};
					
					for(int j = 0; j < 9; j++)
					{
						if(number2[sdoq[j][i]])
						{
							check = false;
							break;
						}
						else
						{
							number2[sdoq[j][i]] = true;
						}
					}
					
					if(check == false)
					{
						break;
					}

				}
			}
			
			
			int row = 0;
			int col = 0;
			
			if(check)
			{
				for(int i = 0; i < 9; i++)
				{
					bool number3[10] = {false};
					
					for(int j = 0; j < 3; j++)
					{
						for(int k =0; k < 3; k++)
						{
							if(number3[sdoq[j+row][k+col]])
							{
								check = false;
								break;
							}
							else
							{
								number3[sdoq[j+row][k+col]] = true;
							}
						}
						
						if(check == false)
						{
							break;
						}
					}
					
					
					if(check == false)
					{
						break;
					}
					
					if(i == 2 || i == 5)
					{
						row += 3;
						col = 0;
					}
					else
					{
						col += 3;
					}
				}
			}
	
			if(check)
			{
				str[ca-1] = "Case " + to_string(ca) + ": CORRECT";
	
			}
			else
			{
				str[ca-1] = "Case " + to_string(ca) + ": INCORRECT";
			}
			
			ca++;
		}
		
		
		for(int i = 0; i < n; i++)
		{
			cout << str[i] << endl;
		}
	}

	return 0;
}
