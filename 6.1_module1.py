# -*- coding: utf-8 -*-

obj = [ "python", "cpp", "c", "git" ]

def tot( *args ):
    """
    
    Parameters
    ----------
    *args : int variables  

    Returns
    -------
    sum of this variables .

    """
    sm = 0 
    for arg in args:
         sm += arg        
    
    return sm 

def hello( s ):
    """
    
    Parameters
    ----------
    s : string
    
    Returns
    -------
    say hello
    
    """
    print( "hello",s )
    
    
