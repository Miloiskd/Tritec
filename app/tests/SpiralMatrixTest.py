import importlib
import sys

class SpiralMatrixTest():
    
    def __init__(self) -> None:
        self._test = {
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
            ([[1]], [1]),
            ([[1, 2], [3, 4]], [1, 2, 4, 3]),
            ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 6, 5, 4]),
            ([[1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 3, 4, 8, 7, 6, 5]),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]),
            ([[]], []), 
        }
        
    def tests(self, name):
        self.reload_module(name)
        
        resultados = []
        for entrada, esperado in self._test:
            try:
                from app.problem_solver.SpiralMatrix import spiral_matrix
                resultado = spiral_matrix(entrada)
                print(f"Resultado: {resultado}, esperado: {esperado}")
            except Exception as e:
                return f"Error: {e}"
            resultados.append(resultado == esperado)
        return resultado
    
    def reload_module(self, name):
        module_name = f"app.problem_solver.SpiralMatrix"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
        
        