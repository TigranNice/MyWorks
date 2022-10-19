#include "Matrix.h"

int main()
{
	setlocale(LC_ALL, "Rus");
	int num = 1;
	while (num != 5)
	{
		cout << endl << "        ����" << endl;
		cout <<
			"1. �������� ���� ������" << endl <<
			"2. ��������� ���� ������" << endl <<
			"3. ��������� ���� ������" << endl <<
			"4. ������������ ���� ������" << endl <<
			"5. ��������� �� ������" << endl <<
			"6. �����������" << endl <<
			"7. �������� �������" << endl <<
			"8. ���������������" << endl <<
			"9. �����" << endl << endl;
		cout << "����� ������ ����:";
		int num;
		cin >> num;
		cout << endl;
		Matrix<double> m1, m2, m3;
		double alpha;
		switch (num)
		{
		case 1:
			cout << "������� ������ �������:" << endl;
			cin >> m1;
			cout << "������� ������ �������:" << endl;
			cin >> m2;
			cout << "���������: " << m1 + m2;
			break;
		case 2:
			cout << "������� ������ �������:" << endl;
			cin >> m1;
			cout << "������� ������ �������:" << endl;
			cin >> m2;
			cout << "���������: " << m1 - m2;
			break;
		case 3:
			cout << "������� ������ �������:" << endl;
			cin >> m1;
			cout << "������� ������ �������:" << endl;
			cin >> m2;
			cout << "���������: " << m1 * m2;
			break;
		case 4:
			cout << "��������: ������������ �� �����������(0) ��� ���������(1)";
			int n;
			cin >> n;
			cout << "������� ������ �������:" << endl;
			cin >> m1;
			cout << "������� ������ �������:" << endl;
			cin >> m2;
			if (n == 0)
				m3 = m1.concatenation(m2, 0);
			else
				m3 = m1.concatenation(m2, 1);
			cout << "���������: " << m3;
			break;
		case 5:
			cout << "������� �������:" << endl;
			cin >> m1;
			cout << "������� �����" << endl;
			cin >> alpha;
			cout << "���������: " << m1 * alpha;
			break;
		case 6:
			cout << "������� �������:" << endl;
			cin >> m1;
			cout << "���������: " << m1.determinant_do();
			break;
		case 7:
			cout << "������� �������:" << endl;
			cin >> m1;
			cout << "���������: " << m1.inverse();
			break;
		case 8:
			cout << "������� �������:" << endl;
			cin >> m1;
			cout << "���������: " << m1.transporation();
			break;
		case 9:
			cout << "GoodBey!" << endl << endl;
			break;
		default:
			cout << "�����";
			cin >> num;
			cout << "�����������. ������� ������." << endl;
			break;
		}
		if (num == 9)
			break;
	}
	system("pause");
	return 0;
}