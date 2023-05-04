# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:21:01 2021

@author: je_su
"""
import unittest
from modulos.conversor_unidades import ConversorUnidadesTemperatura

class TestConversorUnidadesTemperatura(unittest.TestCase):
    
    def setUp(self):
        self.miConversor = ConversorUnidadesTemperatura() 
    
    def test_convertir_a_kelvin(self):
        """ pruebo valores de temperatura para convertir a unidades Kelvin"""
        # Pruebo valores de temperatura de conversión válidos
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(0, 'C'), 273.15, places=2 )
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(-273.15, 'C'), 0, places=2 )
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(0, 'F'), 255.37, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(-459.67, 'F'), 0, places=2)

        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(100, 'C'), 373.15, places=2 )
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(-10, 'C'), 263.15, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(450, 'F'), 505.37, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_a_kelvin(-40, 'F'), 233.15, places=2)
        
        # Pruebo que se lanza una excepción cuando la conversión me devuelve temperatura en K con valores negativos 
        self.assertRaises(ValueError, self.miConversor.convertir_a_kelvin, -274, 'C')
        self.assertRaises(ValueError, self.miConversor.convertir_a_kelvin, -460, 'F')               
    
    def test_convertir_desde_kelvin(self):
        """ pruebo valores de temperatura para convertir desde unidades Kelvin"""
        # Pruebo valores de temperatura de conversión válidos
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(273.15, 'C'), 0, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(0, 'C'), -273.15, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(255.37, 'F'), 0, places=2)         
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(0, 'F'), -459.67, places=2) 

        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(373.15, 'C'), 100, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(3.5, 'C'), -269.65, places=2)        
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(303.5, 'F'), 86.63, places=2)         
        self.assertAlmostEqual( self.miConversor.convertir_desde_kelvin(10.5, 'F'), -440.77, places=2) 
        
        # Pruebo que se lanza una excepción cuando quiero convertir temperatura en K con valores negativos
        self.assertRaises(ValueError, self.miConversor.convertir_desde_kelvin, -10, 'C')
        self.assertRaises(ValueError, self.miConversor.convertir_desde_kelvin, -100, 'F')
    
    def test_convertir_unidades(self):
        """pruebo conversiones de temperatura desde una unidad a otra"""
        # Pruebo valores de temperatura de conversión válidos
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(0, 'C', 'F'), 32, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(100, 'C', 'F'), 212, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(-40, 'C', 'F'), -40, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(0, 'F', 'C'), -17.78, places=2)
        self.assertAlmostEqual( self.miConversor.convertir_unidades_temperatura(100, 'F', 'C'), 37.78, places=2)
        
        # Pruebo valores de temperatura de conversión no válidos
        self.assertRaises( ValueError, self.miConversor.convertir_unidades_temperatura, -274, 'C', 'F')
        self.assertRaises( ValueError, self.miConversor.convertir_unidades_temperatura, -460, 'F', 'C')       
    
    def test_unidades_incorrectas(self):
        """
        pruebo que se lanza la excepción KeyError si ingreso unidades diferentes de temperatura
        """
        self.assertRaises( KeyError, self.miConversor.convertir_a_kelvin, 0, 'A')
        self.assertRaises( KeyError, self.miConversor.convertir_desde_kelvin, 0, 'B')
        self.assertRaises( KeyError, self.miConversor.convertir_unidades_temperatura, 0, 'A', 'F')
        self.assertRaises( KeyError, self.miConversor.convertir_unidades_temperatura, 0, 'F', 'T')
    
    
if __name__ == '__main__':
    
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    