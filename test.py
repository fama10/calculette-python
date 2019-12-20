import addition
import soustraction
import division
import multiplication
import ProgrammeServeur
import ProgrammeClient

def test():
    
    assert(addition.addition(1,2)) == 3
    assert(addition.addition(2,3)) == 5
    assert(addition.addition(2,-1)) == 1

    assert(soustraction.soustraction(1,2)) == -1
    assert(soustraction.soustraction(3,3)) == 0
    assert(soustraction.soustraction(2,-1)) == 4

    assert(multiplication.multiplication(1,2)) == 1
    assert(multiplication.multiplication(2,3)) == 6
    assert(multiplication.multiplication(2,-1)) == -2

    assert(division.division(1,0)) == 3
    assert(division.division(6,3)) == 5
    assert(division.division(8,4)) == 1

    


