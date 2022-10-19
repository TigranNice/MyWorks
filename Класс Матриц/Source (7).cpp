#include "Matrix.h"

int main()
{
	setlocale(LC_ALL, "Rus");
	int num = 1;
	while (num != 5)
	{
		cout << endl << "        МЕНЮ" << endl;
		cout <<
			"1. Сложение двух матриц" << endl <<
			"2. Вычитание двух матриц" << endl <<
			"3. Умножение двух матриц" << endl <<
			"4. Конкатенация двух матриц" << endl <<
			"5. Умножение на скаляр" << endl <<
			"6. Детерминант" << endl <<
			"7. Обратная матрица" << endl <<
			"8. Транспонировать" << endl <<
			"9. Выход" << endl << endl;
		cout << "Выбор пункта меню:";
		int num;
		cin >> num;
		cout << endl;
		Matrix<double> m1, m2, m3;
		double alpha;
		switch (num)
		{
		case 1:
			cout << "Введите первую матрицу:" << endl;
			cin >> m1;
			cout << "Введите вторую матрицу:" << endl;
			cin >> m2;
			cout << "Результат: " << m1 + m2;
			break;
		case 2:
			cout << "Введите первую матрицу:" << endl;
			cin >> m1;
			cout << "Введите вторую матрицу:" << endl;
			cin >> m2;
			cout << "Результат: " << m1 - m2;
			break;
		case 3:
			cout << "Введите первую матрицу:" << endl;
			cin >> m1;
			cout << "Введите вторую матрицу:" << endl;
			cin >> m2;
			cout << "Результат: " << m1 * m2;
			break;
		case 4:
			cout << "Выберите: конкатенация по горизотнали(0) или вертикали(1)";
			int n;
			cin >> n;
			cout << "Введите первую матрицу:" << endl;
			cin >> m1;
			cout << "Введите вторую матрицу:" << endl;
			cin >> m2;
			if (n == 0)
				m3 = m1.concatenation(m2, 0);
			else
				m3 = m1.concatenation(m2, 1);
			cout << "Результат: " << m3;
			break;
		case 5:
			cout << "Введите матрицу:" << endl;
			cin >> m1;
			cout << "Введите число" << endl;
			cin >> alpha;
			cout << "Результат: " << m1 * alpha;
			break;
		case 6:
			cout << "Введите матрицу:" << endl;
			cin >> m1;
			cout << "Результат: " << m1.determinant_do();
			break;
		case 7:
			cout << "Введите матрицу:" << endl;
			cin >> m1;
			cout << "Результат: " << m1.inverse();
			break;
		case 8:
			cout << "Введите матрицу:" << endl;
			cin >> m1;
			cout << "Результат: " << m1.transporation();
			break;
		case 9:
			cout << "GoodBey!" << endl << endl;
			break;
		default:
			cout << "Опция";
			cin >> num;
			cout << "отсутствует. Введите другую." << endl;
			break;
		}
		if (num == 9)
			break;
	}
	system("pause");
	return 0;
}