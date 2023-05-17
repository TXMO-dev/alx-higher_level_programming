#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list;

    if (!PyList_Check(p))
    {
        printf("[*] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GET_ITEM(p, i);
        const char *item_type = Py_TYPE(item)->tp_name;

        printf("Element %zd: %s\n", i, item_type);
    }
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    Py_ssize_t size, i;

    if (!PyBytes_Check(p))
    {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %zd bytes:", size < 10 ? size : 10);
    for (i = 0; i < (size < 10 ? size : 10); i++)
    {
        printf(" %.2x", bytes->ob_sval[i]);
    }
    printf("\n");
}
