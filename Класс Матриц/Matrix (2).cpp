#include "Matrix.h"

template Matrix<double>;
template <typename T>
Matrix<T>::Matrix()
{
	massive = {};
	n = 0;
	m = 0;
}
template <typename T>
Matrix<T>::Matrix(int n1, int m1)
{
	n = n1;
	m = m1;
}
template <typename T>
Matrix<T>::Matrix(const vector < vector <T> > mas, int nx, int mx)
{
	massive = mas;
	n = nx;
	m = mx;
}
template <typename T>
Matrix<T>::~Matrix()
{
	massive = {};
	n = 0;
	m = 0;
}
template <typename T>
double Matrix<T>::determinant_do()
{
	if (n == m)
	{
		return determinant();
	}
	else
	{
		cout << "no" << endl;
		return 0;
	}
}
template <typename T>
double Matrix<T>::determinant()
{
	int k, l, i, j, cot = 0;
	double det = 1, koef;
	T d;

	Matrix mas(massive, n, m);

	for (i = 0; i < n - 1; i++) {
		for (j = i + 1; j < m; j++) {
			if (mas.massive[i][i] == 0) {
				for (k = 1; k < n; k++) {
					if (mas.massive[k][i] != 0) {
						for (l = 0; l < m; l++) {
							d = mas.massive[i][l];
							mas.massive[i][l] = mas.massive[k][l];
							mas.massive[k][l] = d;
						}
					}
				}
				cot += 1;
			}

			if (mas.massive[i][i] == 0)
			{
				return det = 0;
			}

			koef = mas.massive[j][i] / mas.massive[i][i];
			for (k = i; k < n; k++)
			{
				mas.massive[j][k] -= mas.massive[i][k] * koef;
			}
		}
	}
	for (i = 0; i < n; i++)
		det *= mas.massive[i][i];
	det *= pow(-1, cot);
	return det;
}
template <typename T>
Matrix<T> Matrix<T>::transporation()
{
	Matrix<T> trans_matrix(m, n);
	for (int i = 0; i < m; i++)
	{
		vector <T> v;
		for (int j = 0; j < n; j++)
		{
			v.push_back(massive[j][i]);
		}

		trans_matrix.massive.push_back(v);
	}
	return trans_matrix;
}
template <typename T>
Matrix<T> Matrix<T>::minor(int st, int col)
{
	Matrix<T> minor(n - 1, m - 1);
	for (int i = 0; i < n; i++) {
		if (i != st) {
			vector <T> v;
			for (int j = 0; j < m; j++)
			{
				if (j != col)
				{
					v.push_back(massive[i][j]);
				}
			}
			minor.massive.push_back(v);
		}
	}
	return minor;
}
template <typename T>
double Matrix<T>::alg_dop(int st, int col)
{
	Matrix<T> mi;
	mi = minor(st, col);
	return mi.determinant() * pow(-1, st + col + 2);
}
template <typename T>
Matrix<T> Matrix<T>::union_matrix()
{
	Matrix<T> un_matr(n, m);
	for (int i = 0; i < n; i++)
	{
		vector <T> v;
		for (int j = 0; j < m; j++)
		{
			v.push_back(alg_dop(i, j));
		}
		un_matr.massive.push_back(v);
	}
	return un_matr;
}
template <typename T>
Matrix<T> Matrix<T>::inverse()
{
	if (n == m && determinant_do() != 0)
		return union_matrix().transporation().multiplication_scalar(1 / determinant_do());
	else
	{
		cout << "no" << endl;
		return *this;
	}
}
template <typename T>
Matrix<T> Matrix<T>::addition(const Matrix<T>& mas)
{
	Matrix<T> sum;
	sum.n = n;
	sum.m = m;
	for (int i = 0; i < n; i++)
	{
		vector <T> v;
		for (int j = 0; j < m; j++)
		{
			T a;
			a = massive[i][j] + mas.massive[i][j];
			v.push_back(a);
		}
		sum.massive.push_back(v);
	}
	return sum;
}
template <typename T>
Matrix<T> Matrix<T>::substruction(const Matrix<T>& mas)
{
	Matrix<T> sum;
	sum.n = n;
	sum.m = m;
	for (int i = 0; i < n; i++)
	{
		vector <T> v;
		for (int j = 0; j < m; j++)
		{
			T a;
			a = massive[i][j] - mas.massive[i][j];
			v.push_back(a);
		}
		sum.massive.push_back(v);
	}
	return sum;
}
template <typename T>
Matrix<T> Matrix<T>::multiplication(const Matrix<T>& mas)
{
	Matrix<T> sum;
	sum.n = n;
	sum.m = m;
	for (int i = 0; i < n; i++)
	{
		vector <T> v;
		for (int j = 0; j < mas.m; j++)
		{
			T a = 0;
			for (int k = 0; k < n; k++)
			{
				a += massive[i][k] * mas.massive[k][j];
			}
			v.push_back(a);
		}
		sum.massive.push_back(v);
	}
	return sum;
}
template <typename T>
Matrix<T> Matrix<T>::multiplication_scalar(const T alpha)
{
	Matrix<T> sum(n, m);
	for (int i = 0; i < n; i++)
	{
		vector <T> v;
		for (int j = 0; j < m; j++)
		{
			T a;
			a = massive[i][j] * alpha;
			v.push_back(a);
		}
		sum.massive.push_back(v);
	}
	return sum;
}
template <typename T>
Matrix<T> Matrix<T>::concatenation(const Matrix<T>& mas2, bool choice)
{
	if (choice == 0)
	{
		if (n = mas2.n)
		{
			Matrix<T> new1(this->n, this->m + mas2.m);
			for (int i = 0; i < n; i++)
			{
				vector <T> v;
				for (int j = 0; j < m + mas2.m; j++)
				{
					if (j < m)
						v.push_back(massive[i][j]);
					else
						v.push_back(mas2.massive[i][j - m]);
				}
				new1.massive.push_back(v);
			}
			return new1;
		}
		else
		{
			cout << "no" << endl;
			return *this;
		}
	}
	else
		if (choice == 1)
		{
			if (m = mas2.m)
			{
				Matrix<T> new1(this->n + mas2.n, this->m);
				for (int i = 0; i < n + mas2.n; i++)
				{
					vector <T> v;
					for (int j = 0; j < m; j++)
					{
						if (i < n)
							v.push_back(massive[i - n][j]);
						else
							v.push_back(mas2.massive[i][j]);
					}
					new1.massive.push_back(v);
				}
				return new1;
			}
		}
		else
		{
			cout << "no" << endl;
			return *this;
		}
	return *this;
}