#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to the Python object
 */
void print_python_string(PyObject *p)
{
	PyObject *str, *repr;
	Py_ssize_t length;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	PyUnicode_READY(p);

	printf("  type: %s\n", (PyCompactUnicode_Check(p)) ? "compact unicode object" : "compact ascii");
	printf("  length: %ld\n", length);

	str = PyUnicode_AsUTF8String(p);
	repr = PyObject_Repr(str);
	Py_DECREF(str);

	printf("  value: %s\n", PyBytes_AS_STRING(repr));
	Py_DECREF(repr);
}
