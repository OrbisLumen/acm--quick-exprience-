#include <iostream>
#include <iomanip>
#include <cmath>
#include <numeric>
#include <vector>
#include <algorithm>

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);

	int T;
	std::cin >> T;

	while (T--)
	{
		int x, y, t;
		std::cin >> x >> y >> t;

		std::string steps;
		std::cin >> steps;

		int cnt = 0;

		if (x == 0 && y == 0)
		{
			std::cout << '0' << '\n';
		}

		for (char ch : steps)
		{
			cnt++;

			if (ch == 'L')
			{
				if (x < 0)
					x += 1;
			}
			else if (ch == 'R')
			{
				if (x > 0)
					x -= 1;
			}
			else if (ch == 'U')
			{
				if (y > 0)
					y -= 1;
			}
			else if (ch == 'D')
			{
				if (y < 0)
					y += 1;
			}

			if (x == 0 && y == 0)
				break;
		}

		if (x == 0 && y == 0)
			std::cout << cnt << '\n';
		else
			std::cout << -1 << '\n';
	}

	return 0;
}