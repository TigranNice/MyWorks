#pragma once
#include <iostream>
#include <locale.h>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

template <typename T>
class Matrix
{
	vector < vector <T> > massive;
	int n, m;
public:
	Matrix();
	Matrix(int n1, int m1);
	Matrix(const vector < vector <T> > mas, int nx, int mx);
	~Matrix();

	double determinant_do();
	double determinant();

	Matrix transporation();
	Matrix minor(int st, int col);
	double alg_dop(int st, int col);
	Matrix union_matrix();
	Matrix inverse();
	Matrix addition(const Matrix<T>& mas);
	Matrix substruction(const Matrix<T>& mas);
	Matrix multiplication(const Matrix<T>& mas);
	Matrix multiplication_scalar(const T alpha);
	Matrix concatenation(const Matrix<T>& mas2, bool choice);

	friend istream& operator >> (istream& stream, Matrix<T>& c)
	{
		cout << "Введите размерность массива:";
		stream >> c.n >> c.m;
		cout << endl << "Введите массив размерности (" << c.n << ", " << c.m << ")" << endl;
		for (int i = 0; i < c.n; i++)
		{
			vector <T> v;
			for (int j = 0; j < c.m; j++)
			{

				T a;
				stream >> a;
				v.push_back(a);
			}
			c.massive.push_back(v);
		}
		return stream;
	}
	friend ostream& operator<<(ostream& stream, const Matrix<T>& c)
	{
		stream << "Матрица размерности: (" << c.n << ", " << c.m << ")" << endl;
		for (int i = 0; i < c.n; i++)
		{
			for (int j = 0; j < c.m; j++)
			{
				if (j != c.m - 1)
					stream << c.massive[i][j] << " ";
				else
					stream << c.massive[i][j] << endl;
			}
		}
		return stream;
	}
	friend Matrix<T> operator + (Matrix<T>& mas, const Matrix<T>& mas1)
	{
		return mas.addition(mas1);
	}
	friend Matrix<T> operator - (Matrix<T>& mas, const Matrix<T>& mas1)
	{
		return mas.substruction(mas1);
	}
	friend Matrix<T> operator * (Matrix<T>& c1, const Matrix<T>& c2)
	{
		return c1.multiplication(c2);
	}
	friend Matrix<T> operator * (Matrix<T>& m, const T alpha)
	{
		return m.multiplication_scalar(alpha);
	}
};