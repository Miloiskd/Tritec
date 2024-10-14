import importlib
import sys

class MergeSortTests:

    def __init__(self) -> None:
        self._tests = [
            ([3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 1, 2, 3, 4, 5, 5, 6, 9]),
            ([10, -1, 2, 0, 5], [-1, 0, 2, 5, 10]),
            ([5], [5]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ]

    def tests(self, name):
        self.reload_module(name)

        resultados = []
        for entrada, esperado in self._tests:
            try:
                from app.problem_solver.MergeSort import merge_sort
                resultado = merge_sort(entrada)
                print(f"Resultado: {resultado}, esperado: {esperado}")
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)

        return resultados

    def reload_module(self, name2):
        module_name = f"app.problem_solver.mergesort"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)


